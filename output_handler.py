def edge_to_command(edge):
    source = edge[0]
    target = edge[1]

    if target[0] - source[0] == 1:
        return 0
    elif target[0] - source[0] == -1:
        return 1
    if target[1] - source[1] == 1:
        return 2
    elif target[1] - source[1] == -1:
        return 3
    if target[2] - source[2] == 1:
        return 4
    elif target[2] - source[2] == -1:
        return 5


def write_output(sx, sy, sz, dx, dy, dz, path):
    # write source point
    print("%d %d %d" % (sx, sy, sz))

    # write target point
    print("%d %d %d" % (dx, dy, dz))

    edges = list(zip(path, path[1:]))

    # if no path exists - write -1 command
    if len(edges) == 0:
        print("-1")
    else:
        for edge in edges:
            command = edge_to_command(edge)
            print("%d " % command)
