#! /bin/bash

killall mongod
rm -rf ./data
mkdir -p ./data/db
mongod --dbpath ./data/db/ --logpath ./data/log --auth --fork
# note, you must fist get the superuser.com data from:
# https://archive.org/download/stackexchange/superuser.com.7z
python loader.py
