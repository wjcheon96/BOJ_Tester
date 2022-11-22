#!/bin/bash

if ! python3 -m venv venv ; then
        exit 1
fi

# activate venv
. venv/bin/activate

# install requirements
if ! pip3 install -r requirements.env ; then
        exit 1
fi

read input

python3 input.py $input
filename=`find .. -name "*$input*"`
result=`find . -name "input*txt"`

python3 $filename $result[2]

rm -rf input*txt