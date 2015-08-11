port = 9095

import sys,glob

sys.path.append('/home/sanjyot/Desktop/INIGO/gen-py')




from add import *
from add.ttypes import *

from shared.ttypes import SharedStruct

from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

class addHandler:
	def __init__(self):
		self.log={}

	def ping(self):
		print 'ping()'

	def add(self,n1,n2):
		print 'add(%d,%d)' % (n1,n2)
		return n1+n2
	def getStruct(self,key):
		print 'getStruct(%d)' %(key)
		return self.log[key]
	def zip(self):
		print 'zip()'


handler = addHandler()
processor = AdditionService.Processor(handler)
transport = TSocket.TServerSocket(port=port)
tfactory = TTransport.TBufferedTransportFactory()
pfactory = TBinaryProtocol.TBinaryProtocolFactory()
 
server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
 
print "Starting python server..."
server.serve()
print 'done.'
