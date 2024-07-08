h,m = map(int,input().split(':'))

minute_angle = m * 6
hour_angle = (h % 12) * 30 + m * 0.5
if hour_angle == int(hour_angle):
    print(f"{int(hour_angle)} {minute_angle}")
else:
    print(f"{hour_angle} {minute_angle}")