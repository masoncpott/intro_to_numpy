import numpy


### example of a numpy array ###
a = numpy.arange(27)

print(a) #prints a n-dimensional-array from 0 to 26

b = a.reshape(3, 9) # create a two dimensional array

print(b)

c = a.reshape(3, 3, 3) # prints a 3 dimensional array

print(c)







### convert a python list to a numpy array ###

d = numpy.asarray([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15])

print(type(d), d) # looks like a list but is actually of data type numpy.ndarray

