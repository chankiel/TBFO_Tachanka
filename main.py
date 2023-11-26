import parser
totalStates = []
inputSymbols = []
stackSymbols = []
pdaStack = []
pdaRules = {}

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
        currentState = (pdaline.strip().split())[0]
    elif linecount == 5:
        pdaStack.append((pdaline.strip().split())[0])
    elif linecount == 6:
        acceptingState = (pdaline.strip().split())[0]
    elif linecount == 7:
        acceptingMethod = (pdaline.strip().split())[0]
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

# for key, value in pdaRules.items():
#     print(f"Key: {key}, Value: {value}")

arr = parser.parser("index.html")
print(arr)
for val in arr:
    if(val==""):
        continue
    top = pdaStack.pop()
    # print("CurrentState : "+currentState)
    # print("input :",val)
    # print("top stack :",top)
    res = pdaRules.get((currentState,val,top),("NO_STATE","NO_TOP"))
    if(res == ("NO_STATE","NO_TOP")):
        res = pdaRules.get((currentState,val,"<X>"),("NO_STATE","NO_TOP"))
    if(res == ("NO_STATE","NO_TOP") or res==("ERROR","e")):
        print(currentState)
        print(val)
        print(top)
        break
    currentState = res[0]
    # print("After currentState:",currentState)
    # print("Next Top", res[1])
    for elmt in reversed(res[1]):
        if(elmt!="" and elmt!='e'):
            if(elmt=='<X>'):
                # print("Elmt append stack:",top)
                pdaStack.append(top)
            else:
                # print("Elmt append stack:",elmt)
                pdaStack.append(elmt)

if(currentState==acceptingState):
    print("Accepted\n")
else:
    print("Syntax Error\n")


# START HTML HEAD BODY HTMLH HTMLHB FINISH TABLE TR