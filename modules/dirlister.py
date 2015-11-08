import os

def run(**args):
   print "[*' i dirlister module."
   files=os.listdir(".")
   return str(files)

