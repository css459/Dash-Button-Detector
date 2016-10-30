#!/bin/bash

function ctrl_c {
    sudo pkill -f sniff.py
    deactivate
}

trap ctrl_c SIGINT
source dash/bin/activate
sudo python sniff.py
