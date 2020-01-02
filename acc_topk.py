def acc_topk(output, target, topk=(1, )):
    maxk = max(topk)
    pred = np.argsort(output, axis=1)[:, -maxk:]

    acc_k = []
    for k in topk:
        correct_k = np.equal(pred[:, -k:], np.expand_dims(target, 1))
        acc_k.append(correct_k.sum() / target.shape[0])

    return acc_k

import numpy as np

output = np.array([[0.1, 0.7, 0.2],[0.6, 0.1, 0.3], [0.1, 0.3, 0.6]])
target = np.ones(3)

a = acc_topk(output, target, (1, 2, 3))
print(a)
