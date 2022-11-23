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
inputcount=`ls | grep input | grep txt | wc -l`
find . -name "input*txt"  >> temp.txt

result=(`cat temp.txt`)

for (( i=0; i<${#result[@]}; i++ )); do
	python3 ${filename} ${result[i]}
	echo
done

unset input
unset filename
unset inputcount
unset result
rm -rf input*txt
rm -rf temp.txt
