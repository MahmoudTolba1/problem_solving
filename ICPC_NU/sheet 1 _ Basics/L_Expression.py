a,b,c = int(input()), int(input()), int(input())

def max_expression_value(a, b, c):
    expressions = [
        a + b + c,
        a + (b * c),
        (a + b) * c,
        a * b * c,
        (a * b) + c,
        a * (b + c)
    ]
    return max(expressions)

print(max_expression_value(a, b, c))