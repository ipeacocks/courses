# You're tasked with writing a function which determines if a word matches a pattern. Ex. given the pattern "d3dog" and the word "datadog" your function should return True. However, given the same pattern and the word "datadogs", your function should return False.


def is_match(some_string, some_pattern):
    some_string_list = list(some_string)
    some_pattern = list(some_pattern)
    # print(some_string_list)
    
    for i in range(len(some_pattern)):
        if some_pattern[i].isdigit():
            # del some_pattern[i]
            j = i
            print(j)
            for j in range(i, int(some_pattern[i]) + j):
                some_pattern.insert(j, "_")
                print(j)
                j += 1
            del some_pattern[j]
    print(some_pattern)
    
    # i = 0
    # while len(some_string) > 0 and len(some_pattern) > 0:
    #     if some_string[i]:
    
    for i in range(some_string):
        if len(some_pattern) == len(some_string):
            retun False
        
        if 
            
    
    # for i in range(0, some_string_list):
    #     if some_string_list[i] != some_pattern[i]:
    #         return False

is_match("datadog", "da3og")
