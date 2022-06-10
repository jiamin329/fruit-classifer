# 图片类别
FRUIT_CLASS = {
    '苹果': '01',
    '香蕉': '02',
    '桃子': '03',
    '葡萄': '04'
}

# 图片保存根目录
IMAGES_ROOT = 'photos'

# 每个类别选取的图片数量
SAMPLES_PER_CLASS = 400

# 参与训练的类别
CLASSES = ['01', '02', '03', '04']

# 参与训练的类别数量
CLASS_NUM = len(CLASSES)

# 类别->编号的映射
CLASS_CODE_MAP = {
    '01': 0,
    '02': 1,
    '03': 2,
    '04': 3
}

# 编号->类别的映射
CODE_CLASS_MAP = {
    0: '苹果',
    1: '香蕉',
    2: '桃子',
    3: '葡萄'
}

# 随机数种子
RANDOM_SEED = 13  # 四个类别时样本较为均衡的随机数种子
# RANDOM_SEED = 19  # 三个类别时样本较为均衡的随机数种子

# 训练集比例
TRAIN_DATASET = 0.6
# 开发集比例
DEV_DATASET = 0.2
# 测试集比例
TEST_DATASET = 0.2

# mini_batch大小
BATCH_SIZE = 16

# imagenet数据集均值
IMAGE_MEAN = [0.485, 0.456, 0.406]
# imagenet数据集标准差
IMAGE_STD = [0.299, 0.224, 0.225]

# 学习率
LEARNING_RATE = 0.001
# 训练epoch数
TRAIN_EPOCHS = 3
# 保存训练模型的路径
MODEL_PATH = 'model.h5'

# Web服务端口
WEB_PORT = 5000