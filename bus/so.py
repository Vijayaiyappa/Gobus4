  
from collections import deque

friends = deque(('Rolf', 'Jose', 'Charlie', 'Jen', 'Anna'))


def friend_upper():
    while friends:
        friend = friends.popleft().upper()
        greeting = yield
        
        print(f'{greeting} {friend}')

def greet(g):
    print("hello iam greet")
    print(g.__name__)
    yield from g
    print(g)


greeter = greet(friend_upper())
greeter.send(None)
greeter.send('Hello')
print('Hello, world! Multitasking..')
greeter.send('How are you,')