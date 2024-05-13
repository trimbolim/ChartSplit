#!/usr/bin/python3

import yaml
import argparse
import pycpdflib
import logging

parser = argparse.ArgumentParser(description='Split Master PDFs into parts')
parser.add_argument('file_to_split',  type=str, 
                    help='Master PDF to be split.')
parser.add_argument('--map', help='path to yaml file with parts map', type=str, required=True)
parser.add_argument('--outfile', help='filename for output files', type=str, required=True)
parser.add_argument('--push', help='push files into Swing Shift folders', action='store_true' )

SWING_SHIFT_PARTS_DIR = "/Users/matthewtrimboli/Google Drive/My Drive/Swing Shift/Charts/Parts"

args = parser.parse_args()

# /Users/matthewtrimboli/drums.pdf
pycpdflib.loadDLL("/usr/local/lib/libpycpdf.so")
bigpdf = pycpdflib.fromFile(args.file_to_split, '')
outfilename = args.outfile


with open(args.map) as file:
    try:
        chartmap = yaml.safe_load(file)   
    except yaml.YAMLError as exc:
        print(exc)

path_prefix = chartmap['destinations']['path_prefix']
for chair in chartmap['destinations']['chairs']:
    weepdf = ""
    r = ""
    print (chartmap['destinations']['chairs'][chair])
    first = chartmap['destinations']['chairs'][chair][0]
    last = chartmap['destinations']['chairs'][chair][1]
    r = pycpdflib.pageRange(first,last)
    weepdf = pycpdflib.selectPages(bigpdf, r)

    if args.push:
        print ("Pushing " + outfilename + " to " + SWING_SHIFT_PARTS_DIR + "/" + chair)
        pycpdflib.toFile(weepdf, SWING_SHIFT_PARTS_DIR + "/" + chair + "/" + outfilename, False, False)
    else:
        print ("I would push " + outfilename + " to " + SWING_SHIFT_PARTS_DIR + "/" + chair)
