from pycocotools.coco import COCO
import matplotlib.pyplot as plt

coco = COCO('/media/zhuzhu/ec114170-f406-444f-bee7-a3dc0a86cfa2/dataset/coco/annotations/person_keypoints_val2017.json')
cat_idx = coco.getCatIds(catNms='person')
img_idx = coco.getImgIds(catIds=cat_idx)
annIds = coco.getAnnIds(imgIds=img_idx[80], catIds=cat_idx)
anns = coco.loadAnns(annIds)         # 长度为一张图片上人的个数的列表, 列表的每个元素是一个字典,
                                     # 包含这个人的标注, 即'segmentation', 'num_keypoints',
                                     # 'area', 'iscrowd', 'keypoints', 'image_id', 'bbox'
                                     # 'category_id', 'id'
# coco.showAnns(anns)
