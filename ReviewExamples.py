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
# Correct output: 2

print(smallest_positive([.2, 5, 3, -.1, 7, 7, 6]))
# Correct output: 0.2

print(smallest_positive([-6, -9, -7]))
# Correct output: None

print(smallest_positive([]))
# Correct output: None

