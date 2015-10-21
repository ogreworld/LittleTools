#!/usr/bin/python
# -*- coding: utf-8 -*-

################################################################################
# Copyright (C), 2015, Luck Lee.
#
# Filename:     rename_files.py
# Version:      1.0.0
# Description:  Delete useless files.
# Author:       Luke Lee
# History:
#       2015-10-21 | First created.
################################################################################

import os
from optparse import OptionParser 

def rename_files(dir_path, old_name, new_name=""):
    
    if not old_name:
        return
        
    for parent, dir_names, file_names in os.walk(dir_path):
        for name in file_names:
            
            if old_name in name:
                tmp_name = name.replace(old_name, new_name)
                option = "y"
                if not tmp_name.split(".")[0]:
                    option = raw_input("Are you sure to delete file \"%s\"(Y/N)"%name)
                
                if option.upper() == "Y":
                    os.rename(os.path.join(parent, name),os.path.join(parent, tmp_name))
                
        for dir_name in dir_names:
            rename_files(os.path.join(parent, dir_name), old_name, new_name)
        
def command_input():
    cur_dir = raw_input("input the path:")
    if not cur_dir:
        cur_dir = os.getcwd()
        
    old_name = raw_input("input the name you want to replace to:")
        
    new_name = raw_input("input the name you want to replace with:")
    rename_files(cur_dir, old_name, new_name)
            
def main():
    parser = OptionParser()  
    parser.add_option("-d", "--dir", dest="dir_name",  
                      help="rename files from dir path")  
    parser.add_option("-o", "--old", dest="old_name",
                      help="the name you want to replace to")  
    parser.add_option("-n", "--new", dest="new_name",
                      help="the name you want to replace with")  
    
    (options, args) = parser.parse_args()  
    
    if len(args) == 0:  
        command_input()
    elif not options.dir_name:
        option.dir_name = os.getcwd()
    
    rename_files(options.dir_name, options.old_name, options.new_name)

if __name__ == "__main__":
    main()
    