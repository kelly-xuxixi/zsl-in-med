from vgg16_hybrid_places_1365 import VGG16_Hubrid_1365
from keras.preprocessing import image
from places_utils import preprocess_input
import numpy as np

model = VGG16_Hubrid_1365(weights='places', include_top=True)

res_path = 'restaurant.jpg'
fish_path = 'fish.jpg'
bak_path = 'bakery.jpg'
res_img = image.load_img(res_path, target_size=(224, 224))
fish_img = image.load_img(fish_path, target_size=(224, 224))
bak_img = image.load_img(bak_path, target_size=(224, 224))
x = np.stack([image.img_to_array(res_img), image.img_to_array(fish_img), image.img_to_array(bak_img)])
print(x.shape)
# x = np.expand_dims(x, axis=0)
x = preprocess_input(x)

probs = model.predict(x)
# print(probs.shape)
# print(probs[:][:10])

preds = np.argsort(probs, axis=1)[:, ::-1]
print(preds[:][:20])  # top 20 categories (not accurate however)
# print(probs[0][preds[0][:20]])
# print(probs[1][preds[1][:20]])
# print(probs[2][preds[1][:20]])
