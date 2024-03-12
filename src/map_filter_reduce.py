from functools import reduce
def cube(x):
    return x*x*x

l = [1 ,2,3,4,5,6]
#newl =[]
#for item in l:
    #newl.append(cube(item))

#print(newl)
print(list(map(cube , l)))


# filter function

def filter_function(a):
    return a>2


print(list(filter(filter_function , l)))


#reduce function

numbers = [1,2,3,4,5]

def sum(x,y):
    return x+y

mysum = reduce(sum , numbers)
print(mysum)
