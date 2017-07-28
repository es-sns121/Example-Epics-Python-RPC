# Python RpcServer and RpcClient Example

## Prequisites

These applications require a working build of EPICS version 4 (4.6.0 as of 28/7/2017)
and Python version 2 (2.6.6 was used).

## Remote Procedure Call (RPC)

RPC is a protocol that one program can use to request a service
from a program located in another computer on a network without
having to understand the network's details.

## rpcServer.py

Serves as an example of how to define functions and register them
as services in EPICS. A server then provides these services that
clients can request.

## rpcClient.py

Serves as an example of how to request services provided by a server.
The services in this example return normative type PvObjects that are
initialized with some random data.
