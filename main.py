# Challenge 1:  add_List

# Prompt:
# - Write a function called add_list that accepts any quantity of numbers as arguments, adds them together and returns the resulting sum.
# - If called with no arguments, return 0 (zero).
# - If any non-number arguments are in the argument, return "NaN"


# Examples:
# add(1) //=> 1
# add(1,50,1.23) //=> 52.23
# add(7,-12) //=> -5
# add("peanut_butter", "marshmellow_fluff") //=> NaN

# In javascript:
# in JS, arguments is like a keyword-->holds all of the arguments that may be passed into teh function
# The parentheses () are empty, indicating that this function doesn't have any declared parameters. Without explicit parameters, the function can accept any number of arguments, and these arguments will be accessible inside the function through the arguments object.
# This is a way to create functions that can handle different numbers of arguments dynamically.
# in js:

# function add_list() {
#   if (arguments.length === 0) {
#     return 0; // If called with no arguments, return 0
#   }

#   let sum = 0;

#   for (let i = 0; i < arguments.length; i++) {
#     if (typeof arguments[i] !== 'number') {
#       return "NaN"; // If any non-number arguments are present, return "NaN"
#     }
#     sum += arguments[i];
#   }
#   }

#   return sum;
# }

# // Example usage:
# console.log(add_list(1, 2, 3));      // Output: 6
# console.log(add_list(5, "a", 2));   // Output: "NaN"
# console.log(add_list());             // Output: 0

#-----------------------------------------------
# Python solution Goes Here - >
#-----------------------------------------------
def add_list (*nums): #* allows many parameters to be inserted
    total = 0
    for num in nums:
        if isinstance(num, (int, float)):
            total += num
    return total

print(add_list(1, 3, 5, 6))
# ^^We use a traditional for loop to iterate through each argument in args.
# For each argument, we check if it's an instance of either int or float.
# If it is, we add it to the total.
# The final total is returned.


# Challenge 2: remove_ends
# Prompt:
# - Write a function called remove_ends that accepts a single string argument, then returns the a string with the first and last characters removed.
# - If the length of the string argument is less than 3, return an empty string.

# Examples:
# remove_ends('Led Zeppelin Rules'); //=> "ed Zeppelin Rule"
# remove_ends('a'); //=> "" (empty string)

# in JS:
# function remove_ends(string) {
#     if (string.length < 3) {
#     return "";
#     } else {return string.slice(1, -1);}
# }

#-----------------------------------------------
# Python Solution Goes Here - >
#-----------------------------------------------
def remove_ends(string):
    if len(string) <3:
        return ""
    else:
        print (string[1:-1])

remove_ends("hello")

# The line of code return input_string[1:-1] in Python uses slicing to create a new 
# string that consists of characters starting from the second character (index 1) up to,
# but not including, the last character.

# Challenge 3: is_palindrome

# Prompt:
# - Write a function called is_palindrome that accepts a single string argument, then returns true or false depending upon whether or not the string is a palindrome.
# - A palindrome is a word or phrase that is the same forward or backward.
# - Casing and spaces are not included when considering whether or not a string is a palindrome.
# - If the length of the string is 0 or 1, return true.
# Examples:
# is_palindrome('SEI Rocks'); //=> false
# is_palindrome('rotor'); //=> true
# is_palindrome('A nut for a jar of tuna'); //=> true
# is_palindrome(''); //=> true

# js solution:
# function is_palindrome(string) {
# if (string.length===1 || string.length ===0 || (string === string.split('').reverse().join('')))
#     {return true}
# else {return false}
# }
#-----------------------------------------------
# Solution Goes Here - >
#-----------------------------------------------
# python solution:

def is_palindrome(string):
    # Convert the string to lowercase and remove spaces
    string = string.lower().replace(" ", "")
    if len(string) ==1 or len(string) ==0 or string == string[::-1]:
        return "true"
    else: return "false"
    
print(is_palindrome("mese"))

# Challenge 4: is_prime

# Prompt:
# - Write a function named is_prime that returns true when the integer argument passed to it is a prime number and false when the argument passed to it is not prime.
# - A prime number is a whole number (integer) greater than 1 that is evenly divisible by only itself.
# Examples:
# is_prime(2) //=> true
# is_prime(3) //=> true 
# is_prime(4) //=> false
# is_prime(29) //=> true
# is_prime(200) //=> false

