def remove(s, indx):
    s = list(s)
    s.pop(indx)
    return ''.join(s)
# test
# str = "abcdef"
# print(str)
# str = remove(str,-2)
# print(str)

def parser(filename):
    strFile = ""
    listFile = []
    listFile2 = []
    listFinal = []
    tempTag = ""
    count = 0
    tempAtt = ""
    with open(filename, 'r',encoding='utf-8') as file:
        # Baca file
        content = file.read()
        strFile = content
    strFile=strFile.replace('\n', '')

    for char in strFile:
        if(char == ">"):
            tempTag += ">"
            if("<!--" in tempTag):
                if("-->" in tempTag):
                    listFile.append("<!---->")
                    tempTag = ""
                else:
                    tempTag += char
            elif(tempTag.count("\"")%2 == 0):
                listFile.append(tempTag)
                tempTag = ""
            elif(tempTag.count("\"")%2 == 1):
                pass
            else:
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
    for k in range(len(listFile)):
        elmt = listFile[k]
        if("<" == elmt[0] and ">" == elmt[-1]):
            listFile2.append(elmt)
        else:
            listFile2.append("X")
    # dekomposisi open tag with att
    for j in range(len(listFile2)):
        elmt = listFile2[j]
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
                                if("\"" in hasil):
                                    if(cc == "\""):
                                        hasil += cc
                                        listFinal.append(hasil)
                                        hasil = ""
                                    elif("type=\"" in hasil or "method=\"" in hasil):
                                        hasil += cc
                                    else:
                                        pass
                                else:    
                                    hasil += cc
                            else:         
                                hasil += cc
    return listFinal