import os
import cv2
import numpy as np
from HighPassFilter import fft
path4Dataset='/home/franciumlee/Dataset/iPhone-4s/'
TargetPath4Dataset='/home/franciumlee/Dataset/FFT_iP4s/'
def DatasetPrePorocess(path4Dataset,TargetPath4Dataset):
    FileArray=os.path.join(path4Dataset)
    FileArray=os.listdir(FileArray)
    if(os.path.exists(TargetPath4Dataset)==False):
        os.mkdir(TargetPath4Dataset)
    for i in FileArray:
        img=cv2.imread(path4Dataset+i,1)

        imgfft=fft(img)
        print(path4Dataset,path4Dataset+i,TargetPath4Dataset+i)
        cv2.imwrite(TargetPath4Dataset+i,imgfft)


    print(FileArray)

if __name__ == '__main__':
    DatasetPrePorocess(path4Dataset,TargetPath4Dataset)