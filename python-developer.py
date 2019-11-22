#!/usr/bin/env python3
"""
Python interview challenge
Developer
Python
"""

import requests as pokemon
import json

api_endpoint = 'https://pokeapi.co/api/v2/pokemon/'

# define a variable 'water' with integer value of 1
# define a variable 'grass' with integer value of 4
# define a variable 'fire' with integer value of 7
water = 1
grass = 4
fire = 7

# create a python list called 'ptypes'
# the list should contain the above variables 'water', 'grass' and 'fire'
ptypes = [ water, grass, fire ]

# create a new function and call it 'pdex'
# it needs to be able to accept a parameter call it 'ptype'
# at first have the 'pdex' function return a NoneType
def pdex(ptype):

# Inside the function 'pdex' you created use the python module 'requests' to call a RESTful API.
# using the 'requests' module, create an object called 'pokemon'
# 'pokemon' will perform a 'get' request.
# The URL will be a string. a combination of 'api_endpoint' defined above plus
# the parameter of the pdex function
# the function 'pdex' return the result of 'pokemon' as json
    print api_endpoint + str(ptype)
    return pokemon.get(api_endpoint + str(ptype))

# In 'main()' below try and call 'pdex' passing the variable 'water'
# write in a way that can handle any error you may encounter while executing the call to the API
# you may print the result out


def main():

    pdex(water)
    # Define an empty python dictionary called 'pdict'
    pdict = {}

    # using the list you created above called 'ptypes',
    # loop through each item in 'ptypes' and call the 'pdex' function you defined above
    for t in ptypes:
        response= pdex(t)
    # pdex will return loads of data as json. We want to filter the json by the key string: 'name'.
        d = json.loads(response.content)

        pdict[t] = d['name']
    # add each result to the dictionary 'pdict' as key, value pairs.
    # the key is each item in 'ptypes' and the value is the returned result from 'pdex',
    # just to remind you the results of pdex will filtered by 'name' and will be of type string.

    # finally print the result of 'pdict'
    print pdict


if __name__ == "__main__":
    main()
