import tensorflow as tf

def vamo_func(input_shape, n_class):
    vamo_base_model = tf.keras.applications.MobileNetV3Small(include_top=False, input_shape=input_shape, pooling='max')
    vamo_model = tf.keras.models.Sequential(
        [vamo_base_model,
        tf.keras.layers.Flatten(),
        tf.keras.layers.Dense(4096, activation='relu'),
        tf.keras.layers.Dense(2048, activation='relu'),
        tf.keras.layers.Dense(1024, activation='relu'),
        tf.keras.layers.Dense(512, activation='relu'),
        tf.keras.layers.Dense(n_class, activation='softmax')
        ],
        name = "vamo_model")
    return vamo_model