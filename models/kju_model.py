import tensorflow as tf

def kju_func(input_shape, n_class):
    kju_model = tf.keras.models.Sequential([
        tf.keras.layers.Conv2D(filters = 96,kernel_size=(11,11),strides=(4,4),padding='valid',activation='relu',input_shape=input_shape),
        tf.keras.layers.BatchNormalization(axis=-1),
        tf.keras.layers.MaxPooling2D((3,3),strides=(2,2)),
        tf.keras.layers.Conv2D(256,(5,5),activation='relu',padding='same',strides=(1,1)),
        tf.keras.layers.BatchNormalization(axis=-1),
        tf.keras.layers.MaxPooling2D((3,3),strides=(2,2)),
        tf.keras.layers.Conv2D(384,(3,3),activation='relu',padding='same',strides=(1,1)),
        tf.keras.layers.Conv2D(384,(3,3),activation='relu',padding='same',strides=(1,1)),
        tf.keras.layers.Conv2D(256,(3,3),activation='relu',padding='same',strides=(1,1)),
        tf.keras.layers.BatchNormalization(axis=-1),
        tf.keras.layers.MaxPooling2D((3,3),strides=(2,2)),
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dropout(.5),
        tf.keras.layers.Dense(1024, activation='relu'),
        tf.keras.layers.BatchNormalization(axis=-1),
        tf.keras.layers.Dropout(.5),
        tf.keras.layers.Dense(1024, activation='relu'),
        tf.keras.layers.BatchNormalization(axis=-1),
        tf.keras.layers.Dropout(.5),
        tf.keras.layers.Dense(n_class, activation='softmax')
        ],
        name = "kju_model")
    return kju_model