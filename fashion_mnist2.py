import numpy as np
import os
from keras import backend as K
from keras.layers.convolutional import Conv2D, MaxPooling2D
from keras.layers.core import Activation, Flatten, Dense,Dropout
from keras.models import Sequential
from keras.utils import np_utils, plot_model
from keras.initializers import Constant
from keras.optimizers import Adam
import matplotlib.pyplot as plt

os.chdir('C:\\Users\\tatab\\OneDrive\\Data\\fashion-mnist')
os.environ["PATH"] += os.pathsep + 'C:/Program Files (x86)/Graphviz2.38/bin/'
def load_mnist(path, kind='train'):
    import gzip

    """Load MNIST data from `path`"""
    labels_path = os.path.join(path,
                               '%s-labels-idx1-ubyte.gz'
                               % kind)
    images_path = os.path.join(path,
                               '%s-images-idx3-ubyte.gz'
                               % kind)
    with gzip.open(labels_path, 'rb') as lbpath:
        labels = np.frombuffer(lbpath.read(), dtype=np.uint8,
                               offset=8)
    with gzip.open(images_path, 'rb') as imgpath:
        images = np.frombuffer(imgpath.read(), dtype=np.uint8,
                               offset=16).reshape(len(labels), 784)
    return images, labels

X_train, y_train = load_mnist('data/fashion', kind='train')
X_test, y_test = load_mnist('data/fashion', kind='t10k')

X_train = X_train.astype('float32') / 255
X_test = X_test.astype('float32') / 255

X_train = X_train.reshape(X_train.shape[0], 1, 28, 28)
X_test = X_test.reshape(X_test.shape[0], 1, 28, 28)
y_train = np_utils.to_categorical(y_train, 10)
y_test = np_utils.to_categorical(y_test, 10)

K.set_image_dim_ordering("th")
# LeNet(relu)
model = Sequential()
model.add(Flatten(input_shape=(1, 28, 28)))

# model.add(Conv2D(20, padding="same",kernel_size=5,  input_shape=(1, 28, 28)))
# model.add(Activation("relu"))
# model.add(MaxPooling2D())
# model.add(Dropout(0.1))
#
# model.add(Conv2D(50, padding="same", kernel_size=5))
# model.add(Activation("relu"))
# model.add(MaxPooling2D())
# model.add(Dropout(0.2))
#
#
# model.add(Conv2D(50, padding="same", kernel_size=5))
# model.add(Activation("relu"))
# model.add(MaxPooling2D())
# model.add(Dropout(0.2))
#
# model.add(Flatten())
model.add(Dense(500))
model.add(Dropout(0.3))


#model.add(Dense(2000))

model.add(Activation("relu"))

model.add(Dense(500))
model.add(Dropout(0.3))
model.add(Activation("relu"))

model.add(Dense(500))
model.add(Dropout(0.3))
model.add(Activation("relu"))

model.add(Dense(10))
model.add(Activation("softmax"))

#モデルのサマリ
model.summary()
plot_model(model, show_shapes=True, show_layer_names=True, to_file='model.png')

model.compile(loss="categorical_crossentropy", optimizer=Adam(), metrics=["accuracy"])
history = model.fit(X_train, y_train, batch_size=128, epochs=30, verbose=1, validation_split=0.2)

score = model.evaluate(X_test, y_test, verbose=1)
print("Test score:", score[0])
print("Test accuracy:", score[1])
print(history.history.keys())

# グラフの表示
plt.plot(history.history['acc'])
plt.plot(history.history['val_acc'])
plt.title('model accuracy')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('model loss')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()