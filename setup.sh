#! /bin/bash

killall mongod
rm -rf ./data
mkdir -p ./data/db
mongod --dbpath ./data/db/ --logpath ./data/log --auth --fork
mongoimport --db zips --collection data zips.json
