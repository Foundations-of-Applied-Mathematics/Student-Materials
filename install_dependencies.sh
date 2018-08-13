#!/bin/bash

conda install --file .requirements.conda.txt --yes
conda update --all --yes
pip install --upgrade pip
pip install --requirement .requirements.pip.txt
