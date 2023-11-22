# class HTMLChecker:
#     def __init__(self):
#         self.stack = []

#     def process_input(self, html_input):
#         for char in html_input:
#             self.process_character(char)

#     def process_character(self, char):
#         if char == '<':
#             self.stack.append(char)
#         elif char == '>':
#             if self.stack and self.stack[-1] == '<':
#                 self.stack.pop()
#             else:
#                 print("Error: Tidak ada tag pembuka yang sesuai.")
#                 exit(1)

#     def is_html_valid(self):
#         return not self.stack

# if __name__ == "__main__":
#     html_input = input("Masukkan HTML: ")
#     checker = HTMLChecker()
#     checker.process_input(html_input)

#     if checker.is_html_valid():
#         print("HTML valid.")
#     else:
#         print("HTML tidak valid.")

totalStates = []
inputSymbols = []
stackSymbols = []
startingStates = []
startingStack = []
acceptingStates = []
acceptingMethod = []
pdaRules = []

with open('pda.txt', 'r') as filepda:
    contentpda = filepda.read()
    filepda.seek(0)
    contentpdaline = filepda.readlines()

# print(contentpda)
linecount = 1
for pdaline in contentpdaline:
    if linecount == 1:
        # print(pdaline)
        totalStates = pdaline.strip().split()
    elif linecount == 2:
        inputSymbols = pdaline.strip().split()
    elif linecount == 3:
        stackSymbols = pdaline.strip().split()
    elif linecount == 4:
        startingStates = pdaline.strip().split()
    elif linecount == 5:
        startingStack = pdaline.strip().split()
    elif linecount == 6:
        acceptingStates = pdaline.strip().split()
    elif linecount == 7:
        acceptingMethod = pdaline.strip().split()
    else:
        pdaRules.append(pdaline.strip().split())
        # pdaRules = (pdaline.strip().split())
    linecount += 1
# print(totalStates)
# print(inputSymbols)
# print(stackSymbols)
# print(startingStates)
# print(startingStack)
# print(acceptingStates)
# print(acceptingMethod)
# print(pdaRules)
    



