# Dash-Button-Detector
Runs code when an amazon dash button is pressed!

### How It Works
This python script simply sniffs for all ARP packets on the network and
runs an execution block if the sender MAC address matches the one provided.

So in order to get your MAC address of the button, you can use **Wireshark**
on your network where you connected the dash button and filter by `arp`. The
sender will be clearly marked.

## Setup

1. Setup your dash button with the app but **do not choose a product to
order**. Only connect it to wifi.

2. (optional) you might want to turn off dash notifications since there will
be one with every press.

3. Set the variables in `sniff.py` for your wireless interface (which you
can get with `ifconfig`) and the MAC address of the dash button (which you
can get with **Wireshark**).

4. Enter the code you want to run under the `EXECUTION BLOCK` comment.

## Running

Simply run from terminal using `./run.sh`

Note: You need to have `virtualenv` installed to use (`pip install virtualenv`).
And if you want to add more libraries to the project, enter the virtualenv
with `virtualenv dash`
