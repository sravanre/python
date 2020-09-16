# Traversing a directory recursively

import os 
import sys
import datetime
import time
folder = os.getcwd()
for (dirname, subdir, files) in os.walk(folder):
        for myfile in files:
              filename=os.path.join(dirname,myfile)
              if ".py" in filename:
                      #print(filename)
                      fileage = time.time() - os.path.getctime(filename)
                      age=24*60*60
                      if age > fileage:
                              print(filename)
                        
                      
        
'''

        for myfile in files:
                #if ".py" in myfile:
                if myfile.endswith(".py"):
                
                       filename=os.path.join(dirname,myfile)   # making an absolute path
                       #print(filename)
                       #print(os.path.getsize(myfile))
                       
                       day = 60*60
                       fileage = time.time() - os.path.getctime(myfile)
                       if fileage < day:
                               print(myfile, fileage)
                               
                       
'''
      
