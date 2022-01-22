#!/bin/sh

input_folder="./output"
schema="./schema.json"

for file in "${input_folder}"/*
do 
    if jq -e . "${file}" >/dev/null; then
        #echo "Good '${file}'"
        true
    else
        #echo "Failed to parse JSON, or got false/null"
        echo "Failed to parse '${file}'"
    fi

done