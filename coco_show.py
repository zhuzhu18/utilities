from pycocotools import coco
import matplotlib.pyplot as plt
import skimage.io as io
import time

time1 = time.time()
annFile = '/media/zhuzhu/ec114170-f406-444f-bee7-a3dc0a86cfa2/dataset/coco/annotations/person_keypoints_val2017.json'
dataDir = '/media/zhuzhu/ec114170-f406-444f-bee7-a3dc0a86cfa2/dataset/coco/images/val2017'
saveDir = '/media/zhuzhu/ec114170-f406-444f-bee7-a3dc0a86cfa2/coco_ground/val2017'

coco = coco.COCO(annFile)
catIds = coco.getCatIds(catNms=['person'])
imgIds = coco.getImgIds(catIds=catIds)

for idx in imgIds:
    img = coco.loadImgs(ids=idx)[0]
    annIds = coco.getAnnIds(imgIds=idx, catIds=catIds)
    anns = coco.loadAnns(ids=annIds)
    plt.figure(idx)
    I = io.imread('%s/%s'%(dataDir, img['file_name']))
    plt.imshow(I)
    plt.axis('off')
    coco.showAnns(anns=anns)
    plt.savefig('%s/%s' % (saveDir, img['file_name']))
    plt.close()

time2 = time.time()
print('spent t = %.2f min' % ((time2 - time1) / 60))
