string = input()

upper_count = sum(1 for i in range(len(string)) if string[i].isupper())

lower_count = sum(1 for i in range(len(string)) if string[i].islower())

if upper_count > lower_count:
    print(string.upper())
else:
    print(string.lower())