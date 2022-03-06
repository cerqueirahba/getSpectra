import os

#Reader for Gaussian 09 output file
######################## List of Outputs #############################
list_of_files = []
for filename in os.listdir():
    if filename.endswith('.log'):
         list_of_files.append(filename)

######################## Functions used #############################
#Defining a function to diferenciate lists
def diferenciate_lists(list1,list2):
    return list(set(list1) - set(list2))

#Defining a function to check double occurrency of the same file on normal_termination_list and delete them
def list_duplicates(seq):
  seen = set()
  seen_add = seen.add
  # adds all elements it doesn't know yet to seen and all other to seen_twice
  seen_twice = set( x for x in seq if x in seen or seen_add(x) )
   #turn the set into a list (as requested)
  return list(seen_twice)
