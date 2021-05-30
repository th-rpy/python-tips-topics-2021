
# The 4th Tips&Topics for Beginner 

# Reverse String using one line code...

## Traditional way using a for loop ...

def reverse(text):
    reversed = ""
    for i in range(1, len(text) + 1):
        reversed += text[len(text) - i]
    return reversed

string = 'Hello Py !'
print(reverse(string)) # Output : '! yP olleH' 

    ## Or ...

## Do the same thing using slicing

string = 'Hello Py !'
print(string[::-1]) # Output : '! yP olleH'
