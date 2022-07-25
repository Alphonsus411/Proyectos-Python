# 4 layer CNN with a softmax output
# test on MNIST data set
# You'll need a gpu and a cudnn library to be installed on your system.
from keras.datasets import mnist

# use a simple structure for your network
# one input, one output (softmax).
model = Sequential()
model.add(Conv2D(filters=20, kernel_size=(5, 5), input_shape=(28, 28, 1)))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Flatten())
model.add(Dense(units=128, activation='relu'))
model.add(Dense(units=10, activation='softmax'))

# create the train/test data loader and the trainer
# keras requires input data to be in a special format
from keras.utils.data_utils import get_file

mnist_path = get_file('mnist_data.npz', shape=(60000, 28, 28, 1),
                      origin='http://yann.lecun.com/exdb/mnist/', checksum=False)
mnist_train, mnist_test = mnist.load_data(mnist_path)

# To evaluate the model on a train dataset, the file should look like this:
# 1- n_samples - n_timesteps - n_samples_per_timestep - n_features - 1
X_train = np.zeros((len(mnist_train), 60000, 28, 28, 1))
y_train = np.zeros((len(mnist_train), 60000), dtype=int)

# we must normalize the data and make it 0-1
X_train = X_train.astype('float32')
X_train /= 255

for i in range(60000):
    image = mnist_train[i].reshape((1, 28, 28, 1))
    y_train[i] = mnist_train[i][0]
    image = np.expand_dims(image, axis=3)
    image = np.expand_dims(image, axis=0)
    image = image.astype('float32') / 255
    X_train[i, :, :, 0] = image

model.fit(X_train, y_train,
          epochs=5,
          batch_size=500,
          validation_data=(X_test, y_test))

print('Evaluation on the test set:')
print(model.evaluate(X_test, y_test, verbose=1))

if __name__ == "__main__":
    # train a model
    model.compile(loss='categorical_crossentropy', optimizer='adam')
    # print(model.summary())
    # learn on dataset
    model.fit(X_train, y_train, batch_size=300, epochs=50)
