#!/usr/bin/python
# -*- coding: utf-8 -*-

from sets import Set
try:
  import json
except ImportError:
  import simplejson as json

__all__ = ['pp', 'pp_str']

def pp(obj):
  print pp_str(obj)

def pp_str(obj):
  if isinstance(obj, Set):
    obj = list(obj)
  if isinstance(obj, list) or isinstance(obj, dict) or isinstance(obj, tuple):
    orig = json.dumps(obj, indent=4)
    return eval("u'''%s'''" % orig).encode('utf-8')
  else:
    return obj

if __name__ == '__main__':
  target = ['want pretty printing', '望麗出力']
  print target
  pp(target)
  target_dict = {'order': {'en':'print prettily', 'ja':'綺麗に出力せよ'}}
  print target_dict
  pp(target_dict)
  from sets import Set
  set1 = Set(['John', 'Jane', 'Jack', 'Janice'])
  pp(set1)
