num, current, steps = map(int, input().split())

initial_step = current - 1

current_position = (initial_step + steps) % num
if current_position < 0:
    current_position += num

print(current_position + 1)
