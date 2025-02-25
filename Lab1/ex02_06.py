input_str = input("Nhap X,Y: ")
dimensions=[int(X) for X in input_str.split(',') ]
rowNum=dimensions[0]
colNum=dimensions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
for now in range(rowNum):
    multilist[row][col]= row*col 
print (multilist)