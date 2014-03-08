import csv
f=open('NewNodes.txt','w')
nodes={}
with open('Android_2008.csv', 'rb') as csvfile:
	x = csv.reader(csvfile, delimiter=',', )
	temp=[]
	for i in x:
		if i[2]=='AskerId' : continue
		if i[2] not in nodes:
			nodes[i[2]]=i[3]
			temp.append(i[2])
		if i[7] not in nodes:
			nodes[i[7]]=i[8]
			temp.append(i[7])
	f.write("New nodes in 2008 ="+str(len(temp))+"\n")

with open('Android_2009.csv', 'rb') as csvfile:
	x = csv.reader(csvfile, delimiter=',', )
	temp=[]
	for i in x:
		if i[2]=='AskerId' : continue
		if i[2] not in nodes:
			nodes[i[2]]=i[3]
			temp.append(i[2])
		if i[7] not in nodes:
			nodes[i[7]]=i[8]
			temp.append(i[7])
	f.write("New Nodes in 2009 ="+str(len(temp))+"\n")

with open('Android_2010.csv', 'rb') as csvfile:
	x = csv.reader(csvfile, delimiter=',', )
	temp=[]
	for i in x:
		if i[2]=='AskerId' : continue
		if i[2] not in nodes:
			nodes[i[2]]=i[3]
			temp.append(i[2])
		if i[7] not in nodes:
			nodes[i[7]]=i[8]
			temp.append(i[7])
	f.write("New Nodes in 2010 ="+str(len(temp))+"\n")

with open('Android_2011.csv', 'rb') as csvfile:
	x = csv.reader(csvfile, delimiter=',', )
	temp=[]
	for i in x:
		if i[2]=='AskerId' : continue
		if i[2] not in nodes:
			nodes[i[2]]=i[3]
			temp.append(i[2])
		if i[7] not in nodes:
			nodes[i[7]]=i[8]
			temp.append(i[7])
	f.write("New Nodes in 2011 ="+str(len(temp))+"\n")

with open('Android_2012.csv', 'rb') as csvfile:
	x = csv.reader(csvfile, delimiter=',', )
	temp=[]
	for i in x:
		if i[2]=='AskerId' : continue
		if i[2] not in nodes:
			nodes[i[2]]=i[3]
			temp.append(i[2])
		if i[7] not in nodes:
			nodes[i[7]]=i[8]
			temp.append(i[7])
	f.write("New Nodes in 2012 ="+str(len(temp))+"\n")

with open('Android_2013.csv', 'rb') as csvfile:
	x = csv.reader(csvfile, delimiter=',', )
	temp=[]
	for i in x:
		if i[2]=='AskerId' : continue
		if i[2] not in nodes:
			nodes[i[2]]=i[3]
			temp.append(i[2])
		if i[7] not in nodes:
			nodes[i[7]]=i[8]
			temp.append(i[7])
	f.write("New Nodes in 2013 ="+str(len(temp))+"\n")
f.close()
