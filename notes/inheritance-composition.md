# Inheritance and Composition

## Contents:

## [Inheritance and Composition: A Python OOP Guide](https://realpython.com/inheritance-composition-python/) <span id="content-1"></span>

### What’s Inheritance?

- Inheritance models what is called an is a relationship. This means that when you have a Derived class that inherits from a Base class, you created a relationship where Derived is a specialized version of Base.
- UML diagram for Inheritance: <br />
  ![](https://files.realpython.com/media/ic-basic-inheritance.f8dc9ffee4d7.jpg)
- In an inheritance relationship:
- Classes that inherit from another are called derived classes, subclasses, or subtypes.
- Classes from which other classes are derived are called base classes or super classes.
- A derived class is said to derive, inherit, or extend a base class.
- This is known as the Liskov substitution principle. The principle states that “in a computer program, if S is a subtype of T, then objects of type T may be replaced with objects of type S without altering any of the desired properties of the program”

### What’s Composition?

- Composition is a concept that models a has a relationship. It enables creating complex types by combining objects of other types. This means that a class Composite can contain an object of another class Component. This relationship means that a Composite has a Component. <br />
  ![](https://files.realpython.com/media/ic-basic-composition.8a15876f7db2.jpg)
- The composite side can express the cardinality of the relationship. The cardinality indicates the number or valid range of Component instances the Composite class will contain.
- In the diagram above, the 1 represents that the Composite class contains one object of type Component. Cardinality can be expressed in the following ways:
  - A number indicates the number of Component instances that are contained in the Composite.
  - The \* symbol indicates that the Composite class can contain a variable number of Component instances.
  - A range 1..4 indicates that the Composite class can contain a range of Component instances. The range is indicated with the minimum and maximum number of instances, or minimum and many instances like in 1..\*.
- Classes that contain objects of other classes are usually referred to as composites, where classes that are used to create more complex types are referred to as components.
- For example, your Horse class can be composed by another object of type Tail. Composition allows you to express that relationship by saying a Horse has a Tail.
- Composition enables you to reuse code by adding objects to other objects, as opposed to inheriting the interface and implementation of other classes. Both Horse and Dog classes can leverage the functionality of Tail through composition without deriving one class from the other.

### An Overview of Inheritance in Python

- Everything in Python is an object. Modules are objects, class definitions and functions are objects, and of course, objects created from classes are objects too.

### The Object Super Class

- dir() returns a list of all the members in the specified object.
- This is because every class you create in Python implicitly derives from object. You could be more explicit and write class MyClass(object):, but it’s redundant and unnecessary.

### Exceptions Are an Exception

- Every class that you create in Python will implicitly derive from object. The exception to this rule are classes used to indicate errors by raising an exception.
- What if you try to raise a class:

  ```python
  >>> class MyError:
  ...     pass
  ...
  >>> raise MyError()

  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  TypeError: exceptions must derive from BaseException
  ```

- You created a new class to indicate a type of error. Then you tried to use it to raise an exception. An exception is raised but the output states that the exception is of type TypeError not MyError and that all exceptions must derive from BaseException.
- BaseException is a base class provided for all error types. To create a new error type, you must derive your class from BaseException or one of its derived classes.
- The convention in Python is to derive your custom error types from Exception, which in turn derives from BaseException.
- This is the way you can create a custom Exception:

  ```python
  >>> class MyError(Exception):
  ...     pass
  ...
  >>> raise MyError()

  Traceback (most recent call last):
    File "<stdin>", line 1, in <module>
  __main__.MyError
  ```

### Creating Class Hierarchies

- Inheritance is the mechanism you’ll use to create hierarchies of related classes. These related classes will share a common interface that will be defined in the base classes.
- You start by implementing a PayrollSystem class that processes payroll:

  ```python
  # In hr.py

  class PayrollSystem:
      def calculate_payroll(self, employees):
          print('Calculating Payroll')
          print('===================')
          for employee in employees:
              print(f'Payroll for: {employee.id} - {employee.name}')
              print(f'- Check amount: {employee.calculate_payroll()}')
              print('')
  ```

- The PayrollSystem implements a .calculate_payroll() method that takes a collection of employees and prints their id, name, and check amount using the .calculate_payroll() method exposed on each employee object.
- Base class:

  ```python
  # In hr.py

  class Employee:
      def __init__(self, id, name):
          self.id = id
          self.name = name
  ```

- Employee is the base class for all employee types. It is constructed with an id and a name. What you are saying is that every Employee must have an id assigned as well as a name.
- The HR system requires that every Employee processed must provide a .calculate_payroll() interface that returns the weekly salary for the employee. The implementation of that interface differs depending on the type of Employee.
- For example, administrative workers have a fixed salary, so every week they get paid the same amount:

  ```python
  # In hr.py

  class SalaryEmployee(Employee):
      def __init__(self, id, name, weekly_salary):
          super().__init__(id, name)
          self.weekly_salary = weekly_salary

      def calculate_payroll(self):
          return self.weekly_salary
  ```

- You create a derived class SalaryEmployee that inherits Employee. The class is initialized with the id and name required by the base class, and you use super() to initialize the members of the base class.
- The company also employs manufacturing workers that are paid by the hour, so you add an HourlyEmployee to the HR system:

  ```python
  # In hr.py

  class HourlyEmployee(Employee):
      def __init__(self, id, name, hours_worked, hour_rate):
          super().__init__(id, name)
          self.hours_worked = hours_worked
          self.hour_rate = hour_rate

      def calculate_payroll(self):
          return self.hours_worked * self.hour_rate
  ```

- The HourlyEmployee class is initialized with id and name, like the base class, plus the hours_worked and the hour_rate required to calculate the payroll. The .calculate_payroll() method is implemented by returning the hours worked times the hour rate.
- Finally, the company employs sales associates that are paid through a fixed salary plus a commission based on their sales, so you create a CommissionEmployee class:

  ```python
  # In hr.py

  class CommissionEmployee(SalaryEmployee):
      def __init__(self, id, name, weekly_salary, commission):
          super().__init__(id, name, weekly_salary)
          self.commission = commission

      def calculate_payroll(self):
          fixed = super().calculate_payroll()
          return fixed + self.commission
  ```

- The problem with accessing the property directly is that if the implementation of SalaryEmployee.calculate_payroll() changes, then you’ll have to also change the implementation of CommissionEmployee.calculate_payroll(). It’s better to rely on the already implemented method in the base class and extend the functionality as needed.
- You created your first class hierarchy for the system. The UML diagram of the classes looks like this: <br />
  ![](https://files.realpython.com/media/ic-initial-employee-inheritance.b5f1e65cb8d1.jpg)
- The diagram shows the inheritance hierarchy of the classes. The derived classes implement the IPayrollCalculator interface, which is required by the PayrollSystem. The PayrollSystem.calculate_payroll() implementation requires that the employee objects passed contain an id, name, and calculate_payroll() implementation.
- Interfaces are represented similarly to classes with the word interface above the interface name. Interface names are usually prefixed with a capital I.
- The application creates its employees and passes them to the payroll system to process payroll:

  ```python
  # In program.py

  import hr

  salary_employee = hr.SalaryEmployee(1, 'John Smith', 1500)
  hourly_employee = hr.HourlyEmployee(2, 'Jane Doe', 40, 15)
  commission_employee = hr.CommissionEmployee(3, 'Kevin Bacon', 1000, 250)
  payroll_system = hr.PayrollSystem()
  payroll_system.calculate_payroll([
      salary_employee,
      hourly_employee,
      commission_employee
  ])
  ```

- Notice how the Employee base class doesn’t define a .calculate_payroll() method. This means that if you were to create a plain Employee object and pass it to the PayrollSystem, then you’d get an error.
- While you can instantiate an Employee object, the object can’t be used by the PayrollSystem. Why? Because it can’t .calculate_payroll() for an Employee. To meet the requirements of PayrollSystem, you’ll want to convert the Employee class, which is currently a concrete class, to an abstract class. That way, no employee is ever just an Employee, but one that implements .calculate_payroll().

### Abstract Base Classes in Python

- Abstract base classes exist to be inherited, but never instantiated.
- You can use leading underscores in your class name to communicate that objects of that class should not be created. Underscores provide a friendly way to prevent misuse of your code, but they don’t prevent eager users from creating instances of that class.
- Snippet:

  ```python
  # In hr.py

  from abc import ABC, abstractmethod

  class Employee(ABC):
      def __init__(self, id, name):
          self.id = id
          self.name = name

      @abstractmethod
      def calculate_payroll(self):
          pass
  ```

- You derive Employee from ABC, making it an abstract base class. Then, you decorate the .calculate_payroll() method with the @abstractmethod decorator.
- This change has two nice side-effects:
  - You’re telling users of the module that objects of type Employee can’t be created.
  - You’re telling other developers working on the hr module that if they derive from Employee, then they must override the .calculate_payroll() abstract method.

### Implementation Inheritance vs Interface Inheritance

- When you derive one class from another, the derived class inherits both:
  - The base class interface: The derived class inherits all the methods, properties, and attributes of the base class.
  - The base class implementation: The derived class inherits the code that implements the class interface.
- In Python, you don’t have to explicitly declare an interface. Any object that implements the desired interface can be used in place of another object. This is known as duck typing. Duck typing is usually explained as “if it behaves like a duck, then it’s a duck.”
- Snippet:

  ```python
  # In disgruntled.py

  class DisgruntledEmployee:
      def __init__(self, id, name):
          self.id = id
          self.name = name

      def calculate_payroll(self):
          return 1000000
  ```

- The PayrollSystem.calculate_payroll() requires a list of objects that implement the following interface:
  - An id property or attribute that returns the employee’s id
  - A name property or attribute that represents the employee’s name
  - A .calculate_payroll() method that doesn’t take any parameters and returns the payroll amount to process
- Since you don’t have to derive from a specific class for your objects to be reusable by the program, you may be asking why you should use inheritance instead of just implementing the desired interface. The following rules may help you:
  - Use inheritance to reuse an implementation: Your derived classes should leverage most of their base class implementation. They must also model an is a relationship. A Customer class might also have an id and a name, but a Customer is not an Employee, so you should not use inheritance.
  - Implement an interface to be reused: When you want your class to be reused by a specific part of your application, you implement the required interface in your class, but you don’t need to provide a base class, or inherit from another class.
- Final snippet:

  ```python
  # In hr.py

  class PayrollSystem:
      def calculate_payroll(self, employees):
          print('Calculating Payroll')
          print('===================')
          for employee in employees:
              print(f'Payroll for: {employee.id} - {employee.name}')
              print(f'- Check amount: {employee.calculate_payroll()}')
              print('')

  class Employee:
      def __init__(self, id, name):
          self.id = id
          self.name = name

  class SalaryEmployee(Employee):
      def __init__(self, id, name, weekly_salary):
          super().__init__(id, name)
          self.weekly_salary = weekly_salary

      def calculate_payroll(self):
          return self.weekly_salary

  class HourlyEmployee(Employee):
      def __init__(self, id, name, hours_worked, hour_rate):
          super().__init__(id, name)
          self.hours_worked = hours_worked
          self.hour_rate = hour_rate

      def calculate_payroll(self):
          return self.hours_worked * self.hour_rate

  class CommissionEmployee(SalaryEmployee):
      def __init__(self, id, name, weekly_salary, commission):
          super().__init__(id, name, weekly_salary)
          self.commission = commission

      def calculate_payroll(self):
          fixed = super().calculate_payroll()
          return fixed + self.commission
  ```

### The Class Explosion Problem

- If you are not careful, inheritance can lead you to a huge hierarchical structure of classes that is hard to understand and maintain. This is known as the class explosion problem.
- The ProductivitySystem tracks productivity based on employee roles. There are different employee roles:
  - Managers: They walk around yelling at people telling them what to do. They are salaried employees and make more money.
  - Secretaries: They do all the paper work for managers and ensure that everything gets billed and payed on time. They are also salaried employees but make less money.
  - Sales employees: They make a lot of phone calls to sell products. They have a salary, but they also get commissions for sales.
  - Factory workers: They manufacture the products for the company. They are paid by the hour.
- You create an employees module and move the classes there:

  ```python
  # In employees.py

  class Employee:
      def __init__(self, id, name):
          self.id = id
          self.name = name

  class SalaryEmployee(Employee):
      def __init__(self, id, name, weekly_salary):
          super().__init__(id, name)
          self.weekly_salary = weekly_salary

      def calculate_payroll(self):
          return self.weekly_salary

  class HourlyEmployee(Employee):
      def __init__(self, id, name, hours_worked, hour_rate):
          super().__init__(id, name)
          self.hours_worked = hours_worked
          self.hour_rate = hour_rate

      def calculate_payroll(self):
          return self.hours_worked * self.hour_rate

  class CommissionEmployee(SalaryEmployee):
      def __init__(self, id, name, weekly_salary, commission):
          super().__init__(id, name, weekly_salary)
          self.commission = commission

      def calculate_payroll(self):
          fixed = super().calculate_payroll()
          return fixed + self.commission
  ```

- With everything in place, you start adding the new classes:

  ```python
  # In employees.py

  class Manager(SalaryEmployee):
      def work(self, hours):
          print(f'{self.name} screams and yells for {hours} hours.')

  class Secretary(SalaryEmployee):
      def work(self, hours):
          print(f'{self.name} expends {hours} hours doing office paperwork.')

  class SalesPerson(CommissionEmployee):
      def work(self, hours):
          print(f'{self.name} expends {hours} hours on the phone.')

  class FactoryWorker(HourlyEmployee):
      def work(self, hours):
          print(f'{self.name} manufactures gadgets for {hours} hours.')
  ```

- ProductivitySystem class:

  ```python
  # In productivity.py

  class ProductivitySystem:
      def track(self, employees, hours):
          print('Tracking Employee Productivity')
          print('==============================')
          for employee in employees:
              employee.work(hours)
          print('')
  ```

- PayrollSystem and ProductivitySystem combined:

  ```python
  # In program.py

  import hr
  import employees
  import productivity

  manager = employees.Manager(1, 'Mary Poppins', 3000)
  secretary = employees.Secretary(2, 'John Smith', 1500)
  sales_guy = employees.SalesPerson(3, 'Kevin Bacon', 1000, 250)
  factory_worker = employees.FactoryWorker(2, 'Jane Doe', 40, 15)
  employees = [
      manager,
      secretary,
      sales_guy,
      factory_worker,
  ]
  productivity_system = productivity.ProductivitySystem()
  productivity_system.track(employees, 40)
  payroll_system = hr.PayrollSystem()
  payroll_system.calculate_payroll(employees)
  ```

- The program works as expected, but you had to add four new classes to support the changes. As new requirements come, your class hierarchy will inevitably grow, leading to the class explosion problem where your hierarchies will become so big that they’ll be hard to understand and maintain.
- New diagram for the new class hierarchy: <br />
  ![](https://files.realpython.com/media/ic-class-explosion.a3d42b8c9b91.jpg)

### Inheriting Multiple Classes

- Multiple inheritance is the ability to derive a class from multiple base classes at the same time.
- Instead, modern programming languages support the concept of interfaces. In those languages, you inherit from a single base class and then implement multiple interfaces, so your class can be re-used in different situations.
- Multiple inheritance code:

  ```python
  # In employees.py

  class TemporarySecretary(Secretary, HourlyEmployee):
      pass
  ```

- New modification:

  ```python
  import hr
  import employees
  import productivity

  manager = employees.Manager(1, 'Mary Poppins', 3000)
  secretary = employees.Secretary(2, 'John Smith', 1500)
  sales_guy = employees.SalesPerson(3, 'Kevin Bacon', 1000, 250)
  factory_worker = employees.FactoryWorker(4, 'Jane Doe', 40, 15)
  temporary_secretary = employees.TemporarySecretary(5, 'Robin Williams', 40, 9)
  company_employees = [
      manager,
      secretary,
      sales_guy,
      factory_worker,
      temporary_secretary,
  ]
  productivity_system = productivity.ProductivitySystem()
  productivity_system.track(company_employees, 40)
  payroll_system = hr.PayrollSystem()
  payroll_system.calculate_payroll(company_employees)
  ```

- You'll have problem to use the above code.
- When a method or attribute of a class is accessed, Python uses the class MRO to find it. The MRO is also used by super() to determine which method or attribute to invoke.

**[⬆ back to top](#list-of-contents)**

<br />

---

## References:

- https://realpython.com/inheritance-composition-python
