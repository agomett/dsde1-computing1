'''
toys.py

Simple toy functions to get comfortable working 
with functions.
'''


# write a function that adds 1
# to the input and prints the result
def inc(a):
    a += 1
    print(a)

#inc(int(input('enter value: ')))

# write a function that adds 1
# to the input and returns the result
def inc_return(a):
    a += 1
    return a   # hint this is incomplete
    
#inc_return(int(input('enter value: '))) 


# write a function that adds
# the two input numbers together
# and returns the sum
def sum(a, b):
    c = a+b
    return (c)

#a = int(input('enter value for a: '))
#b = int(input('enter value for b: '))
#sum(a, b)


# write a function that takes two
# numbers, adds them together using 
# sum() and then increments the sum
# using inc_return
def sum_inc(a, b):
    return inc_return(sum(a,b))


#a = int(input('enter value for a: '))
#b = int(input('enter value for b: '))
#sum(a, b)
#sum_inc(a, b)

# write a function that returns a 
# boolean (True or False) for whether 
# the input number is even
def is_even(a):
    print(a%2 == 0)
    return a%2 == 0

#a = int(input('enter value for a: '))
#b = int(input('enter value for b: '))
#is_even(a, b)



# create a for loop that takes a string
# and an integer and returns a new string 
# that is the string repeated equal to 
# integer
# e.g. string_repeat('ho', 3) returns
# 'hohoho'
def string_repeat(phrase, repeat):
    print(phrase*repeat)
    # hint: you can add strings together
    # in order to concatenate them
    return(phrase*repeat)

#phrase = str(input('enter word: '))
#repeat = int(input('enter number: '))
#string_repeat(a, b)
