import cv2
import numpy as np
from skimage.feature import graycomatrix, graycoprops
from pyfeats import fos
from pyfeats import fdta
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from scipy import ndimage
import random
import pyfeats

# define the mouse callback function for selecting the ROI
def select_roi(event, x, y, flags, param):
    global roi_pts1, roi_pts2, roi_pts3, roi_selected

    if event == cv2.EVENT_LBUTTONDOWN:
        if param == 1:
            roi_pts1.append((x, y))
        elif param == 2:
            roi_pts2.append((x, y))
        elif param == 3:
            roi_pts3.append((x, y))

    elif event == cv2.EVENT_RBUTTONDOWN:
        if param == 1:
            roi_pts1.append((x, y))
            roi_selected[0] = True
        elif param == 2:
            roi_pts2.append((x, y))
            roi_selected[1] = True
        elif param == 3:
            roi_pts3.append((x, y))
            roi_selected[2] = True

# create a window for each image and set the mouse callback function
cv2.namedWindow('image1')
cv2.setMouseCallback('image1', select_roi, param=1)
cv2.namedWindow('image2')
cv2.setMouseCallback('image2', select_roi, param=2)
cv2.namedWindow('image3')
cv2.setMouseCallback('image3', select_roi, param=3)

# initialize the ROI points and ROI selected flag for each image
roi_pts1 = []
roi_selected1 = False
roi_pts2 = []
roi_selected2 = False
roi_pts3 = []
roi_selected3 = False
roi_selected = [False, False, False]

# load the images
img1 = cv2.imread('test1.png')
img2 = cv2.imread('test2.png')
img3 = cv2.imread('test3.png')

# loop until the ROIs are selected for all images
while not all(roi_selected):
    # display the images
    clone1 = img1.copy()
    if len(roi_pts1) > 0:
        cv2.polylines(clone1, [np.array(roi_pts1)], True, (0, 255, 0), 2)
    cv2.imshow('image1', clone1)

    clone2 = img2.copy()
    if len(roi_pts2) > 0:
        cv2.polylines(clone2, [np.array(roi_pts2)], True, (0, 255, 0), 2)
    cv2.imshow('image2', clone2)

    clone3 = img3.copy()
    if len(roi_pts3) > 0:
        cv2.polylines(clone3, [np.array(roi_pts3)], True, (0, 255, 0), 2)
    cv2.imshow('image3', clone3)

    key = cv2.waitKey(1) & 0xFF

    # if the 'c' key is pressed for any image, clear the ROI points
    if key == ord('c'):
        if roi_selected[0]:
            roi_pts1 = []
            roi_selected[0] = False
        if roi_selected[1]:
            roi_pts2 = []
            roi_selected[1] = False
        if roi_selected[2]:
            roi_pts3 = []
            roi_selected[2] = False

# extract the ROIs from each image
x1, y1, w1, h1 = cv2.boundingRect(np.array(roi_pts1))
roi_img1 = img1[y1:y1+h1, x1:x1+w1]

x2, y2, w2, h2 = cv2.boundingRect(np.array(roi_pts2))
roi_img2 = img2[y2:y2+h2, x2:x2+w2]

x3, y3, w3, h3 = cv2.boundingRect(np.array(roi_pts3))
roi_img3 = img3[y3:y3+h3, x3:x3+w3]

# convert the ROIs to grayscale
gray_roi1 = cv2.cvtColor(roi_img1, cv2.COLOR_BGR2GRAY)
gray_roi2 = cv2.cvtColor(roi_img2, cv2.COLOR_BGR2GRAY)
gray_roi3 = cv2.cvtColor(roi_img3, cv2.COLOR_BGR2GRAY)

# calculate the texture features for each ROI
glcm1 = graycomatrix(gray_roi1, [1], [0, np.pi/4, np.pi/2, 3*np.pi/4], levels=256, symmetric=True, normed=True)
contrast1 = graycoprops(glcm1, 'contrast')
homogeneity1 = graycoprops(glcm1, 'homogeneity')
energy1 = graycoprops(glcm1, 'energy')
correlation1 = graycoprops(glcm1, 'correlation')
ASM1 = graycoprops(glcm1, 'ASM')

glcm2 = graycomatrix(gray_roi2, [1], [0, np.pi/4, np.pi/2, 3*np.pi/4], levels=256, symmetric=True, normed=True)
contrast2 = graycoprops(glcm2, 'contrast')
homogeneity2 = graycoprops(glcm2, 'homogeneity')
energy2 = graycoprops(glcm2, 'energy')
correlation2 = graycoprops(glcm2, 'correlation')
ASM2 = graycoprops(glcm2, 'ASM')

