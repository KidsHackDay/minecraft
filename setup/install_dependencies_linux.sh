#!/bin/bash

sudo apt-get update
sudo apt-get install -y python build-essential python-dev

curl https://bootstrap.pypa.io/get-pip.py | python

sudo pip install numpy