from datetime import date

class Wine:
    """This class describes wine collection
    """
    def __init__(self,name,mark,country, birthyear, birthmonth, birthday, information=''):
        """Constructor of the object
        :param - name
        :type -
        :param - mark
        :type - str
        :param - country
        :type - str
        :param - birthyear
        :type - int
        :param - birthmonth
        :type - int
        :param - birthday
        :type - int
        :param - information
        :type - str
        """
        self._name = name
        self._mark = mark
        self._country = country
        self._birthyear = birthyear
        self._birthmonth = birthmonth
        self._birthday = birthday
        self._information = information

    @property
    def name(self):
        return self._name
    @property
    def mark(self):
        return self._mark
    @property
    def country(self):
        return self._country
    @property
    def birthyear(self):
        return self._birthyear
    @property
    def birthmonth(self):
        return self._birthmonth
    @property
    def birthday(self):
        return self._birthday
    @property
    def information(self):
        return  self._information
    @name.setter
    def name(self,new_name):
        self._name = new_name
    @mark.setter
    def mark(self,new_mark):
        self._mark = new_mark
    @country.setter
    def country(self,new_country):
        self._country = new_country
    @birthyear.setter
    def birthyear(self,new_year):
        self._birthyear = new_year
    @birthmonth.setter
    def birthmonth(self,new_month):
        self._birthmonth = new_month
    @birthday.setter
    def birthday(self,new_day):
        self._birthday = new_day
    @information.setter
    def information(self, new_information):
        self._information = new_information

    def Extract(self, current_year, current_month, current_day):
        """This method calculate quantity of the days
        :param - current_year
        :type - int
        :param - current_month
        :type - int
        :param - current_day
        :type - int
        :return - quantity of days from birth to exact date
        :type - date
        """
        return (date(current_year, current_month, current_day) - date(self.birthyear, self.birthmonth, self.birthday))

if __name__ == '__main__':
    b = Wine('Norm', 'Kol', 'stan',1993, 9, 20, 'Good Wine')
    print(b.Extract(2005, 8, 17))