#coding = utf-8
import os
from PIL import Image


def picture(mydir):
	myBasename = os.path.basename(mydir)
	myDirname = os.path.dirname(mydir)
	myNewDir = os.path.join(myBasename,myDirname+' copy')
