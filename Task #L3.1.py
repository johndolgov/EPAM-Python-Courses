def from_string_to_int(str):
    '''This function returns
    unique integer value for string
    :param - str
    :type - string
    :return - integer
    :type - int
    '''
    if not str:
        return 0
    else:
        a = ord(str[-1])
        power = 0
        while a >= 10:
            a = a//10
            power += 1
        power += 1
        return ord(str[-1]) + from_string_to_int(str[:len(str)-1])*(10)**(power)

if __name__ == "__main__":
    print (from_string_to_int('abcd'))
    print (from_string_to_int('bdbfgd'))
    print (from_string_to_int('1234'))
