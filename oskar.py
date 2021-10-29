from input_handler import parse_input, validate_input, parse_obstacle_file
from graph_handler import find_path, construct_free_space_graph, validate_source_point, validate_target_point
from output_handler import write_output

if __name__ == "__main__":
    # handle input
    sx, sy, sz, dx, dy, dz, filename = parse_input()
    validate_input(sx, sy, sz, dx, dy, dz, filename)
    x_dim, y_dim, z_dim, xy_plane, yz_plane, zx_plane = parse_obstacle_file(filename)

    # construct free-space graph, and find solution
    free_space_graph = construct_free_space_graph(x_dim, y_dim, z_dim, xy_plane, yz_plane, zx_plane)
    validate_source_point(free_space_graph, sx, sy, sz)
    validate_target_point(free_space_graph, dx, dy, dz)
    path = find_path(free_space_graph, sx, sy, sz, dx, dy, dz)

    # handle output
    write_output("solution.txt", sx, sy, sz, dx, dy, dz, path)
