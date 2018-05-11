#!/bin/bash
# Download data files and place them in the lab folders.

SOURCE="https://github.com/Foundations-of-Applied-Mathematics/Data.git"
GIT="https://git-scm.com"
TEMPDIR="_DATA_"`date +%s`"_"

# Check that git is installed.
command -v git > /dev/null ||
{ echo -e "\nERROR: git is required. Download it at $GIT.\n"; exit 1; }

# Download the data using git sparse checkout and git lfs.
mkdir ${TEMPDIR}
cd ${TEMPDIR}
git init --quiet
echo -e "\nInitializing Download ...\n"
git remote add -f origin "${SOURCE}"
git config core.sparseCheckout true
echo "Conditioning_Stability" >> .git/info/sparse-checkout
echo "DataVisualization" >> .git/info/sparse-checkout
echo "Differentiation" >> .git/info/sparse-checkout
echo "DrazinInverse" >> .git/info/sparse-checkout
echo "Exceptions_FileIO" >> .git/info/sparse-checkout
echo "FacialRecognition" >> .git/info/sparse-checkout
echo "ImageSegmentation" >> .git/info/sparse-checkout
echo "LeastSquares_Eigenvalues" >> .git/info/sparse-checkout
echo "LinearTransformations" >> .git/info/sparse-checkout
echo "MatplotlibIntro" >> .git/info/sparse-checkout
echo "NumpyIntro" >> .git/info/sparse-checkout
echo "PageRank" >> .git/info/sparse-checkout
echo "SVD_ImageCompression" >> .git/info/sparse-checkout
git pull origin master
cd ../

# Migrate the files from the temporary folder.
set +e
echo -e "\nMigrating files ..."

cp -v ${TEMPDIR}/Conditioning_Stability/* ./Conditioning_Stability/
cp -v ${TEMPDIR}/DataVisualization/* ./DataVisualization/
cp -v ${TEMPDIR}/Differentiation/* ./Differentiation/
cp -v ${TEMPDIR}/DrazinInverse/* ./DrazinInverse/
cp -v ${TEMPDIR}/Exceptions_FileIO/* ./Exceptions_FileIO/
cp -v ${TEMPDIR}/FacialRecognition/* ./FacialRecognition/
cp -v ${TEMPDIR}/ImageSegmentation/* ./ImageSegmentation/
cp -v ${TEMPDIR}/LeastSquares_Eigenvalues/* ./LeastSquares_Eigenvalues/
cp -v ${TEMPDIR}/LinearTransformations/* ./LinearTransformations/
cp -v ${TEMPDIR}/MatplotlibIntro/* ./MatplotlibIntro/
cp -v ${TEMPDIR}/NumpyIntro/* ./NumpyIntro/
cp -v ${TEMPDIR}/PageRank/* ./PageRank/
cp -v ${TEMPDIR}/SVD_ImageCompression/* ./SVD_ImageCompression/

# Delete the temporary folder.
rm -rf ${TEMPDIR}
echo -e "\nDone.\n"
