def isGoal(string1,string2):
    curString = ""
    for i in range(len(string1)):
        if curString == string2:
            return True
        else:
            string1 += string1[i]
            curString = string1[i+1:len(string1)+i]
    return False


string1 = input()
string2 = input()
# string1,string2 = string.split()
if(isGoal(string1,string2)):
    print("true")
else:
    print("false")
# print(string)