def coins(amount):
    five = amount//5
    while five >= 0:
        remainder = amount-(five*5)
        if remainder % 2 == 0:
            two = remainder // 2
            print(f"five {five} , two {two}")
            return
        five -= 1
    print("not possible")
amount = int(input("enter the amount."))
coins(amount)