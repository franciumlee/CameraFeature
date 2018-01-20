import cv2
import numpy as np
#from matplotlib import pyplot as plt
import os
def fft(img):
    #print(img.dtype)
    array=np.float64(img)
    #print(array.dtype)
    #dft=cv2.dft(array,flags=cv2.DFT_COMPLEX_OUTPUT)
    dft=np.fft.fft2(img)
    dft_shift=np.fft.fftshift(dft)

    MAS=20*np.log(np.abs(dft_shift))#cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))
    return MAS

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


IMAGE_SIZE = 64
def resize_with_pad(image, height=IMAGE_SIZE, width=IMAGE_SIZE):

    def get_padding_size(image):
        h, w, _ = image.shape
        longest_edge = max(h, w)
        top, bottom, left, right = (0, 0, 0, 0)
        if h < longest_edge:
            dh = longest_edge - h
            top = dh // 2
            bottom = dh - top
        elif w < longest_edge:
            dw = longest_edge - w
            left = dw // 2
            right = dw - left
        else:
            pass
        return top, bottom, left, right

    top, bottom, left, right = get_padding_size(image)
    BLACK = [0, 0, 0]
    constant = cv2.copyMakeBorder(image, top , bottom, left, right, cv2.BORDER_CONSTANT, value=BLACK)

    resized_image = cv2.resize(constant, (height, width))

    return resized_image


images = []
labels = []
def traverse_dir(path):
    for file_or_dir in os.listdir(path):
        abs_path = os.path.abspath(os.path.join(path, file_or_dir))
        print(abs_path)
        if os.path.isdir(abs_path):  # dir
            traverse_dir(abs_path)
        else:                        # file
            if file_or_dir.endswith('.jpg'):
                image = read_image(abs_path)
                images.append(image)
                labels.append(path)

    return images, labels


def read_image(file_path):
    image = cv2.imread(file_path)
    image = resize_with_pad(image, IMAGE_SIZE, IMAGE_SIZE)

    return image

def extract_data(path):
    images,labels=traverse_dir(path)
    images=np.array(images)
    newlist=[]
    '''
    for label in labels:
        if("HTC-1-M7" in label):
             newlist.append(0)
        elif("iPhone-4s" in label):
            #labels =np.array([1])
             newlist.append( 1)
        elif ("iPhone-6" in label):
            #labels  = np.array([2])
             newlist.append( 2)
        elif ("LG-Nexus-5x" in label):
            #labels  = np.array([3])
             newlist.append( 3)
        elif ("Motorola-Droid-Maxx" in label):
            #labels  = np.array([4])
             newlist.append( 4)
        elif ("Motorola-Nexus-6" in label):
            #labels  = np.array([5])
             newlist.append( 5)
        elif ("Motorola-X" in label):
            #labels  = np.array([6])
             newlist.append( 6)
        elif ("Samsung-Galaxy-Note3" in label):
            #labels  = np.array([7])
             newlist.append( 7)
        elif ("Samsung-Galaxy-S4" in label):
            #labels  = np.array([8])
             newlist.append(8)
        elif ("Sony-NEX-7" in label):
            #labels  = np.array([9])
            newlist.append(9)
    #print(labels)
    #print(newlist)
    #print(images)
    '''
    return images,newlist#, labels

if __name__ == '__main__':
    path='/home/franciumlee/Dataset/HTC-1-M7/'
    path_1 = '/home/franciumlee/Dataset/FFT/'
#    img=cv2.imread(path+'(HTC-1-M7)1.jpg',0)
#    img2=fft(img)
#    print(img2)
    DatasetPrePorocess(path,path_1)
#    plt.subplot(121),plt.imshow(img2,cmap='gray')
#    plt.show()

