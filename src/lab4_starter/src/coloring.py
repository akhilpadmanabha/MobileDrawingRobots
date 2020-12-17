#!/usr/bin/env python
"""Segmentation skeleton code for Lab 6
Course: EECS C106A, Fall 2019
Author: Grant Wang

This Python file is the skeleton code for Lab 3. You are expected to fill in
the body of the incomplete functions below to complete the lab. The 'test_..'
functions are already defined for you for allowing you to check your 
implementations.

When you believe you have completed implementations of all the incompeleted
functions, you can test your code by running python segmentation.py at the
command line and step through test images
"""

import os
import numpy as np
import cv2
import matplotlib.pyplot as plt

this_file = os.path.dirname(os.path.abspath(__file__))
IMG_DIR = '/'.join(this_file.split('/')[:-2])  + '/lab4_starter/src'
c_trajectories = []

def read_image(img_name, grayscale=False):
    """ reads an image

    Parameters
    ----------
    img_name : str
        name of image
    grayscale : boolean
        true if image is in grayscale, false o/w
    
    Returns
    -------
    ndarray
        an array representing the image read (w/ extension)
    """

    if not grayscale:
        img = cv2.imread(img_name)
    else:
        img = cv2.imread(img_name, 0)

    return img

def write_image(img, img_name):
    """writes the image as a file
    
    Parameters
    ----------
    img : ndarray
        an array representing an image
    img_name : str
        name of file to write as (make sure to put extension)
    """

    cv2.imwrite(img_name, img)

def show_image(img_name, title='Fig', grayscale=False):
    """show the  as a matplotlib figure
    
    Parameters
    ----------
    img_name : str
        name of image
    tile : str
        title to give the figure shown
    grayscale : boolean
        true if image is in grayscale, false o/w
    """

    if not grayscale:
        plt.imshow(img_name)
        plt.title(title)
        plt.show()
    else:
        plt.imshow(img_name, cmap='gray')
        plt.title(title)
        plt.show()



def do_kmeans(data, n_clusters):
    """Uses opencv to perform k-means clustering on the data given. Clusters it into
       n_clusters clusters.

       Args:
         data: ndarray of shape (n_datapoints, dim)
         n_clusters: int, number of clusters to divide into.

       Returns:
         clusters: integer array of length n_datapoints. clusters[i] is
         a number in range(n_clusters) specifying which cluster data[i]
         was assigned to. 
    """
    criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 100, 0.2)
    _, clusters, centers = kmeans = cv2.kmeans(data.astype(np.float32), n_clusters, bestLabels=None, criteria=criteria, attempts=1, flags=cv2.KMEANS_RANDOM_CENTERS)

    return clusters

def cluster_segment(img, n_clusters, robot_num, random_state=0):
    """segment image using k_means clustering

    Parameter
    ---------
    img : ndarray
        rgb image array
    n_clusters : int
        the number of clusters to form as well as the number of centroids to generate
    random_state : int
        determines random number generation for centroid initialization

    Returns
    -------
    ndarray
        clusters of gray_img represented with similar pixel values
    """

    # Downsample img by a factor of 2 first using the mean to speed up K-means
    img_d = cv2.resize(img, dsize=(img.shape[1]/2, img.shape[0]/2), interpolation=cv2.INTER_NEAREST)

    # TODO: Generate a clustered image using K-means

    # first convert our 3-dimensional img_d array to a 2-dimensional array
    # whose shape will be (length * width, number of channels) hint: use img_d.shape
    len = img_d.shape[0]
    img_r = img_d.reshape(-1,3)
    #print(img_r.shape)
    
    # fit the k-means algorithm on this reshaped array img_r using the
    # the do_kmeans function defined above.
    clusters = do_kmeans(img_r, n_clusters)

    # reshape this clustered image to the original downsampled image (img_d) shape
    #print(clusters.shape)
    cluster_img = clusters.reshape(img_d.shape[0],img_d.shape[1])
    #print(cluster_img.shape)

    # Upsample the image back to the original image (img) using nearest interpolation
    img_u = cv2.resize(src=cluster_img, dsize=(img.shape[1], img.shape[0]), interpolation=cv2.INTER_NEAREST)
    print(img_u)
    print(img_u.shape)
    a,b,c,d,e,f = 0,0,0,0,0,0
    for n in img_u:
        #print(n)
        for m in n:
            if m == 0:
                a += 1
            elif m == 1:
                b += 1
            elif m == 2:
                c += 1
            elif m ==3:
                d += 1
            elif m ==4:
                e += 1
            elif m == 5:
                f += 1

    clu = [a,b,c,d,e,f]
    index = 0
    max_v = max(clu)
    min_v = min(clu)
    print(max_v)
    print(min_v)
    for index in range(6):
        if clu[index] == max_v or clu[index] == min_v:
            clu[index] = 0
    print(clu)
    color_trajectories(clu,robot_num,img_u)


    return img_u.astype(np.uint8)


def color_trajectories(clusters,robot_num,img_u):
    
    x_len = len(img_u[0])
    y_len = len(img_u)
    print(x_len)
    colored_grid = np.zeros((x_len,y_len))
    print(colored_grid.shape)
    for i in range(len(clusters)): #:range(1)
        single_trajectory = []
        if clusters[i] != 0:
            for n in range(0,y_len,2):
                for m in range(0,x_len,8):      #increase the step size for speed up since we don't have to worry pixel by pixel
                    x = m
                    y = y_len - n - 1
                    #assume all same colors are clustered together for now, skip first pixel (edge anyway)
                    if img_u[n][m] == i and img_u[n][m-1] == i:       
                        single_trajectory.append([x,y])
        #print(single_trajectory)
        if single_trajectory != []:
            c_trajectories.append(single_trajectory)
        #print(c_trajectories)
    return None


def to_grayscale(rgb_img):
    return np.dot(rgb_img[... , :3] , [0.299 , 0.587, 0.114])

def segment_image(img): 
    # ONLY USE ONE SEGMENTATION METHOD

    # perform thresholding segmentation
    binary = threshold_segment_naive(to_grayscale(img), 100, 255).astype(np.uint8)

    # perform clustering segmentation.
    # binary = cluster_segment(img, 2).astype(np.uint8)

    # if np.mean(binary) > 0.5:
    #     binary = 1 - binary #invert the pixels if K-Means assigned 1's to background, and 0's to foreground

    return binary


"""
below are tests used for sanity checking you image, edit as you see appropriate

"""


def test_cluster(img, n_clusters,robot_num):
    # For visualization, we need to scale up the image so it
    # is in range(256) instead of range(n_clusters).
    clusters = (cluster_segment(img, n_clusters,robot_num) * (255 / (n_clusters-1))).astype(np.uint8)

    cv2.imwrite(IMG_DIR + "/cluster.jpg", clusters)
    clusters = cv2.imread(IMG_DIR + '/cluster.jpg')
    show_image(clusters, title='cluster')

if __name__ == '__main__':
    # adjust the file names here
    #test_img = read_image(IMG_DIR + '/chrome.jpg', grayscale=True)
    robot_num = 1 # int(sys.argv[1])
    test_img_color = read_image(IMG_DIR + '/chrome.jpg')

    test_cluster(test_img_color,3,robot_num)
