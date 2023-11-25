totalStates = []
inputSymbols = []
stackSymbols = []
pdaStack = []
pdaRules = {}
prevStatus = True 
# True jika menerima input parser

with open('pda.txt', 'r') as filepda:
    contentpdaline = filepda.readlines()

# print(contentpda)
linecount = 1
for pdaline in contentpdaline:
    if linecount == 1:
        totalStates = pdaline.strip().split()
    elif linecount == 2:
        inputSymbols = pdaline.strip().split()
    elif linecount == 3:
        stackSymbols = pdaline.strip().split()
    elif linecount == 4:
        currentState = pdaline.strip().split()
    elif linecount == 5:
        pdaStack.append(pdaline.strip().split())
    elif linecount == 6:
        acceptingState = pdaline.strip().split()
    elif linecount == 7:
        acceptingMethod = pdaline.strip().split()
    else:
        arr = pdaline.strip().split()
        key = (arr[0],arr[1],arr[2])
        newTop = []
        idx = arr[4].find('>')
        newTop.append(arr[4][:idx+1])
        newTop.append(arr[4][idx+1:])
        
        value = (arr[3],newTop)
        pdaRules[key] = value
    linecount += 1

arr = parser("temp.txt")

for val in arr:
    if(val[0]=='<'):
        prevStatus = True
    elif(val[0]=='>'):
        prevStatus = False
    if(prevStatus==False):
        continue
    top = pdaStack.pop()
    res = pdaRules.get((currentState,val,top),("NO_STATE","NO_TOP"))
    if(res == ("NO_STATE","NO_TOP")):
        res = pdaRules.get((currentState,val,"<X>"),("NO_STATE","NO_TOP"))
    if(res == ("NO_STATE","NO_TOP")):
        break
    currentState = res[0]
    for elmt in reversed(res[1]):
        pdaStack.append(elmt)
    
if(currentState==acceptingState):
    print("Accepted\n")
else:
    print("Syntax Error\n")