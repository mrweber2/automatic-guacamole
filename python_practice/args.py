#!/usr/bin/python


###############################
#                             #
# Matthew Weber, NCSA         #
# 3/29/2016                   #
#                             #
############################### 


# import modules
import argparse
import random

# parse arguments
parser = argparse.ArgumentParser(description='Practice Input Arguments')
parser.add_argument('-i', type=str, required=True, metavar='<str>', help="Please enter your name after '-i'")

args = parser.parse_args()

# set variables to input arguments
NAME = args.i


# do something with arguments
print NAME
