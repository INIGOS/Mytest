for line in open('twittersearchconnector.dat','r'):
	item=line.rstrip()
	#print item
	new=item.split('|')
	ans=new[4]
	print ans
	print "-------------"
