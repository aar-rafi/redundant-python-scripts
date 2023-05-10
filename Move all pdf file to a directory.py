import glob
import os
import shutil

path = r'F:/'
dest = r'F:/all_pdfs/'

pattern ='*.pdf'
files = glob.glob(dest+pattern)

i=0

for file in files:
    file_name = os.path.basename(file)
    shutil.move(file, dest+file_name)
    i+=1
    print('Moved:',file,"  ",i)
    
