# flexible parameter in a function
# *args, **kwargs
def mean(*numbers):
    total=0
    for item in numbers:
        if isinstance(item,(int,float)):

            total+=item
        return total/len(numbers)

def report(**marks):
    total_marks=0
    for k,v in marks.items():
        print(f'{k} got {v} marks')
        total_marks += v
    return total_marks

print(report(ram=80,shyam=90,mini=60,ishu=70))
print(mean(1,2,3,4))
print(mean(3,4,5,6,7,8,9))
print(mean(34,6,789,908,4,5,322,67,89,34,54,65))
print(mean(12,'b',5,'444',69,76))