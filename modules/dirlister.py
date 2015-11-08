import os

def run(**args):
   print "[*' i dirlister module."
   files=os.listdir(".")
   print files
   return str(files)

