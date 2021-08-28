def loop_example():
    for i in [1, 2, 3]:
        print(i)
        for j in [1, 2, 3]:
            print(j)
            print(i + j)
        print(i)
    print('done looping')

long_winded_computation = (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9)

list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

easer_to_read_list = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]

# Importing things
import re as regex

my_regex = regex.compile('[0-9]+', regex.I)

from collections import defaultdict, Counter

lookup = defaultdict(int)
my_counter = Counter()

# Functions
def double(x):
    """This is where we put docstrings"""
    return 2 * x

def apply_to_one(f):
    """Call the f function with 1 as an argument"""
    return f(1)

my_double = double

x = apply_to_one(my_double)

y = apply_to_one(lambda x: x + 4) # 2

# Default parameters
def my_print(message='my default message'):
    print(message)
    
def full_name(first="What's-his-name", last='something'):
    return first + ' ' + last

assert full_name('Josue', 'Canaviri') == 'Josue Canaviri'
assert full_name('Josue') == 'Josue something'
assert full_name(last='Canaviri') == "What's-his-name Canaviri"

# Strings can be delimited by single or double quotation marks 
# (but the quotes have to match)
single_quoted_string = 'data science'
double_quoted_string = "data science"

tab_string = '\tTitle'
no_tab_string = r'\tTitle'
multi_line_string = """This is the first line
this is the second line
and this is the third line."""

# f strings
first_name = 'Josue'
last_name = 'Canaviri'

full_name1 = first_name + ' ' + last_name
full_name2 = "{0} {1}".format(first_name, last_name)
full_name3 = f'{first_name} {last_name}'
# print(full_name3)

# Exceptions
try:
    result = 0 / 0
except ZeroDivisionError:
    print('Cannot divide by zero')

# ============
#    Lists
# ============
integer_list = [1, 2, 3]
heterogeneous_list = ['string', 0.1, True]
list_of_lists = [integer_list, heterogeneous_list, []]

list_length = len(integer_list)  # equals to 3
list_sum = sum(integer_list)     # equals to 6

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# Get an element
zero = x[0]
one = x[1]
nine = x[-1]
eigth = x[-2]

# Slicing
first_three = x[:3]     # [0, 1, 2]
three_to_end = x[3:]    # [3, 4, 5, 6, 7, 8, 9]
one_to_four = x[1:5]

last_three = x[-3:]
without_first_last = x[1:-1]

evens = x[::2]
odds = x[1::2]

assert 2 in [1, 2, 3]
assert not 42 in [1, 2, 3]

x = [1, 2, 3]
x.extend([4, 5, 6])
assert x == [1, 2, 3, 4, 5, 6]

x.append(7)
assert x == [1, 2, 3, 4, 5, 6, 7]

a, b = [3, 4]
_, y = [3, 4]

assert a == 3 and b == 4

# ============
#   Tuples
# ============
my_list = [1, 2]
my_list[0] = 7

my_tuple = (1, 2)
try:
    my_tuple[0] = 7
except TypeError:
    print('cannot change the value of a tuple')

def sum_and_product(x, y):
    return (x + y), (x * y)

sp = sum_and_product(4, 5)      # (9, 20)
s, p = sum_and_product(4, 5)    # 9, 20

# ================
#   Dictionaries
# ================
empty_dict = {} # Pythonic
empty_dict2 = dict() # less Pythonic
grades = {"Joel": 80, "Tim": 95} # dictionary literal

joels_grade = grades['Joel']

try:
    kates_grade = grades['Kate']
except KeyError:
    print('no grade for Kate!')

joel_has_grade = 'Joel' in grades   # True
kate_has_grade = 'Kate' in grades   # False

joels_grade = grades.get('Joel', 0) # equals 80
kates_grade = grades.get('Kate', 0) # equals 0
who_knows = grades.get('Who Knows') # default is None

grades["Tim"] = 99 # replaces the old value
grades["Kate"] = 100 # adds a third entry
num_students = len(grades) # equals 3
# Data structures
tweet = {
    "user" : "joelgrus",
    "text" : "Data Science is Awesome",
    "retweet_count" : 100,
    "hashtags" : ["#data", "#science", "#datascience",
    "#awesome", "#yolo"]
}

tweet_keys = tweet.keys() # iterable for the keys
tweet_values = tweet.values() # iterable for the values
tweet_items = tweet.items() # iterable for the (key, value) tuples

"user" in tweet_keys # True, but not Pythonic
"user" in tweet # Pythonic way of checking for keys
"joelgrus" in tweet_values # True (slow but the only way to check)


# counting words example
document = 'example texts'

word_counts = {}
for word in document:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

word_counts = {}
for word in document:
    try:
        word_counts[word] += 1
    except KeyError:
        word_counts[word] = 1

# All the code below can be replaced with this
from collections import Counter
c = Counter([0, 1, 2, 0])
word_counts = Counter(document)

# ========
#   Set
# ========
s = set()
s.add(1)
s.add(2)
s.add(2)

stopwords_list = ["a", "an", "at", "yet", "you"]
assert not 'zip' in stopwords_list

stopwords_set = set(stopwords_list)
assert not 'zip' in stopwords_list

item_list = [1, 2, 3, 1, 2, 3]
num_items = len(item_list) # 6
item_set = set(item_list) # {1, 2, 3}
num_distinct_items = len(item_set) # 3
distinct_item_list = list(item_set) # [1, 2, 3]

# IF ELSE statemets
if 1 > 2:
    message = 'if only 1 were greater than two...'
elif 1 > 3:
    message = 'elif stands for "else if"'
else:
    message = 'when all else fails use else (if you want to)'

