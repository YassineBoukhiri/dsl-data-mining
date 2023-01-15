a  = 1, 2, 3
print(type(a))

import re 

class InputParam:
    def __init__(self, input):
        self.input = input
    
    def __or__(self, other):
        return self.input + other.input

x = InputParam("x")
y = InputParam("y")
print(x | y)

b = [i for i in range(1,10,2)]
def to_range(input: InputParam):
    # check if input match pattern [%s-%s]
    print(input)
    if re.match(r'\[([0-9]+):([0-9]+)\]', input):
        print('match')
        print('first number : ' + re.match(r'\[([0-9]+):([0-9]+)\]', input).group(1))
        print('second number : ' + re.match(r'\[([0-9]+):([0-9]+)\]', input).group(2))
    else: 
        print("no match")

to_range([1:2])
