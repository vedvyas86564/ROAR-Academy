#importing libraries
import tensorflow as tf
import tensorflow_datasets as tfds

#Loading the MNIST Dataset
(ds_train, ds_test), ds_info = tfds.load(
    'mnist',
    #splitting the data for training and testing
    split=['train', 'test'],
    #shuffles the dataset for better testing
    shuffle_files=True,
    #Returns the dataset in (image, label) pairs.
    as_supervised=True,
    #Provides additional dataset information.
    with_info=True,
)
#normalize_img: A function to normalize the pixel values of the images from uint8 (0-255) to float32 (0-1).
def normalize_img(image, label):
  """Normalizes images: `uint8` -> `float32`."""
  return tf.cast(image, tf.float32) / 255., label
#ds_train.map: Applies the normalization function to each image.
ds_train = ds_train.map(
    normalize_img, num_parallel_calls=tf.data.AUTOTUNE) #num_parallel_calls=tf.data.AUTOTUNE: Optimizes the number of parallel calls for performance.
ds_train = ds_train.cache() #ds_train.cache(): Caches the dataset in memory for faster access.
ds_train = ds_train.shuffle(ds_info.splits['train'].num_examples) #ds_train.shuffle: Shuffles the dataset.
ds_train = ds_train.batch(128) #ds_train.batch(128): Batches the dataset into groups of 128 samples.
ds_train = ds_train.prefetch(tf.data.AUTOTUNE) #Prefetches the data for performance optimization.

ds_test = ds_test.map(
    normalize_img, num_parallel_calls=tf.data.AUTOTUNE)
ds_test = ds_test.batch(128)
ds_test = ds_test.cache()
ds_test = ds_test.prefetch(tf.data.AUTOTUNE)

model = tf.keras.models.Sequential([ #Defines a sequential model.
  tf.keras.layers.Flatten(input_shape=(28, 28)), #Flattens the 28x28 images into a 1D array of 784 elements.
  tf.keras.layers.Dense(128, activation='relu'), #Adds a dense (fully connected) layer with 128 units and ReLU activation.
  tf.keras.layers.Dense(10) #Adds a dense layer with 10 units (one for each digit class).
])
model.compile(
    optimizer=tf.keras.optimizers.Adam(0.001), #Uses the Adam optimizer with a learning rate of 0.001.
    loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True), #Uses sparse categorical cross-entropy loss function.
    metrics=[tf.keras.metrics.SparseCategoricalAccuracy()], #Tracks the sparse categorical accuracy metric.
)

model.fit(
    ds_train,#Trains the model.
    epochs=6,
    validation_data=ds_test, #The testing dataset for validation during training.
)