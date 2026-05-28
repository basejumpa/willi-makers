#!/usr/bin/env bash

### Enable exit on error ######################################################
set -e

### Update local apt index ####################################################

sudo apt-get update -y

### Make python3 available under name "python" ################################

export DEBIAN_FRONTEND=noninteractive
sudo apt-get install -y   \
    python-is-python3

### Install pip  ##############################################################

curl -sS https://bootstrap.pypa.io/get-pip.py | python


### Install venv  #############################################################

sudo apt-get install -y python3-venv


### Install poetry inside pipx ################################################
sudo python -m pip install pipx
sudo python -m pipx install poetry
sudo pipx ensurepath
export PATH="$PATH:$HOME/.local/bin" # Works at least for root. That's fine for docker/devcontainers


### Make available drawio in headless mode ####################################

# Install drawio

if which drawio; then
    echo "drawio is already installed"
else
    drawio_package=drawio-amd64-24.4.13.deb
    sudo curl -L -o $drawio_package https://github.com/jgraph/drawio-desktop/releases/download/v24.4.13/$drawio_package
    sudo apt install -y ./$drawio_package
    rm $drawio_package
fi

# Install virtual X-Server
sudo apt-get install -y xvfb


### Install mermaid command line tool #########################################

# This is only necessary when building PDFs
# TODO: Activate this

# apt-get install -y npm

# npm install -g @mermaid-js/mermaid-cli

### EOF #######################################################################


