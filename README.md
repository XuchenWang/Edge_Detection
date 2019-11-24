# Xuchen Wang - CIS 581 Project 1

This project uses canny edge detection to draw out image edge.

## Getting Started

The folder contains several scripts: findDerivatives.py contains the findDerivatives function that can detects the magnitude and the orientation of the image derivatives; nonMaxSup.py combine the lines to make edges thinner; edgeLink.py links the edges together by two thresholds; cannyEdge.py is the main file that execute the three files mentioned above.

## Running the tests

Simply running cannyEdge.py will get the image gradients (magnitude, x-axis, y-axis, and orientation), as will as the results of nonMaxSup and edgeLink. The images are stored in the folder called images. 

## Acknowledgments

* Collaberated with Yuezhan Tao for this project.

