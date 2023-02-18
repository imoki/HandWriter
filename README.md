# HandWriter
判断两个手写签名之间的相似度

## 原理
1. 特征提取  
通过SIFT算法对两幅手写签名图片进行特征提取  
2. 相似度计算  
利用结构相似性算法（SSIM）计算相似度  
3. 相似度阈值设定
如果相似度大于 0.7，则可以认为两个图像是相似的  

## 运行  
python3运行
```
python handwrite.py
```

* 两张**不同**签名的对比  
调用compare_signatures函数，对比signature1和signature2签名
```
sim = compare_signatures('signature1.png', 'signature2.png')
```
输出：
```
相似度： 0.5455296833278869
```
  
  
* 两张**相同**签名的对比  
调用compare_signatures函数，对比signature1和signature1签名
```
sim = compare_signatures('signature1.png', 'signature1.png')
```
输出：
```
相似度： 1.0
```

## 其他  
代码仅供参考，由于签名的多样性和可变性，相同人的签名图片之间的相似度也可能不高。  
因此，需要根据具体应用场景和需求，设定合适的相似度阈值来判断两个签名是否来自同一人。  