glcm3 = graycomatrix(gray_roi3, [1], [0, np.pi/4, np.pi/2, 3*np.pi/4], levels=256, symmetric=True, normed=True)
contrast3 = graycoprops(glcm3, 'contrast')
homogeneity3 = graycoprops(glcm3, 'homogeneity')
energy3 = graycoprops(glcm3, 'energy')
correlation3 = graycoprops(glcm3, 'correlation')
ASM3 = graycoprops(glcm3, 'ASM')

# display the ROIs and texture features for each image
cv2.imshow('ROI 1', roi_img1)
print('Contrast (ROI1):', contrast1[0][0])
print('Homogeneity (ROI1):', homogeneity1[0][0])
print('Energy (ROI1):', energy1[0][0])
print('Correlation (ROI1):', correlation1[0][0])
print('ASM (ROI1):', ASM1[0][0])

cv2.imshow('ROI 2', roi_img2)
print('Contrast (ROI2):', contrast2[0][0])
print('Homogeneity (ROI2):', homogeneity2[0][0])
print('Energy (ROI2):', energy2[0][0])
print('Correlation (ROI2):', correlation2[0][0])
print('ASM (ROI2):', ASM2[0][0])

cv2.imshow('ROI 3', roi_img3)
print('Contrast (ROI3):', contrast3[0][0])
print('Homogeneity (ROI3):', homogeneity3[0][0])
print('Energy (ROI3):', energy3[0][0])
print('Correlation (ROI3):', correlation3[0][0])
print('ASM (ROI3):', ASM3[0][0])

# calculate the average texture features
contrast_avg = (contrast1[0][0] + contrast2[0][0] + contrast3[0][0]) / 3
homogeneity_avg = (homogeneity1[0][0] + homogeneity2[0][0] + homogeneity3[0][0]) / 3
energy_avg = (energy1[0][0] + energy2[0][0] + energy3[0][0]) / 3
correlation_avg = (correlation1[0][0] + correlation2[0][0] + correlation3[0][0]) / 3
ASM_avg = (ASM1[0][0] + ASM2[0][0] + ASM3[0][0]) / 3

# display the average texture features
print('Contrast (Avg):', contrast_avg)
print('Homogeneity (Avg):', homogeneity_avg)
print('Energy (Avg):', energy_avg)
print('Correlation (Avg):', correlation_avg)
print('ASM (Avg):', ASM_avg)

# display the ROIs
cv2.imshow('ROI 1', roi_img1)
cv2.imshow('ROI 2', roi_img2)
cv2.imshow('ROI 3', roi_img3)
cv2.waitKey(0)
cv2.destroyAllWindows()

# Simulate the image and extract features for each ROI
features_list = []
for gray_roi in [gray_roi1, gray_roi2, gray_roi3]:
    simulated_image = gray_roi * 256
    A = simulated_image.astype(np.int16)

    features, labels = fos(gray_roi, mask=None)
    feature_dict = dict(zip(labels, features))
    features_list.append(feature_dict)

# Calculate the average FOS features
avg_features_dict = {}
for key in labels:
    avg_features = np.mean([f[key] for f in features_list])
    avg_features_dict[key] = avg_features

# Print the average FOS features
for key, feat in avg_features_dict.items():
    print(f"{key}: {feat:.3f}")

# Simulate the image and extract GLCM features for each ROI
features_list = []
for gray_roi in [gray_roi1, gray_roi2, gray_roi3]:
    simulated_image = gray_roi * 256
    A = simulated_image.astype(np.int16)
    features_mean, features_range, labels_mean, labels_range = pyfeats.glcm_features(gray_roi, ignore_zeros=True)
    feature_dict = dict(zip(labels_mean, features_mean))
    features_list.append(feature_dict)

# Calculate the average GCLM features
avg_features_dict = {}
for key in labels_mean:
    avg_features = np.mean([f[key] for f in features_list])
    avg_features_dict[key] = avg_features

# Print the average GCLM features
for key, feat in avg_features_dict.items():
    print(f"{key}: {feat:.3f}")

# Simulate the image and extract GLDS features for each ROI
features_list = []
for gray_roi in [gray_roi1, gray_roi2, gray_roi3]:
    simulated_image = gray_roi * 256
    A = simulated_image.astype(np.int16)
    features, labels = pyfeats.glds_features(gray_roi, mask=None, Dx=[0,1,1,1], Dy=[1,1,0,-1])
    feature_dict = dict(zip(labels, features))
    features_list.append(feature_dict)

# Calculate the average GLDS features
avg_features_dict = {}
for key in labels:
    avg_features = np.mean([f[key] for f in features_list])
    avg_features_dict[key] = avg_features

