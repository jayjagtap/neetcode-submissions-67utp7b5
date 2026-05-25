
from collections import Counter

# Counter  Counter([]) , Counter("".split), Counter.most_common(2)
text = "the quick brown fox jumps over the lazy dog the fox"

# a) Find the 3 most common words.
# b) How many times does the word "fox" appear? (access it like a dict)

c = Counter(text.split())
print(c.most_common(3))
print(c["fox"])

# defaultdict(int) defaults to 0, defaultdict(list), defaultdict(set)

transactions = [
    ("Alice", 50),
    ("Bob", 30),
    ("Alice", 80),
    ("Carol", 20),
    ("Bob", 60),
    ("Alice", 40),
]


# Using defaultdict, build a dict that maps each person to a list of their transaction amounts.
# Then in a separate loop, print each person and their total
from collections import defaultdict

txn_amounts = defaultdict(int) 
for name, amount in transactions: 
    txn_amounts[name]+=amount

print(txn_amounts)

students = [
    ("Alice",   "math"),
    ("Bob",     "science"),
    ("Alice",   "science"),
    ("Carol",   "math"),
    ("Bob",     "math"),
    ("Carol",   "science"),
    ("Alice",   "history"),
    ("Dave",    "math"),
]

# You have a list of (student, subject) enrollments.
# Three parts:
# a) Build a defaultdict mapping each student → list of subjects they're enrolled in.
# b) Using that dict, print only students enrolled in more than 2 subjects.
# c) Build a second defaultdict mapping each subject → number of students enrolled in it. (use defaultdict(int))


student_subjects = defaultdict(list)
for name, sub in students:
    student_subjects[name].append(sub)

# a 
print(student_subjects)

# b
print({name: subjects for name, subjects in student_subjects.items() if len(subjects)>2})

# c
subject_num = defaultdict(int)
for name, sub in students:
    subject_num[sub] += 1

print(subject_num)


# deque
from collections import deque

stream = [10, 25, 8, 33, 17, 42, 5, 28, 19, 36]
# Using a deque with maxlen=3, iterate through the stream and print the running average of the last 3 numbers at each step — but only once the window is full.

k = 3
d = deque(maxlen=k)
print(d)
sum = 0
for num in stream:
    d.append(num)
    sum += num
    if len(d) == k:
        print(f"{list(d)} -> avg: {sum/k}")
        sum -= d[0]
    
# heapq  Common Interview Patterns nums = [5, 1, 8, 3, 9, 2] heapq.nlargest(3, nums) # → [9, 8, 5] heapq.nsmallest(3, nums) # → [1, 2, 3]
# Time Complexity heapify O(n) , push O(logn), pop O(1)

scores = [
    ("Alice", 88),
    ("Bob",   95),
    ("Carol", 72),
    ("Dave",  95),
    ("Eve",   60),
]

# Two parts:
# a) Using heapq.nlargest, get the top 2 scores (full tuples).
# b) Using a max-heap (negation trick), push all scores in, then pop them out one by one to print names in order of highest score first.
import heapq

heapq.heapify(scores)
print(heapq.nlargest(2, scores, key=lambda p: p[1]))

scores_heap = []

# Create a Heap
for name, score in scores:
    heapq.heappush(scores_heap, (-score, name))

for score, name in scores:
    score, name = heapq.heappop(scores_heap)
    print(f"{name}: {-score}")

# Time Complexity
# heapify O(logn) , heappush O(log N), heappop O(1), nlargest O(n log K), nsmallest O(n log K)
# heap shines when your data is changing (streaming, dynamic inserts) and you always need the current min/max. For a static list, sorted() or nlargest is simpler.


# Itertools

from itertools import combinations
from itertools import permutations
from itertools import chain

players = ["Alice", "Bob", "Carol"]

print(list(combinations(players, 2)))
print(list(permutations(players, 2)))

a = [1, 2, 4, 5] 
b = ["a", "b", "c"]
c = [34, 12, 66]

print(list(chain(a,b,c)))

# Puzzle 12
nums = [1, 2, 3, 4, 5]

# Two parts:
# a) Using combinations, find all pairs that sum to 6.
# b) Using permutations, find all 2-digit arrangements from [1, 2, 3] where the first number is greater than the second.

sum6 = [(x,y) for x,y in combinations(nums, 2) if x+y == 6]
print(sum6)

nums = [1,2,3]

print([(x,y) for x, y in permutations(nums, 2) if x > y ])

# f strings and type hints
students = [
    {"name": "Alice",  "score": 0.9234},
    {"name": "Bob",    "score": 0.7891},
    {"name": "Carol",  "score": 0.8512},
]

# Print a formatted leaderboard using f-strings:
# 1. Alice    | 92.3%  
# 2. Bob      | 78.9%  
# 3. Carol    | 85.1%
# Requirements:

# Rank number from enumerate
# Name left-aligned in a field of 8 characters
# Score as a percentage with 1 decimal place

for i, x in enumerate(students, start=1):
    name, score = x["name"] , x["score"]
    print(f"{i}. {name:<10}   | {score:.2%}")


# Type Hints
name: str = "Alice"


def get_top_students(students: list, passing_score: int) -> list:
    result = []
    for student in students:
        if student["score"] >= passing_score:
            result.append(student["name"])
    return result


data = [
    {"name": "Alice", "score": 88},
    {"name": "Bob",   "score": 55},
    {"name": "Carol", "score": 91},
]

threshold = 60
print(get_top_students(data, threshold))

# orderedDict

from collections import OrderedDict


# LRU Cache Puzzle

cache = OrderedDict()
actions = ["page1", "page2", "page3", "page1", "page4"]
MAX = 3


for page in actions:

    if page in cache:
        cache.move_to_end(page)
    else:
        cache[page] = True 

        # Capacity Check 
        if len(cache) > MAX:
            cache.popitem(last=False)
    print(cache.keys())



# Sorting arrays to solve problems in O(nlogn) time complexity instead of O(n)

arr = [4, 1, 8, 3, 2, 7]
target = 9
# Expected: [(1, 8), (2, 7)]
# Given an unsorted array, find all pairs that sum to a target using the two-pointer approach. Return the pairs as values (not indices).

# Brute Force
pairs = []
for i in range((size := len(arr))):
    for j in range(i+1, size):
        if arr[i] + arr[j] ==  target:
            pairs.append((arr[i], arr[j]))

print(f"Pairs: {pairs}")


# Sort first and use 2 pointers. Time Complexit O(n log n)

def find_pairs(arr, target):
    i, j = 0, len(arr)-1
    arr = sorted(arr)
    pairs = []
    while i < j:
        sum = arr[i] + arr[j]
        if sum > target:
            j-=1
        elif sum < target:
            i+=1
        else: # target = sum , move to next set of numbers
            pairs.append((arr[i], arr[j]))
            i+=1
            j-=1

    return pairs

print(find_pairs(arr, target))
        























