# The Second Tips&Topics for Beginner 

# Merging two dictionaries...

## Traditional way to do this ...

    ## Declare a function merge 

def merge (dict1, dict2):
    dict_3 = dict1.copy()
    dict_3.update(dict2)
    return dict_3

dict1 = {'one': 1, 'two': 2, 'three':3}
dict2 = {'four':4, 'five':5}
dict_merged = print(merge(dict1, dict2)) # Output : {'one': 1, 'two': 2, 'three':3, 'four':4, 'five':5}

    ### Or ... ###

## Using the merging Python Tips to do it ... 

dict1 = {'one': 1, 'two': 2, 'three':3}
dict2 = {'four':4, 'five':5} 
dict3 = {'six':6, 'seven':7}
dict_merged = dict1 | dict2 | dict3 # or use {**dict1, **dict2, **dict3}
print(dict_merged) # Output : {'one': 1, 'two': 2, 'three':3, 'four':4, 'five':5}



