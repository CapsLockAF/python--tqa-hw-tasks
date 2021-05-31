## Task 8. OOP

#### Task 1. Make a Circle with OOP

Your task is to create a _Circle_ constructor that creates a circle with a radius provided by an argument.   
The circles constructed must have two getters _getArea() (PIr^2)_ and _getPerimeter() (2PI*r)_ which give both respective areas and perimeter (circumference).

For help with this class, I have provided you with a Rectangle constructor which you can use as a base example.
  
_Notes_
Round results up to the nearest integer.  

_Examples_  
```plaintext
circy = Circle(11)
circy.getArea()

# Should return 380.132711084365

circy = Circle(4.44)
circy.getPerimeter()

# Should return 27.897342763877365
```
  
 

#### Task 2. Simple OOP Calculator 

Create methods for the **Calculator** class that can do the following:

- Add two numbers.
- Subtract two numbers.
- Multiply two numbers.
- Divide two numbers.  

_Notes_  

The methods should return the result of the calculation.  

Don't worry about needing to handle division by zero errors.

_Examples_  
```plaintext
calculator = Calculator()
calculator.add(10, 5) ➞ 15
calculator.subtract(10, 5) ➞ 5
calculator.multiply(10, 5) ➞ 50
calculator.divide(10, 5) ➞ 2
```


#### Task 3. Food for Everyone!

Create a **Person** class which will have three properties:

- Name
- List of foods they like
- List of foods they hate  

In this class, create the method _taste()_:

It will take in a food name as a string.  

_Return {person_name} eats the {food_name}_.  

If the food is in the person's like list, add _'and loves it!'_ to the end.  

If it is in the person's hate list, add _'and hates it!'_ to the end.  

If it is in neither list, simply add an _exclamation mark_ to the end.  

_Notes_  

A person can have an empty list for foods they hate and/or love.

_Examples_  
```plaintext
p1 = Person("Sam", ["ice cream"], ["carrots"])
p1.taste("ice cream") ➞ "Sam eats the ice cream and loves it!"
p1.taste("cheese") ➞ "Sam eats the cheese!"
p1.taste("carrots") ➞ "Sam eats the carrots and hates it!"
```


#### Task 4. Ones, Threes and Nines

Given an int, figure out how many ones, threes and nines you could fit into the number.   
You must create a class **OnesThreesNines**. You will make variables (_self.ones, self.threes, self.nines_) to do this.

_Examples_  
```plaintext
n1 = OnesThreesNines(5)
n1.nines ➞ 0
n1.ones ➞ 5
n1.threes ➞ 1
```

#### Task 5. Classes For Fetching Information on a Sports Player

Create a class **Player** that takes the following four arguments for a particular football player:

- name
- age
- height
- weight  

Also, create three functions for the class that returns the following strings:

- get_age() returns "_name_ is age _age_"
- get_height() returns "_name_ is *heigh*tcm"
- get_weight() returns "_name_ weighs *weight*kg"
 
_Notes_  

_name_ will be passed in as a string and _age_, _height_, _weight_ will be integers.  

_Examples_  
```plaintext
p1 = Player("David Jones", 25, 175, 75)

p1.get_age() ➞ "David Jones is age 25"
p1.get_height() ➞ "David Jones is 175cm"
p1.get_weight() ➞ "David Jones weighs 75kg"
```
