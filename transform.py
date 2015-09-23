#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import markdown
import re

TEMPLATE_FILE = 'template.html'
PRE_SUBST = {
}
POST_SUBST = {
  '---': '&mdash;',
}
INPUT_FILE = sys.argv[1]
OUTPUT_FILE = sys.argv[2]
NUM = int(re.search(r'(\d+)\.md', INPUT_FILE).groups()[0])

other_files_links = []
if os.path.isfile( '%d.md' % (NUM-1) ):
  other_files_links.append( u'<a href="%d.html">poprzedni temat</a>' % (NUM-1) )
if os.path.isfile( '%d.md' % (NUM+1) ):
  other_files_links.append( u'<a href="%d.html">następny temat</a>' % (NUM+1) )
other_files = u'&nbsp;|&nbsp;'.join(other_files_links)

def apply_subst(text, subst):
  for k, v in subst.items():
    text = text.replace(k,v)
  return text

with open(TEMPLATE_FILE, 'r') as templateFile:
  template = templateFile.read().decode('utf-8')
with open(INPUT_FILE, 'r') as inputFile:
  inputStr = inputFile.read().decode('utf-8')

inputStr = apply_subst(inputStr, PRE_SUBST)
innerHtml = markdown.markdown(inputStr, output_format='xhtml5')
innerHtml = apply_subst(innerHtml, POST_SUBST)
outputStr = template % {
  'content': innerHtml,
  'original_doc': INPUT_FILE,
  'title': 'title',
  'other_files': other_files,
}

with open(OUTPUT_FILE, 'w') as outputFile:
  outputFile.write( outputStr.encode('utf-8') )
