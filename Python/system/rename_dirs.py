#!/usr/bin/python
# -*- coding: utf-8 -*-

################################################################################
# Copyright (C), 2015, Luck Lee.
#
# Filename:     rename_dirs.py
# Version:      1.0.0
# Description:  Delete useless files.
# Author:       Luke Lee
# History:
#       2015-10-21 | First created.
################################################################################

import os
import shutil
from optparse import OptionParser 

def rename_dirs(dir_path, old_name, new_name=""):
    
        
    for parent, dir_names, file_names in os.walk(dir_path):
                
        for name in dir_names:
            if old_name in name:
                tmp_name = name.replace(old_name, new_name)
                option = "y"
                if not tmp_name:
                    option = raw_input("Are you sure to delete dir \"%s\"(Y/N)"%name)
                    if option.upper() == "Y":
                        shutil.rmtree(os.path.join(parent, name))
                else:
                    os.rename(os.path.join(parent, name),os.path.join(parent, tmp_name))
                    
            else:    
                rename_dirs(os.path.join(parent, name), old_name, new_name)
        
def command_input():
    cur_dir = raw_input("input the path:")
    if not cur_dir:
        cur_dir = os.getcwd()
        
    old_name = raw_input("input the name you want to replace to:")
        
    new_name = raw_input("input the name you want to replace with:")
    rename_dirs(cur_dir, old_name, new_name)
            
def main():
    parser = OptionParser()  
    parser.add_option("-d", "--dir", dest="dir_name",  
                      help="rename dirs from dir path")  
    parser.add_option("-o", "--old", dest="old_name",
                      help="the name you want to replace to")  
    parser.add_option("-n", "--new", dest="new_name",
                      help="the name you want to replace with")  
    
    (options, args) = parser.parse_args()  
    
    if len(args) == 0:  
        command_input()
    elif not options.dir_name:
        option.dir_name = os.getcwd()
    
    rename_dirs(options.dir_name, options.old_name, options.new_name)

if __name__ == "__main__":
    main()
    