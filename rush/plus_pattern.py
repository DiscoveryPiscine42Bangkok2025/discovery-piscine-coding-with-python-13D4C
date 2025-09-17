import numpy as np

def create_plus_pattern(size, center_row, center_col):
    # Step 1: Initialize a 2D array with zeros
    pattern = np.zeros((size, size), dtype=int)

    # Step 2: Set the elements of the array to form a plus pattern
    pattern[center_row, :] = 1  # Horizontal line
    pattern[:, center_col] = 1  # Vertical line

    return pattern

size = 5  # Size of the array
center_row = 0  # Center row index
center_col = 1  # Center column index
plus_pattern = create_plus_pattern(size, center_row, center_col)
print("Plus Pattern:")
print(plus_pattern)
