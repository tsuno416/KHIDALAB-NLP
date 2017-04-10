# -*- coding: utf-8 -*- 
#!/usr/bin/python


import sys
import re

def case5(self,wgram,corpus):
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
    n-gram
    '''
    wgram = sys.argv[1]
    textdata = sys.argv[2]
    case5(wgram,corpus)
    print(result_hash)
