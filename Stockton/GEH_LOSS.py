import tensorflow as tf
epsilon = 0.000001


def GEH_loss(actual, predicted):      # my GEH
    actual = actual * 12
    predicted = predicted * 12
    
    geh_vector = tf.sqrt(2 * (tf.square(predicted - actual + epsilon)) / (predicted + actual + epsilon))
    fail_count = geh_vector[geh_vector>5]
    
    return tf.reduce_mean(fail_count)


def rGEH_loss(actual, predicted):     # Relative GEH loss
    actual = actual * 12
    predicted = predicted * 12
    
    geh_vector = tf.sqrt(2 * (tf.square(predicted - actual + epsilon)) / (predicted + actual + epsilon))
    fail_count = geh_vector[geh_vector>0]
    
    return tf.reduce_mean(fail_count)


# def rcustom_loss(actual, predicted):     # loss
#     actual = actual * 12
#     predicted = predicted * 12
    
#     # outputs a value between 0 and 20
#     vector = tf.sqrt(2 * (tf.square(predicted - actual + epsilon)) / (predicted + actual + epsilon))
#     vector = vector[vector>5]
    
#     # sigmoid of elements above threshold value of 5
#     fail_count = tf.math.sigmoid(vector)
    
#     return tf.reduce_sum(fail_count)


def custom_loss(actual, predicted):     # loss
    actual = actual * 12
    predicted = predicted * 12
    
    # outputs a vector of GEHs
    vector = tf.sqrt(2 * (tf.square(predicted - actual + epsilon)) / (predicted + actual + epsilon))
    total = tf.cast(tf.size(vector), tf.float32)          # Keeps mean divisor constant
    
    # sigmoid of elements above threshold value of 5
    vector = vector[vector>5]
    fail_count = tf.math.sigmoid(vector)
    
    return tf.reduce_sum(fail_count)/total