import tensorflow as tf
import matplotlib.pyplot as plt

#  Imagenes 28x28
mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()

plt.imshow(x_train[0])
plt.show()

print(x_train[0])

x_train = tf.keras.utils.normalize(x_train, axis=1)
