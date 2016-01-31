#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygments import lexers

def make_default_c_lexer():
  c_lexer = lexers.get_lexer_by_name('c')
  def get_c_lexer(*args, **kwargs):
    return c_lexer
  lexers.guess_lexer = get_c_lexer
