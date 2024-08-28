import numpy as np

def hamming_window(n):
    """
    Generate a hamming window of n points as a numpy array.
    """
    return 0.54 - 0.46 * np.cos(2 * np.pi / n * (np.arange(n) + 0.5))

def mel_filterbank(p, n, fs):
    """
    Return a Mel filterbank matrix as a numpy array.
    Inputs:
        p:  number of filters in the filterbank
        n:  length of fft
        fs: sample rate in Hz
    Ref. http://www.ifp.illinois.edu/~minhdo/teaching/speaker_recognition/code/melfb.m
    """
    f0 = 700.0 / fs
    fn2 = int(np.floor(n/2))
    lr = np.log(1 + 0.5/f0) / (p+1)
    CF = fs * f0 * (np.exp(np.arange(1, p+1) * lr) - 1)
    bl = n * f0 * (np.exp(np.array([0, 1, p, p+1]) * lr) - 1)
    b1 = int(np.floor(bl[0])) + 1
    b2 = int(np.ceil(bl[1]))
    b3 = int(np.floor(bl[2]))
    b4 = min(fn2, int(np.ceil(bl[3]))) - 1
    pf = np.log(1 + np.arange(b1, b4+1) / f0 / n) / lr
    fp = np.floor(pf)
    pm = pf - fp
    M = np.zeros((p, 1+fn2))
    for c in range(b2-1, b4):
        r = int(fp[c] - 1)
        M[r, c+1] += 2 * (1 - pm[c])
    for c in range(b3):
        r = int(fp[c])
        M[r, c+1] += 2 * pm[c]
    return M, CF

def dct_matrix(bands, coefs):
    """
    Return the DCT-II matrix of order n as a numpy array.
    Calculating the DCT of an array using this matrix is
    equivalent to using scipy.fftpack.dct and then
    dividing by four.
    """
    x, y = np.meshgrid(range(bands), range(bands)[1:coefs+1])
    D = np.sqrt(2.0/bands) * np.cos(np.pi * (2*x+1) * y / (2*bands))
    D[0] /= np.sqrt(2)
    return D

# These are computed once to save a bit inside the function.
# Left as constants for simplicity of use for students, since
#   they never need to edit them.
FS = 44100                              # Sampling rate
FRAME_LEN = int(0.03 * FS)              # Frame length
FRAME_SHIFT = int(0.01 * FS)            # Frame shift
FFT_SIZE = 2048                         # How many points for FFT
WINDOW = hamming_window(FRAME_LEN)             # Window function
PRE_EMPH = 0.95                         # Pre-emphasis factor

BANDS = 40                              # Number of Mel filters
COEFS = 10                              # Number of Mel cepstra coefficients to keep
POWER_SPECTRUM_FLOOR = 1e-100           # Flooring for the power to avoid log(0)
M, CF = mel_filterbank(BANDS, FFT_SIZE, FS)      # The Mel filterbank matrix and the center frequencies of each band
D = dct_matrix(BANDS, COEFS)            # The DCT matrix.

def extract(x):
    """
    Extract MFCC coefficients of the sound x in numpy array format.
    """
    if x.ndim > 1:
        x = np.mean(x, axis=1)

    frames = (len(x) - FRAME_LEN) // FRAME_SHIFT + 1
    feature = []
    for f in range(frames):
        # Windowing
        frame = x[f * FRAME_SHIFT: f * FRAME_SHIFT + FRAME_LEN] * WINDOW
        # Pre-emphasis
        frame[1:] -= frame[:-1] * PRE_EMPH
        # Power spectrum
        X = np.abs(np.fft.fft(frame, FFT_SIZE)[:FFT_SIZE//2+1]) ** 2
        X[X < POWER_SPECTRUM_FLOOR] = POWER_SPECTRUM_FLOOR  # Avoid zero
        # Mel filtering, logarithm, DCT
        X = D @ np.log(M@X)
        feature.append(X)
    feature = np.row_stack(feature)

    # Mean & variance normalization
    if feature.shape[0] > 1:
        mu = np.mean(feature, axis=0)
        sigma = np.std(feature, axis=0)
        feature = (feature - mu) / sigma

    return feature
