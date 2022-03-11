# [Inheritance and Composition: A Python OOP Guide](https://realpython.com/inheritance-composition-python/)

## List of Contents:## Contents:

### 1. [What Are Inheritance and Composition?](#content-1)

### 2. [An Overview of Inheritance in Python](#content-2)

### 3. [Composition in Python](#content-3)

### 4. [Choosing Between Inheritance and Composition in Python](#content-4)

<br />

---

## Contents:

## [What Are Inheritance and Composition?](https://realpython.com/inheritance-composition-python/#what-are-inheritance-and-composition) <span id="content-1"></span>

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

**[⬆ back to top](#content-1)**

<br />

---

## [An Overview of Inheritance in Python](https://realpython.com/inheritance-composition-python/#an-overview-of-inheritance-in-python) <span id="content-2"></span>

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
- Evaluate MRO:

  ```python
  >>> from employees import TemporarySecretary
  >>> TemporarySecretary.__mro__

  (<class 'employees.TemporarySecretary'>,
  <class 'employees.HourlyEmployee'>,
  <class 'employees.Secretary'>,
  <class 'employees.SalaryEmployee'>,
  <class 'employees.Employee'>,
  <class 'object'>
  )
  ```

- The MRO shows the order in which Python is going to look for a matching attribute or method. In the example, this is what happens when we create the TemporarySecretary object:
  - The TemporarySecretary.**init**(self, id, name, hours_worked, hour_rate) method is called.
  - The super().**init**(id, name, hours_worked, hour_rate) call matches HourlyEmployee.**init**(self, id, name, hour_worked, hour_rate).
  - HourlyEmployee calls super().**init**(id, name), which the MRO is going to match to Secretary.**init**(), which is inherited from SalaryEmployee.**init**(self, id, name, weekly_salary).
- As you can see, multiple inheritance can be confusing, especially when you run into the diamond problem. <br />
  ![](https://files.realpython.com/media/ic-diamond-problem.8e685f12d3c2.jpg)
- Still, when you run into the diamond problem, it’s better to re-think the design. You will now make some changes to leverage multiple inheritance, avoiding the diamond problem.
- Inside productivity.py:

  ```python
  # In productivity.py

  class ProductivitySystem:
      def track(self, employees, hours):
          print('Tracking Employee Productivity')
          print('==============================')
          for employee in employees:
              result = employee.work(hours)
              print(f'{employee.name}: {result}')
          print('')

  class ManagerRole:
      def work(self, hours):
          return f'screams and yells for {hours} hours.'

  class SecretaryRole:
      def work(self, hours):
          return f'expends {hours} hours doing office paperwork.'

  class SalesRole:
      def work(self, hours):
          return f'expends {hours} hours on the phone.'

  class FactoryRole:
      def work(self, hours):
          return f'manufactures gadgets for {hours} hours.'
  ```

- Inside hr.py:

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

  class SalaryPolicy:
      def __init__(self, weekly_salary):
          self.weekly_salary = weekly_salary

      def calculate_payroll(self):
          return self.weekly_salary

  class HourlyPolicy:
      def __init__(self, hours_worked, hour_rate):
          self.hours_worked = hours_worked
          self.hour_rate = hour_rate

      def calculate_payroll(self):
          return self.hours_worked * self.hour_rate

  class CommissionPolicy(SalaryPolicy):
      def __init__(self, weekly_salary, commission):
          super().__init__(weekly_salary)
          self.commission = commission

      def calculate_payroll(self):
          fixed = super().calculate_payroll()
          return fixed + self.commission
  ```

- Inside employees.py:

  ```python
  # In employees.py

  from hr import (
      SalaryPolicy,
      CommissionPolicy,
      HourlyPolicy
  )
  from productivity import (
      ManagerRole,
      SecretaryRole,
      SalesRole,
      FactoryRole
  )

  class Employee:
      def __init__(self, id, name):
          self.id = id
          self.name = name

  class Manager(Employee, ManagerRole, SalaryPolicy):
      def __init__(self, id, name, weekly_salary):
          SalaryPolicy.__init__(self, weekly_salary)
          super().__init__(id, name)

  class Secretary(Employee, SecretaryRole, SalaryPolicy):
      def __init__(self, id, name, weekly_salary):
          SalaryPolicy.__init__(self, weekly_salary)
          super().__init__(id, name)

  class SalesPerson(Employee, SalesRole, CommissionPolicy):
      def __init__(self, id, name, weekly_salary, commission):
          CommissionPolicy.__init__(self, weekly_salary, commission)
          super().__init__(id, name)

  class FactoryWorker(Employee, FactoryRole, HourlyPolicy):
      def __init__(self, id, name, hours_worked, hour_rate):
          HourlyPolicy.__init__(self, hours_worked, hour_rate)
          super().__init__(id, name)

  class TemporarySecretary(Employee, SecretaryRole, HourlyPolicy):
      def __init__(self, id, name, hours_worked, hour_rate):
          HourlyPolicy.__init__(self, hours_worked, hour_rate)
          super().__init__(id, name)
  ```

- UML diagram for the new design: <br />
  ![](https://files.realpython.com/media/ic-inheritance-policies.0a0de2d42a25.jpg)

**[⬆ back to top](#content-1)**

<br />

---

## [Composition in Python](https://realpython.com/inheritance-composition-python/#composition-in-python) <span id="content-3"></span>

- Composition is an object oriented design concept that models a has a relationship.
- In composition, a class known as composite contains an object of another class known to as component. In other words, a composite class has a component of another class.
- Composition allows composite classes to reuse the implementation of the components it contains
- The composition relation between two classes is considered loosely coupled. That means that changes to the component class rarely affect the composite class, and changes to the composite class never affect the component class.
- When looking at two competing software designs, one based on inheritance and another based on composition, the composition solution usually is the most flexible.
- You’ve already used composition in our examples. If you look at the Employee class, you’ll see that it contains two attributes:
  - id to identify an employee.
  - name to contain the name of the employee.
  - These two attributes are objects that the Employee class has. Therefore, you can say that an Employee has an id and has a name.
- Another attribute for an Employee might be an Address:

  ```python
  # In contacts.py

  class Address:
      def __init__(self, street, city, state, zipcode, street2=''):
          self.street = street
          self.street2 = street2
          self.city = city
          self.state = state
          self.zipcode = zipcode

      def __str__(self):
          lines = [self.street]
          if self.street2:
              lines.append(self.street2)
          lines.append(f'{self.city}, {self.state} {self.zipcode}')
          return '\n'.join(lines)
  ```

- You can now add the Address to the Employee class through composition:

  ```python
  # In employees.py

  class Employee:
      def __init__(self, id, name):
          self.id = id
          self.name = name
          self.address = None
  ```

- Composition is a loosely coupled relationship that often doesn’t require the composite class to have knowledge of the component.
- The UML Diagram representing the relationship between Employee and Address looks like this: <br />
  ![](https://files.realpython.com/media/ic-employee-address.240e806b1101.jpg)
- Leverage address in payroll system:

  ```python
  # In hr.py

  class PayrollSystem:
      def calculate_payroll(self, employees):
          print('Calculating Payroll')
          print('===================')
          for employee in employees:
              print(f'Payroll for: {employee.id} - {employee.name}')
              print(f'- Check amount: {employee.calculate_payroll()}')
              if employee.address:
                  print('- Sent to:')
                  print(employee.address)
              print('')
  ```

### Flexible Designs With Composition

- Composition is more flexible than inheritance because it models a loosely coupled relationship. Changes to a component class have minimal or no effects on the composite class. Designs based on composition are more suitable to change.
- You can start by implementing the functionality of the ProductivitySystem:

  ```python
  # In productivity.py

  class ProductivitySystem:
      def __init__(self):
          self._roles = {
              'manager': ManagerRole,
              'secretary': SecretaryRole,
              'sales': SalesRole,
              'factory': FactoryRole,
          }

      def get_role(self, role_id):
          role_type = self._roles.get(role_id)
          if not role_type:
              raise ValueError('role_id')
          return role_type()

      def track(self, employees, hours):
          print('Tracking Employee Productivity')
          print('==============================')
          for employee in employees:
              employee.work(hours)
          print('')
  ```

- Implement different role classes:

  ```python
  # In productivity.py

  class ManagerRole:
      def perform_duties(self, hours):
          return f'screams and yells for {hours} hours.'

  class SecretaryRole:
      def perform_duties(self, hours):
          return f'does paperwork for {hours} hours.'

  class SalesRole:
      def perform_duties(self, hours):
          return f'expends {hours} hours on the phone.'

  class FactoryRole:
      def perform_duties(self, hours):
          return f'manufactures gadgets for {hours} hours.'
  ```

- Implement payroll system:

  ```python
  # In hr.py

  class PayrollSystem:
      def __init__(self):
          self._employee_policies = {
              1: SalaryPolicy(3000),
              2: SalaryPolicy(1500),
              3: CommissionPolicy(1000, 100),
              4: HourlyPolicy(15),
              5: HourlyPolicy(9)
          }

      def get_policy(self, employee_id):
          policy = self._employee_policies.get(employee_id)
          if not policy:
              return ValueError(employee_id)
          return policy

      def calculate_payroll(self, employees):
          print('Calculating Payroll')
          print('===================')
          for employee in employees:
              print(f'Payroll for: {employee.id} - {employee.name}')
              print(f'- Check amount: {employee.calculate_payroll()}')
              if employee.address:
                  print('- Sent to:')
                  print(employee.address)
              print('')
  ```

- Payroll policy classes:

  ```python
  # In hr.py

  class PayrollPolicy:
      def __init__(self):
          self.hours_worked = 0

      def track_work(self, hours):
          self.hours_worked += hours

  class SalaryPolicy(PayrollPolicy):
      def __init__(self, weekly_salary):
          super().__init__()
          self.weekly_salary = weekly_salary

      def calculate_payroll(self):
          return self.weekly_salary

  class HourlyPolicy(PayrollPolicy):
      def __init__(self, hour_rate):
          super().__init__()
          self.hour_rate = hour_rate

      def calculate_payroll(self):
          return self.hours_worked * self.hour_rate

  class CommissionPolicy(SalaryPolicy):
      def __init__(self, weekly_salary, commission_per_sale):
          super().__init__(weekly_salary)
          self.commission_per_sale = commission_per_sale

      @property
      def commission(self):
          sales = self.hours_worked / 5
          return sales * self.commission_per_sale

      def calculate_payroll(self):
          fixed = super().calculate_payroll()
          return fixed + self.commission
  ```

- Employee's contacts:

  ```python
  # In contacts.py

  class Address:
      def __init__(self, street, city, state, zipcode, street2=''):
          self.street = street
          self.street2 = street2
          self.city = city
          self.state = state
          self.zipcode = zipcode

      def __str__(self):
          lines = [self.street]
          if self.street2:
              lines.append(self.street2)
          lines.append(f'{self.city}, {self.state} {self.zipcode}')
          return '\n'.join(lines)
  ```

- Implementing EmployeeDatabase:

  ```python
  # In employees.py

  from productivity import ProductivitySystem
  from hr import PayrollSystem
  from contacts import AddressBook

  class EmployeeDatabase:
      def __init__(self):
          self._employees = [
              {
                  'id': 1,
                  'name': 'Mary Poppins',
                  'role': 'manager'
              },
              {
                  'id': 2,
                  'name': 'John Smith',
                  'role': 'secretary'
              },
              {
                  'id': 3,
                  'name': 'Kevin Bacon',
                  'role': 'sales'
              },
              {
                  'id': 4,
                  'name': 'Jane Doe',
                  'role': 'factory'
              },
              {
                  'id': 5,
                  'name': 'Robin Williams',
                  'role': 'secretary'
              },
          ]
          self.productivity = ProductivitySystem()
          self.payroll = PayrollSystem()
          self.employee_addresses = AddressBook()

      @property
      def employees(self):
          return [self._create_employee(**data) for data in self._employees]

      def _create_employee(self, id, name, role):
          address = self.employee_addresses.get_employee_address(id)
          employee_role = self.productivity.get_role(role)
          payroll_policy = self.payroll.get_policy(id)
          return Employee(id, name, address, employee_role, payroll_policy)
  ```

- Employee class:

  ```python
  # In employees.py

  class Employee:
      def __init__(self, id, name, address, role, payroll):
          self.id = id
          self.name = name
          self.address = address
          self.role = role
          self.payroll = payroll

      def work(self, hours):
          duties = self.role.perform_duties(hours)
          print(f'Employee {self.id} - {self.name}:')
          print(f'- {duties}')
          print('')
          self.payroll.track_work(hours)

      def calculate_payroll(self):
          return self.payroll.calculate_payroll()
  ```

- UML Diagram of the new design: <br />
  ![](https://robocrop.realpython.net/?url=https%3A//files.realpython.com/media/ic-policy-based-composition.6e78bdb5824f.jpg&w=609&sig=2a14268f94d82ac5f5c64d115f02f8eeea808580)
- Usage of the new design:

  ```python
  # In program.py

  from hr import PayrollSystem
  from productivity import ProductivitySystem
  from employees import EmployeeDatabase

  productivity_system = ProductivitySystem()
  payroll_system = PayrollSystem()
  employee_database = EmployeeDatabase()
  employees = employee_database.employees
  productivity_system.track(employees, 40)
  payroll_system.calculate_payroll(employees)
  ```

### Customizing Behavior With Composition

- Imagine that our manager all of a sudden becomes a temporary employee that gets paid by the hour. You can modify the object during the execution of the program in the following way:

  ```python
  # In program.py

  from hr import PayrollSystem, HourlyPolicy
  from productivity import ProductivitySystem
  from employees import EmployeeDatabase

  productivity_system = ProductivitySystem()
  payroll_system = PayrollSystem()
  employee_database = EmployeeDatabase()
  employees = employee_database.employees
  manager = employees[0]
  manager.payroll = HourlyPolicy(55)

  productivity_system.track(employees, 40)
  payroll_system.calculate_payroll(employees)
  ```

- The program gets the employee list from the EmployeeDatabase and retrieves the first employee, which is the manager we want. Then it creates a new HourlyPolicy initialized at $55 per hour and assigns it to the manager object.

**[⬆ back to top](#content-1)**

<br />

---

## [Choosing Between Inheritance and Composition in Python](https://realpython.com/inheritance-composition-python/#choosing-between-inheritance-and-composition-in-python) <span id="content-4"></span>

### Introduction

- The general advice is to use the relationship that creates fewer dependencies between two classes. This relation is composition. Still, there will be times where inheritance will make more sense.

### Inheritance to Model “Is A” Relationship

- Inheritance should only be used to model an is a relationship.
- Liskov’s substitution principle says that an object of type Derived, which inherits from Base, can replace an object of type Base without altering the desirable properties of a program.
- Fortunately, there is a simple test you can use to determine if your design follows Liskov’s substitution principle. Let’s say you have a class A that provides an implementation and interface you want to reuse in another class B. Your initial thought is that you can derive B from A and inherit both the interface and implementation. To be sure this is the right design, you follow theses steps:
  - Evaluate B is an A: Think about this relationship and justify it. Does it make sense?
  - Evaluate A is a B: Reverse the relationship and justify it. Does it also make sense?
- If you can justify both relationships, then you should never inherit those classes from one another.
- Concrete example:
  - You have a class Rectangle which exposes an .area property. You need a class Square, which also has an .area. It seems that a Square is a special type of Rectangle, so maybe you can derive from it and leverage both the interface and implementation.
  - Before you jump into the implementation, you use Liskov’s substitution principle to evaluate the relationship.
  - A Square is a Rectangle because its area is calculated from the product of its height times its length. The constraint is that Square.height and Square.length must be equal.
  - It makes sense. You can justify the relationship and explain why a Square is a Rectangle. Let’s reverse the relationship to see if it makes sense.
  - A Rectangle is a Square because its area is calculated from the product of its height times its length. The difference is that Rectangle.height and Rectangle.width can change independently.
  - It also makes sense. You can justify the relationship and describe the special constraints for each class. This is a good sign that these two classes should never derive from each other.
- First, you implement Rectangle. You’re even going to encapsulate the attributes to ensure that all the constraints are met:

  ```python
  # In rectangle_square_demo.py

  class Rectangle:
      def __init__(self, length, height):
          self._length = length
          self._height = height

      @property
      def area(self):
          return self._length * self._height
  ```

- Now, you derive Square from Rectangle and override the necessary interface to meet the constraints of a Square:

  ```python
  # In rectangle_square_demo.py

  class Square(Rectangle):
      def __init__(self, side_size):
          super().__init__(side_size, side_size)
  ```

- Small program to assert the above code:

  ```python
  # In rectangle_square_demo.py

  rectangle = Rectangle(2, 4)
  assert rectangle.area == 8

  square = Square(2)
  assert square.area == 4

  print('OK!')
  ```

- Later on, you need to support resizing Rectangle objects, so you make the appropriate changes to the class:

  ```python
  # In rectangle_square_demo.py

  class Rectangle:
      def __init__(self, length, height):
          self._length = length
          self._height = height

      @property
      def area(self):
          return self._length * self._height

      def resize(self, new_length, new_height):
          self._length = new_length
          self._height = new_height
  ```

- What happen if we're using the same method to Square?

  ```python
  # In rectangle_square_demo.py

  square.resize(3, 5)
  print(f'Square area: {square.area}')
  ```

- The reality is that if you’re able to justify an inheritance relationship between two classes both ways, you should not derive one class from another.
- In the example, it doesn’t make sense that Square inherits the interface and implementation of .resize() from Rectangle. That doesn’t mean that Square objects can’t be resized. It means that the interface is different because it only needs a side_size parameter.
- This difference in interface justifies not deriving Square from Rectangle like the test above advised.

### Mixing Features With Mixin Classes

- One of the uses of multiple inheritance in Python is to extend a class features through mixins. A mixin is a class that provides methods to other classes but are not considered a base class.
- A mixin allows other classes to reuse its interface and implementation without becoming a super class. They implement a unique behavior that can be aggregated to other unrelated classes. They are similar to composition but they create a stronger relationship.
- Let’s say you want to convert objects of certain types in your application to a dictionary representation of the object. You could provide a .to_dict() method in every class that you want to support this feature, but the implementation of .to_dict() seems to be very similar.
- This could be a good candidate for a mixin. You start by slightly modifying the Employee class from the composition example:

  ```python
  # In employees.py

  class Employee:
      def __init__(self, id, name, address, role, payroll):
          self.id = id
          self.name = name
          self.address = address
          self._role = role
          self._payroll = payroll


      def work(self, hours):
          duties = self._role.perform_duties(hours)
          print(f'Employee {self.id} - {self.name}:')
          print(f'- {duties}')
          print('')
          self._payroll.track_work(hours)

      def calculate_payroll(self):
          return self._payroll.calculate_payroll()
  ```

- The change is very small. You just changed the role and payroll attributes to be internal by adding a leading underscore to their name. You will see soon why you are making that change.

  ```python
  # In representations.py

  class AsDictionaryMixin:
      def to_dict(self):
          return {
              prop: self._represent(value)
              for prop, value in self.__dict__.items()
              if not self._is_internal(prop)
          }

      def _represent(self, value):
          if isinstance(value, object):
              if hasattr(value, 'to_dict'):
                  return value.to_dict()
              else:
                  return str(value)
          else:
              return value

      def _is_internal(self, prop):
          return prop.startswith('_')
  ```

- Modification to Employee:

  ```python
  # In employees.py

  from representations import AsDictionaryMixin

  class Employee(AsDictionaryMixin):
      def __init__(self, id, name, address, role, payroll):
          self.id = id
          self.name = name
          self.address = address
          self._role = role
          self._payroll = payroll

      def work(self, hours):
          duties = self._role.perform_duties(hours)
          print(f'Employee {self.id} - {self.name}:')
          print(f'- {duties}')
          print('')
          self._payroll.track_work(hours)

      def calculate_payroll(self):
          return self._payroll.calculate_payroll()
  ```

- AsDictionaryMixin for address:

  ```python
  # In contacts.py

  from representations import AsDictionaryMixin

  class Address(AsDictionaryMixin):
      def __init__(self, street, city, state, zipcode, street2=''):
          self.street = street
          self.street2 = street2
          self.city = city
          self.state = state
          self.zipcode = zipcode

      def __str__(self):
          lines = [self.street]
          if self.street2:
              lines.append(self.street2)
          lines.append(f'{self.city}, {self.state} {self.zipcode}')
          return '\n'.join(lines)
  ```

### Composition to Model “Has A” Relationship

- Composition models a has a relationship. With composition, a class Composite has an instance of class Component and can leverage its implementation. The Component class can be reused in other classes completely unrelated to the Composite.
- In the composition example above, the Employee class has an Address object. Address implements all the functionality to handle addresses, and it can be reused by other classes.
- The following changes might improve your design. You can start with the productivity module:

  ```python
  # In productivity.py

  class _ProductivitySystem:
      def __init__(self):
          self._roles = {
              'manager': ManagerRole,
              'secretary': SecretaryRole,
              'sales': SalesRole,
              'factory': FactoryRole,
          }

      def get_role(self, role_id):
          role_type = self._roles.get(role_id)
          if not role_type:
              raise ValueError('role_id')
          return role_type()

      def track(self, employees, hours):
          print('Tracking Employee Productivity')
          print('==============================')
          for employee in employees:
              employee.work(hours)
          print('')

  # Role classes implementation omitted

  _productivity_system = _ProductivitySystem()

  def get_role(role_id):
      return _productivity_system.get_role(role_id)

  def track(employees, hours):
      _productivity_system.track(employees, hours)
  ```

- First, you make the \_ProductivitySystem class internal, and then provide a \_productivity_system internal variable to the module. You are communicating to other developers that they should not create or use the \_ProductivitySystem directly. Instead, you provide two functions, get_role() and track(), as the public interface to the module. This is what other modules should use.
- What you are saying is that the \_ProductivitySystem is a Singleton, and there should only be one object created from it.
- Inside hr module:

  ```python
  # In hr.py

  class _PayrollSystem:
      def __init__(self):
          self._employee_policies = {
              1: SalaryPolicy(3000),
              2: SalaryPolicy(1500),
              3: CommissionPolicy(1000, 100),
              4: HourlyPolicy(15),
              5: HourlyPolicy(9)
          }

      def get_policy(self, employee_id):
          policy = self._employee_policies.get(employee_id)
          if not policy:
              return ValueError(employee_id)
          return policy

      def calculate_payroll(self, employees):
          print('Calculating Payroll')
          print('===================')
          for employee in employees:
              print(f'Payroll for: {employee.id} - {employee.name}')
              print(f'- Check amount: {employee.calculate_payroll()}')
              if employee.address:
                  print('- Sent to:')
                  print(employee.address)
              print('')

  # Policy classes implementation omitted

  _payroll_system = _PayrollSystem()

  def get_policy(employee_id):
      return _payroll_system.get_policy(employee_id)

  def calculate_payroll(employees):
      _payroll_system.calculate_payroll(employees)
  ```

- For the address:

  ```python
  # In contacts.py

  class _AddressBook:
      def __init__(self):
          self._employee_addresses = {
              1: Address('121 Admin Rd.', 'Concord', 'NH', '03301'),
              2: Address('67 Paperwork Ave', 'Manchester', 'NH', '03101'),
              3: Address('15 Rose St', 'Concord', 'NH', '03301', 'Apt. B-1'),
              4: Address('39 Sole St.', 'Concord', 'NH', '03301'),
              5: Address('99 Mountain Rd.', 'Concord', 'NH', '03301'),
          }

      def get_employee_address(self, employee_id):
          address = self._employee_addresses.get(employee_id)
          if not address:
              raise ValueError(employee_id)
          return address

  # Implementation of Address class omitted

  _address_book = _AddressBook()

  def get_employee_address(employee_id):
      return _address_book.get_employee_address(employee_id)
  ```

- You are basically saying that there should only be one \_AddressBook, one \_PayrollSystem, and one \_ProductivitySystem. Again, this design pattern is called the Singleton design pattern, which comes in handy for classes from which there should only be one, single instance.
- Changing the EmployeeDatabase:

  ```python
  # In employees.py

  from productivity import get_role
  from hr import get_policy
  from contacts import get_employee_address
  from representations import AsDictionaryMixin

  class _EmployeeDatabase:
      def __init__(self):
          self._employees = {
              1: {
                  'name': 'Mary Poppins',
                  'role': 'manager'
              },
              2: {
                  'name': 'John Smith',
                  'role': 'secretary'
              },
              3: {
                  'name': 'Kevin Bacon',
                  'role': 'sales'
              },
              4: {
                  'name': 'Jane Doe',
                  'role': 'factory'
              },
              5: {
                  'name': 'Robin Williams',
                  'role': 'secretary'
              }
          }


      @property
      def employees(self):
          return [Employee(id_) for id_ in sorted(self._employees)]

      def get_employee_info(self, employee_id):
          info = self._employees.get(employee_id)
          if not info:
              raise ValueError(employee_id)
          return info

  class Employee(AsDictionaryMixin):
      def __init__(self, id):
          self.id = id
          info = employee_database.get_employee_info(self.id)
          self.name = info.get('name')
          self.address = get_employee_address(self.id)
          self._role = get_role(info.get('role'))
          self._payroll = get_policy(self.id)

      def work(self, hours):
          duties = self._role.perform_duties(hours)
          print(f'Employee {self.id} - {self.name}:')
          print(f'- {duties}')
          print('')
          self._payroll.track_work(hours)

      def calculate_payroll(self):
          return self._payroll.calculate_payroll()


  employee_database = _EmployeeDatabase()
  ```

- Changing the main program:

  ```python
  # In program.py

  import json

  from hr import calculate_payroll
  from productivity import track
  from employees import employee_database, Employee

  def print_dict(d):
      print(json.dumps(d, indent=2))

  employees = employee_database.employees

  track(employees, 40)
  calculate_payroll(employees)

  temp_secretary = Employee(5)
  print('Temporary Secretary:')
  print_dict(temp_secretary.to_dict())
  ```

### Composition to Change Run-Time Behavior

- Inheritance, as opposed to composition, is a tightly couple relationship. With inheritance, there is only one way to change and customize behavior. Method overriding is the only way to customize the behavior of a base class. This creates rigid designs that are difficult to change.
- Add a new policy:

  ```python
  # In hr.py

  class LTDPolicy:
      def __init__(self):
          self._base_policy = None

      def track_work(self, hours):
          self._check_base_policy()
          return self._base_policy.track_work(hours)

      def calculate_payroll(self):
          self._check_base_policy()
          base_salary = self._base_policy.calculate_payroll()
          return base_salary * 0.6

      def apply_to_policy(self, base_policy):
          self._base_policy = base_policy

      def _check_base_policy(self):
          if not self._base_policy:
              raise RuntimeError('Base policy missing')
  ```

- Adjusting Employee class:

  ```python
  # In employees.py

  class Employee(AsDictionaryMixin):
      def __init__(self, id):
          self.id = id
          info = employee_database.get_employee_info(self.id)
          self.name = info.get('name')
          self.address = get_employee_address(self.id)
          self._role = get_role(info.get('role'))
          self._payroll = get_policy(self.id)


      def work(self, hours):
          duties = self._role.perform_duties(hours)
          print(f'Employee {self.id} - {self.name}:')
          print(f'- {duties}')
          print('')
          self._payroll.track_work(hours)

      def calculate_payroll(self):
          return self._payroll.calculate_payroll()

      def apply_payroll_policy(self, new_policy):
          new_policy.apply_to_policy(self._payroll)
          self._payroll = new_policy
  ```

- New program:

  ```python
  # In program.py

  from hr import calculate_payroll, LTDPolicy
  from productivity import track
  from employees import employee_database

  employees = employee_database.employees

  sales_employee = employees[2]
  ltd_policy = LTDPolicy()
  sales_employee.apply_payroll_policy(ltd_policy)

  track(employees, 40)
  calculate_payroll(employees)
  ```

### Choosing Between Inheritance and Composition in Python

- Python, as an object oriented programming language, supports both inheritance and composition. You saw that inheritance is best used to model an is a relationship, whereas composition models a has a relationship.
- Sometimes, it’s hard to see what the relationship between two classes should be, but you can follow these guidelines:
  - Use inheritance over composition in Python to model a clear is a relationship. First, justify the relationship between the derived class and its base. Then, reverse the relationship and try to justify it. If you can justify the relationship in both directions, then you should not use inheritance between them.
  - Use inheritance over composition in Python to leverage both the interface and implementation of the base class.
  - Use inheritance over composition in Python to provide mixin features to several unrelated classes when there is only one implementation of that feature.
  - Use composition over inheritance in Python to model a has a relationship that leverages the implementation of the component class.
  - Use composition over inheritance in Python to create components that can be reused by multiple classes in your Python applications.
    = Use composition over inheritance in Python to implement groups of behaviors and policies that can be applied interchangeably to other classes to customize their behavior.
  - Use composition over inheritance in Python to enable run-time behavior changes without affecting existing classes.

**[⬆ back to top](#content-1)**

<br />

---

## References:

- https://realpython.com/inheritance-composition-python
