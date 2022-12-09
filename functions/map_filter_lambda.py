f=lambda x : x*5
print(f(7),f(67),f(-34))

# actual usage of lambda function
x=[23,45,67,22,87,41,82]

x2=list(map(lambda i: i**2,x))                # map function
print(x2)

a=[2,3,1,4,5,8,9]
b=[2,3,1,7,5,6,15]

ab= list(map(lambda i,j: i*j,a,b))            # map function with multiple list
print(ab)

# filter
evens = list(filter(lambda i:i%2==0,x))
print(evens)