# -*- coding: utf-8 -*- 
#!/usr/bin/python


import sys
import re

def pick_up_words(string):
    result_list = []
    result_hash = {}
    for word  in re.split('\W+',string):
        result_list.append(word)
    for word in result_list:
        if result_list.index(word) + 1  in[1,5,6,7,8,9,15,16,19]:
            kigou = word[:1]
        else: 
            kigou = word[:2] 
        result_hash[kigou] = result_list.index(word) + 1 
        
    return result_hash

if __name__ == "__main__":
    '''
    print specific char of the words  from  given string
    this only support 1 arguments
    original param should be "Hi He Lied Because Boron\
    Could Not Oxidize Fluorine. New Nations Might Also\
    Sign Peace Security Clause. Arthur King Can."
    '''
    string = sys.argv[1]
    result_hash = pick_up_words(string)
    print(result_hash)
