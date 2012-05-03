#!/usr/bin/env python
import sys
from distutils.core import setup, Extension

if sys.platform == "darwin":
	module1 = Extension('cTimer',
		sources = ['cTimer.c'])
else:
	module1 = Extension('cTimer',
		sources = ['cTimer.c'],
		extra_link_args = ['-lrt'])

setup (name = 'cTimer',
	version = '0.1',
	description = 'A high precision timer.',
	author = 'Chaordix (Russ Porosky)',
	author_email = 'russ@chaordix.com',
	url = 'https://github.com/chaordix/cTimer/',
	ext_modules = [module1])
