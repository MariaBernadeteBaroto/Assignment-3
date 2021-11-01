import math
amount_of_money = int(input('Enter Amount of Money: '))
apple = int(input('How much apple?: '))
price_apple = apple*15
change = amount_of_money - price_apple
number_of_apple = math.floor(amount_of_money/15)
print(f'You can buy {number_of_apple} apples and your change is {change} pesos.')
