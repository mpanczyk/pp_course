#!/usr/bin/env python
# -*- coding: utf-8 -*-

from re import compile, IGNORECASE

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

regex = compile(
          ur'\s((' + u'|'.join(prepositions) + ur')\s+)',
          flags=IGNORECASE,
        )

def insert_nbsp(string):
  return regex.sub(r' \2&nbsp;', string)
