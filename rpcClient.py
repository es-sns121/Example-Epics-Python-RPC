#! /usr/bin/env python
# -*- coding: utf-8  -*-

from pvaccess import *

rpcClient = RpcClient('createNTTable')

pvArgument = PvObject({'nRows' : INT, 'nCols' : INT})

pvArgument.set({'nRows' : 10, 'nCols' : 10})

pvResponse = rpcClient.invoke(pvArgument)

ntTable = NtTable(pvResponse)

print ntTable
