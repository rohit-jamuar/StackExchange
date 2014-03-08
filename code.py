import csv
with open('Android_2011.csv', 'rb') as csvfile:
	x = csv.reader(csvfile, delimiter=',', )
	nodes,count={},1
	for i in x:
		if i[2]=='AskerId' : continue
		if i[2] not in nodes:
			nodes[i[2]]=[count,i[3]]
			count+=1
		if i[7] not in nodes:
			nodes[i[7]]=[count,i[8]]
			count+=1
	temp={}	
	for i in nodes:
		temp[nodes[i][0]]=nodes[i][1]
	g=open('Android_2011.net','w')
	g.write('*Vertices '+str(len(nodes))+"\n")
	for i in sorted(temp):
		g.write(str(i)+' "'+str(temp[i])+'"\n')	
	g.write("*arcs\n")
	
	csvfile.seek(0)
	edges={}

	for i in x:
		if i[2]=='AskerId' : continue
		if nodes.get(i[2])[0] not in edges:
			edges[nodes.get(i[2])[0]]=[nodes.get(i[7])[0]]
		else:
			edges[nodes.get(i[2])[0]].append(nodes.get(i[7])[0])

	for i in edges:
		for j in range(len(edges[i])):
			g.write(str(edges[i][j])+" "+str(i)+"\n")

	g.write('*edgelist\n')
	for i in edges:
		g.write(str(i)+" ")
		for j in edges[i]:
			g.write(str(j)+" ")
		g.write('\n')

	g.close()
