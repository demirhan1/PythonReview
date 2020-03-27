#Python Review with Examples

my_list = [7,1,2,3,4,5]

# Printing each value in my_list. Note you can use the "in" keyword to iterate over a list.
for item in my_list:
    print('The value of the item: ' + str(item))

# Printing each index and value pair.
for i, value in enumerate(my_list):
    print("The index value: " +str(i) + ". The value at i: " +str(value))

# Printing each number from 0 to 9 using a while loop.
i = 0
while(i<10):
    print(i)
    i+=1
# Printing each key and dictionary value. Note that you can use the "in" keyword
# to iterate over dictionary keys.
my_dict = {'a': 'max', 'b': 'tim', 'c': 'tin'}
for key in my_dict:
    print(key + ',' + my_dict[key])

# Output of the following code is [0, 1, 6, 9]
my_dict = {'a':[0, 1, 2, 3, 4], 'b':[0, 1, 2, 3,7], 'c':[0, 8, 6, 3,9], 'd':[3,0, 1, 9, 3]}
i = 0
output = []
for key in my_dict:
    output.append(my_dict[key][i])
    i += 1
print(output)

# Output is The number equals to 7
num = 7
if num < 7:
    print('The number is smaller than than 7')
elif num == 7:
    print('The number equals to 7')
else:
    print('The number is greater than the 7')

# TODO: Define a control structure that finds the smallest positive
# number in in_list and returns the correct smallest number.
def smallest_positive(in_list):
    smallest_pos = None
    for num in in_list:
        if num > 0:
            # Note: we use a logical "or" in this solution to form
            # the conditional statement, although this was
            # not introduced above.
            if smallest_pos == None or num < smallest_pos:
                smallest_pos = num
    return smallest_pos

# Test cases

print(smallest_positive([4, -6, 7, 2, -4, 10]))
# output: 2

print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
# output: 0.2

print(smallest_positive([-6, -9, -7]))
# output: None

print(smallest_positive([]))
# output: None

def when_offered(courses, course):
    # TODO: Fill out the function here.
    semesters = []
    for semester in courses:
        if course in courses[semester]:
            semesters.append(semester)
    # TODO: Return list of semesters here.
    return semesters

courses = {
    'spring2020': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Peter C.'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian',
                           'assistant': 'Andy'}},
    'fall2020': { 'cs101': {'name': 'Building a Search Engine',
                           'teacher': 'Dave',
                           'assistant': 'Sarah'},
                 'cs212': {'name': 'The Design of Computer Programs',
                           'teacher': 'Peter N.',
                           'assistant': 'Andy',
                           'prereq': 'cs101'},
                 'cs253': {'name': 'Web Application Engineering - Building a Blog',
                           'teacher': 'Steve',
                           'prereq': 'cs101'},
                 'cs262': {'name': 'Programming Languages - Building a Web Browser',
                           'teacher': 'Wes',
                           'assistant': 'Peter C.',
                           'prereq': 'cs101'},
                 'cs373': {'name': 'Programming a Robotic Car',
                           'teacher': 'Sebastian'},
                 'cs387': {'name': 'Applied Cryptography',
                           'teacher': 'Dave'}},
    'spring2044': { 'cs001': {'name': 'Building a Quantum Holodeck',
                           'teacher': 'Dorina'},
                        'cs003': {'name': 'Programming a Robotic Robotics Teacher',
                           'teacher': 'Jasper'},
                     }
    }


print(when_offered(courses, 'cs101'))
# Correct result:
# ['fall2020', 'spring2020']

print(when_offered(courses, 'bio893'))
# Correct result:
# []

# Function and Generator Review
# Python Functions
# Example function 1: return the sum of two numbers.
def sum(a, b):
    return a+b

# Example function 2: return the size of list, and modify the list to now be sorted.
def list_sort(my_list):
    my_list.sort()
    return len(my_list),  my_list

# Definition of the generator to produce even numbers.
def all_even():
    n = 0
    while True:
        yield n
        n += 2

my_gen = all_even()

# Generate the first 5 even numbers.
for i in range(5):
    print(next(my_gen))
    print('action')
# Now go and do some other processing.
do_something = 4
do_something += 3
print(do_something)
print('action 2')

# Now go back to generating more even numbers.
for i in range(7):
    print(next(my_gen))
    print('action 3')

# TODO change output to the product of a and b
def prod(a,b):

    return a*b

def fact_gen():
    i = 1
    n = i
    while True:
        output = prod(n, i)
        yield output
        # TODO: update i and n
        # Hint: i is a successive integer and n is the previous product
        i += 1
        n = output

# Test block
my_gen = fact_gen()
num = 5
for i in range(num):
    print(next(my_gen))

# Correct result when num = 5:
# 1
# 2
# 6
# 24
# 120

# An example solution for the check_sudoku() function
correct = [[1, 2, 3],
           [2, 3, 1],
           [3, 1, 2]]

incorrect = [[1, 2, 3, 4],
             [2, 3, 1, 3],
             [3, 1, 2, 3],
             [4, 4, 4, 4]]

incorrect2 = [[1, 2, 3, 4],
              [2, 3, 1, 4],
              [4, 1, 2, 3],
              [3, 4, 1, 2]]

incorrect3 = [[1, 2, 3, 4, 5],
              [2, 3, 1, 5, 6],
              [4, 5, 2, 1, 3],
              [3, 4, 5, 2, 1],
              [5, 6, 4, 3, 2]]

incorrect4 = [['a', 'b', 'c'],
              ['b', 'c', 'a'],
              ['c', 'a', 'b']]

incorrect5 = [[1, 1.5],
              [1.5, 1]]



# Define a function check_sudoku() here:
def check_sudoku(square):
    for row in square:
        # Create a list with the integers 1, 2, ..., n.
        # We will check that each number in the row is in the list
        # and remove the numbers from the list once they are verified
        # to ensure that each number only occurs once in the row.
        check_list = list(range(1, len(square[0]) + 1))
        for i in row:
            if i not in check_list:
                return False
            check_list.remove(i)
    for n in range(len(square[0])):
        # We do the same here for each column in the square.
        check_list = list(range(1, len(square[0]) + 1))
        for row in square:
            if row[n] not in check_list:
                return False
            check_list.remove(row[n])
    return True
print(check_sudoku(incorrect))
# >>> False

print(check_sudoku(correct))
# >>> True

print(check_sudoku(incorrect2))
# >>> False

print(check_sudoku(incorrect3))
# >>> False

print(check_sudoku(incorrect4))
# >>> False

print(check_sudoku(incorrect5))
# >>> False

