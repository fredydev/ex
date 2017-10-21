# -*-coding:Latin-1 -*

import os
source = "/home/saintil/exoPyton"
dest= "donfredeveloper@gmail.com"

os.system("rsync -avz " + source +" "+ dest)
#the script can be automated using crontab -e
#adding this following line  " */10 *   *        *    *  /home/saintil/exoPyton/cro.sh"
