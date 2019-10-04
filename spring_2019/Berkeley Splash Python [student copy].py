#!/usr/bin/env python
# coding: utf-8

# # Berkeley Splash: Learing about Python, the Computing Language not the Snake
# ## 03/16/2019
# ### Table of Contents:
# 1. [Basic Python Syntax](#section1)  
#     1.1 [Jupyter Notebooks](#section1.1)  
#     1.2 [Text](#section1.2)  
#     1.3 [Code](#section1.3)  
#     1.4 [Writing in Jupyter Notebooks](#section1.4)  
#     1.5 [Errors](#section1.5)  
# 2. [Numbers](#section2)  
#     2.1 [Basic Arithmetic Operations](#section2.1)  
# 3. [Variables and Functions](#section3)  
#     3.1 [Commenting](#section3.1)  
#     3.2 [Assignment Statments](#section3.2)  
#     3.3 [Functions](#section3.3)  
#     3.4 [Data Types](#section3.4)  
#     3.5 [Importing Code](#section3.5)  
# 4. [Arrays](#section4)  
# 5. [Challenge Questions](#section5)  
#     5.1 [Arithmetic](#section5.1)   
#     5.2 [Printing and Strings](#section5.2)   
#     5.3 [Arrays and Arithmetic](#section5.3)   
#     
# 
# 
# ## Contacts:
# **Co-Teachers:**
# [Shivani Patel](mailto:shivanijpatel@berkeley.edu) & [Sindhu Goli](mailto:sindhugoli@berkeley.edu)
# 
# **Assistants:**
# [Sage Jeon](mailto:sungjoojeon@berkeley.edu) & [Hailey Tran](mailto:hailey.tran@berkeley.edu)
#     

# <a id='section1'></a>
# # Part 1: Basic Python Syntax

# This course will teach you to:
# 1. navigate Jupyter Notebooks (like this one)
# 2. write and evaluate some basic *expressions* in Python
# 3. call *functions* to use prewritten code other people have written;
# 4. break down Python code into smaller parts to understand it.

# <a id='section1.1'></a>
# ### 1.1 Jupyter Notebooks

#  - Some shortcuts:
#      - `Esc` - `a`: creates a cell above current cell
#      - `Esc` - `b`: creates a cell below current cell
#      - Alternatives to `shift` - `enter`:
#          - `ctrl` - `enter`: run cell, keeps cursor in cell
#          - `opt` - `enter`: run cell, create new cell below

# Each rectangle containing text is a *cell*.
# 
# There are two types of cells: Text and Code

# <a id='section1.2'></a>
# ### 1.2 Text
#     - simple cells with text (like this one)
#     - can be edited by double-clicking on the cell.

# **Practice:**
# 
#     Complete the following sentence structure:

# Hi, my name is

# <a id='section1.3'></a>
# ### 1.3 Code
#    - The language that we are using in this notebook is Python 3
#    - "running a cell" will execute all of the code it the cell contains
#    - cells can be edited by double-clicking the cell, it'll be highlighted with a little green or blue rectangle
#    - to run the code in a cell press the ▶| button or press `shift` + `enter`
# 
# Try running this cell:

# In[ ]:


print("Berkeley Splash is the best!!!")


# And this one:

# In[ ]:


print("\N{WAVING HAND SIGN}, \N{EARTH GLOBE ASIA-AUSTRALIA}!")


# Code is broken down into different lines called expressions. Cells can contain multiple lines with multiple expressions. When you run a cell, the lines of code are executed in the order in which they appear. 
# 
# Every `print` expression prints a line. Run the next line and notice the order of the output

# In[ ]:


print('This line is first,')
print('and this one is last.')


# **Question 1.3.1.** Change the cell above so that it prints out:
#     
#     This line is first,
#     then the whole 🌏,
#     and this one is last.
# 
# Hint: if you are stuck on the Earth symbol, try asking your neighbor :)

