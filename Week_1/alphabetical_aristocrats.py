

stringList = []
n = int(input())
for _ in range(n):
    string = input()
    stringList.append(string)

def cut_until_first_capital(s):
    for i, char in enumerate(s):
        if char.isupper():
            return s[i:]
    return s 

def compare(string1, string2):
    new_string1 = cut_until_first_capital(string1)
    new_string2 = cut_until_first_capital(string2)
    return new_string1 < new_string2  # Lexicographical comparison

# Sort the list using the compare function
for i in range(len(stringList)):
    for j in range(i + 1, len(stringList)):
        if not compare(stringList[i], stringList[j]):
            stringList[i], stringList[j] = stringList[j], stringList[i]

for surname in stringList:
    print(surname)