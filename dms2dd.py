# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 22:31:19 2020

@author: LeanderOliveira
"""

import re

import pandas as pd

uri = 'https://raw.githubusercontent.com/leanderor/dms2dd/master/dms.csv'
df = pd.read_csv(uri)

df.columns = ["lat","long"]

n = len(df)

def dms2dd(degrees, minutes, seconds, direction):
    dd = round(float(degrees) + float(minutes)/60 + float(seconds)/(3600),6);
    if direction.lower() == 'n' or direction.lower() == 'e':
        return dd 
    elif direction.lower() == 's' or direction.lower() == 'w':
        return -dd
    else:
        return('Invalid cardinal direction!')

def parse_dms (coord):
    parts = re.split('[°\'" ]+', coord)
    lat = dms2dd(parts[0], parts[1], parts[2], parts[3])
    return (lat)

print('{:=^115}'.format(''))
print('|{0:^25}|{1:^25}|{2:^30}|{3:^30}|'.format('Lat [DMS]','Long [DMS]','Lat [DD]','Long [DD]'))
print('{:-^115}'.format(''))
for i in range(n):
  lat_dd = parse_dms(df.lat[i])
  long_dd = parse_dms(df.long[i])
  print('|{0:^25}|{1:^25}|{2:^30}|{3:^30}|'.format(df.lat[i],df.long[i],lat_dd,long_dd))
print('{:=^115}'.format(''))
