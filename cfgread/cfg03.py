#!/usr/bin/env python3
## create file object in "r"ead mode

inputcfg = input("Please enter the name of the config file to read-> ")

#with open("vlanconfig.cfg", "r") as configfile:
with open(inputcfg, "r") as configfile:
    ## readlines() creates a list by reading target
    ## file line by line
    configlist = configfile.readlines()
    
## file was just auto closed (no more indenting)

## each item of the list now has the "\n" characters back
print(configlist)
print(f"\nThis file has {str(len(configlist))} lines\n")

