# -*- coding: utf-8 -*- 
#!/usr/bin/python


import sys
import re

def count_words(string):
    result_list = []
    for word  in re.split('\W+',string):
        result_list.append(len(word))
    return result_list

if __name__ == "__main__":
    '''
    print length of words  from  given string
    this only support 1 arguments
    original param should be "Now I need a drink, alcoholic of course,\
     after the heavy lectures involving quantum mechanics."
    '''
    string = sys.argv[1]
    result_list = count_words(string)
    print(result_list)
