class SchoolMember:
    """Class SchoolMember
    This class describes any school member (Student, Teacher)
    """
    def __init__(self,name,age):
        """Constructor of class
        :param - name
        :type - str
        :param - age
        :type - int
        """
        self._name = name
        self._age = age
        print('Создан SchoolMember: {}'.format(self._name))
    def show(self):
        """Method which show all information
        about object
        """
        show_dict = {}
        show_dict['Name'] = self._name
        show_dict['Age'] = self._age
        for key in show_dict:
            print('{}: {}'.format(key, show_dict[key]))

class Student(SchoolMember):
    """Class Student describes student"""
    def __init__(self,name,age,note):
        """Constructor of object
        :param - name
        :type - str
        :param - age
        :type - int
        :param - note
        :type - int
        """

        super().__init__(name,age)
        self._note = note
        print('Создан Student: {}'.format(self._name))

    def show(self):
        """Method which show all information
        about object
        """

        show_dict = {}
        show_dict['Name'] = self._name
        show_dict['Age'] = self._age
        show_dict['Note'] = self._note
        for key in show_dict:
            print('{}: {}'.format(key, show_dict[key]))

class Teacher(SchoolMember):
    """Class teacher describes teacher"""

    def __init__(self,name,age,salary):
        """Constructor of object
        :param - name
        :type - str
        :param - age
        :type - int
        :param - salary
        :type - int
        """
        super().__init__(name, age)
        self._salary = salary
        print('Создан Teacher: {}'.format(self._name))

    def show(self):
        """Method which show all information
        about object
        """

        show_dict = {}
        show_dict['Name'] = self._name
        show_dict['Age'] = self._age
        show_dict['Salary'] = self._salary
        for key in show_dict:
            print('{}: {}'.format(key, show_dict[key]))

if __name__ == '__main__':
    b = Student('Morty','16','5')
    b.show()

