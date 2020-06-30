# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 22:31:19 2020

@author: LeanderOliveira
"""

def dms2dd(degrees,minutes,seconds,cardinal_direction):
  dec = round(degrees + (minutes/60) + (seconds/3600),6)
  if cardinal_direction.lower() == "n" or cardinal_direction.lower() == "e":
    print(dec)
  elif cardinal_direction.lower() == "s" or cardinal_direction.lower() == "w":
    print(-dec)
  else:
    print('Invalid cardinal direction!')

dms2dd(75,59,32.483,'N')