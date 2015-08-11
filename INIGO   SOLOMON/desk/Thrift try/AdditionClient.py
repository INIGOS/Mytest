import sys
sys.path.append('../gen-py')

from tutorial import AdditionService
from tutorial.ttypes import *

from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

try:

	transport=TSocket.TSocket('localhost',9090)
	transport=TTransport.TBufferedTransport(transport)
	protocol=TBinaryProtocol.TBinaryProtocol(transport)
	client=AdditionService.Client(protocol)
	transport.open()
	sum=client.add(4,5)
	print '4+5=%d' %(sum)
	transport.close()
except Thrift.TException,tx:
	print '%s' %(tx.message)
