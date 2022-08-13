#!/bin/bash
# Download data files and place them in the lab folders.

SOURCE="https://github.com/Foundations-of-Applied-Mathematics/Data.git"
LABS=("ARMA" "Animation" "AnisotropicDiffusion" "BinaryTrees" "BreadthFirstSearch" "CDHMM" "CVXPY_Intro" "Conditioning_Stability" "DataAugmentation" "DataCleaning" "DataVisualization" "Differentiation" "DrazinInverse" "Ethics" "Exceptions_FileIO" "FacialRecognition" "FourierTransform" "GMM" "Gibbs_LDA" "GradientMethods" "HMM" "ImageSegmentation" "InformationTheory" "InteriorPoint_Linear" "InteriorPoint_Quadratic" "KMeans" "LSI_SkLearn" "LeastSquares_Eigenvalues" "LinearRegression" "LinearTransformations" "LinkedLists" "MarkovChains" "MatplotlibIntro" "Metropolis" "NMF" "NMF_Recommender" "NaiveBayes" "NearestNeighbor" "NumpyIntro" "PageRank" "Pandas1" "Pandas2" "Pandas3" "Pandas4" "PolynomialInterpolation" "Profiling" "RandomForest" "RegularExpressions" "SIR" "SQL1" "SQL2" "SVD_ImageCompression" "Simplex" "Spark" "TotalVariation" "UnixShell1" "UnixShell2" "Wavelets" "WebScraping" "WebTechnologies")
GIT="https://git-scm.com"
TEMPDIR="_DATA_"`date +%s`"_"

# Check that git is installed.
command -v git > /dev/null ||
{ echo -e "\nERROR: git is required. Download it at $GIT.\n"; exit 1; }

# Download the data using git sparse checkout.
mkdir ${TEMPDIR}
cd ${TEMPDIR}
git init --quiet
git remote add origin "${SOURCE}"
git config core.sparseCheckout true
for lab in ${LABS[@]}; do
    echo "${lab}" >> .git/info/sparse-checkout
done
echo -e "\nInitializing Download ...\n"
git pull origin master
cd ../

# Migrate the files from the temporary folder.
set +e
echo -e "\nMigrating files ..."
for lab in ${LABS[@]}; do
    # Check that the target directory exists before copying.
    if [ -d "./${lab}" ]; then
        cp -v ${TEMPDIR}/${lab}/* ./${lab}/
    else
        echo -e "\nERROR: directory '${lab}' not found!\n"
    fi
done

# Delete the temporary folder.
rm -rf ${TEMPDIR}
echo -e "\nDone.\n"
