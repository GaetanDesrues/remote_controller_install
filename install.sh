#!/bin/bash

if [ ! -d "venv" ]; then
	python3 -m venv venv
	source venv/bin/activate
	git clone git@github.com:GaetanDesrues/remote_controller_install.git
	cd remote_controller_install
	pip install --upgrade pip
	pip install -r requirements.txt
else
	source venv/bin/activate
	cd remote_controller_install
fi

# Get last input event
INP="/dev/input/$(ls /dev/input | grep js | tail -n 1)"

python start.py $INP