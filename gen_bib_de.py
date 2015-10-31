#!/usr/bin/env python3

'''Convert Karol Conner's spreadsheet to BibTeX for import into Zotero

Note that we are using Python *3* (developed with 3.4) so by default, we're
working in utf-8. (The default for Python source is also utf-8.)'''

# I use string.Template to avoid confusion with BibTeX's {}'s
from string import Template
from csv import DictReader
from glob import glob
from os.path import basename, splitext

bib_templates = {}
for template_file in glob('templates/*.bib'):
    name, _ = splitext(basename(template_file))
    with open(template_file) as template_in:
        bib_templates[name] = Template(template_in.read())

with open('./german-studies.csv') as infile:
    for i, bib in enumerate(DictReader(infile)):
        # I think Zotero just throws this away...
        bib['key'] = str(i)

        print(bib_templates[bib['bibtex_type'].substitute(bib))
