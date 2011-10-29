#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import unittest
try:
  import json
except ImportError:
  import simplejson as json
from prettyprint import pp, pp_str

class PrettyPrintTest(unittest.TestCase):
  def testList(self):
    orig = [u'output prettily', u'綺麗に出力せよ']
    res  = pp_str(orig)
    self.assertEqual(orig, json.loads(res))

  def testDict(self):
    orig = {'en':u'output prettily', 'ja':u'綺麗に出力せよ'}
    res  = pp_str(orig)
    self.assertEqual(orig, json.loads(res))

  def testTuple(self):
    orig = (u'output prettily', u'綺麗に出力せよ')
    res  = pp_str(orig)
    self.assertEqual(orig[0], json.loads(res)[0])
    self.assertEqual(orig[1], json.loads(res)[1])

  def testSet(self):
    set1 = set(['John', 'Jane', 'Jack', 'Janice'])
    print pp_str(set1)
    self.assertTrue(True)

if __name__ == '__main__':
  unittest.main()
  
