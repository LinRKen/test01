#!/bin/bash
 wget -O tmp_data.txt  $1 
touch tmp_name.txt
./analysis.py | cat
./visualization.py
rm -r tmp_data.txt
rm -r tmp_name.txt

