import json
import os
from pathlib import Path


def make_safe_filename(s):
    def safe_char(c):
        keepcharacters = (' ','_')
        return c if c.isalnum() or c in keepcharacters  else "_"

    return "".join(safe_char(c) for c in s).strip('\r\n').rstrip("_")[:230]


files = {}

FILE = 'arxiv-metadata-oai-snapshot.json'
with open(FILE) as f:
    for i, line in enumerate(f, start=1):
        if i % 100000 == 0:
            print(f"Processou {i}")

        paper = json.loads(line)
        year = paper['update_date'].split('-')[0]
        if year not in files:
            t = open(f'arxiv-metadata-import_{year}.json', 'w')
            t.write('{"articles":[')
            t.write(f'{line}')
            files[year] =  t
        else:
            files[year].write(f',{line}')

    for t in files.values():
        t.write(']}')
        t.close()
f.close()
a = 1/0            

FILE = 'arxiv-metadata-oai-snapshot.json'
date = 0
with open(FILE) as f:
    for i, line in enumerate(f, start=1):
        if (i % 100000) == 0:
            print(f"Processou {i} artigos")
        paper = json.loads(line)
        year = paper['update_date'].split('-')[0]
        date = int(year)
        os.makedirs(year, exist_ok=True)
        new_file = f"{year}/{paper['update_date']}_{make_safe_filename(paper['title'])}.txt"
        
        with open(new_file, 'w') as n:
            n.write(paper['abstract'])
            n.close()

