#!/bin/bash

for i in `cat cute.map`
do 
    j=`echo $i | cut -f2 -d:`
    k=`echo $i | cut -f1 -d: `
    cpdf "Cute (Hefti).pdf" $j -o $k/422.pdf
done
