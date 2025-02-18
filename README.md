# 2D-distribution-of-particle-orientation-for-RELION

## Overview
 This is a script developed for RELION to convert distribution of particle orientation to 2D. 　　
 Although RELION has a 3D distribution of particle orientations, detailed evaluation can be difficult in 3D. On the other hand, CryoSPARC has a 2D distribution of particle orientation, but it does not consider the symmetry of the structure.　　
 This script uses only the .star file output by Refine3D job. As a result, it outputs a 2D distribution of particle orientation. In addition, this script outputs symmetry-aware figure.　　
 This script allows for detailed evaluation, such as a quantitative evaluation of the particle orientation distribution.　　

## Requirement
・Linux　　
・Python (＞= 3.8)　　
・pip (＞= 21) 　　

## Usage
“python 2D_plot.py”　　
Please enter the input .star file path　　
Please enter the output .txt file path　　
Please enter the output 2D plot file path　　
Please enter the symmetry (C1, C2, D2, etc.)　　

## Author
Yonekura Lab. @Tohoku university　　
