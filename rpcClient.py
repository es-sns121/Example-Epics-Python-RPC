#! /usr/bin/env python
# -*- coding: utf-8  -*-

from pvaccess import *

def NTTable():
	# register the client with the service provided by the server
	rpcClient = RpcClient('createNTTable')

	# Create the argument and initialize it
	pvArgument = PvObject({'nRows' : INT, 'nCols' : INT})

	pvArgument.set({'nRows' : 5, 'nCols' : 5})

	# Invoke sends the argument to the server.
	pvResponse = rpcClient.invoke(pvArgument)

	# Print the structure sent back
	ntTable = NtTable(pvResponse)

	print ntTable

def NTMatrix():
	# register the client with the service provided by the server
	rpcClient = RpcClient('createNTMatrix')

	pvArgument = PvObject({'dim1' : INT, 'dim2' : INT})

	# Request a 3x3 matrix
	pvArgument.set({'dim1' : 3, 'dim2' : 3})

	# Invoke sends the argument to the server.
	pvResponse = rpcClient.invoke(pvArgument)

	print pvResponse

def main():
	
	# Request an NTTable PvObject from the rpcServer
	NTTable()

	# Request an NTMatrix PvObject from the rpcServer
	NTMatrix()

if __name__ == '__main__':
	main()
