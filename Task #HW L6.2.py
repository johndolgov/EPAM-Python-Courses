class Prop(object):
    """Descriptor Property which acts like decorator"""

    def __init__(self, function_to_get=None, function_to_set=None, function_to_delete=None):
        """Constructor of Descriptor
        :param - function_to_get
        :type - function
        :param - function_to_set
        :type - function
        :param - function_to_delete
        :type - function
        """
        self.function_to_get = function_to_get
        self.function_to_set = function_to_set
        self.function_to_delete = function_to_delete

    def __get__(self, instance, owner = None):
        """Method get for descriptor"""

        if instance is None:
            return self

        if self.function_to_get is None:
            raise AttributeError('You do not have attribute here')

        return self.function_to_get(instance)

    def __set__(self, instance, value):
        """Method set for descriptor"""

        if self.function_to_set is None:
            raise AttributeError('You can not set attribute')

        self.function_to_set(instance, value)

    def __delete__(self, instance):
        """Method delete for descriptor """

        if self.function_to_delete is None:
            raise AttributeError('You can not delete attribute')

        self.function_to_delete(instance)

class Something:

    def __init__(self,x):
        self.x = x
    @Prop
    def attr(self):
        return self.x**2

if __name__ == '__main__':
    s = Something(10)
    print(s.attr)