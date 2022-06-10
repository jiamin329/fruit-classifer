import tensorflow as tf
import matplotlib.pyplot as plt
from tensorflow.python.keras.utils.vis_utils import plot_model
import settings

# 模型加载，指定图片处理的大小和是否进行迁移学习
def my_densenet():
    IMG_SHAPE = (224, 224, 3)
    # 选择base model
    # base_model = tf.keras.applications.VGG16(include_top=False, weights='imagenet', input_shape=IMG_SHAPE)
    # base_model = tf.keras.applications.ResNet50(include_top=False, weights='imagenet', input_shape=IMG_SHAPE)
    # base_model = tf.keras.applications.DenseNet121(include_top=False, weights='imagenet', pooling='max')
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
    # 输出模型结构
    plot_model(model, to_file='model.png', show_shapes=True, show_layer_names=False)
    return model



# 展示训练过程的曲线
def show_loss_acc(history):
    acc = history.history['accuracy']
    val_acc = history.history['val_accuracy']

    loss = history.history['loss']
    val_loss = history.history['val_loss']

    plt.figure(figsize=(8, 8))
    plt.subplot(2, 1, 1)
    plt.plot(acc, label='Training Accuracy')
    plt.plot(val_acc, label='Validation Accuracy')
    plt.legend(loc='lower right')
    plt.ylabel('Accuracy')
    plt.ylim([min(plt.ylim()), 1])
    plt.title('Training and Validation Accuracy')

    plt.subplot(2, 1, 2)
    plt.plot(loss, label='Training Loss')
    plt.plot(val_loss, label='Validation Loss')
    plt.legend(loc='upper right')
    plt.ylabel('Cross Entropy')
    plt.ylim([0, 1.0])
    plt.title('Training and Validation Loss')
    plt.xlabel('epoch')
    plt.show()


if __name__ == '__main__':
    model = my_densenet()
    model.summary()
