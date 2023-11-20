strFile = ""
listFile = []

# Open a file for reading
with open('index.html', 'r') as file:
    # Read the entire contents of the file into a string
    content = file.read()
    strFile = content
print(strFile)
strFile=strFile.replace('\n', '')
listFile = strFile.split(" ")
print(listFile)
if '' in listFile:
    listFile = listFile.remove('')
