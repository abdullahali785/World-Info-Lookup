#!/usr/bin/env python3
"""
World

@author: Abdullah 
@date: 8th December, 2024.
"""

import csv
from typing import Union


def gather_info(country: str) -> dict[str, Union[int, str]]:
    """Return the country data"""
    info = {}

    with open('world_codes.csv', mode='r', encoding = 'utf-8') as f:
    
        for info_codes in csv.DictReader(f):
            if info_codes['Country'] == country:
                info['Official_name'] = info_codes['Official state name']
            
    
    with open('world_gov.csv', mode='r', encoding = 'utf-8') as f:
    
        for info_gov in csv.DictReader(f):
            if info_gov['Country'] == country:
                info['Government'] = (info_gov['Constitutional form'])
            
   
    with open('world_regions.csv', mode='r', encoding = 'utf-8') as f:
    
        for info_regions in csv.DictReader(f):
            if info_regions['Country'] == country:
                if info_regions['Region'] != '':
                    info['Region'] = (info_regions['Region'])

    with open('world_geo.csv', mode='r', encoding = 'utf-8') as f:
    
        for info_geo in csv.DictReader(f):
            if info_geo['Country'] == country:
                info_geo['Total (km2)'] = (info_geo['Total (km2)']).replace(',','') 
                info['Area'] = int(info_geo['Total (km2)'])
            
    
    with open('world_demo.csv', mode='r', encoding = 'utf-8') as f:

        for info_demo in csv.DictReader(f):
            if info_demo['Country'] == country:
                info_demo['Population'] = info_demo['Population'].replace(',','') 
                info['Population'] = int(info_demo['Population'])

    return f'{country} ({info['Official_name']}) is a(n) {info['Government']} form of government in {info['Region']} with an area of {info['Area']} square kilometers and {info['Population']} number of people.'

print(gather_info('Pakistan'))