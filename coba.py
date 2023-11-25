strFile = ""
listFile = []
tempTag = ""
count = 0
tempAtt = ""
# Open a file for reading
with open('index.html', 'r') as file:
    # Read the entire contents of the file into a string
    content = file.read()
    print(content)
    strFile = content
strFile=strFile.replace('\n', '')
# if '' in listFile:
#     listFile = listFile.remove('')
for char in strFile:
    if(char == "<"):
        if(len(tempTag) == 0):
            tempTag += char
        else:
            listFile.append(tempTag)
            tempTag = ""
            tempTag += char
    elif(char == ">"):
        if(tempTag[-1] == ' '):
            print("beanr")
            tempTag = tempTag.replace(" ", ">")
            if(tempTag[0] == "<" and tempTag[1] == "/"):
                listFile.append(tempTag)
                tempTag = ""
        else:
            tempTag += char
            if(tempTag[0] == "<" and tempTag[1] == "/"):
                listFile.append(tempTag)
                tempTag = ""
    elif(char == " "):
        x = len(tempTag)
        if(x != 0):
            if(tempTag[-1] == " "):
                pass
            else:
                # tempTag += char
    # elif(char == "="):
    #     if(te)
    else:
        tempTag += char
print(listFile)