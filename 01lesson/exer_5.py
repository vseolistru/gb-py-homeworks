""" Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.  """
def input_values(args):
    values = ["x", "y", "z"]
    a = []
    for i in range(args):
        a.append(input(f'Input Values {values[i]} - '))
    return a


def checkPredicate(args):
    state_left = not (args[0] or args[1] or args[2])
    state_right = not args[0] and not args[1] and not args[2]
    if state_left == state_right:
      return True
    return False


statement = input_values(3)

if checkPredicate(statement) == True:
    print('Result is a true')
else:
    print('Result is a false')