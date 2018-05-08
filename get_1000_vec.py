from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array

from keras.applications.vgg16 import VGG16
from keras.applications.vgg16 import preprocess_input
from keras.applications.vgg16 import decode_predictions
from config import cfg

import numpy as np
import os


def get_1000_vec(model, folder_path):
    files = os.listdir(folder_path)
    imgs = []
    for file in files:
        if not os.path.isdir(file) and file.endswith('.jpg'):
            print(file)
            image = load_img(file, target_size=(224, 224))
            image = img_to_array(image)
            print(image.shape)
            imgs.append(image)
    imgs = np.stack(imgs)
    imgs = preprocess_input(imgs)
    probs = model.predict(imgs)

    if cfg.vis_imagenet_pred:
        predictions_to_return = 5
        top_preds = np.argsort(probs, axis=1)[:, ::-1]

        # load the class label
        file_name = 'imageNet_1000.txt'
        classes = list()
        with open(file_name) as class_file:
            for line in class_file:
                line = line.strip()
                idx = line.index(' ')
                line = line[idx + 1:]
                classes.append(line)
        classes = tuple(classes)

        print('--IMAGENET CATEGORIES:')
        # output the prediction
        for line in top_preds:
            for i in range(0, predictions_to_return):
                print(classes[line[i]])
            print('-------------')

    return probs


def main():
    folder_path = '.'
    model = VGG16()
    get_1000_vec(model, folder_path)


if __name__ == '__main__':
    main()





