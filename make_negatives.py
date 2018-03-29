import cv2
from os import listdir,makedirs
from os.path import isfile,join

downloads=r'/Users/чуч№/Documents/LOGGERHEADER/training_cascade/downloads'
folder = r'/Users/чуч№/Documents/LOGGERHEADER/training_cascade/downloads/*' # Source Folder
dstpath = r'/Users/чуч№/Documents/LOGGERHEADER/training_cascade/negatives' # Destination Folder

try:
    makedirs(dstpath)
except:
    print ("Directory already exist, images will be written in same folder")

# Folder won't used

folders=[f for f in listdir(downloads)]
for folder in folders:
    images = [i for i in listdir(folder) if isfile(join(folder,i))] 
    for image in images:
    try:
        img = cv2.imread(os.path.join(pathfolder,image))
        gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        img = cv2.resize(img, (100, 100))
        dstPath = join(dstpath,image)
        cv2.imwrite(dstpath,gray)
    except:
        print ("{} is not converted".format(image))
