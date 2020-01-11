import numpy as np

a = np.array([500, 900])

def resize(a, min_size=608, max_size=1024):
    '''
    控制最大边长不超过1024, 最短边长不超过608, 且其中一条边长等于608或1024
    '''
    scale = min_size / min(a)
    if scale * max(a) > max_size:
        scale = max_size / max(a)

    return scale * a

print(resize(a))
