#!/usr/bin/python
# -*- coding: utf-8 -*-

################################################################################
# Copyright (C), 2015, Luck Lee.
#
# Filename:     delete_dirs.py
# Version:      1.0.0
# Description:  Delete useless files.
# Author:       Luke Lee
# History:
#       2015-10-21 | First created.
################################################################################

import os
import shutil
from optparse import OptionParser 

def del_dirs(dir_path, dir_name):
        
    for parent, dir_names, file_names in os.walk(dir_path):
                
        for name in dir_names:
            if dir_name in name:
                shutil.rmtree(os.path.join(parent, name))
                # os.remove(os.path.join(parent, name))
            else:
                del_dirs(dir_path, dir_name)
        
def command_input():
    cur_dir = raw_input("input the path:")
    if not cur_dir:
        cur_dir = os.getcwd()
        
    dir_name = raw_input("input the words included in the dir name you want to delete:")
    del_dirs(cur_dir, dir_name)
            
def main():
    parser = OptionParser()  
    parser.add_option("-d", "--dir", dest="dir_path",  
                      help="delete dirs from dir path")  
    parser.add_option("-n", "--name", dest="dir_name",
                      help="the words included in the dir name you want to delete")  
    
    (options, args) = parser.parse_args()  
    
    if len(args) == 0:  
        command_input()
    elif not options.dir_name:
        option.dir_name = os.getcwd()
    
    del_dirs(options.dir_path, options.dir_name)

if __name__ == "__main__":
    main()
    