
# glob - filename pattern matching 
# input: a path to files
# output:a list of filenames 

import glob
for name in glob.glob('/home/hanl9/Documents/4-live-skills/*'):
    print(name)



# ref:
glob – Filename pattern matching - Python Module of the Week
https://pymotw.com/2/glob/






# os.path.basename() method in Python is used to get the base name in specified path. This method internally use os.path.split() method to split the specified path into a pair (head, tail). os.path.basename() method returns the tail part after splitting the specified path into (head, tail) pair.


import os.path 
  
# Path 
path = '/home/User/Documents'
  
  
# Above specified path 
# will be splited into 
# (head, tail) pair as 
# ('/home/User', 'Documents') 
  
# Get the base name   
# of the specified path 
basename = os.path.basename(path) 
  
# Print the base name   
print(basename) 




  
# Path 
path = '/home/User/Documents/file.txt'
  
# Above specified path 
# will be splited into 
# (head, tail) pair as 
# ('/home/User/Documents', 'file.txt') 
  
# Get the base name   
# of the specified path 
basename = os.path.basename(path) 
  
# Print the basename name   
print(basename) 



# enumarate python 
# Enumerate() method adds a counter to an iterable and returns it in a form of enumerate object.
l1 = ["eat","sleep","repeat"] 
s1 = "geek"


enumerate(l1)

list(enumerate(l1))

dict(enumerate(l1))
