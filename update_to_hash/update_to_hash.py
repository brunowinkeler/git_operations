## @package update_to_hash.py
#  Automatic checkout using a given txt file with repositories.
#
#  With this code it is possible to checkout for specific projects
#     using the tag, hash or branch informed in the file repos.txt.

import os

cmd_ = 'cls'
os.system(cmd_)

with open('repos.txt', 'r') as file_: 
    for line_ in file_:   
        addr_ = line_.split()[0]
        hash_ = line_.split()[1]
        
        cmd_ = 'git -C '+ addr_ + ' checkout '+ hash_
        os.system(cmd_)      

        print('\n')