#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import markdown
import re

prepositions = u'a aby bez beze dla do jako\
                ku między mimo na nad nade niby\
                o obok od ode około oprócz\
                po pod podczas pode pomiędzy\
                pomimo ponad poniżej poprzez\
                pośród powyżej poza prócz\
                przed przede przez przeze\
                przy spod spode spośród spoza\
                sprzed u w wbrew we wedle\
                według wewnątrz wobec wokół\
                wraz wskutek wśród wzdłuż\
                względem z za ze znad znade zza\
                oraz i nie np. że'.split()

def insert_nbsp(s):
  pattern = ur'\s((' + u'|'.join(prepositions) + ur')\s+)'
  return re.sub(pattern, r' \2&nbsp;',s, flags=re.IGNORECASE)

TEMPLATE_FILE = 'topic.html.template'
PRE_SUBST = {
}
POST_SUBST = {
  '---': '&mdash;',
  'fun1': insert_nbsp,
}
INPUT_FILE = sys.argv[1]
OUTPUT_FILE = sys.argv[2]
NUM = int(re.search(r'(\d+)\.md', INPUT_FILE).groups()[0])

other_files_links = []
if os.path.isfile( 'topics/%d.md' % (NUM-1) ):
  other_files_links.append( u'<a href="%d.html">poprzedni temat</a>' % (NUM-1) )
other_files_links.append(u'<a href="../">w górę</a>')
if os.path.isfile( 'topics/%d.md' % (NUM+1) ):
  other_files_links.append( u'<a href="%d.html">następny temat</a>' % (NUM+1) )
other_files = u'&nbsp;|&nbsp;'.join(other_files_links)

def apply_subst(text, subst):
  for k, v in subst.items():
    if k.startswith('fun'):
      text = v(text)
    else:
      text = text.replace(k, v)
  return text

with open(TEMPLATE_FILE, 'r') as templateFile:
  template = templateFile.read().decode('utf-8')
with open(INPUT_FILE, 'r') as inputFile:
  inputStr = inputFile.read().decode('utf-8')

title = "%d: %s" %(NUM, inputStr.split('\n')[0])
inputStr = apply_subst(inputStr, PRE_SUBST)
innerHtml = markdown.markdown(inputStr, output_format='xhtml5')
innerHtml = apply_subst(innerHtml, POST_SUBST)
outputStr = template % {
  'content': innerHtml,
  'original_doc': INPUT_FILE,
  'title': title,
  'other_files': other_files,
}

with open(OUTPUT_FILE, 'w') as outputFile:
  outputFile.write( outputStr.encode('utf-8') )
