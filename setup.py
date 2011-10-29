# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
import sys
import unittest

import prettyprint
from prettyprint import __version__, __license__, __author__, __doc__

if __name__ == '__main__':
  # build distribution package
  setup(
    packages         = ('prettyprint',),
    name             = 'prettyprint',
    version          = __version__,
    py_modules       = find_packages(exclude=["test"]),
    description      = 'prettyprint print list/dict/tuple object prettily',
    long_description = __doc__,
    test_suite       = 'test',
    author           = __author__,
    author_email     = 'taichino@gmail.com',
    url              = 'http://github.com/taichino/prettyprint',
    keywords         = 'pretty print',
    license          = __license__,
    classifiers      = ["Development Status :: 3 - Alpha",
                        "Intended Audience :: Developers",
                        "License :: OSI Approved :: MIT License",
                        "Operating System :: POSIX",
                        "Programming Language :: Python",
                        "Topic :: Software Development :: Libraries :: Python Modules"]
  )
