#!/usr/bin/env python
# -*- coding: utf-8 -*-

# OKA 2024.2.19
# Create a 2D plot of particle distribution for RELION
# Use only .star file of Refine3D
# Extract AngleRot & AngleTilt from .star file
# This 2D plot is normalized

import matplotlib.pyplot as plt

############# Parameters ##############

# Input .star file path
input_file = input("Please enter the input .star file path (default: run_data.star) → ").strip()
if not input_file:
    input_file = "run_data.star"

# Output .txt file path
output_file = input("Please enter the output .txt file path (default: AngleRot_AngleTilt.txt) → ").strip()
if not output_file:
    output_file = "AngleRot_AngleTilt.txt"

# Output 2D plot(.png) path
output_figure = input("Please enter the output 2D plot file path (default: 2D_plot.png) → ").strip()
if not output_figure:
    output_figure = "2D_plot.png"

# Symmetry (Set the symmetry: "C1","C2","D2" etc.)
symmetry = input("Please enter the symmetry (C1, C2, D2, etc.) → ").strip().upper()

#######################################



########################################################
# typically no need to change anything below this line #
########################################################

# READ DATA
with open(input_file, "r") as f:
    lines = f.readlines()

print("------------------------------")
print("STEP0: Use", input_file)
print("------------------------------")


###                                        ###
# STEP1_find specific words and extract data #
###                                        ###

import re

# FIND AngleRot & AngleTilt 
x_col, y_col = None, None
for line in lines:
    match_rot = re.search(r"_rlnAngleRot #(\d+)", line)
    match_tilt = re.search(r"_rlnAngleTilt #(\d+)", line)
    if match_rot:
        x_col = int(match_rot.group(1)) - 1  # 0-indexed
    if match_tilt:
        y_col = int(match_tilt.group(1)) - 1
    if x_col is not None and y_col is not None:
        break

for i, line in enumerate(lines):
    if line.strip() and line.strip()[0].isdigit():
        data_start = i
        break

# EXTRACT DATA
data = []
for line in lines[data_start:]:
    values = line.split()
    if len(values) > max(x_col, y_col):
        data.append((float(values[x_col]), float(values[y_col])))

# SAVE OUTPUT FILE
with open(output_file, "w") as f:
    for x, y in data:
        f.write(f"{x}\t{y}\n")
print("STEP1_IT: Save", output_file)
        
print("STEP1: Done!")
print("------------------------------")


###                    ###
# STEP2_create a 2D plot #
###                    ###

import numpy as np
from matplotlib.colors import Normalize
from tqdm import tqdm

# 2D PLOT
data = np.array(data)
data_x, data_y = data[:, 0], data[:, 1]

# DISPLAY RANGE SETTINGS BASED ON SYMMETRY
symmetry_ranges = { "C1": (0, 360, 0, 360),
                    "C2": (0, 180, 0, 180),
                    "C3": (0, 120, 0, 180),
                    "C4": (0, 90, 0, 180),
                    "C5": (0, 72, 0, 180),
                    "C6": (0, 60, 0, 180),
                    "D2": (0, 180, 0, 90),
}

if symmetry in symmetry_ranges:
    x_min, x_max, y_min, y_max = symmetry_ranges[symmetry]
else:
    raise ValueError(f"Unknown symmetry: {symmetry}")

# DISPLAY RANGE
plt.xlim(x_min, x_max)
plt.ylim(y_min, y_max)
print(f"STEP2_IT: {symmetry} Symmetry→ xlim({x_min}, {x_max}), ylim({y_min}, {y_max})")

# DENSITY GRADATION_SIZE & COLOR
plt.hexbin(data_x, data_y, gridsize=200, cmap='rainbow', mincnt=1, norm = Normalize(vmin=0, vmax=200))

# LABEL AND TITLE 
plt.xlabel("AngleRot (0≦θ≦π)")
plt.ylabel("AngleTilt (0≦φ≦π/2)")
plt.title("Particle Distribution")

# COLORBAR
plt.colorbar(label='#particle', ticks=[1, 50, 100, 150, 200])

# FRAME BORDER
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# USE GRID?
plt.grid(False)

# SAVE FIGURE
with tqdm(total=1) as pbar:
    plt.savefig(output_figure, dpi=300)
    print("STEP2_IT: Save" ,output_figure)
    print("STEP2: Done!")
    pbar.update(1)

# SHOW GRAPH
plt.show()

exit(0)
