import networkx as nx


def validate_source_point(graph, sx, sy, sz):
    assert validate_free_space_point(graph, sx, sy, sz), "Source point is invalid"


def validate_target_point(graph, dx, dy, dz):
    assert validate_free_space_point(graph, dx, dy, dz), "Target point is invalid"


def validate_free_space_point(graph, x, y, z):
    return graph.has_node((x, y, z))


def construct_free_space_graph(x_dim, y_dim, z_dim, xy_plane, yz_plane, zx_plane):
    free_space_graph = nx.grid_graph([x_dim, y_dim, z_dim])

    # remove illegal nodes according to obstacle planes
    # xy_plane illegal nodes removal
    for x_index in range(x_dim):
        for y_index in range(y_dim):
            if xy_plane[x_index][y_index] == 1:
                for z_index in range(z_dim):
                    if free_space_graph.has_node((x_index, y_index, z_index)):
                        free_space_graph.remove_node((x_index, y_index, z_index))

    # yz_plane illegal nodes removal
    for y_index in range(y_dim):
        for z_index in range(z_dim):
            if yz_plane[y_index][z_index] == 1:
                for x_index in range(x_dim):
                    if free_space_graph.has_node((x_index, y_index, z_index)):
                        free_space_graph.remove_node((x_index, y_index, z_index))

    # zx_plane illegal nodes removal
    for z_index in range(z_dim):
        for x_index in range(x_dim):
            if zx_plane[z_index][x_index] == 1:
                for y_index in range(y_dim):
                    if free_space_graph.has_node((x_index, y_index, z_index)):
                        free_space_graph.remove_node((x_index, y_index, z_index))

    return free_space_graph


def find_path(graph, sx, sy, sz, dx, dy, dz):
    source_node = (sx, sy, sz)
    target_node = (dx, dy, dz)
    shortest_path = nx.shortest_path(graph, source=source_node, target=target_node)
    return shortest_path
