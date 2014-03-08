import csv
from sys import argv

nodes={}
for j in argv[1:]:
	f=open('NewNodes.txt','w')
	with open(j, 'rb') as csvfile:
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
		f.write("\nNew nodes from "+j+" = "+str(len(temp))+"\n\n")
