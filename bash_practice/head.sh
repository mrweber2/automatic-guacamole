#!/bin/bash

############################################################
# save a certain amount of lines and grep a certain string #
############################################################

head -n $2 $1 | grep "$3" > $4
