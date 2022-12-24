import datetime
import time


def get_time():
    return datetime.datetime.now().microsecond%8


def func_sort(arg):
    res = []
    for i in range(arg):
        if i >= 0 and i <= 1:
          res.append(i+datetime.datetime.now().microsecond%10)
        elif i >= 2 and i <= 3:
            res.append(i*datetime.datetime.now().microsecond%10 - 2)
        elif i >= 4 and i <= 5:
            res.append(i+datetime.datetime.now().microsecond%10 + 4)
        elif i >= 6 and i <= 7:
            res.append(i*datetime.datetime.now().microsecond%10 - 1)
        elif i >= 8 and i <= 9:
            res.append(i*datetime.datetime.now().microsecond%10 + 3)
    some_res = 0
    try :
      some_res = (max(res) - min(res))
    except:
      some_res = (10 - datetime.datetime.now().microsecond%10 * 2)
    return some_res

n = get_time()
time.sleep(0.6)
m = func_sort(n)

if n < m:
  print(f'{n}, {m}')
elif n > m:
  print(f'{m}, {n}')
else:
    print(1 ,20)