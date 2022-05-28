# *args
def sum_caculator(*args):
    sum = 0
    for n in args:
        sum += n # sum = sum + n

    print(sum)

# **kwargs
def info(**kwargs):
    print("Data type of argument:",type(kwargs))

    for key, value in kwargs.items():
        print(f"{key} is {value}.")
    
