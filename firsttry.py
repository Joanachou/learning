def sayhello(someone):
    print(someone, "says hello")
    return 10


n=sayhello("Julia")
print(n)


def plus(x, y=5, retun=None):
    #x = int(input("please input the number:"))
    #y = int(input("please input another number:"))
    print(x + y)
    return 1000


nm=plus(6,10)
print(nm)


def hello(name='China'):
    print('hello',name)

hello('python')


def double(a):
    return a * 2

x = 3
y = double(x)
print(y)

def plus(num1, num2):
   print(num1+num2)
   return 100

x = plus(3, 4)
y = x * 5
print(y)

a=3
m=print(a)
print(type(m))

