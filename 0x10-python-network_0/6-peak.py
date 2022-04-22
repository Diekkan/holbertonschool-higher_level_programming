#!/usr/bin/python3
"""
Fun that finds a peak
"""

def find_peak(list_of_integers):
""" Find the peak of a list """
    if (list_of_integers):
    	peak = list_of_integers[0]
    	for i in range(len(list_of_integers)):
            if peak < list_of_integers:
	        peak = i
    return peak		
