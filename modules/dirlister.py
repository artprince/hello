import os

def run(**args):
   print "[*' i dirlister module."
   files=os.lisdir(".")
   return str(files)

