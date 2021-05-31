def mineral_formation(stones):
    return 1 in stones[0] and 1 in stones[3] and "both" or \
           1 not in stones[0] and "stalagmites" or\
           "stalactites"

