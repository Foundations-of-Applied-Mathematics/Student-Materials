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

	pip3.10 install --upgrade pip
	pip3.10 install --requirement requirements.txt

elif [[ $(uname) == "Linux" ]]; then   # WSL Detected
	echo "WSL Detected"

	# If these don't install, do it manually
	sudo apt install -y graphviz
	sudo apt install -y libopenmpi-dev
	sudo apt install -y ffmpeg
	sudo apt install -y g++
	sudo apt install -y python3-tk
	sudo apt install -y openjdk-8-jdk
	sudo apt install -y unzip

	pip install --upgrade pip
	pip install --requirement requirements.txt
	pip install mpi4py              # Latest Version = 3.1.4
fi
