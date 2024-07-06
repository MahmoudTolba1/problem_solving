string = input()
upper_count = sum(1 for c in string if c.isupper())
lower_count = sum(1 for c in string if c.islower())

if upper_count > lower_count:
    print(string.upper())
elif upper_count == lower_count:
    print(string.lower())
else:
    print(string.lower())