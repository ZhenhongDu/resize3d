import cv2
import numpy as np

def resize3d(img,XYscale = 4,Zscale = 1):
    """
    Input: img --> input image 
           XYscale --> downsample rate in XY axis
           Zscale --> downsample rate in Z axis
    Output:
           out --> downsampled image stack
    """
    zsize, ysize, xsize = img.shape

    temp = np.zeros((zsize, ysize //XYscale, xsize //XYscale), dtype='uint16')
    xy_dim = (xsize //XYscale,ysize //XYscale)
    for zz in range(0, zsize):
        temp[zz, :, :] = cv2.resize(img[zz, :, :], xy_dim, interpolation=cv2.INTER_AREA)

    xz_dim = (xsize //XYscale, zsize //Zscale)
    out = np.zeros((zsize //Zscale, ysize //XYscale, xsize //XYscale), dtype='uint16')

    for yy in range(0, ysize //XYscale):
        out[:, yy, :] = cv2.resize(temp[:, yy, :], xz_dim, interpolation=cv2.INTER_AREA)

    print("3d resize done !!!")

    return out