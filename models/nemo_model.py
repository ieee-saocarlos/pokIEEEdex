import tensorflow as tf

def nemo_func(input_shape, n_class):
    pre_trained_model = tf.keras.applications.InceptionV3(input_shape = input_shape, 
                                                          include_top = False, 
                                                          weights = "imagenet")

    last_layer = pre_trained_model.get_layer('mixed7')
    # print('last layer output shape: ', last_layer.output_shape)
    last_output = last_layer.output

    x = tf.keras.layers.Flatten()(last_output)
    x = tf.keras.layers.Dense(1024, activation='relu')(x)
    x = tf.keras.layers.Dropout(0.2)(x)    
    x = tf.keras.layers.Dense(n_class, activation='sigmoid')(x)           

    nemo_model = tf.keras.models.Model(pre_trained_model.input, x, name = "nemo_model")
    return nemo_model