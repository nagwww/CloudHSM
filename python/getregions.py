#!/usr/bin/python

"""
- Author : Nag m
- Hack   : Get all the CloudHSM regions
- Info   : Get all the CloudHSM regions
"""

import boto
from boto.cloudhsm.connection import Location

def getregions():
    for region in dir(Location):
        if region[0].isupper():
           print region

if __name__ == "__main__":
    getregions()
