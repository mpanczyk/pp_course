#!/usr/bin/env python
# -*- coding: utf-8 -*-

from sys import argv
from os.path import isfile
import markdown
import re

from nbsp import insert_nbsp
from configure_highlighter import make_default_c_lexer
make_default_c_lexer()

TEMPLATE_FILE = 'topic.html.template'
PRE_SUBST = {
}
POST_SUBST = {
  '---': '&mdash;',
  'fun1': insert_nbsp,
}
INPUT_FILE = argv[1]
OUTPUT_FILE = argv[2]
NUM = int(re.search(r'(\d+)\.md', INPUT_FILE).groups()[0])
MD_EXTENSIONS = [
  'markdown.extensions.codehilite',
  'markdown.extensions.attr_list',
]


def apply_subst(text, subst):
  for k, v in subst.items():
    if k.startswith('fun'):
      text = v(text)
    else:
      text = text.replace(k, v)
  return text


def read_unicode_from_file(filename):
  with open(filename, 'r') as f:
    return f.read().decode('utf-8')


def get_navigation_links():
  # These are used on top and bottom of the page.
  other_files_links = []
  if isfile( 'topics/%d.md' % (NUM-1) ):
    # It is not the first topic.
    other_files_links.append( u'<a href="%d.html">poprzedni temat</a>' % (NUM-1) )
  other_files_links.append(u'<a href="../">w górę</a>')
  if isfile( 'topics/%d.md' % (NUM+1) ):
    # It is not the last topic.
    other_files_links.append( u'<a href="%d.html">następny temat</a>' % (NUM+1) )
  return u' | '.join(other_files_links)


def get_fill_dict():
  inputStr = read_unicode_from_file(INPUT_FILE)
  title = "%d: %s" %(NUM, inputStr.split('\n')[0])
  inputStr = apply_subst(inputStr, PRE_SUBST)

  md = markdown.Markdown(
    output_format='html5',
    extensions=MD_EXTENSIONS,
  )
  innerHtml = md.convert(inputStr)

  innerHtml = apply_subst(innerHtml, POST_SUBST)

  return {
    'content': innerHtml,
    'title': title,
    'other_files': get_navigation_links(),
  }


def main():
  template = read_unicode_from_file(TEMPLATE_FILE)
  output = template % get_fill_dict()
  with open(OUTPUT_FILE, 'w') as outputFile:
    outputFile.write( output.encode('utf-8') )


if __name__ == '__main__':
  main()
