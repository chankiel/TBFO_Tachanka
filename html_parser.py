
def remove(s, indx):
    s = list(s)
    s.pop(indx)
    return ''.join(s)
def parser(nameFile):
    strFile = ""
    listFile = []
    listFile2 = []
    listFile3 = []
    listFinal = []
    tempTag = ""
    count = 0
    tempAtt = ""
    # Buka file
    with open(nameFile, 'r') as file:
        # Baca file
        content = file.read()
        strFile = content
    strFile=strFile.replace('\n', '')

    # dekomposisi awal pisahin tag awal(<tag>), isi, dan tag akhir(</tag>)
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
    listFile.append(tempTag)
    # listFile = listFile.remove('')

    # clear whitespace behind ">"
    for i in range(len(listFile)):
        elmt = listFile[i]
        if(len(elmt) > 1):
            if(elmt[0] == "<"):
                if(elmt[-2] == " "):
                    elmt = remove(elmt,-2)
                    listFile[i] = elmt
    # print(listFile) # check proses 1
    # print("\n")

    # clear isi
    for k in range(len(listFile)):
        elmt = listFile[k]
        if(len(elmt) != 0):
            if("<" == elmt[0] and ">" == elmt[-1]):
                listFile2.append(elmt)
            else:
                listFile2.append("X")
            # if((k-1 >= 0) and ("html" in listFile[k-1] or "head" in listFile[k-1] or "body" in listFile[k-1] or "table" in listFile[k-1] or "tr" in listFile[k-1] or "div" in listFile[k-1]) and ("strong" not in listFile[k-1])):
            #     listFile2.append("X")
            # elif(k-1 < 0):
            #     listFile2.append("X")
            # else:
            #     pass
    # print(listFile2)



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
                            if("=" in hasil):
                                if(hasil.count("\"")%2 == 0):
                                    listFile.append(hasil)
                                    listFile.append(">")
                                    hasil = ""
                                elif(hasil.count("\"")%2 == 1):
                                    pass
                            else:
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

    # print(listFile)
    # listFinal.remove("")
    # print("\n")
    # print(listFinal)