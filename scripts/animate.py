#! /usr/bin/env python
import os
import sys
import shutil

indir= sys.argv[1]
pattern=sys.argv[2]

files=os.listdir(indir)
good_files=[]
for fl in files:
    if pattern in fl:
        good_files.append(fl)
good_files.sort()
i=0
for fl in good_files:
    nn="/data/atbmedia_%03d.png" %i
    print indir+fl, nn
    shutil.copyfile(indir+fl, nn)
    i+=1
#-i %d.png -f mp4 -vcodec h264 test.mp4
os.system('ffmpeg -i /data/atbmedia_%03d.png -f mp4 -vcodec h264 -pix_fmt yuv420p ' + sys.argv[3])
