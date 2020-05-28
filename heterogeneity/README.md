Sample Python codes for the analysis of medical images, specifically heterogeneity (textual) analysis using python modules

### Description of the files ###

***heterogeneity.py*** - how to load image, convert to GLCM (grey-level co-variance matrix) and calculate several heterogeneity parameters.

***heterogeneity_parse.py*** - script will open window to choose directory with image files (TIF, 8-bit) and analyze all images in this directory for several heterogeneity parameters. It contains code from _heterogeneity.py_ script.

***GLCM_testing.py*** - testing several arrays and plotting GLCM.

***plot_glcm.py*** - another example of the code for GLCM analysis.

***convert_RGD_to_8bit.py*** - script to read all files (here RGB tif files) and convert them to 8-bit tif files with suffix '_converted' and save in the source directory. Heterogeneity analysis can be done only on 8-bit images.
