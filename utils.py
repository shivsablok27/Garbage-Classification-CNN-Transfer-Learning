import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

model = None  # <- Global reference

class_info = {
    0: 'Cardboard',
    1: 'Glass',
    2: 'Metal',
    3: 'Paper',
    4: 'Plastic',
    5: 'Trash'
}

def predict_trash(image_path):
    global model
    if model is None:
        model = load_model("best_model.h5", compile=False)

    img = image.load_img(image_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0

    predictions = model.predict(img_array)
    predicted_class_index = np.argmax(predictions[0])
    predicted_class_name = class_info[predicted_class_index]
    confidence_score = float(round(predictions[0][predicted_class_index] * 100, 2))

    return {
        'class': predicted_class_name,
        'confidence': confidence_score
    }
