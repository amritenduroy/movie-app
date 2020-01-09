
def getRatings(user_id, movie_id):
    from tensorflow import keras
    import numpy as np
    model = keras.models.load_model('model.h5')
    u = np.reshape(np.array([user_id]),(-1,1))
    m = np.reshape(np.array([movie_id]),(-1,1))
    prediction = list(model.predict([u, m]))[0][0] + 3.50
    prediction = min(5, round(prediction, 1))
    model = None
    return prediction
