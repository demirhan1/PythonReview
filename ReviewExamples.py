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

#---------------------------------------
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

#---------------------------------------

# Classes

class Person:
    def __init__(self, name, age):
        self.person_name = name
        self.person_age = age

    def birthday(self):
        self.person_age += 1

    def getName(self):
        return self.person_name
bob = Person('Bob', 32)
print(bob.getName())
# prints Bob

bob.birthday()
print(bob.person_age)
# prints 33

class Person:
    def __init__(self, name, age, month):
        self.name = name
        self.age = age
        self.birthday_month = month

    def birthday(self):
        self.age += 1


def create_person_objects(names, ages, months):
    my_data = zip(names, ages, months)
    person_objects = []
    for item in my_data:
        person_objects.append(Person(*item))
    return person_objects


def get_april_birthdays(people):
    # TODO:
    # Increment "age" for all people with birthdays in April.
    # Return a dictionary "april_birthdays" with the names of
    # all people with April birthdays as keys, and their updated ages
    # as values. See the test below for an example expected output.
    april_birthdays = {}
    for person in people:
        if person.birthday_month == 'April':
            person.age += 1
            april_birthdays[person.name] = person.age

    return april_birthdays


def get_most_common_month(people):
    # TODO: Use the "months" dictionary to record counts of
    # birthday months for persons in the "people" data.
    # Return the month with the largest number of birthdays.
    months = {'January': 0, 'February': 0, 'March': 0, 'April': 0, 'May': 0,
              'June': 0, 'July': 0, 'August': 0, 'September': 0, 'October': 0,
              'November': 0, 'December': 0}

    for person in people:
        months[person.birthday_month] += 1

    max_month = None
    max_value = 0
    for key in months.keys():
        if months[key] > max_value:
            max_value = months[key]
            max_month = key

    return max_month


def test():
    # Here is the data for the test. Assume there is a single most common month.
    names = ['Howard', 'Richard', 'Jules', 'Trula', 'Michael', 'Elizabeth', 'Richard', 'Shirley', 'Mark', 'Brianna',
             'Kenneth', 'Gwen', 'William', 'Rosa', 'Denver', 'Shelly', 'Sammy', 'Maryann', 'Kathleen', 'Andrew',
             'Joseph', 'Kathleen', 'Lisa', 'Viola', 'George', 'Bonnie', 'Robert', 'William', 'Sabrina', 'John',
             'Robert', 'Gil', 'Calvin', 'Robert', 'Dusty', 'Dario', 'Joeann', 'Terry', 'Alan', 'Rosa', 'Jeane', 'James',
             'Rachel', 'Tu', 'Chelsea', 'Andrea', 'Ernest', 'Erica', 'Priscilla', 'Carol', 'Michael', 'Dale', 'Arthur',
             'Helen', 'James', 'Donna', 'Patricia', 'Betty', 'Patricia', 'Mollie', 'Nicole', 'Ernest', 'Wendy',
             'Graciela', 'Teresa', 'Nicole', 'Trang', 'Caleb', 'Robert', 'Paul', 'Nieves', 'Arleen', 'Milton', 'James',
             'Lawrence', 'Edward', 'Susan', 'Patricia', 'Tana', 'Jessica', 'Suzanne', 'Darren', 'Arthur', 'Holly',
             'Mary', 'Randal', 'John', 'Laura', 'Betty', 'Chelsea', 'Margaret', 'Angel', 'Jeffrey', 'Mary', 'Donald',
             'David', 'Roger', 'Evan', 'Danny', 'William']
    ages = [17, 58, 79, 8, 10, 57, 4, 98, 19, 47, 81, 68, 48, 13, 39, 21, 98, 51, 49, 12, 24, 78, 36, 59, 3, 87, 94, 85,
            43, 69, 15, 52, 57, 36, 52, 5, 52, 5, 33, 10, 71, 28, 70, 9, 25, 28, 76, 71, 22, 35, 35, 100, 9, 95, 69, 52,
            66, 91, 39, 84, 65, 29, 20, 98, 30, 83, 30, 15, 88, 89, 24, 98, 62, 94, 86, 63, 34, 23, 23, 19, 10, 80, 88,
            67, 17, 91, 85, 97, 29, 7, 34, 38, 92, 29, 14, 52, 94, 62, 70, 22]
    months = ['January', 'March', 'January', 'October', 'April', 'February', 'August', 'January', 'June', 'August',
              'February', 'May', 'March', 'June', 'February', 'August', 'June', 'March', 'August', 'April', 'April',
              'June', 'April', 'June', 'February', 'September', 'March', 'July', 'September', 'December', 'June',
              'June', 'August', 'November', 'April', 'November', 'August', 'June', 'January', 'August', 'May', 'March',
              'March', 'March', 'May', 'September', 'August', 'April', 'February', 'April', 'May', 'March', 'March',
              'January', 'August', 'October', 'February', 'November', 'August', 'June', 'September', 'September',
              'January', 'September', 'July', 'July', 'December', 'June', 'April', 'February', 'August', 'September',
              'August', 'February', 'April', 'July', 'May', 'November', 'December', 'February', 'August', 'August',
              'September', 'December', 'February', 'March', 'June', 'December', 'February', 'May', 'April', 'July',
              'March', 'June', 'December', 'March', 'July', 'May', 'September', 'November']
    people = create_person_objects(names, ages, months)

    # Calls to the two functions you have completed.
    print(get_april_birthdays(people))
    print(get_most_common_month(people))


test()
# Expected result:
# {'Michael': 11, 'Erica': 72, 'Carol': 36, 'Lisa': 37, 'Lawrence': 87, 'Joseph': 25, 'Margaret': 35, 'Andrew': 13, 'Dusty': 53, 'Robert': 89}
# August
