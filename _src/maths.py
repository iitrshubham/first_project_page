class basic_1:
    """
    This class containing the grade 1 mathematical operations: Addition and substract.

    :param num1: First number
    :type num1: float
    :param num2: Second number
    :type num2: float


    """
    def __init__(self,num1,num2):
        """
        Class constructure
        """
        self.num1 = num1
        self.num2 = num2
    def add(self):
        """
        This function returns the sum of two numbers.

        :param num1: First number
        :type num1: float
        :param num2: Second number
        :type num2: float

        :return: sum of num1 and num2
        :rtype: float
        """        
        return self.num1+self.num2

    def subtract(self):
        """
        This function returns the subtraction of one number from another.

        :param num1: First number
        :type num1: float
        :param num2: Second number
        :type num2: float

        :returns: subtraction of num2 from num1
        :rtype: float
        """
        return self.num1-self.num2
    
class basic_2:
    """
    This class containing the grade 2 mathematical operations.
    
    This document is an awesome tool to explain the stuff

    :param num1: First number
    :type num1: float
    :param num2: Second number
    :type num2: float

    .. code-block:: python

        import maths as m
        nums = m.grade_2(6,2)
        div = nums.divide()
    
    """
    def __init__(self,num1,num2):
        """
        Class constructure

        """
        self.num1 = num1
        self.num2 = num2
    def multiply(self):
        """
        This function returns the multiplcation of two numbers.

        :param num1: First number
        :type num1: float
        :param num2: Second number
        :type num2: float

        :returns: multiplication of num1 and num2
        :rtype: float

        """
        return self.num1*self.num2
    def divide(self):
        """
        This function returns the division of two numbers.

        :param num1: First number
        :type num1: float
        :param num2: Second number
        :type num2: float

        :returns: division of num1 off num2
        :rtype: float
        """
        return self.num1/self.num2
        