# Dash-Button-Detector
Runs code when an amazon dash button is pressed!

## Setup

1. Set the variables in `sniff.py` for your wireless interface (which you
can get with `ifconfig`) and the MAC address of the dash button (which you
can get with **Wireshark**).

2. Enter the code you want to run under the `EXECUTION BLOCK` comment.

## Running

Simply run from terminal using `./run.sh`

Note: You need to have `virtualenv` installed to use (`pip install virtualenv`). And if you want to add more libraries to the project, enter the virtualenv with `virtualenv dash`