# Print the average GLDS features
for key, feat in avg_features_dict.items():
    print(f"{key}: {feat:.3f}")

# Simulate the image and extract NGTDM features for each ROI
features_list = []
for gray_roi in [gray_roi1, gray_roi2, gray_roi3]:
    simulated_image = gray_roi * 256
    A = simulated_image.astype(np.int16)
    features, labels = pyfeats.ngtdm_features(gray_roi, mask=None, d=1)
    feature_dict = dict(zip(labels, features))
    features_list.append(feature_dict)

# Calculate the average NGTDM features
avg_features_dict = {}
for key in labels:
    avg_features = np.mean([f[key] for f in features_list])
    avg_features_dict[key] = avg_features

# Print the average NGTDM features
for key, feat in avg_features_dict.items():
    print(f"{key}: {feat:.3f}")

# Simulate the image and extract SFM features for each ROI
features_list = []
for gray_roi in [gray_roi1, gray_roi2, gray_roi3]:
    simulated_image = gray_roi * 256
    A = simulated_image.astype(np.int16)
    features, labels = pyfeats.sfm_features(gray_roi, mask=None, Lr=4, Lc=4)
    feature_dict = dict(zip(labels, features))
    features_list.append(feature_dict)

# Calculate the average SFM features
avg_features_dict = {}
for key in labels:
    avg_features = np.mean([f[key] for f in features_list])
    avg_features_dict[key] = avg_features

# Print the average SFM features
for key, feat in avg_features_dict.items():
    print(f"{key}: {feat:.3f}")

# Simulate the image and extract GLRLM features for each ROI
features_list = []
for gray_roi in [gray_roi1, gray_roi2, gray_roi3]:
    simulated_image = gray_roi * 256
    A = simulated_image.astype(np.int16)
    features, labels = pyfeats.glrlm_features(gray_roi, mask=None, Ng=256)
    feature_dict = dict(zip(labels, features))
    features_list.append(feature_dict)

# Calculate the average GLRLM features
avg_features_dict = {}
for key in labels:
    avg_features = np.mean([f[key] for f in features_list])
    avg_features_dict[key] = avg_features

# Print the average GLRLM features
for key, feat in avg_features_dict.items():
    print(f"{key}: {feat:.3f}")

# Simulate the image and extract GLSZM features for each ROI
features_list = []
for gray_roi in [gray_roi1, gray_roi2, gray_roi3]:
    simulated_image = gray_roi * 256
    A = simulated_image.astype(np.int16)
    features, labels = pyfeats.glszm_features(gray_roi, mask=None)
    feature_dict = dict(zip(labels, features))
    features_list.append(feature_dict)

# Calculate the average GLSZM features
avg_features_dict = {}
for key in labels:
    avg_features = np.mean([f[key] for f in features_list])
    avg_features_dict[key] = avg_features

# Print the average GLSZM features
for key, feat in avg_features_dict.items():
    print(f"{key}: {feat:.3f}")

# Simulate the image and extract FDTA features for each ROI
features_list = []
for gray_roi in [gray_roi1, gray_roi2, gray_roi3]:
    simulated_image = gray_roi * 256
    A = simulated_image.astype(np.int16)

    h, labels = fdta(gray_roi, mask= None, s=3)
    feature_dict = dict(zip(labels, h))
    features_list.append(feature_dict)

# Calculate the average FDTA features
avg_features_dict = {}
for key in labels:
    avg_features = np.mean([f[key] for f in features_list])
    avg_features_dict[key] = avg_features

# Print the average FDTA features
for key, feat in avg_features_dict.items():
    print(f"{key}: {feat:.3f}")

# load and preprocess the three images' ROIs
roi_img1 = roi_img1.astype(np.float32)
roi_img2 = roi_img2.astype(np.float32)
roi_img1 = roi_img2.astype(np.float32)


# calculate color heterogeneity for each ROI
def get_color_heterogeneity(img):
    # calculate the variance of the color channels for each pixel
    variance = np.var(img, axis=2)

    # compute the average variance for the image
    avg_variance = np.mean(variance)

    # compute the percentage of pixels with above-average color variance
    threshold = avg_variance
    above_threshold = np.sum(variance > threshold)
    total_pixels = variance.size
    percentage_above_threshold = above_threshold / total_pixels * 100
    
    return percentage_above_threshold

ch1 = get_color_heterogeneity(roi_img1)
ch2 = get_color_heterogeneity(roi_img2)
ch3 = get_color_heterogeneity(roi_img3)

# compute the average color heterogeneity across the three images
average_ch = np.mean([ch1, ch2, ch3])

# print the average color heterogeneity in percentage
print(f"Average color heterogeneity: {average_ch:.2f}%")