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
    pp(set1)
    expected='''
[
    "Jane", 
    "Janice", 
    "John", 
    "Jack"
]
'''.strip()
    self.assertEqual(pp_str(set1), expected)

  def testNestedSet(self):
    set1 = list([6, set([2,1,3]), 5,[3,1,2], None])
    pp(set1)
    expected='''
[
    6, 
    [
        1, 
        2, 
        3
    ], 
    5, 
    [
        3, 
        1, 
        2
    ], 
    null
]
'''.strip()
    self.assertEqual(pp_str(set1), expected)

  def testObject(self):
    class MyClass(object):
      def __str__(self):
          return "<MyClass>"
    ls = list([1, MyClass()])
    pp(ls)
    expected='''
[
    1, 
    "<MyClass>"
]
'''.strip()
    self.assertEqual(pp_str(ls), expected)

if __name__ == '__main__':
  unittest.main()
  
