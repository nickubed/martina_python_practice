# name is a "string"
my_name = 'Nick'
# age is an integer
my_age = 2021 - 1993
# alive is a boolean
is_alive = True

# conditional hinging on a boolean value of "my_name"
if(not my_name):
    print(len(my_name))
    print('Hey, we\'ve got a name')


my_hobbies = ['board games', 0, False, 'running', 'running']

person = {
    "name": None,
    "hobby": [],
    "age": 0
}

people = [
    {"name": "Martina", "hobby": "board games", "age": 27},
    {"name": "Nick", "hobby": "running", "age": 250},
    {"name": "Steve", "hobby": "running", "age": 25},
    {"name": "Amanda", "hobby": "running", "age": 37},
    {"name": "Barry", "hobby": "running", "age": 52}
]

# for i in range(0, 100):
#     print(i)
#     if(i == my_age):
#         print(f'🦩🦩🦩🦩🦩🦩🦩🦩 Age is: {i}')

# for person in people:
#     if person['hobby'] == 'running' and person['age'] < 30:
#         person['name'] = 'Running Man'

# for person in people:
#     if person['name'] == 'Running Man':
#         print(person['age'])

# for hobby in my_hobbies:
#     if(hobby == 'running'):
#         print(hobby)

# a condition to handle if the number is divisible by 3 >>> print "fizz"
# a condition to handle if the number is divisible by 5 >>> print "buzz"
# a condition to handle if the number is divisible by 3 & 5 >>> print "fizzbuzz"
# if the number does not pass these tests, print the number.

def fizzbuzz(number, string="fizzbuzz"):
    for i in range(1, number):
        if i % 3 == 0 and i % 5 == 0:
            print(string)
        elif i % 3 == 0:
            print('fizz')
        elif i % 5 == 0:
            print('buzz')
        else:
            print(i)

def greet(name="Nick"):
    return f'Hello {name}'


fizzbuzz(16, greet('Nick'))