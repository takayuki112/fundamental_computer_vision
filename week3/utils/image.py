import cv2
import numpy as np

def resize(img, scale=0.5):
    w = int(scale * img.shape[1])
    h = int(scale * img.shape[0])
    return cv2.resize(img, (w, h), interpolation=cv2.INTER_LINEAR)


# Lab 3, Question 1 ~ Histogram Equalization

def luminance_histogram_equalization(img):
    yuv_image = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    yuv_image[:, :, 0] = cv2.equalizeHist(yuv_image[:, :, 0])
    eqed = cv2.cvtColor(yuv_image, cv2.COLOR_YUV2BGR)
    return eqed

def monochrome_histogram_equalization(img):
    return cv2.equalizeHist(img)

def adaptive_histogram_equalization(image, tile_grid_size=(8, 8)):
    
    # Get the dimensions of the image
    height, width = image.shape
    
    # Calculate the size of each tile
    tile_height = height // tile_grid_size[0]
    tile_width = width // tile_grid_size[1]
    
    # Initialize an empty array to store the equalized image
    equalized = np.zeros_like(image)
    
    # Loop through each tile
    for i in range(tile_grid_size[0]):
        for j in range(tile_grid_size[1]):
            # Define the region for the current tile
            y_start = i * tile_height
            y_end = (i + 1) * tile_height if (i + 1) < tile_grid_size[0] else height
            x_start = j * tile_width
            x_end = (j + 1) * tile_width if (j + 1) < tile_grid_size[1] else width
            
            # Extract the current tile from the image
            tile = image[y_start:y_end, x_start:x_end]
            
            # Apply histogram equalization to the tile
            tile_hist, bins = np.histogram(tile.flatten(), 256, [0, 256])
            cdf_tile = tile_hist.cumsum()
            cdf_tile_normalized = cdf_tile * (255 / cdf_tile[-1])
            
            # Use linear interpolation to map the pixel values of the tile
            tile_equalized = np.interp(tile.flatten(), bins[:-1], cdf_tile_normalized).reshape(tile.shape)
            
            # Place the equalized tile back into the image
            equalized[y_start:y_end, x_start:x_end] = tile_equalized
    
    return equalized.astype(np.uint8)

# Lab 3, Question 2 ~ Histogram Matching

def histogram_matching_grey(source, reference):
    source_hist, bins = np.histogram(source.flatten(), 256, [0, 256])
    reference_hist, bins = np.histogram(reference.flatten(), 256, [0, 256])
    
    cdf_source = source_hist.cumsum()  # CDF of source
    cdf_reference = reference_hist.cumsum()  # CDF of reference
    
    cdf_source_normalized = cdf_source * (255 / cdf_source[-1])
    cdf_reference_normalized = cdf_reference * (255 / cdf_reference[-1])
    
    lookup_table = np.interp(cdf_source_normalized, cdf_reference_normalized, np.arange(256))
    
    matched = cv2.LUT(source, lookup_table.astype(np.uint8))
    
    return matched
