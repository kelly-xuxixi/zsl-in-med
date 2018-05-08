from vgg16_places_365 import VGG16_Places365
from keras.preprocessing.image import load_img
from keras.preprocessing.image import img_to_array
from places_utils import preprocess_input
from config import cfg
import numpy as np
import os


def get_365_vec(model, folder_path):
    files = os.listdir(folder_path)
    imgs = []
    for file in files:
        if not os.path.isdir(file) and file.endswith('.jpg'):
            print(file)
            image = load_img(file, target_size=(224, 224))
            image = img_to_array(image)
            imgs.append(image)
    imgs = np.stack(imgs)
    imgs = preprocess_input(imgs)
    probs = model.predict(imgs)

    if cfg.vis_places_pred:
        predictions_to_return = 5
        top_preds = np.argsort(probs, axis=1)[:, ::-1]

        # load the class label
        file_name = 'categories_places365.txt'
        classes = list()
        with open(file_name) as class_file:
            for line in class_file:
                classes.append(line.strip().split(' ')[0][3:])
        classes = tuple(classes)

        print('--SCENE CATEGORIES:')
        # output the prediction
        for line in top_preds:
            for i in range(0, predictions_to_return):
                print(classes[line[i]])
            print('-------------')

    return probs


def main():
    folder_path = '.'
    model = VGG16_Places365(weights='places')
    get_365_vec(model, folder_path)


if __name__ == '__main__':
    main()