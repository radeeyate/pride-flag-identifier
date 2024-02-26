from keras.models import load_model
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from keras.applications.vgg16 import VGG16
import numpy as np

from keras.models import load_model

model = load_model('./flags.h5')

image = load_img('data/test/trans/1.jpg', target_size=(500, 500))
img = np.array(image)
img = img / 255.0
img = img.reshape(1,500,500,3)
label = model.predict(img)
classes = {0: "pride", 1: "trans"}
print(label[0][0])
print(f"Predicted Class: {classes[round(label[0][0])]}")