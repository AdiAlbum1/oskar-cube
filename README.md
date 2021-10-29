# Oskar's Cube Algorithmic Solution

## Table of Contents

- [Task](#task)
- [Installation](#installation)
- [Usage](#usage)
- [Verify Results](#verify_results)

## Task
Write a program that solves Oskar’s cube. The matrices that describe the faces
of the cube appear in the course’s website, together with specifications how to output a solution path
from start to goal
[The Course's Website](http://acg.cs.tau.ac.il/courses/algorithmic-robotics/fall-2021-2022/assignments/assignment-1)

## Installation
```sh
git clone https://github.com/AdiAlbum1/oskar-cube
cd oskar-cube
pip install -r requirments.txt
```

## Usage
```sh
python oskar.py sx sy sz dx dy dz filename
```
Where:
- sx, sy, sz are the source point's position
- dx, dy, dz are the target point's position
- filename is the path to obstacle description file

## Verify Results
Results will be saved to solution.txt file, you may verify the result is correct with [The Simulator](http://www.cs.tau.ac.il/~michaelmoshe/oskar-visualization/)