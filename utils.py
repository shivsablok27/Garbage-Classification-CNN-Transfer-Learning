import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image

model = load_model("best_model.h5", compile=False)

class_info = {
    0: 'Cardboard',
    1: 'Glass',
    2: 'Metal',
    3: 'Paper',
    4: 'Plastic',
    5: 'Trash'
}

def predict_trash(image_path):
    # Load the image
    img = image.load_img(image_path, target_size=(224, 224))
    
    # Convert the image to an array
    img_array = image.img_to_array(img)
    
    # Expand dimensions to match model input shape
    img_array = np.expand_dims(img_array, axis=0)
    
    # Normalize the image array
    img_array /= 255.0
    
    # Make prediction
    predictions = model.predict(img_array)
    
    # Get the class index with the highest probability
    predicted_class_index = np.argmax(predictions[0])
    
    # Get the class name
    predicted_class_name = class_info[predicted_class_index]

    # Get the confidence score
    confidence_score = (predictions[0][predicted_class_index])* 100  # Convert to percentage
    confidence_score = float(round(confidence_score, 2))

    # Return the result as a dictionary
    return {
        'class': predicted_class_name,
        'confidence': confidence_score
    }
    

