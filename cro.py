# -*-coding:Latin-1 -*

import os
source = "/home/saintil/exoPyton"
#if source == "":
#   source=os.system("pwd")

dest= "donfredeveloper@gmail.com"
#while dest == "":
#   dest = input("Entrer repertoire de destination (user@server:/path/to) :"

os.system("rsync -avz " + source +" "+ dest)
