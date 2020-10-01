#!/usr/bin/python3

from bs4 import BeautifulSoup;
import requests;
import pandas as pd;
import json;

ctftime_url = "https://ctftime.org/event/list/upcoming";
table_class = "table table-striped";
headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86 64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36'};
response = requests.get(ctftime_url, headers=headers);
soupy = BeautifulSoup(response.text, 'html.parser');

ctftime_table = soupy.find('table', attrs={'class': table_class});
df = pd.read_html(str(ctftime_table));
df = df[0];
result = df.to_json(orient='index');
parsed = json.loads(result);
with open('this.json', 'w') as outfile:
    json.dump(parsed, outfile, indent=4);