# js solution:
# function is_prime(number) {
#     // Check if the number is less than 2 (not a prime number)
#     if (number < 2) {
#         return false;
#     }
#     // Check for factors from 2 to the square root of the number
#     for (let i = 2; i < number; i++) {
#         if (number % i === 0) {
#             return false;  // If the number is divisible, its not prime
#         }
#     }
#     return true
# }
#-----------------------------------------------
# Solution goes here ->
#-----------------------------------------------
# python solution:
def is_prime(number) :
 if number < 2:
     return "not prime"
 for i in range(2, number, +1):
     if number%i==0:
         return "not prime"
 else: return "prime"
         
print (is_prime(2))


# Challenge 5: total_checkout_cost

# Prompt -> Using this list of dictionary items, write a function to calculate the total cost 
# if there is an 8.5% sales tax attached to each item. 
# Then set up a conditional that adds a $10 Shipping Fee if the user lives in 
# HI, AK, TX, or FL, a $5 Fee for AL, MS, NV, or IL. 
# All other states recieve free shipping. 

# Your function should take the list and the user's homestate as arguments

shopping_cart = [ 
  {"item": "headphones", "price": 25},
  {"item": "speakers", "price": 40 },
  {"item": "microphone", "price": 70},
  {"item": "lamp", "price": 15 },
  {"item": "tower fan", "price": 35 },
]
#-----------------------------------------------
# Solution Goes Here ->
#-----------------------------------------------
def calculate(shopping_cart):
# drill into array for every object
    for i in range (0, len(shopping_cart), +1):
        item=shopping_cart[i]
        price=item["price"]
        full_price=price + (price * .085)
        print(f"Item: {item['item']}, Total Price: {full_price:.2f}")
    return "there you go!"
print(calculate(shopping_cart))


# Challenge 6: fizz_buzz

# Prompt -> Write a program that prints the numbers from 1 to 50. 
# But for multiples of three print “Fizz” instead of the number and for the 
# multiples of five print “Buzz”. For numbers which are multiples of both 
# three and five print “FizzBuzz”
# If your argument is not a number, return "is not a number"

# Examples:
# fizz_buzz(10) //=> 10 "Buzz"
# fizz_buzz(30) //=> 30 "FizzBuzz"
# fizz_buzz(18) //=> 18 "Fizz"
# fizz_buzz(22) //=> 22 ""
# fizz_buzz(ham_sandwich) //=> "ham_sandwich is not a Number"

#-----------------------------------------------
# Solution Goes Here ->
#-----------------------------------------------
# print all numbers:
def fizz_buzz():
    for i in range(1, 51, +1):
        if i % 3 ==0 and i % 5 == 0:
            print ("fizzbuzz")
        elif i % 3 ==0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print (i)

fizz_buzz()

# print only the number that's input:
def fizz_buzz_number(number):
    if not isinstance(number, int):
        return f'"{number}" is not a number'
    if number % 3 ==0 and number % 5 == 0:
            print ("fizzbuzz")
    elif number % 3 ==0:
            print("fizz")
    elif number % 5 == 0:
            print("buzz")
    else:
            print (number)

fizz_buzz_number(5)

# Challenge 7 - Chessboard Creator

# A grid is a perfect starting point for many games (Chess, battleships, Candy Crush!).

# Making a digital chessboard is an interesting way of visualising how loops can work together.

# Your task is to write a function that takes two integers rows and columns and returns a chessboard pattern as a two dimensional array.

# So chess_board(6,4) should return an array like this:

[
    ["O","X","O","X"],
    ["X","O","X","O"],
    ["O","X","O","X"],
    ["X","O","X","O"],
    ["O","X","O","X"],
    ["X","O","X","O"]
]
# And chess_board(3,7) should return this:


[
    ["O","X","O","X","O","X","O"],
    ["X","O","X","O","X","O","X"],
    ["O","X","O","X","O","X","O"]
]

#The white spaces should be represented by an: 'O' and the black an: 'X'

# The first row should always start with a white space 'O'


#-----------------------------------------------
# Solution Goes Here - >
#-----------------------------------------------
