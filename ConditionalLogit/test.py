#!/usr/bin/python


def bubble_sort_the_alternatives(alternatives):
    for passnumber in range(len(alternatives)-1, 0, -1):
        for i in range(passnumber):
            if int(alternatives[i]) > int(alternatives[i+1]):
                temp = alternatives[i]
                alternatives[i] = alternatives[i+1]
                alternatives[i+1] = temp
    return alternatives


alternative_list = ['4', '2', '1']

choice_list = bubble_sort_the_alternatives(alternative_list)
print choice_list
