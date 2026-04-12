def get_coins(amount):
    five = amount // 5
    while five >= 0:
        remainder = amount-(five*5)
        if remainder % 2 == 0:
            two = remainder // 2
            return five,two
        five -= 1
    return "not possible"
print(get_coins(30))