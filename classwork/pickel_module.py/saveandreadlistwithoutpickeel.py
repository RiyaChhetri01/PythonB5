filepath ='listData.txt'
data=[1,2,4,5,6]
with open(filepath,"w")as fileHandle:
    fileHandle.write(str(data))

with open(filepath,"r") as fileHandle:
    readData = fileHandle.read()
    print(readData)
#read the same file and recover data as list
with open(filepath,"r") as fileHandle:
    readData=fileHandle.read()
    print(f"data read is{readData} \nits type is
           {type(readData)} and \nlength is {len(readData)}")