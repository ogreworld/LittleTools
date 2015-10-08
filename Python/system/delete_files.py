#!/usr/bin/python
# -*- coding: utf-8 -*-

################################################################################
# Copyright (C), 2015, Luck Lee.
#
# Filename:     delete_files.py
# Version:      1.0.0
# Description:  Delete useless files.
# Author:       Luke Lee
# History:
#       2015-09-15 | First created.
################################################################################

import os
from optparse import OptionParser 

def del_files(dir_path, file_name="", suffix=""):
    
    if not file_name and not suffix:
        return
        
    for parent, dir_names, file_names in os.walk(dir_path):
        for name in file_names:
            dot_split = name.split(".")
            end = dot_split[-1]
            front = ".".join(dot_split[:-1])
            
            success = True
            if suffix and not (suffix in end):
                success = False
                
            if file_name and not (file_name in front):
                success = False
                
            if success:
                os.remove(os.path.join(parent, name))
                
        for dir_name in dir_names:
            del_files(os.path.join(parent, dir_name), file_name, suffix)
        
def command_input():
    cur_dir = raw_input("input the path:")
    if not cur_dir:
        cur_dir = os.getcwd()
        
    suffix = raw_input("input the words included in the suffix you want to delete:")
        
    file_name = raw_input("input the words included in the file you want to delete:")
    del_files(cur_dir, file_name, suffix)
            
def main():
    parser = OptionParser()  
    parser.add_option("-d", "--dir", dest="dir_name",  
                      help="delete files from dir path")  
    parser.add_option("-s", "--suffix", dest="suffix",
                      help="the suffix you want to search to delete")  
    parser.add_option("-f", "--filename", dest="file_name",
                      help="including the filename you want to search to delete")  
    
    (options, args) = parser.parse_args()  
    
    if len(args) == 0:  
        command_input()
    elif not options.dir_name:
        option.dir_name = os.getcwd()
    
    del_files(options.dir_name, options.file_name, options.suffix)

if __name__ == "__main__":
    main()
    