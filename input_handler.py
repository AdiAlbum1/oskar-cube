import argparse
import os
import numpy as np

def parse_input():
    parser = argparse.ArgumentParser(description='Process Oskar\'s Cube inputs')
    parser.add_argument('sx', type=int, nargs=1, help='source point - x position')
    parser.add_argument('sy', type=int, nargs=1, help='source point - y position')
    parser.add_argument('sz', type=int, nargs=1, help='source point - z position')
    parser.add_argument('dx', type=int, nargs=1, help='target point - x position')
    parser.add_argument('dy', type=int, nargs=1, help='target point - y position')
    parser.add_argument('dz', type=int, nargs=1, help='target point - z position')
    parser.add_argument('filename', type=str, nargs=1, help='a filename of a file describing the obstacles')

    args = parser.parse_args()

    sx = args.sx[0]
    sy = args.sy[0]
    sz = args.sz[0]
    dx = args.dx[0]
    dy = args.dy[0]
    dz = args.dz[0]
    filename = args.filename[0]

    return sx, sy, sz, dx, dy, dz, filename

# A simple series of tests to validate input
def validate_input(sx, sy, sz, dx, dy, dz, filename):
    assert sx >= 0 and sy >= 0 and sz >= 0, "Invalid source point - must be non-negative position"
    assert dx >= 0 and dy >= 0 and dz >= 0, "Invalid target point - must be non-negative position"
    assert os.path.isfile(filename), "file doesn't exist"

def parse_obstacle_file_dimensions(obstacle_file):
    first_line = obstacle_file.readline()
    dimension_lst = list(map(int, first_line.split()))
    x_dim, y_dim, z_dim = dimension_lst

    return x_dim, y_dim, z_dim

def parse_obstacle_file(filename):
    obstacle_file = open(filename, "r")
    x_dim, y_dim, z_dim = parse_obstacle_file_dimensions(obstacle_file)

    xy_plane = np.zeros((x_dim, y_dim), dtype=int)
    yz_plane = np.zeros((y_dim, z_dim), dtype=int)
    xz_plane = np.zeros((x_dim, z_dim), dtype=int)

    for i in range(z_dim):
        xy_plane[i][:] = list(map(int, obstacle_file.readline().split()))

    obstacle_file.readline()
    for i in range(x_dim):
        yz_plane[i][:] = list(map(int, obstacle_file.readline().split()))

    obstacle_file.readline()
    for i in range(y_dim):
        xz_plane[i][:] = list(map(int, obstacle_file.readline().split()))

    return xy_plane, yz_plane, xz_plane