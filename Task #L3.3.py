def validate(low_bound=0, upper_bound=256):
    """This decorator allow to create pixel
    if parameters of the pixel will more or less
    than lower or upper bound - you con not to call this function
    :param - low_bound and upper_bound
    :type - int"""
    def decorator(func):
        def wrapper(pix_values):
            bool = True
            for arg in pix_values:
                if arg < low_bound or arg > upper_bound:
                    bool = False
            if bool:
                func(pix_values)
            else:
                print('Function call is not valid!')
        return wrapper
    return decorator



@validate(low_bound=0, upper_bound=256)
def set_pixel(pixel_values):
    """This function creates pixel if lower and upper bound
    are normal
    :param - values of pixel
    :type - tuple"""
    print ('Pixel created!')

if __name__ == "__main__":
    pixel_values = (1,2,3)
    set_pixel(pixel_values)
    pixel_values = (257,1,2)
    set_pixel(pixel_values)
    pixel_values = (1,2,257)
    set_pixel(pixel_values)
