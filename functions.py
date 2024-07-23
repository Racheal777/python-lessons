# def introduce(name):
#     print(f"Hi i am {name}")
#     return name + ' Doe'
#
#
# print(introduce('Racheal'))
#
#
# # introduce('Ike')
#
# def multiply(num):
#     return num ** 2
#
#
# print(multiply(3))
#
#
# def multiply2(num):
#     result = multiply(num)
#     return num + result
#
# print(multiply2(4))
#
#
# def is_even(num):
#     return num % 2 != 1
#
# print(is_even(11))
#
# def find_max(x, y, z, i):
#     lists = [x, y, z, i]
#     max = 0
#     for i in lists:
#         if i > max:
#             max = i
#     return max
#
# print(find_max(8,3,5, 7))

# def find_max2(a,b,c):
#     return  max(a,b,c)
#
# print(find_max2(3,2,4))

from random import randint


def guess_the_number():
    lower = 1
    higher = 100

    secret_number = randint(lower, higher)

    while True:

        print(f'secret {secret_number}')


        try:
            guess = int(input('Enter your guess > '))

            if guess == secret_number:
                print("You are right, congrats")
                break
            elif guess != secret_number:
                if guess > 100 or guess < 1:
                    print( "your guess is out of range")
                elif guess < secret_number:
                    print("Too low")
                elif guess > secret_number:
                    print("Too high")
                else:
                    print('Number not in range')
        except ValueError:
            print(f'enter a whole  number between {lower} and {higher}')

guess_the_number()
