# coding=utf-8

import random



def permutation(n):
    ret = list(range(1, n+1))
    for _ in range(2 * n):
        i = random.randint(0, n-1)
        j = random.randint(0, n-1)
        ret[i], ret[j] = ret[j], ret[i]
    return ret


def flat_block(i, j, m, size):
    a, b = (i // size) * size, (j // size) * size
    ret = []
    for l in range(size):
        ret.extend(m[a+l][b:b+size])
    return ret


def valid(i, j, v, m, size):
    return not any([
        v in m[i],
        v in [k[j] for k in m],
        v in flat_block(i, j, m, size)
    ])


def randomize_algorithm(size):
    m = [['*' for _ in range(size**2)] for __ in range(size**2)]
    for i in range(size**2):
        for j in range(size**2):
            a = set(filter(lambda x: x != '*', [
                *[k[j] for k in m],
                *m[i],
                *flat_block(i, j, m, size)
            ]))
            b = list(set(range(1,size**2+1)) - a)
            if len(b) == 0:
                continue
            v = random.choice(list(b))
            m[i][j] = v
    return m


def backtracking(i, m, candidate, size):
    if i < size ** 4:
        x, y = i // size ** 2, i % size ** 2
        for v in candidate:
            if valid(x, y, v, m, size):
                m[x][y] = v
                if i == size ** 4 - 1:
                    return True
                done = backtracking(i+1, m, candidate, size)
                if not done:
                    m[x][y] = '*'
                else:
                    return True


def backtrack_algorithm(size):
    m = [['*' for _ in range(size**2)] for __ in range(size**2)]
    candidate = permutation(size**2)
    backtracking(0, m, candidate, size)
    return m
