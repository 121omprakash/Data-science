#!/bin/bash
set -e
pip install --force-reinstall ipykernel

pip install traitlets==5.9

jupyter notebook

