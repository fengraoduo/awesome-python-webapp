#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__="michelle"

'''
database operation module.
'''

import time,uuid,functools,threading,logging

#Dict object:

class Dict(dict):
	'''
	Simple dict but support access as x.y style

	>>>d1=Dict()
	