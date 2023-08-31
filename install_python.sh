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

	source ~/.zshrc

elif [[ $(uname) == "Linux" ]]; then    # WSL Detected
	echo "WSL Detected"
	sudo apt-get update && sudo apt-get upgrade
	sudo apt install python3.10 python3-pip ipython3
	alias python=python3
	alias pip=pip3
	alias ipython=ipython3
	sudo apt install python-is-python3
fi
