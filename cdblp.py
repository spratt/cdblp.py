#!/usr/bin/env python3
################################################################################
import argparse
parser = argparse.ArgumentParser(description='Count publications on dblp')
parser.add_argument('-a', '--author', help='Author name',
                    default='Timothy M. Chan')
parser.add_argument('-p', '--publication', help='Publication name',
                    default='Foundations of Computer Science, FOCS')
parser.add_argument('-d', '--debug', help="Debug mode",
                    action="store_true")
args=parser.parse_args()
################################################################################
name=args.author.replace('.','=')
names=name.split()
last=names[len(names)-1]
first='_'.join(names[:len(names)-1])
initial=last[0].lower()
publications=list(map(str.strip, args.publication.split(',')))
################################################################################
import urllib.request
url='http://dblp.uni-trier.de/pers/xx/{}/{}:{}.xml'.format(initial,last,first)
xmlstr=urllib.request.urlopen(url).read().decode('utf-8')
################################################################################
if args.debug:
    print('AUTHOR:        {}'.format(args.author))
    print('SEARCHING FOR: {}'.format(args.publication))
    print('URL:           {}'.format(url))
################################################################################
import xml.etree.ElementTree as ET
root = ET.fromstring(xmlstr)
count = 0
types={'article':'journal',
       'inproceedings':'booktitle'}
for t in types.keys():
    for x in root.iter(t):
        for publication in publications:
            if publication in x.find(types[t]).text:
                count+=1
print(count)
