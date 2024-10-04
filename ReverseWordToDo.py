# Reversing a Word
# For this first example of using a stack, we examine a simple task: reversing a word. When you run the program, you type in a word or phrase, and the program displays the reversed version.

# A stack is used to reverse the letters. 
# First, the characters are extracted one by one from the input string and pushed onto the stack. 
# Then they’re popped off the stack and displayed. Because of its last-in, first-out characteristic, 
# the stack reverses the order of the characters. 
# Example:
# Word to reverse: draw
# The reverse of draw is ward



# A program to reverse the letters of a word

#import stack class
from stacktodo import Stack

def is_balanced(s: str) -> bool:
     # Create a stack to hold letters
    stack = Stack(len(s))
    library = {")": "(", "}": "{", "]": "["}
    for ch in s:
        if ch in library:
            stack.push(ch)
        elif ch in library:
            if stack.isEmpty() or stack.pop() != library[ch]:
                return False
    return stack.isEmpty() 

#Get user input
s = input("Please enter a 10 letter word or less:")

if len(s) > 10:
    raise ValueError("Input is longer than 10 char!")
    # Loop over letters in word

stack = Stack(10)

for letter in s:
    # Push letters on stack if not full
    stack.push(letter)

print(stack)

if is_balanced(s):
    print("The expression is balanced.")
else:
    print("The expression is not balanced.")

# Build the reversed version
reversed_word = ""
while not stack.isEmpty():
    reversed_word += stack.pop()
# Print reverse the letters of a word
print("Reversed version of word is:", reversed_word)

if is_balanced(reversed_word):
    print("The expression is balanced.")
else:
    print("The expression is not balanced.")