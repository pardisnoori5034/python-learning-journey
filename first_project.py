def my_sum(a, b):
    result = a+b
    print(result)

def my_sub(a, b):
    result = a-b
    print(result)

def my_mul(a, b):
    result = a*b
    print(result)

def my_div(a, b):
    result = a/b
    print(result)

def my_calculator():
    a = int(input("enter your first number \n"))
    b = int(input("enter your second nmber \n"))

    operator = input("enter your operator \n")

    if operator=="+":
        my_sum(a, b)
    elif operator=="-":
        my_sub(a, b)
    elif operator=="*":
        my_mul(a, b)
    elif operator=="/":
        my_div(a, b)
    else:
        print("our calculator can not efford this operation")

my_calculator()