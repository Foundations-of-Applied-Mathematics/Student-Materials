#!/bin/bash

if [[ $(uname) == "Darwin" ]]; then     # Mac Detected
	echo "Mac Detected"
	brew install python@3.10

	if [ ! -f ~/.zshrc ]; then
		touch ~/.zshrc
	fi

	echo "" >> ~/.zshrc
	echo "# More convenient python access" >> ~/.zshrc
	echo 'alias python="python3.10"' >> ~/.zshrc
	echo 'alias pip="pip3.10"' >> ~/.zshrc
	echo 'alias ipython="ipython3"' >> ~/.zshrc

	# Prevent pip from installing packages unless it's in a virtual environment.
	python3 -m pip config set global.require-virtualenv True

	source ~/.zshrc

elif [[ $(uname) == "Linux" ]]; then    # WSL Detected
	echo "WSL Detected"
	
	sudo apt-get update && sudo apt-get upgrade
	sudo apt install python3.10 python3-pip ipython3 python3.10-venv
	sudo apt install python-is-python3

	# Prevent pip from installing packages unless it's in a virtual environment.
	python -m pip config set global.require-virtualenv True
fi
