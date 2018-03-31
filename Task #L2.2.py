def from_string_to_int(str):
    '''This function returns
    unique integer value for string'''
    if str == '':
        return None
    str = reversed(str)
    integer = 0
    power = 0
    for i in str:
        a = ord(i)
        integer += ord(i) * (10) ** (power)
        while a >= 10:
            a = a//10
            power += 1
        power += 1
    return integer
