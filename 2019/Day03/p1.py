#!/usr/bin/python3

def create_path(in_str):
    point = (0,0)
    path = [point]
    for step in in_str:
        # print(step)
        direction = step[0]
        lenght = int(step[1:])
        if direction == 'U':
            for s in range(1, lenght + 1):
                path.append((point[0], point[1] + s))
            point = (point[0], point[1] + lenght)
        elif direction == 'D':
            for s in range(1, lenght + 1):
                path.append((point[0], point[1] - s))
            point = (point[0], point[1] - lenght)
        elif direction == 'R':
            for s in range(1, lenght + 1):
                path.append((point[0] + s, point[1]))
            point = (point[0] + lenght, point[1] )
        elif direction == 'L':
            for s in range(1, lenght + 1):
                path.append((point[0] - s, point[1]))
            point = (point[0] - lenght, point[1])
            
    # print(point)
    return path

def inters(la, lb):
    return list(set(la) & set(lb))

def m_dist(pa,pb):
    return abs(pa[0] - pb[0]) + abs(pa[1] - pb[1])

def input_proc(file_i):
    out = []
    with open(file_i) as f:
        for line in f:
            out.append([x for x in line.strip().split(',')])
    return out

def nstep(i, path):
    for pos, item in enumerate(path):
        if item == i:
            return pos

if __name__=="__main__":
    tmp = input_proc('input')
    path0 = create_path(tmp[0])
    path1 = create_path(tmp[1])
    intersection = inters(path0, path1)
    intersection.remove((0,0))
    min_dist = float('inf')
    min_point = None


    for i in intersection:
        step0 = nstep(i, path0)
        step1 = nstep(i, path1)
        tmp_d = step0 + step1
        if tmp_d < min_dist:
            min_dist = tmp_d
            min_point = i

    # for i in intersection:
        # if i == (0,0):
            # continue
        # tmp_d = m_dist((0,0), i)
        # if tmp_d < min_dist:
            # min_dist = tmp_d
            # min_point = i
    print(min_point)
    print(min_dist)

    


