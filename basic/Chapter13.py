"""At this chapter we are learn about Custom Types
                        CHAPTER 13                  """

# ----------------------------------------------------------------------------------------------------------------------
# 13.1 Circle Objects


class Circle:
    """ Represents a geometric circle object """
    def __init__(self, center, radius):
        if radius < 0:
            raise ValueError("Negative radius")
        self.center = center
        self.radius = radius

    def get_radius(self):
        """ Return the radius of the circle """
        return self.radius

    def get_center(self):
        """ Return the center of the circle """
        return self.center

    def get_area(self):
        """ Compute and return the area of the circle """
        from math import pi
        return pi*self.radius*self.radius

    def get_circumference(self):
        """ Compute and return the circumference of the circle """
        from math import pi
        return 2*pi*self.radius

    def move(self, pt):
        """ Moves the enter of the circle to point pt """
        self.center = pt

    def grow(self):
        """ Increases the radius of the circle """
        self.radius += 1

    def shrink(self):
        """ Decreases the radius of the circle,
            does not effect a circle with radius zero"""
        if self.radius > 0:
            self.radius -= 1


# ----------------------------------------------------------------------------------------------------------------------
# 13.3 Restricting access to members

class MyClass:
    def __init__(self,name, age):
        self.__name = name
        self._age = age


# ----------------------------------------------------------------------------------------------------------------------
#13.3 Rational Numbers


class Rational:
    """
    Represents a rational number (fraction)
    """
    def __init__(self, numerator, denominator):
        self.__numerator = numerator
        if denominator != 0:
            self.__denominator = denominator
        else:
            raise ValueError("Attempt to make an illegal rational number")

    def get_numerator(self):
        """ Returns the numerator """
        return self.__numerator

    def get_denominator(self):
        """ Returns the denominator """
        return self.__denominator

    def set_numeraotor(self, n):
        """ Sets the numerator to n """
        self.__numerator = n

    def set_denominator(self, d):
        """ Sets the denominator of the fraction to d, unless d is zero """
        if d != 0:
            self.__denominator = d
        else:
            raise ValueError("Error: Zero denominator!")

    def __mul__(self, other):
        """ Returns the product of this rational number object
            with the other raional object """
        return Rational(self.__numerator * other.__numerator,
                        self.__denominator * other.__denominator)

    def __add__(self, other):
        """ Returns the sum of the rational number """
        pass

    def __str__(self):
        """Make string representation """
        return str(self.get_numerator()) + "/" + str(self.get_denominator())


# ----------------------------------------------------------------------------------------------------------------------
#13.4 Bank account objects


class BankAccount:
    """ Model a bank account """
    def __init__(self, number, name, balance):
        """ Initialize the instance variables of a bank account object.
            Disallows a negative initial balance """
        if balance < 0:
            raise ValueError("Negative initial balance")
        self.__account_number = number
        self.__name = name
        self.__balance = balance

    def id(self):
        """ Returns the account number of this bank object """
        return self.__account_number

    def deposit(self, amount):
        """ Add funds to the account. There is no limit to the size
            of the deposit """
        self.__balance += amount

    def withdraw(self, amount):
        """ Remove funds from account, if possible """
        result = False
        if self.__balance - amount >= 0:
            self.__balance -= amount
            result = True
        return result

    def __str__(self):
        """ Returns the string representation for this object """
        return '[{:>5} {:<10} {:>7} ]'.format(self.__account_number,
                                              self.__name, self.__balance)


# ----------------------------------------------------------------------------------------------------------------------
# 13.9 Dynamic Content
# it is mean that you can add another content to some class because python is dynamic


class Widget:
    def __init__(self):
        self.a = 5  # initialize the instance variable a to integer 5


class X:
    pass


# ----------------------------------------------------------------------------------------------------------------------
# main method


def main():
    x_obj = X()
    print(type(x_obj))
    print(type(X))
    print(x_obj.__class__)




if __name__ == "__main__":
    main()