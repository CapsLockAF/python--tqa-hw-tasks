### Task 6. Python Tuples, Sets, Dictionaries

##### Task 1. Get Sum of People's Budget

Create the function **get_budgets()** that takes a list of dictionaries and returns the sum of people's budgets.

_Examples_
```plaintext
get_budgets([
  { "name": "John", "age": 21, "budget": 23000 },
  { "name": "Steve",  "age": 32, "budget": 40000 },
  { "name": "Martin",  "age": 16, "budget": 2700 }
]) ➞ 65700

get_budgets([
  { "name": "John",  "age": 21, "budget": 29000 },
  { "name": "Steve",  "age": 32, "budget": 32000 },
  { "name": "Martin",  "age": 16, "budget": 1600 }
]) ➞ 62600
```

##### Task 2. Get Student Names

Create a function **get_student_names()** that takes a dictionary of student names and returns a list of student names in alphabetical order.

_Examples_
```plaintext
get_student_names({
  "Student 1" : "Steve",
  "Student 2" : "Becky",
  "Student 3" : "John"
}) ➞ ["Becky", "John", "Steve"]
```  

##### Task 3. Filter Repeating Character Strings

Create a function **identical_filter()** that keeps only strings with repeating identical characters (in other words, it has a set size of 1).  

_Notes._
A string with a single character is trivially counted as a string with repeating identical characters.
If there are no strings with repeating identical characters, return an empty array

_Examples_
```plaintext
identical_filter(["aaaaaa", "bc", "d", "eeee", "xyz"])
➞ ["aaaaaa", "d", "eeee"]

identical_filter(["88", "999", "22", "545", "133"])
➞ ["88", "999", "22"]

identical_filter(["xxxxo", "oxo", "xox", "ooxxoo", "oxo"])
➞ []
```

##### Task 4. Subset Validation

Write a function **validate_subsets()** that returns _True_ if all subsets in a list belong to a given set.

_Notes._
The empty set and the set itself are both valid subsets of a set (we are not talking about proper subsets here).
The set and the subset will each have unique elements.  

_Examples_
```plaintext
validate_subsets([[1, 2], [2, 3], [1, 3]], [1, 2, 3]) ➞ True
validate_subsets([[1, 2, 3], [2], [3], []], [1, 2, 3]) ➞ True
validate_subsets([[1, 2], [2, 3], [1, 4]], [1, 2, 3]) ➞ False
validate_subsets([[1, 2, 3, 4]], [1, 2, 3]) ➞ False
```
  

##### Task 5. Priority Sort

Given a list and a set, define a function **priority_sort()** that return a sorted list with its items in ascending order but prioritize the elements in the set over the other items in the list.

_Notes_
- If the list is empty, return an empty list.
- If the set is empty there is nothing to prioritize, but the list should still be sorted.
- The set may contain values that are not in the list.
- The list may contain duplicates.
- The list and the set will only contain integer values.

_Examples_
```plaintext
priority_sort([5, 4, 3, 2, 1], {2, 3}) ➞ [2, 3, 1, 4, 5]
priority_sort([5, 4, 3, 2, 1], {3, 6}) ➞ [3, 1, 2, 4, 5]
priority_sort([-5, -4, -3, -2, -1, 0], {-4, -3}) ➞ [-4, -3, -5, -2, -1, 0]
```


##### Task 6. Find the Maximum Length of a Chain Consisting from the Given Pairs
The function **len_longest_chain()** is given a list of tuples. Each tuple has two numbers _tpl[0] < tpl[1]_. A chain can be made from these tuples that satisfies the condition: _(n1, n2) -> (n3, n4) -> ..._ for each pair of consecutive tuples _n2 < n3_. Find the maximum length of such chain made from the given list.

_Examples_  
```plaintext
len_longest_chain([(2, 3), (3, 4), (3, 5)]) ➞ 1
# Any of the given tuple make a chain of length 1
len_longest_chain([(2, 3), (3, 4), (1, 2)]) ➞ 2
# (1, 2) -> (3, 4) => len_chain = 2
len_longest_chain([(-15, -11), (17, 22), (8, 12), (-11, -10), (-4, -1)]) ➞ 4
# (-15, -11) -> (-4, -1) -> (8, 12) -> (17, 22) => len_chain = 4
len_longest_chain([(-5, 0), (-4, 0), (4, 5), (3, 4), (-1, 1), (-6, -2)]) ➞ 3
# (-6, -2) -> (-1, 1) -> (3, 4) => len_chain = 3
```
  
##### Task 7. Invert Colors
Create a function **color_invert()** that inverts the _rgb_ values of a given tuple.  
_Notes._  
- Must return a tuple.
- 255 is the max value of a single color channel.

_Examples_  
```plaintext
color_invert((255, 255, 255)) ➞ (0, 0, 0)
# (255, 255, 255) is the color white.
# The opposite is (0, 0, 0), which is black.

color_invert((0, 0, 0)) ➞ (255, 255, 255)

color_invert((165, 170, 221)) ➞ (90, 85, 34)
```

  
##### Task 8. Are They the Same?
Create a function **check()** that takes three arguments (first dictionary, second dictionary, key) in order to:
- Return the boolean _True_ if both dictionaries have the same values for the same keys.
- If the dictionaries don't match, return the string _"Not the same"_, or the string _"One's empty"_ if only one of the dictionaries contains the given key.  
_Notes._  
- Dictionaries are an unordered data type.
- Double quotes may be helpful.
- _KeyError_ can occur when trying to access a dictionary key that doesn't exist.  

_Examples_  
```plaintext
dict_first = { "sky": "temple", "horde": "orcs", "people": 12, "story": "fine", "sun": "bright" }
dict_second = { "people": 12, "sun": "star", "book": "bad" }

check(dict_first, dict_second, "horde") ➞ "One's empty"

check(dict_first, dict_second, "people") ➞ True

check(dict_first, dict_second, "sun") ➞ "Not the same"
```


  