# variable = true_value if cond else false_value
number = 17
is_even = "yes" if number % 2 == 0 else "no"
print(is_even)

# While loop
x = 0
while x < 5:
    # print(f'{x} is less thant 5')
    x += 1

for x in ['John', 'Susan', 'Dave']:
    pass
    # print(x)

x = [1, 2, 3]
y = [4, 5, 6]
for x, y in zip(x, y):
    print(f'{x} => {y}')

x = None
assert x == None, 'This is not the pythonic way to check for'
assert x is None, 'This is the pythonic way to check for None'

safe_x = x if x is not None else 0

all([True, 1, {3}])  # True
all([True, 1, {}])   # False
any([True, 1, {}])   # True
all([])              # True
any([])              # False


# Sorting
x = [4, 3, 1, 2]
y = sorted(x)   # now y is [1, 2, 3, 4]

# sort the list by absolute value from largest to smallest
x = sorted([-4, 1, -2, 3], key=abs, reverse=True) # is [-4, 3, -2, 1]
# sort the words and counts from highest count to lowest
wc = sorted(
    word_counts.items(),
    key=lambda word_and_count: word_and_count[1],
    reverse=True)

# List comprehensions
even_numbers = [x for x in range(5) if x % 2 == 0]  # [0, 2, 4]
squares = [x * x for x in range(5)]                 # [0, 1, 4, 9, 16]
even_squares = [x * x for x in even_numbers]        # [0, 4, 16]

square_dict = {x: x*x for x in range(5)}    # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

zeros = [0 for _ in even_numbers]   # has the same size of even_numbers but only have zeros

pairs = [(x, y) 
        for x in range(10)
        for y in range(10)]

increasing_pairs = [(x, y)
                    for x in range(10)
                    for y in range(x+1, 10)]


assert 1 + 1 == 2
assert 1 + 1 == 2, "1 + 1 should be equal to 2 but didn't"

def smallest_item(xs):
    return min(xs)

assert smallest_item([10, 20, 5, 40]) == 5
assert smallest_item([1, 0, -1, 2]) == -1

# Classes
class CountingClicker:
    """A class can/should have a docstring, just like a function"""
    def __init__(self, count=0) -> None:
        self.count = count

    def __repr__(self) -> str:
        return f'CountingClicker(count={self.count})'
    
    def click(self) -> None:
        """Click the clicker some number of times."""
        self.count += 1

    def read(self) -> int:
        return self.count

    def reset(self) -> None:
        self.count = 0


clicker1 = CountingClicker() # initialized to 0
clicker2 = CountingClicker(100) # starts with count=100
clicker3 = CountingClicker(count=100) # more explicit way of doing the same

clicker = CountingClicker()

assert clicker.read() == 0, "clicker should start with count 0"
# Making 2 clicks
clicker.click()
clicker.click()

assert clicker.read() == 2, "after two clicks, clicker should have count 2"

# Reset to 0
clicker.reset()
assert clicker.read() == 0, "after reset, clicker should be back to 0"

class NoResetClicker(CountingClicker):
    def reset(self) -> None:
        pass

clicker2 = NoResetClicker()
assert clicker2.read() == 0
clicker2.click()
assert clicker2.read() == 1
clicker2.reset()
assert clicker2.read() == 1, "reset shouldn't do anything"

def generate_range(n):
    i = 0
    while i < n:
        yield i # Every call produces a new value
        i += 1

def natural_numbers():
    """Returns 1, 2, 3, ..."""
    n = 1
    while True:
        yield n
        n += 1

evens_below_20 = (i for i in range(20) if i % 2 == 0)
# None of these computations *does* anything until we iterate
data = natural_numbers()
evens = (x for x in data if x % 2 == 0)
even_squares = (x ** 2 for x in evens)
even_squares_ending_in_six = (x for x in even_squares if x % 10 == 6)
# and so on

import random
random.seed(42)  # This ensures that we get the same results every time

four_unifor_randoms = [random.random() for _ in range(4)]
# print(four_unifor_randoms)

up_to_ten = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
random.shuffle(up_to_ten)  # Reorder the elements
# print(up_to_ten)

lottery_numbers = range(60)
winning_numbers = random.sample(lottery_numbers, 6)
# print(winning_numbers)

import re

re_examples = [
    not re.match('a', 'cat'),               # cat doen't start with a
    re.search('a', 'cat'),                  # cat has the letter 'a'
    not re.search('c', 'dog'),              # dog doesn't have a 'c' 
    3 == len(re.split('[ab]', 'carbs')),    # splits the string carbs in a or b
    'R-D-' == re.sub('[0-9]', '-', 'R2D2')  # Replace digits with -
]

assert all(re_examples)

# Unpacking elements
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]

# zip is lazy, so you have to do something like the following
pairs = [pair for pair in zip(list1, list2)]    # [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)                  # letters = ('a', 'b'. 'c') and numbers = (1, 2 ,3)
def doubler(f):
    # Here we define a new function that keeps a reference to f
    def g(x):
        return 2 * f(x)
    # And return that new function
    return g

def f1(x):
    return x + 1

g = doubler(f1)
assert g(3) == 8, "(3 + 1) * 2 should equal 8"
assert g(-1) == 0, "(-1 + 1) * 2 should equal 0"

def magic(*args, **kwargs):
    print("unnamed args:", args)
    print("keyword args:", kwargs)

magic(1, 2, key="word", key2="word2")
# prints
# unnamed args: (1, 2)
# keyword args: {'key': 'word', 'key2': 'word2'}

from typing import List # note capital L

def total(xs: List[float]) -> float:
    return sum(xs)
