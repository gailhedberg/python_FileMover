# gail hedberg - file_mover.py
# july 14, 2015
#
#copy files from c:\desktop\foldera to folderb
#

import shutil
import os
from os import path

def main():
  # src = "c:\users\gail\desktop\foldera"
  # dst = "c:\users\gail\desktop\folderb"

  file_list = os.listdir('c:\users\gail\Desktop\FolderA')

  #print file_list
  
  for fname in os.listdir('c:\users\gail\Desktop\FolderA'):
    src_fname = 'c:\users\gail\Desktop\FolderA\%s' % fname
    dst_fname = 'c:\users\gail\Desktop\FolderB\%s' % fname

    print 'Moving file : %s ' % (src_fname)
    print '     To loc : %s ' % (dst_fname)
    
    shutil.move(src_fname, dst_fname)
       
         
        
      
if __name__ == "__main__":
  main()




