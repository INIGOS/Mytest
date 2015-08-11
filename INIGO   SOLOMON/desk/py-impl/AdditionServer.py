import sys
sys.path.append('/home/sanjyot/Desktop/gen-py') 
from add import AdditionService
from add.ttypes import *
 
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

import socket
 
class AdditionServiceHandler:
  def __init__(self):
    self.log = {}
 
  def ping(self):
    print "ping()"
 

 
  def sayMsg(self, msg):
    
    return "say " + msg + " from " + socket.gethostbyname(socket.gethostname())
 
handler = AdditionServiceHandler()
processor = AdditionService.Processor(handler)
transport = TSocket.TServerSocket(9090)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()
 
server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
 
print "Starting python server..."
server.serve()
print "done!"
