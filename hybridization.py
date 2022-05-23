#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    keyLength = first_multiple_input[0]

    length = int(first_multiple_input[1])
    #dlugosc lancucha

    second_multiple_input = input().rstrip().split()

    keyStart = second_multiple_input[0]

    start = second_multiple_input[1]
    #

    third_multiple_input = input().rstrip().split()

    keyProbe = third_multiple_input[0]

    probe = int(third_multiple_input[1])
    #rozmiar jednego oligonukleotydu

    oligonucleotides = []

    for _ in range(length - probe + 1):
        oligonucleotides_item = input()
        oligonucleotides.append(oligonucleotides_item)
    olis = oligonucleotides
    olis.remove(start)
    
    #print(start)
    found = [start]
    
    def search(found, olis, first):
        for ol in olis:
            if (first[1:] == ol[:-1]):
                #print(ol)
                found.append(ol)
                olis.remove(ol)
                #searched.append(ol)
                return found, olis, ol
        olis.append(found[-1])
        found.remove(found[-1])

    
    found, olis, st = search(found, olis, start)
    while(olis != []):
        #print(olis, st, found)
        found, olis, st = search(found, olis, st)
        
    
    answear = start
    for i in range(len(found)-1):
        answear = answear + found[i+1][-1]
    print(answear)
    

    
