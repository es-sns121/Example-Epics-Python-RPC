#! /usr/bin/env python
# -*- coding: utf-8 -*-

from pvaccess import *
import random


# ============ From the pvaPy doc, written by Sinisa Veseli ============
def createNTTable(pvRequest):
	
	nRows = pvRequest.getInt('nRows')
	
	nCols = pvRequest.getInt('nCols')

	ntTable = NtTable(nCols, DOUBLE)

	labels = []

	for j in range(0, nCols):
		
		labels.append('Column%s' % j)

		column = []

		for i in range(0, nRows):

			column.append(random.uniform(0, 1))

		ntTable.setColumn(j, column)

	ntTable.setLabels(labels)

	ntTable.setDescriptor('Automatically generated by pvaPy RPC server')

	return ntTable
# =======================================================================


def createNTMatrix(pvRequest):

	dim1 = pvRequest.getInt('dim1')
	
	dim2 = pvRequest.getInt('dim2')

	ntMatrix = PvObject({'value' : [DOUBLE], 
						 'dim' : [INT], 
						 'descriptor' : STRING},
						 'epics:nt/NTMatrix:1.0')

	# Values are held in a 1 dimensional array, row-major-order.
	value = []
		
	for i in range(dim1):
		for j in range(dim2):
			value.append(random.uniform(0, 1))

	dim = []
	dim.append(dim1)
	dim.append(dim2)

	ntMatrix['value'] = value
	ntMatrix['dim'] = dim
	ntMatrix['descriptor'] = str('Automatically generated by pvaPy RPC server')

	return ntMatrix


def main():
	
	rpcServer = RpcServer()

	# Register the services to be provided by the server

	rpcServer.registerService('createNTTable', createNTTable)

	rpcServer.registerService('createNTMatrix', createNTMatrix)

	# Start a listener in another thread. 
	rpcServer.startListener()

	# Wait for input to exit.
	while True:

		usr_input = raw_input("type 'exit' to quit: ")
		
		if usr_input == 'exit':
			
			# Stop the listener to shut down cleanly
			rpcServer.stopListener()
			
			break


if __name__ == '__main__':
	main()
