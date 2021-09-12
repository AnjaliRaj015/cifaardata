from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
from werkzeug.utils import secure_filename
import cv2
import numpy as np

names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 'dog', 'frog', 'horse', 'ship', 'truck']
model = load_model('cifaar_10.h5')

def prediction(IMG_PATH):
    img = cv2.imread(IMG_PATH)
    img = cv2.resize(img, (32, 32))
    img = img/ 255.0
    img = img_to_array(img)
    img = np.expand_dims(img, axis=0)

    r = model.predict(img)

    label = np.argmax(r)
    labelName = names[label]
    print("The image is of ", labelName)

    pred = dict()
    pred['label'] = labelName
    return pred
