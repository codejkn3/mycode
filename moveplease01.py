#!/usr/bin/env python3
import shutil
import os

#change directory
os.chdir('/home/student/mycode/')

#move the file to a new directory
shutil.move('raynor.obj', 'ceph_storage/')

#rename a file after prompting the user for the new name
xname = input('What is the new name for kerrigan.obj? ')
shutil.move('ceph_storage/kerrigan.obj', 'ceph_storage/' + xname)

