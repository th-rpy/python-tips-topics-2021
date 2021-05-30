# The first Tips&Topics for Beginner 

# Unpacking...

## Traditional way to declare a variables ...

var1 = 1
var2 = 2
var3 = 3

        ## or instead we can do it with a modern way ...

## Using Unpacking to declare a set of variables using a one line of code ...

var1, var2, var3 = 1, 2, 3 # Output : var1 = 1, var2 = 2, var3 = 3

var1, var2, var3 = [1, 2, 3] # Output : var1 = 1, var2 = 2, var3 = 3

var1, var2, var3 = (1, 2, 3)    # Output : var1 = 1, var2 = 2, var3 = 3

var1, var2, var3 = {'one': 1, 'two':2, 'three': 3} # Output : var1 = 'one', var2 = 'two', var3 = 'three'

var1, var2, var3 = (2 * i + 1 for i in range(3))   # Output : var1 = 1, var2 = 2, var3 = 3

var1, (var2, var3), var4 = [1, (2, 3), 4]  # Output : var1 = 1, var2 = 2, var3 = 3, var4 = 4

var1, *var2, var3 = 'Hello' # Output : var1 = 'H' , var2 = ['e', 'l', 'l'] , var3 = 'o'

*var, = 1,2,3  # Output : var = [1, 2, 3]