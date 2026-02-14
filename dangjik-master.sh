#!/bin/bash

fuser -k 8000/tcp
python3 server.py &
sleep 1
xdg-open "http://localhost:8000"
