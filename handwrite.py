import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim

def compare_signatures(img_path1, img_path2):
    # 读入两张签名图片
    img1 = cv2.imread(img_path1, 0)
    img2 = cv2.imread(img_path2, 0)

    # 调整图片大小
    img1 = cv2.resize(img1, (200, 100))
    img2 = cv2.resize(img2, (200, 100))

    # 提取SIFT特征
    sift = cv2.SIFT_create()
    keypoints1, descriptors1 = sift.detectAndCompute(img1, None)
    keypoints2, descriptors2 = sift.detectAndCompute(img2, None)

    # BFMatcher进行匹配
    matcher = cv2.BFMatcher()
    matches = matcher.match(descriptors1, descriptors2)

    # 选出最佳匹配
    matches = sorted(matches, key=lambda x: x.distance)
    good_matches = matches[:10]

    # 计算相似度, 结构相似性算法（SSIM）
    # 基于均值、方差和协方差的指标，可以用来衡量两幅图像的质量和相似度。
    # SSIM 相似度的计算过程中，涉及到对两幅图像的余弦相似度进行加权平均。
    sim = ssim(img1, img2)

    return sim

# 如果相似度大于 0.7，则可以认为两个图像是相似的

# 相似度： 0.5455296833278869
sim = compare_signatures('signature1.png', 'signature2.png')

# 相似度： 1.0
# sim = compare_signatures('signature1.png', 'signature1.png')
print('相似度：', sim)