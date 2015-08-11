import sys, glob
sys.path.append('/home/sanjyot/Desktop/INIGO/gen-py')





from thrift import Thrift
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

try:

	transport=TSocket.TSocket('localhost',9095)
	
	transport=TTransport.TBufferedTransport(transport)

	protocol=TBinaryProtocol.TBinaryProtocol(transport)

	client=AdditionService.Client(protocol)
	transport.open()
	
	#client.ping()
	#print 'ping()'

	sum=client.add(3,4)
	print '3+4=%d' %(sum)

	transport.close()

except Thrift.TException,tx:
	print '%s' % (tx.message)
