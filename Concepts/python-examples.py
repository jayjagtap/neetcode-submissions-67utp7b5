# Enumerate

words = ["python", "is", "awesome", "and", "fun"]

for i , word in enumerate(words, start=1):
    if i % 2 != 0:
        print(f"index {i} -> {word}")

# We can also traverse thorugh the tuples
new_list = list(enumerate(words))

for i, j in new_list:
    print(f"{i}", {j})


# zip
keys   = ["name", "age", "city"]
values = ["Alice", 30, "Boston"]

names = {}

for key, value in zip(keys, values):
    names[key] = value

print(names)

# One lines to convert it into dict

print(dict(zip(keys, values)))

# Topic 3: List / Dict / Set Comprehensions

sentence = "the quick brown fox jumps over the lazy dog"
sentence = sentence.split()

sentence_dict = {word: len(word) for word in sentence if len(word) > 3}
print(sentence_dict)

# flatten a 2d list

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

matrix_flat = [n for row in matrix for n in row]
print(matrix_flat)

# Using a set comprehension, get all unique grades from the list.

students = [
    {"name": "Alice", "grade": "A"},
    {"name": "Bob",   "grade": "B"},
    {"name": "Carol", "grade": "A"},
    {"name": "Dave",  "grade": "B"},
]

students_grades = {s["grade"] for s in students}
print(students_grades)

# Lambda

square = lambda x: x**2 
print(square(10))

products = [
    {"name": "banana", "price": 1.2},
    {"name": "apple",  "price": 0.8},
    {"name": "mango",  "price": 2.5},
    {"name": "grape",  "price": 1.8},
]

# Sort this list by price in descending order (most expensive first) using sorted() and a lambda. No extra variables — one line.

print(sorted(products, key=lambda p:-p["price"]))

# sorted 

words = ["banana", "fig", "kiwi", "apple"] 

print(sorted(words, key=len))
print(sorted(words, key=lambda p:len(p)))

list_names = [(12,2), (34,1), (23,4), (67,3)]

print(sorted(list_names, key=lambda p:p[1]))

names = ["alice", "Bob", "carol", "Dave"] 
print(sorted(names))

students = [
    {"name": "Dave",  "grade": "B", "score": 78},
    {"name": "Alice", "grade": "A", "score": 95},
    {"name": "Bob",   "grade": "A", "score": 88},
    {"name": "Carol", "grade": "B", "score": 82},
]

# Sort by grade ascending (A before B), then by score descending within the same grade. One line.

grades_sorted = sorted(students, key=lambda p: (p["grade"].upper(), -p["score"]))
print(grades_sorted)


# any() and all()

users = [
    {"name": "Alice", "active": True,  "age": 25},
    {"name": "Bob",   "active": False, "age": 17},
    {"name": "Carol", "active": True,  "age": 32},
    {"name": "Dave",  "active": True,  "age": 15},
]
# Answer both in one line each:
# a) Are all active users adults (age >= 18)?
# b) Is any user both inactive and under 18?

print(all(person["age"] > 18 for person in users if person["active"]))
print(any(person["active"] and person["age"] < 18 for person in users))


# Walrus Operator, compute once and use multiple times
import math
nums = [1, 4, 9, -1, 16, -4, 25]

# Using a list comprehension with the walrus operator, build a list of square roots — but only for numbers where the square root is greater than 2. Compute math.sqrt() only once per number.
import math

nums = [root for num in nums if num > 0 and (root := math.sqrt(num))  > 2]
print(nums)

import random
random.seed(42)

def get_value():
    return random.randint(0, 10)

while (value := get_value()) != 7:
    print(f"Got {value}")
print(f"Got: {value} - stopping")

# Combination Puzzles

# Puzzle A
subjects = ["math", "science", "english", "history"]
scores   = [88, 95, 72, 85]

subject_scores = { sub: score for sub, score in zip(subjects, scores) if score > 80}
print(subject_scores)

# Puzzle B
# Two parts:
# b1) Filter to only teams where all members are adults (≥ 18), then sort them by average age descending. Return a list of team names only.
# b2) Which teams have any member under 18? Return team names, one line.

teams = [
    {"team": "Alpha", "members": [22, 25, 17, 30]},
    {"team": "Beta",  "members": [19, 28, 24, 21]},
    {"team": "Gamma", "members": [16, 15, 20, 18]},
]
import math
# Filter to only teams where all members are adults
print(sorted([team for team in teams 
              if all(age >= 18 for age in team["members"])], key=lambda team: sum(team["members"])/len(team["members"])))

print([team["team"] for team in teams if any(age < 18 for age in team["members"])])

# Puzzle C

import math


data = [4, -1, 9, 0, 16, -9, 25, 3]
# Build a list of (number, sqrt) tuples for numbers where:

# The number is positive
# math.sqrt(num) (computed once via walrus) is not a whole number (i.e. the sqrt has a decimal part)

# Normal method
sqrt = [math.sqrt(a) if a > 0 else 0 for a in data]
print([(a,b) for a, b in zip(data, sqrt) if not b.is_integer()])

# Walrus operator
root = [(a, b) for a in nums if a > 0 and not (b := math.sqrt(a)).is_integer()]


    



















