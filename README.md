# Python RpcServer and RpcClient Example

## Remote Procedure Call (RPC)

RPC is a protocol that one program can use to request a service
froma program located in another computer on a network without
having to unserstand the network's details.

## rpcServer.py

Serves as an example of how to define functions and register them
as services in EPICS. A server then provides these services that
clients can request.

## rpcClient.py

Serves as an example of how to request services provided by a server.
The services in this example return normative type PvObjects that are
initialized with some random data.
