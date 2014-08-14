#! /bin/bash

killall mongod
rm -rf ./data
mkdir -p ./data/db
mongod --dbpath ./data/db/ --logpath ./data/log --fork
# note, you must fist get the taxi data from:
# http://www.andresmh.com/nyctaxitrips/
python loader.py
