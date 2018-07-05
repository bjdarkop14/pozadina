import random
import numpy

def TwoPoint(ind1, ind2):
    size = min(len(ind1), len(ind2))
    cxpoint1 = random.randint(1, size)
    cxpoint2 = random.randint(1, size - 1)
    if cxpoint2 >= cxpoint1:
        cxpoint2 += 1
    else:
        cxpoint1, cxpoint2 = cxpoint2, cxpoint1

    ind1[cxpoint1:cxpoint2], ind2[cxpoint1:cxpoint2] \
        = ind2[cxpoint1:cxpoint2], ind1[cxpoint1:cxpoint2]

    return ind1, ind2

def OnePoint(ind1, ind2):
    size = min(len(ind1), len(ind2))
    cxpoint = random.randint(1, size - 1)
    ind1[cxpoint:], ind2[cxpoint:] = ind2[cxpoint:], ind1[cxpoint:]

    return ind1, ind2

def SrednjiCrossOver(ind1, ind2):
    old1_set = numpy.array(ind1)
    old2_set = numpy.array(ind2)
    return (old1_set + old2_set) / 2

def RandomCrossOver(ind1, ind2):
    rnd = random.randint(2,12)
    for i in range(0, rnd):
        rnd1 = random.randint(0, len(ind1))
        rnd2 = random.randint(0, len(ind2))
        print(len(ind1))
        print(len(ind2))
        ind1[rnd1], ind2[rnd2] = ind2[rnd2], ind1[rnd1]

    return ind1, ind2