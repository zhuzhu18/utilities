import io
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

def caculate_roc(threshold, dist, groundtruth):
    pred_mask = np.less(dist, threshold)
    tp = np.sum(np.logical_and(pred_mask, groundtruth))
    tn = np.sum(np.logical_and(np.logical_not(pred_mask), np.logical_not(groundtruth)))
    fp = np.sum(np.logical_and(pred_mask, np.logical_not(groundtruth)))
    fn = np.sum(np.logical_and(np.logical_not(pred_mask), groundtruth))

    tpr = tp / (tp + fn)
    fpr = fp / (fp + tn)

    acc = (tp + tn) / len(dist)

    return tpr, fpr, acc

dist = np.random.random(100)
groundtruth = np.random.choice([0, 1], 100)
thresholds = np.arange(0, 1, 0.01)

tprs = np.zeros(thresholds.shape)
fprs = np.zeros(thresholds.shape)
accs = np.zeros(thresholds.shape)

for idx, threshold in enumerate(thresholds):
    tprs[idx], fprs[idx], accs[idx] = caculate_roc(thresholds[idx], dist, groundtruth)
plt.xlabel('false positive rate', fontsize=14)
plt.ylabel('true positive rate', fontsize=14)
plt.title('ROC Curve', fontsize=14)
plt.xlim(0, 1)
plt.ylim(0, 1)
plt.plot(fprs, tprs, linewidth=2, color='red')
plt.fill_between(fprs, tprs, interpolate=True, color='green', alpha=0.5)

buff = io.BytesIO()
plt.savefig(buff, format='jpeg')
buff.seek(0)
plt.close()

image = Image.open(buff)
image.show()
