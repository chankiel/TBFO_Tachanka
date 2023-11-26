import html_parser
import argparse
totalStates = []
inputSymbols = []
stackSymbols = []
pdaStack = []
pdaRules = {}

parser = argparse.ArgumentParser(description='PDA Filename and HTML Filename')

parser.add_argument('file1', type=str, help='PDA Filename')
parser.add_argument('file2', type=str, help='HTML Filename')

args = parser.parse_args()
pdaFile = args.file1
htmlFile = args.file2

with open(pdaFile, 'r') as filepda:
    contentpdaline = filepda.readlines()

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

arr = html_parser.parser(htmlFile)
for val in arr:
    if(val==""):
        continue
    top = pdaStack.pop()
    res = pdaRules.get((currentState,val,top),("NO_STATE","NO_TOP"))
    if(res == ("NO_STATE","NO_TOP")):
        res = pdaRules.get((currentState,val,"<X>"),("NO_STATE","NO_TOP"))
    if(res == ("NO_STATE","NO_TOP") or res==("ERROR","e")):
        print("Current State:",currentState)
        print("Input:",val)
        print("Top:",top)
        break
    currentState = res[0]
    for elmt in reversed(res[1]):
        if(elmt!="" and elmt!='e'):
            if(elmt=='<X>'):
                pdaStack.append(top)
            else:
                pdaStack.append(elmt)

if(currentState==acceptingState):
    print("Accepted\n")
else:
    print("Syntax Error\n")