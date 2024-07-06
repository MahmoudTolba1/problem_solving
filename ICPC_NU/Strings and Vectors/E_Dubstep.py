string = input()
string2 = "WUB"
string3 = "WUBWUB"

string = string.split(string3)
string = " ".join(string)
string = string.split(string2)
print(*string)