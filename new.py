print("hjhfg")
sdfsdfgsdgsdg
# line = f.readlines()
# print(line)
# for line in f:
#     print(line)
# f.close
# n = 10
# f = open('result.txt', 'w')
# for i in range(n, 2*n):
#     current_string = ' ' * (2*n-1-i) +  '* ' * i + '\n'
    
#     f.write(current_string)

# for i in range(2*n-2, n - 1, -1):
#     current_string = ' ' * (2*n-1-i) +  '* ' * i + '\n'
#     f.write(current_string)
# f.close()    
# n = 2
#  * *
# * * *
#  * *
# import requests
# print(requaests.get('https://google.com/').text)
d = {}
## Decorator
# import time
# def benchmark(inter = 10):
#     def decorator(func):
#         def wrapper(*args, **kwargs):
#             print('до функции')
#             start = time.time()
#             result = func()
#             func_name = func.__qualname__
#             d.update({func_name: d.get(func_name, 0) + 1})
#             # import pdb; pdb.set_trace()
#             finish = time.time()
#             print('после функции')
#             print(f'time work func: {(finish - start) / 10}')
#             return result
#         return wrapper
#     return decorator

# @benchmark(inter = 5)
# def hello(name = 'world'):
#     print(f'hello, {name}')
#     time.sleep(0.1)
# @benchmark(inter = 5)
# def name():
#     print(1234567)
# hello('Yan')
# name()
# print(d)

##Generator

# def countdown(n):
#     print('start working')
#     while n > 0:
#         yield n
#         n -= 1

# timer = countdown(10)
# for t in timer:
#     print(t)

# list = ['a', 'b', 'c', 'f']
# gen = (x for x in list)

# print(type(gen))
# for t in gen:
#     print(t)

# def check_log(path = None):
#     f = open(path, 'r')
#     for i,l in enumerate(f):
#         if 'ERROR 404' in l:
#             yield i + 1
#     f.close()
# logger = check_log('error.txt')
# for log in logger:
#     print(log)