# <a id='section1.4'></a>
# ### 1.4. Writing in Jupyter Notebooks
# Although we have created this notebook for you to learn, you will most likely need to know how to create your own in the future. Lets start with adding new cells for text and code
# 
# To add a cell, click the + button in the menu bar. If the left sidebar has `In [ ]` then it is a code cell, if it is blank it is a text cell. To change the type of cell you can do either of these options:
# 1. select the cell then click cell from the toolbar and choose Cell Type. (Don't worry about "Raw NBConvert").
# 2. click the left side of the cell and press `m` for markdown cell or `y` for a code cell.
# 
# **Question 1.4.1*** Add a code cell below this one.  Write code in it that prints out:
#    
#     Music makes the world round! ♪🌏♪
# 
# Hint: That musical note symbol is like the Earth symbol.  Its long-form name (code) is `\N{EIGHTH NOTE}`.
# 
# Run your cell to verify that it works.

# ### 1.5. Errors
# Python is just like any other language you learn, there are grammer rules and these are really important. The computer is designed to excute code based on what it was programmed to understand.
# 1. The rules are *simple*
# 2. The most common error is a Syntax Error
# 
# Today we are going to teach you a simple error to fix: `SyntaxError`. It tells you that you have created an illegal structure, or in other words, you broke the "grammar rules"
# 
# We have made an error in the next cell. Run it and see what happens.

# In[ ]:


