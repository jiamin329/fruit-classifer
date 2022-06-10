# 水果分类 fruit-classifer

基于深度学习的水果分类

本项目使用迁移学习技术，对在ImageNet数据集上带有预训练权重VGG16、ResNet50、MobileNetV2、DenseNet121模型进行微调，然后将其用在水果数据集上。最终训练后的模型能够准确对输入图片进行分类，并且最高准确率达到93.08%。

#### 一、数据集制作

##### 1.1爬虫获取数据

```python
FRUIT_CLASS = {
    '苹果': '01',
    '香蕉': '02',
    '桃子': '03',
    '葡萄': '04'
}
#spider.py实现本功能
```

##### 1.2手动删除不相关图片

##### 1.3数据增强扩充数据集

```python
def Brightness(root_path, img_name): 	#亮度增强
def Contrast(root_path, img_name): 		#对比度增强
def crop(root_path, img_name): 			#随机裁剪
def flip(root_path, img_name): 			#左右翻转
def rotation(root_path, img_name): 		#随机旋转
#createImage.py ImageEnhance.py实现本功能
```

#### 二、模型训练

##### 2.1迁移学习

```python
# 模型加载，指定图片处理的大小和是否进行迁移学习
def my_densenet():
    IMG_SHAPE = (224, 224, 3)
    # 选择base model
    base_model = tf.keras.applications.MobileNetV2(include_top=False, weights='imagenet', input_shape=IMG_SHAPE)

    base_model.trainable = False
    model = tf.keras.models.Sequential([
        # 输入层，shape为(None,224,224,3)
        tf.keras.layers.Input((224, 224, 3)),
        # 输入到base_model中
        base_model,
        # 将base_model的输出展平，以作为全连接层的输入
        tf.keras.layers.Flatten(),
        # BN层
        tf.keras.layers.BatchNormalization(),
        # 输出层，为了保证输出结果的稳定，这里就不添加Dropout层了
        tf.keras.layers.Dense(settings.CLASS_NUM, activation=tf.nn.softmax)
        ])
    return model
#models.py实现本功能
```

##### 2.2模型训练

```python
# settings.py	参数设置
# data.py		数据预处理
# train.py 		训练模型
```

#### 三、系统实现

设计并实现前后端分离系统，前端Vue，后端Flask

后端模型对输入图片识别并返回用户

运行app.py在本地计算机使用系统，地址为http://192.168.1.29:5000/


