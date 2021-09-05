#!/bin/bash

if [ ! -d "venv" ]; then
	python -m venv venv
	source venv/bin/activate
	git clone git@github.com:GaetanDesrues/RemoteController.git
	cd RemoteController/Client
	pip install -r requirements.txt
else
	source venv/bin/activate
	cd RemoteController/Client
fi

# Get last input event
INP="/dev/input/$(ls /dev/input | grep js | tail -n 1)"

python start.py $INP