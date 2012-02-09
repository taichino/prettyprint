#!/usr/bin/python
# -*- coding: utf-8 -*-

try:
  import json
except ImportError:
  import simplejson as json

__all__ = ['pp', 'pp_str']

class MyEncoder (json.JSONEncoder):
    def default(self, o):
        try:
            iterable = iter(o)
        except TypeError:
            pass
        else:
            return list(iterable)
        
        try:
            return json.JSONEncoder.default(self, o)
        except TypeError:
            return str(o)

def pp(obj):
  print pp_str(obj)

def pp_str(obj):
  orig = json.dumps(obj, 
               indent=4, 
               sort_keys=True, 
               skipkeys=True, 
               cls=MyEncoder)
  return eval("u'''%s'''" % orig).encode('utf-8')

if __name__ == '__main__':
  target = ['want pretty printing', '望麗出力']
  print target
  pp(target)
  target_dict = {'order': {'en':'print prettily', 'ja':'綺麗に出力せよ'}}
  print target_dict
  pp(target_dict)

  set1 = set(['John', 'Jane', 'Jack', 'Janice'])
  pp(set1)

  orig = set(['item1', 'item2'])
  res  = pp_str(orig)
  print res
  print json.loads(res)
  
