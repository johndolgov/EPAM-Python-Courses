import time
import contextlib
import datetime


class ContextManagerError:

    """Context manager which allow to write text of the error in the file"""

    def __init__(self,file_path):

        """Constructor of class
        :param - file_path - path to the file into which error text will be written
        :type - string
        """
        self.start_time = None
        self.launch_date = None
        self.file_path = file_path

    def __enter__(self):

        """Defining of the Context Manager
        defining start_time for calculating program runtime
        defining launch_date for calculating today's date
        """

        self.start_time = time.time()
        self.launch_date = datetime.datetime.now()

    def __exit__(self, exc_type, exc_val, exc_tb):

        """Exiting from Context Manager
        If error happens file will be created
        and error text with date and program runtime will be written to this file
        """

        if exc_val:
            file = open(self.file_path,'w')
            file.write("There is an ERROR with type {}\n"
                       "This ERROR has value {}\n"
                       "Traceback of the ERROR is {}\n"
                       "It happens at date {}\n"
                       "Your program run time is {}".format(exc_type,exc_val,exc_tb,self.launch_date,
                                                             time.time()-self.start_time))
            file.close()


if __name__ == '__main__':
    def error():
        time.sleep(1)
        a = 1/0
    #with ContextManagerError('test.txt'):
    #    error()

    def withouterror():
        pass

    with ContextManagerError('test1.txt'):
        withouterror()

    def error2():
        a = [1,2,3,4]
        b = a[4]

    with ContextManagerError('test2.txt'):
        error2()
