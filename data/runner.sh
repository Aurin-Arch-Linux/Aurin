#!/bin/bash
#python3 -m http.server --cgi 8009 --directory /home/aurin/ &> /dev/null &
#pid=$!
python3 $HOME/.aurin/install.py $1

#kill "${pid}"
