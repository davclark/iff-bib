#!/usr/bin/env python3

'''Convert Karol Conner's spreadsheet to BibTeX for import into Zotero

Note that we are using Python *3* (developed with 3.4) so by default, we're
working in utf-8. (The default for Python source is also utf-8.)'''

# I use string.Template to avoid confusion with BibTeX's {}'s
from string import Template
from csv import DictReader

with open('./template.bib') as template_in:
    bib_template = Template(template_in.read())

# For the title, we wrap capitalized words in {}'s
# Not sure if this matters for Zotero, but we may as well produce relatively
# well-formatted BibTeX
wrap_template = Template('{$word}')

with open('./feld-studies.csv') as infile:
    for i, bib in enumerate(DictReader(infile)):
        # Wrap capitalized words in {}'s - though the logic isn't quite right
        # (see for example the results of the first entry, around the ':').
        # This is an example of how we might do other necessary
        # transformations.
        new_title_words = []
        for word in bib['Title'].split():
            if word[0].isupper():
                new_title_words.append(wrap_template.substitute(word=word))
            else:
                new_title_words.append(word)

        bib['Title'] = ' '.join(new_title_words)
        # We can't have spaces or slashes in our template identifiers
        bib['Abstract'] = bib['Abstract / Summary']

        # I think Zotero just throws this away...
        bib['key'] = str(i)

        print(bib_template.substitute(bib))
