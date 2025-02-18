# 2D-distribution-of-particle-orientation-for-RELION

## Overview
 This is a script developed for RELION to convert distribution of particle orientation to 2D. <br>
 Although RELION has a 3D distribution of particle orientations, detailed evaluation can be difficult in 3D. On the other hand, CryoSPARC has a 2D distribution of particle orientation, but it does not consider the symmetry of the structure.<br>
 This script uses only the .star file output by Refine3D job. As a result, it outputs a 2D distribution of particle orientation. In addition, this script outputs symmetry-aware figure.<br>
 This script allows for detailed evaluation, such as a quantitative evaluation of the particle orientation distribution.<br>

## Requirement
・Linux<br>
・Python (＞= 3.8)<br>
・pip (＞= 21) <br>

## Usage
“python 2D_plot.py”<br>
Please enter the input .star file path<br>
Please enter the output .txt file path<br>
Please enter the output 2D plot file path<br>
Please enter the symmetry (C1, C2, D2, etc.)<br>

## Author
Yonekura Lab. @Tohoku university$('https://www2.tagen.tohoku.ac.jp/lab/yonekura/').hide();<br>
