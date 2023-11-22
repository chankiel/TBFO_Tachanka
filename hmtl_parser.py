strFile = ""
listFile = []
listFinal = []
tempTag = ""
count = 0
tempAtt = ""

def remove(s, indx):
    s = list(s)
    s.pop(indx)
    return ''.join(s)
# test
# str = "abcdef"
# print(str)
# str = remove(str,-2)
# print(str)

# Buka file
with open('index.html', 'r') as file:
    # Baca file
    content = file.read()
    print(content)
    strFile = content
strFile=strFile.replace('\n', '')

for char in strFile:
    if(char == ">"):
        tempTag += ">"
        listFile.append(tempTag)
        tempTag = ""
    elif(char == "<"):
        if(len(tempTag) == 0):
            tempTag += "<"
        else:
            if(tempTag[0] != "<"):
                listFile.append(tempTag)
                tempTag = "<"
            else:
                tempTag += "<"
    elif(char == " "):
        x = len(tempTag)
        if(x != 0):
            if(tempTag[-1] == " "):
                pass
            else:
                tempTag += char
    else:
        tempTag += char

# clear whitespace behind ">"
for i in range(len(listFile)):
    elmt = listFile[i]
    if(len(elmt) > 1):
        if(elmt[0] == "<"):
            if(elmt[-2] == " "):
                elmt = remove(elmt,-2)
                listFile[i] = elmt

# dekomposisi open tag with att
for j in range(len(listFile)):
    elmt = listFile[j]
    if(len(elmt) <= 1):
        listFinal.append(elmt)
    else:
        if(elmt[0] != "<"):
            listFinal.append(elmt)
        else:
            if(elmt[1] == "/"):
                listFinal.append(elmt)
                
            else:
                temp = list(elmt)
                hasil = ""
                for cc in temp:
                    if(cc == " "):
                        if(len(hasil) != 0):
                            if(hasil[0] == "<"):
                                listFinal.append(hasil)
                                hasil = ""
                            elif(hasil[-1] == "="):
                                pass
                            elif(len(hasil)>1 and hasil[-1] == "\"" and hasil[-2] == "\""):
                                listFinal.append(hasil)
                                hasil = ""
                    elif(cc == ">"):
                        listFinal.append(hasil)
                        listFinal.append(">")
                        hasil = ""

                    else:
                        if(len(hasil) != 0):
                            if(hasil[-1] == "\""):
                                if(cc == "\""):
                                    hasil += cc
                                    listFinal.append(hasil)
                                    hasil = ""
                                else:
                                    pass
                            else:    
                                hasil += cc
                        else:         
                            hasil += cc

# print(listFile)
listFinal.remove("")
print(listFinal)