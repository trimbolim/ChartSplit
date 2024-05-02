#!/usr/bin/python3

import yaml
import argparse
import pycpdflib

parser = argparse.ArgumentParser(description='Split Master PDFs into parts')
parser.add_argument('file_to_split',  type=str, 
                    help='Master PDF to be split.')
parser.add_argument('--map', help='path to yaml file with parts map', type=str, required=True)
parser.add_argument('--outfile', help='filename for output files', type=str, required=True)

args = parser.parse_args()

#print (args)
#print (args.outfile)


# /Users/matthewtrimboli/drums.pdf
pycpdflib.loadDLL("/usr/local/lib/libpycpdf.so")
bigpdf = pycpdflib.fromFile('/Users/matthewtrimboli/drums.pdf', '')
outfilename = args.outfile

#def pageRange(f, t):
#""" Nuild a range from one page to another inclusive.
#r = pycpdflib.pageRange(1,1)

# selectPages(pdf, r):
#weepdf = pycpdflib.selectPages(bigpdf, r)

# pycpdflib.toFile(merged, 'merged.pdf', False, False)
#pycpdflib.toFile(weepdf, '/Users/matthewtrimboli/drums-wee.pdf', False, False)

with open('cute.yml') as file:
    try:
        chartmap = yaml.safe_load(file)   
        #print(chartmap)
    except yaml.YAMLError as exc:
        print(exc)

path_prefix = chartmap['destinations']['path_prefix']
for chair in chartmap['destinations']['chairs']:
    weepdf = ""
    r = ""
    print (chartmap['destinations']['chairs'][chair])
    first = chartmap['destinations']['chairs'][chair]['first']
    last = chartmap['destinations']['chairs'][chair]['last']
    r = pycpdflib.pageRange(first,last)
    weepdf = pycpdflib.selectPages(bigpdf, r)
    pycpdflib.toFile(weepdf, '/Users/matthewtrimboli/' + chair + "-" + outfilename, False, False)


#chartmap = yaml.load("cute.yml")

#for i in `cat cute.map`
#do 
    #j=`echo $i | cut -f2 -d:`
    #k=`echo $i | cut -f1 -d: `
    #cpdf "Cute (Hefti).pdf" $j -o $k/422.pdf
#done
