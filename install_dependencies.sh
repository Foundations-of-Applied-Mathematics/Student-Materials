#!/bin/bash

if [[ $(uname) == "Darwin" ]]; then    # Mac Detected
	echo "Mac Detected"

	brew install graphviz
	brew install openmpi
	brew install mpi4py            # Latest Version = 3.1.4
	brew install ffmpeg
	brew install gcc
	brew install cmake
	brew install python-tk@3.10

	# If we are not in a virtual environment, IN_VENV is 0. If we are, IN_VENV is 1.
	# When an environment is activtated, `sys.prefix` becomes the folder that houses the environment (e.g., .venv).
	# `sys.base_prefix` is the folder where the base Python executable is located.
	IN_VENV=$( python -c 'import sys ; print( 0 if sys.prefix == sys.base_prefix else 1 )' )
	if [[ $IN_VENV == 1 ]]; then
		# Inside virtual environment.
		python -m pip install --upgrade pip
		python -m pip install --requirement requirements.txt
		
		printf "\nPython dependencies successfully installed!\n"
	else
		printf "\nNot inside virtual environment.\nActivate environment, then run this script again.\n"
	fi

elif [[ $(uname) == "Linux" ]]; then   # WSL Detected
	echo "WSL Detected"

	sudo apt install -y graphviz
	sudo apt install -y libopenmpi-dev
	sudo apt install -y ffmpeg
	sudo apt install -y g++
	sudo apt install -y python3-tk
	sudo apt install -y openjdk-8-jdk
	sudo apt install -y unzip

	# If we are not in a virtual environment, IN_VENV is 0. If we are, IN_VENV is 1.
	# When an environment is activtated, `sys.prefix` becomes the folder that houses the environment (e.g., .venv).
	# `sys.base_prefix` is the folder where the base Python executable is located.
	IN_VENV=$( python -c 'import sys ; print( 0 if sys.prefix == sys.base_prefix else 1 )' )
	if [[ $IN_VENV == 1 ]]; then
		# Inside virtual environment.
		python -m pip install --upgrade pip
		python -m pip install --requirement requirements.txt
		python -m pip install mpi4py              # Latest Version = 3.1.4

		printf "\nPython dependencies successfully installed!\n"
	else
		printf "\nNot inside virtual environment.\nActivate environment, then run this script again.\n"
	fi
fi
