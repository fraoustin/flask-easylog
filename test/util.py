#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Module test for flask_easylog
------------------------------

test for flask_easylog

"""

from logging import Handler, NOTSET

class ListHandler(Handler):
    def __init__(self, level=NOTSET):
        Handler.__init__(self, level)
        self.data=[]
    
    def clear(self):
        self.data=[]

    def emit(self, record):
        self.data.append({"level": record.levelno, 
            "msg": self.format(record),
            "record": record})
    
    def __len__(self):
        return len(self.data)