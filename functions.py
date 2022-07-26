from ast import Lambda


def welcome():
    print("hello world !!!")


def add():
    a = int(input("enter the frst value :"))
    b = int(input("enter the second value :"))
    c = a + b
    print("the total of a and  b are ", c)

# add()


def sub(a, b):
    c = a-b
    print(c)


#sub(50, 20)
def mul():
    a = 10
    b = 20
    c = a*b
    return c


#x = mul()
# print(x)
def stu_name(*name):
    print(name)


#stu_name("jaya", 'sutha', 'ramu')
def bio(name, age):
    print("name is :", name, "age ", age)


#bio(name="sutha", age=18)
def user(name, city="cuddalore"):
    print("name is ", name, "age :", city)


# user("jayasutha")
#user("sutha", "madurai")
def total(marks):
    return sum(marks)


#print(total([20, 30, 50, 40, 10]))
def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * (factorial(x-1)))


# recursive
print("factorial :", factorial(5))

# lambda function


def c(a): return a+50


def c(a): return a + 50


print(c(5))
