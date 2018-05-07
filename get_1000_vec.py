from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array

from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions

model = VGG16()

image = load_img('fish.jpg', target_size=(224, 224))
image = img_to_array(image)
image = image.reshape((1, image.shape[0], image.shape[1], image.shape[2]))
image = preprocess_input(image)

prob = model.predict(image)
label = decode_predictions(prob)
print(label)





