def pair_division():
    """This function allow to divide two number
    :return - result of division or message about exception
    """
    n = int(input('Please enter quantity of your attempts '))
    for i in range(n):
        l = input('Please enter a pair of numbers').split()
        msgs = []
        if len(l) != 2:
            print('You must enter a pair')
        try:
            msgs.append(int(l[0])/int(l[1]))
        except (ZeroDivisionError, ValueError) as e:
            msgs.append('Error code: {}'.format(e))

    for msg in msgs:
        print (msg)

if __name__ == '__main__':
    pair_division()