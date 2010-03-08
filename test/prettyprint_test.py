#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import unittest
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

if __name__ == '__main__':
  unittest.main()
