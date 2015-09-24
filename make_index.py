#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import markdown
import re

TEMPLATE_FILE = 'index.md'
HTML_TEMPLATE = 'index.html.template'
OUTPUT_FILE = 'index.html'
h2re = re.compile(r'<h2>([^<]+)</h2>')

with open(TEMPLATE_FILE, 'r') as templateFile:
  template = templateFile.read().decode('utf-8')

with open(HTML_TEMPLATE, 'r') as templateFile:
  html_template = templateFile.read().decode('utf-8')

def get_subj_max_num():
  num = 0;
  while os.path.isfile('%d.md' % (num+1)):
    num += 1
  return num

def gen_all_subj_links(num):
  items = []
  for i in range(1, num+1):
    with open('%d.md' % i) as f:
      title = f.readline().decode('utf-8')
    items.append(u'  %(n)d. [%(title)s](%(n)d.html)' % {
      'n': i,
      'title': title,
    })
  return u'\n'.join(items)

max_cnt = get_subj_max_num()
all_subj_links = gen_all_subj_links( max_cnt )
inputStr = template % {
  'tematy': all_subj_links,
}
innerHtml = markdown.markdown(inputStr, output_format='xhtml5')
outputStr = html_template % {
  'content': innerHtml,
}

with open(OUTPUT_FILE, 'w') as outputFile:
  outputFile.write( outputStr.encode('utf-8') )
