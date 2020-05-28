#!/usr/bin/env python3

#
#  _ _ _ _____ _ _ _ _____ _____ _____
# | | | |  _  | | | |     |   __|__   |
# | | | |     | | | |  |  |__   |   __|
# |_____|__|__|_____|_____|_____|_____|
#
# (C) 2019 by Wawrzyniec L. Dobrucki
# wawosz@gmail.com
#
# Syntax: python3 write_dicom.py
#
# Python script to save numpy array to DICOM file
#
#

import dicom
import dicom.UID
from dicom.dataset import Dataset, FileDataset
import numpy as np
import datetime
import time


def write_dicom(pixel_array, filename):
    """
    INPUTS:
    pixel_array: 2D or 3D numpy ndarray.
    filename: string name for the output file.
    """

    file_meta = Dataset()
    file_meta.MediaStorageSOPClassUID = '1.1'
    file_meta.MediaStorageSOPInstanceUID = '1.2'
    file_meta.ImplementationClassUID = '1.3'
    ds = FileDataset(filename, {}, file_meta=file_meta, preamble=b'\x00'*128)
    ds.Modality = 'PET'  # imaging modality name
    ds.ContentDate = str(datetime.date.today()).replace('-', '')
    ds.ContentTime = str(time.time())  # milliseconds since the epoch
    ds.StudyInstanceUID = '1.3'
    ds.SeriesInstanceUID = '1.3'
    ds.SOPInstanceUID = '1.3'
    ds.SOPClassUID = 'Secondary Capture Image Storage'
    ds.SecondaryCaptureDeviceManufctur = 'Python 3.7.5'

    # Patient-related data
    ds.PatientName = 'Wawrzyniec L. Dobrucki'
    ds.PatientID = 'M12345'
    ds.PatientSex = 'M'
    ds.PatientBirthDate = '12/12/12'
    ds.SeriesNumber = 5
    ds.SeriesDescription = 'test image'

    ds.SliceThickness = '0.5'  # slice thickness in mm
    ds.PixelSpacing = '0.5'    # pixel spacing or size in mm

    # These are the necessary imaging components of the FileDataset object.
    ds.SamplesPerPixel = 1
    ds.PhotometricInterpretation = "MONOCHROME2"
    ds.PixelRepresentation = 0  # unsigned (default)
    ds.HighBit = 15
    ds.BitsStored = 16  # default
    ds.BitsAllocated = 16  # default
    ds.NumberOfFrames = 216  # number of frames for 3D files
    # ds.SmallestImagePixelValue = '\\x00\\x00'
    # ds.LargestImagePixelValue = '\\xff\\xff'
    ds.Columns = pixel_array.shape[0]
    ds.Rows = pixel_array.shape[1]
    if pixel_array.dtype != np.uint16:
        pixel_array = pixel_array.astype(np.uint16)
    ds.PixelData = pixel_array.tostring()

    ds.save_as(filename)
    return


# Create your 3D array with numpy and write to the file
if __name__ == "__main__":
    pattern = np.tile(np.arange(256).reshape(16, 16), (6, 6))  # 2D pattern
    # creating 3D array 96 x 96 x 216 by repeating pattern 216 times
    pixel_array = np.repeat(pattern, 216, axis=0).reshape(96, 96, 216)
    write_dicom(pixel_array, 'test-image_96x96x216.dcm')
