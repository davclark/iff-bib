#!/usr/bin/env python3

from csv import DictReader


with open('./feld-studies.csv') as infile:
    entries = [bib for bib in DictReader(infile)]

print(entries[0])