print("This line is missing something."


# Lets break this down, the last line of the error output attempts to tell you in english what went wrong. "`EOF`" means "end of file". Also notice how there is a small carrot that points to a part of the ran cell. This attempts to tell you "where" you made the error.
# 
# There is a lot of unnessary cryptic terminology in programming languages but you don't need to understand it all, try to just look at the last line of the error, that is the most simple version of the problem.
# 
# **Question 1.5.1.** Try to fix the code above so that you can run the cell and see the intended message instead of an error

# <a id='section2'></a>
# # Part 2: Numbers
# In addition to representing commands to print out lines of code, or *expressions* Python also knows how to intrepret and evaluate numbers. The expression `15.0210000` evaluates to the number 15.021. Run the cell below and see:

# In[ ]:


15.0210000


# Notice how we didn't use the function `print`. This is because the last line has a value it will print that value for you. BUT, it will disregard any prior lines.

# In[ ]:


1
2
3


# **Question 2.0.1.** If you want the output to include 1, use the function `print`. Change the cell below to produce an output with 1 and 3

# In[ ]:


1
2
3


# <a id='section2.1'></a>
# ### 2.1 Basic Arithmetic Operations
# Lets learn a few basic (and extremely useful) operations 

# Addition: `+`

# In[ ]:





# Subtraction: `-`

# In[ ]:





# Multiplication: `*`

# In[ ]:





# Division: `/`

# In[ ]:





# Floor Division: `//`
# This divides the number and rounds down

# In[ ]:





# Remainder: `%`

# In[ ]:





# Exponetiation: `**`

# In[ ]:





# Note: `2 * * 5` will return an error. See below:

# In[ ]:


2 * * 5


# Python has rules like order of operations (PEMDAS), run the following cell:

# In[ ]:


3+6*5-6*3**2*2**3/4*7


# Now run this cell, notice the use of parenthesis. Happy New Year!!

# In[ ]:


3+(6*5-(6*3))**2*((2**3)/4*7)


# This is what Python reads for the first expression:
# 
# $$3+6 \times 5-6 \times 3^2 \times \frac{2^3} {4} \times 7$$
# 
# The second expression is evaluated as:
# 
# $$3 + (6 \times 5 - (6 \times3))^2 \times (\frac{(2^3)}{4} \times 7)$$

# **Question 2.1.1** Write a python expression below that is equal to:
# 
# 

# <a id='section3'></a>
# # Part 3: Varibles and Fuctions

# <a id='section3.1'></a>
# ### 3.1 Commenting
# A *comment* is a line of code that the computer does not run. Why do we need this? When code has hundreds or even thousands of lines, it is sometimes hard to know what exactly the computer is computing in certain places. Adding comments allow the coder (you) to write in english what the line means/evaluates to.
# 
# To add a comment, we use a `#` symbol, everything to the right of the # is apart of the comment.

# In[ ]:


#Calculating an approximation for pi
about_pi = 22/7
about_pi


# <img src="http://imgs.xkcd.com/comics/future_self.png">
# Source: http://imgs.xkcd.com/comics/future_self.png

# <a id='section3.2'></a>
# ### 3.2 Assignment Statements
# When we speak we don't say, "WOW look at that mammal with black and white stripes!" Instead, we say, "Zebra!"
# 
# Python can also do the same sort of classfication. We can assign a variable to an expression. This helps when we have really complicated code. We call this an *assignment statement* Python will evaluate the expression on the right side of the `=` and will store it to the variable on the left of the `=`. Once you run the line of code, everytime you call that varible later on, Python will insert the evaluated expression.
# 
# As we have seen, programing does not only include just numbers. Text is one of the most common types of values used in programs.
# 
# `string` is a programming term for a sequence of characters. This can include a single character, a word, a sentence, or a whole book. The contents can be anything; words, numbers, symbols.
# 
# In order to create a string of characters, we put double quotes`(")` or single quotes`(')` (both produce the same function) but, the opening and ending quotes must match.
# 
# We have seen strings before in `print` statements
# 
# Note: 
# 1. Variables are case senstive
# 2. They cannot start with a number like `6` but, `six` will work.
# 3. There cannot be any spaces, instead we use `_` (underscore) to seperate words.

# In[ ]:


thesis = 


# Notice how no output was produced? This is because Python stored the expression in the variable `thesis`. Run the following cell:

# In[ ]:


thesis


# If no value has been assigned to a name, Python will return a NameError:

# In[ ]:


topic_sentence


# **Question 3.2.1** Assign a value to the `topic_sentence` below:

# In[ ]:





# In[ ]:


topic_sentence


# A common pattern that in JN is to use assignment statements and then immediately evaluate the name in the last line of the cell.

# In[ ]:


close_to_pi = 355/113
close_to_pi


# Another common use of variables in JN is a series of lines in a single cell. This is a more complex computation in stages naming the end result rather than individual values

# In[ ]:


rent = 
months = 
total_rent_paid = rent* months
total_rent_paid


# **Question 3.2.2** Assign the name `seconds_in_a_year` to the number of seconds in a year. Compute 365 days for the year.
# 
# If you're stuck read the comments for hints :)

# In[ ]:


# Change the next line so it computes the number of seconds in a year
# Try not to use a computer and instead use the Arithmetic functions to solve this

seconds_in_a_year = 

#We've put this line in the cell so that it will print your corresponding value
#Do not change this part!
#Hint: your output should start with 3 and end with three 0's
seconds_in_a_year


# <a id='section3.4'></a>
# ### 3.4 Functions
# *Functions* are pieces of code written by others that you can freely use. A functions is called through its name and then its argument or arguments the syntax of a function looks like this:
# `function(argument)`. *Functions are case sensitive*. 
# 
# For example: `f(27)`
# 
# This is called a *call expression* because `f` is the name of the function being called and `27` is the argument being passed in.
# 
# Python has a set of built-in functions that are very simple to use. Lets look at a few!

# In[ ]:


abs()


# **Question 3.4.1.** Pick a random number and assign it to the value n. Then, execute the cell:

# In[ ]:


n = 
abs(n)


# Some functions take in multiple arguments, seperated by commas. Lets look at a few:

# In[ ]:


max()


# In[ ]:


max()


# In[ ]:


min()


# In[ ]:


sum()


# You can also pass in expressions into the functions. Below is an example of the function `round()`.

# In[ ]:


# Run this cell and see the result
num_rotations = 4
radians_turned = 2 * about_pi * num_rotations
radians_turned


# In[ ]:


#Run this cell and see the evidence of rounding
# round() rounds the output to the nearest integer
approx_radians_turned = round(2 * about_pi * num_rotations)
approx_radians_turned


# *Nesting* is the term for what was displayed above. Here is a more simple example:

# In[ ]:


abs(4 - max(2,3,4,5,6,9))


# <a id='section3.5'></a>
# ### 3.5 Data Types
# Python has several types of data.
# 1. Numbers look like this `[1.22, 4, 0.45, 2.0]
# 2.`string` are a "string" of characters refer to the string section for more details
# 3. `bool` this is a fancy way of saying `True/False` or `1/0`
# 
# You can also convert different data types.
# 1. `int` is a solid number such as, 6, 2, 5500 etc.
# 2. `float` is a number with decimal places such as, 1.34, 88.3, 3.0
# 
# Lets look at some examples:

# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# <a id='section3.6'></a>
# ### 3.6 Importing Code
# 
# A really nice feature that Python has is built-in functions. These are functions that were already defined by other people can be imported and used without having to define functions.
# 
# Let's look at the `import math` function:

# In[ ]:


import math

#math is super useful when trying to use functions like pi or square root
print(math.pi)
print(math.sqrt(16))


# Once you import the code once in the notebook, python does not need a reminder everytime you use the function
# Here are some functions you can use in the `math` notebook:
# 
# |Method Name|Value|
# |-|-|
# |`cos(x)`|returns the cosine of x radians|
# |`sin(x)`|returns the sine of x radians|
# |`tan(x)`|returns the tangent of x radians|
# |`e`|returns the value of *e*|
# |`pi`|returns the value of pi (3.14)|
# |`factorial`| calculates factorials|
# |`log(logarithm, base)`|calculates logarithms. The first number is the logarithm and the second number is the base.|
# |`sqrt`| calculates square roots|

# **Question 3.6.1** 
# Let's create some code:
# 
# Write this code in the next line! 
# 
# **Hint**: just simply stating the function does not tell python where to get it from. Remember to write `math.` before each function
# $$cos(\pi)$$

# In[ ]:





# Try this one:
# $$\sqrt(16)$$

# In[ ]:





# $$\log(8,2)$$

# In[ ]:





# find the factorial of 5

# In[ ]:





# <a id='section4'></a>
# # Part 4: Arrays
# Although we could code every little detail in our computer, we can also tell Python to do some work for us. An array puts many values into one place so we can tell functions to operate them as a group. Lets take a look at a couple ways we can do this!

# <a id='section4.1'></a>
# ### 4.1 Make_array
# The `make_array` functions allows us to create a list of values which will then output an array. 
# 
# We can make an array of 'string' values:

# In[ ]:


#Run this cell
from datascience import *
rainbow_colors= make_array('red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'purple')
rainbow_colors


# We can also make an array of numbers:

# In[ ]:


small_numbers = 
small_numbers


# **Question 4.1.1.** Make an array containing the numbers 6,7,8,9,10, in that order. Name it `large_numbers`:

# In[ ]:





# **Question 4.1.2.** Add both `small_numbers` and `large_numbers` together.
# 
# Hint: You should be using the names above and an arithmetic operation to complete this question. Do not manually compute this, let the computer do the hard work.

# In[ ]:





# Try running this cell:

# In[ ]:


small_numbers + make_array(3,2,1)


# We recieve a ValueError, why do you think? Talk with a partner next to you, then we will go over this in class.

# Write your notes here:
# 
# 
# 

# <a id='section4.2'></a>
# ### 4.2 Single Elements of Arrays ('indexing')
# A lot of times in Python we import tables that have hundreds of array values. Lets look at an example below:

# In[ ]:


#run this cell to load the data
import numpy as np
random_array = np.arange(0, 20000, 2)


# This creates an array of 10,000 values. Lets assume we want to find the 100th value. To do this, we use a term called indexing, the function that correspondes to this is `.item()`. But, there are some key features you should know first:
# 
# 1. `.item()` is written after the array
# 2. indexing also starts with `0` not `1`. This means that if we do `item(1)` it will give us the second element of the array, `item(0)` will give the first element of the array.

# **Question 4.2.1** Find the 100th element in `random_array`:

# In[ ]:





# **Question 4.2.1** How about the 289th element?

# In[ ]:





# Since `make_array` returns an array, we can also index a number in the same line of code.

# In[ ]:


make_array()


# In[ ]:


WRITE RESTAURANT BILLS WITH TAXES CODE


# <a id='section5'></a>
# # Part 5: Challenge Questions

# <a id='section5.1'></a>
# ### 5.1 Arithmetic
# **Question 5.1.1** In the next cell assign the name `new_year` to the larger number amoung the following two numbers:
# 1. the absolute value of $2^{5}-2^{11}-2^1$ AND
# 2. $5 \times 13 \times 31 +2$
# 
# Challenge yourself and use one statement (one line of code):

# In[ ]:


new_year = 


# <a id='section5.2'></a>
# ### 5.2 Printing and Strings
# **Question 5.2.** Yuri Gagarin was the first person to travel through outer space. When he emerged from his capsule upon landing on Earth, he reportedly had the following conversation with a woman and girl who saw the landing:
# 
#     The woman asked: "Can it be that you have come from outer space?"
#     Gagarin replied: "As a matter of fact, I have!"
#     
# Complete the cell below and assign expressions to the following names, replace the `...`. 

# In[ ]:


woman_asking = ...
woman_quote = ...
gagarin_reply = ...
gagarin_quote = ...

#Do not change these next lines, run the cell after completing the above statements
print(woman_asking, woman_quote)
print(gagarin_reply, gagarin_quote)


# <a id='section5.3'></a>
# ### 5.3 Arrays and Arithmetic
# Here is a (modified) menu for the best fast-food joint ever!

# In[ ]:


#Run this cell
from datascience import *
food = make_array('Double-Double', 'Cheeseburger', 'Hamburger', 'French Fries', 'Shake (any flavour)', 'Small Drink', 'Medium Drink', 'Large Drink')
prices = make_array('3.45', '2.40', '2.10', '1.60', '2.15', '1.50', '1.65', '1.85')
In_n_out = Table().with_columns('Food', food, 'Prices ($)', prices)
In_n_out


# In[1]:


#Run this cell
from datascience import *
food = make_array('Double-Double', 'Cheeseburger', 'Hamburger', 'French Fries', 'Shake (any flavour)', 'Small Drink', 'Medium Drink', 'Large Drink')
prices = make_array('3.45', '2.40', '2.10', '1.60', '2.15', '1.50', '1.65', '1.85')
In_n_out = Table().with_columns('Food', food, 'Prices ($)', prices)
In_n_out


# Using this table lets answer some challenge questions:

# **Question 5.3.1** Use the `.item` and the array `prices` to calculate Jenny's order:
#     - Cheeseburger
#     - French Fries
#     - Chocolate Shake
# Use `jenny_bill` as the name of the calculation.

# In[ ]:


jenny_bill = 


# **Question 5.3.2**
# The combined sales tax rate for Berkeley, CA is [9.25%]('https://www.avalara.com/taxrates/en/state-rates/california/cities/berkeley/'). Calculate Jenny's total restaurant bill with tax below:

# In[ ]:


jenny_total = 


# **Question 5.3.3** Now compute the following orders with the given names:
# 
# |Name|Order|
# |-|-|
# |Mark|Cheeseburger and Medium Drink|
# |Ajay|French Fries and Small Drink|
# |Kevin|Hamburger, French Fries, Large Drink|
# |Ani|Double-Double and Small Drink|

# In[ ]:


#Cheeseburger and a Medium Drink
mark_bill = 

#French Fries and Small Drink
ajay_bill = 

#Hamburger, French Fries, Large Drink
kevin_bill = 

#Double-Double and Small Drink
ani_bill = 


# **Question 5.3.4** Now create an array of restaurant bills with Jenny, Mark, Ajay, Kevin, and Ani's bills calculated above.
# 
# Hint: Use the `make_array()` function

# In[ ]:


all_restaurant_bills = 


# Now, we could individually multiply each bill by the tax to find the total bill BUT why do that if we can tell the computer to do most of the work!
# 
# We can do this by assigning the decimal of tax to `tax`. Then multiplying `all_restaurant_bills` to `tax`. This will produce a new array of total bills.
# 
# Hint: remember that if we want to find the total bill we CANNOT set `tax` equal to 0.0925, add 1 to this.

# In[ ]:


tax = 
all_total_restaurant_bills = 
all_total_restaurant_bills


# In[ ]:


# Just run this cell to see the values in a table
# We did not go over tables but once you take a more advanced class you will learn about it :)
Table.with_column('Name', make_array('Jenny', 'Mark', 'Ajay', 'Kevin', 'Ani'), 
                  'Order', make_array('Cheeseburger, French Fries, Chocolate Shake', 'Cheeseburger and Medium Drink', 
                                     'French Fries and Small Drink', 'Hamburger, French Fries, and Large Drink',
                                     'Double-Double and Small Drink'),
                  'Restaurant Bills w/o Tax ($)', all_restaurant_bills,
                  'Final Bill ($)', all_total_restaurant_bills)

