def pattern_detector(l):
    p = 1
    for i in range(1,int(len(l))):
        if (l[i] != l[i%p]):
            p=i+1
    return l[:p]