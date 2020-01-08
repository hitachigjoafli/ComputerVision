# -*- coding: utf-8 -*-

# This driver performs 2-functions for the validation images specified in configuration file:
#     1) evaluate fscore of validation images.
#     2) stores the prediction results of the validation images.

import argparse
import json
import cv2
import numpy as np
from yolo.frontend import create_yolo
from yolo.backend.utils.box import draw_scaled_boxes
from yolo.backend.utils.annotation import parse_annotation
from yolo.backend.utils.eval.fscore import count_true_positives, calc_score

from pascal_voc_writer import Writer
from shutil import copyfile
import os
import yolo


DEFAULT_CONFIG_FILE = os.path.join("/content/Yolo-digit-detector/configs", "raccoon.json")
DEFAULT_WEIGHT_FILE = os.path.join("/content/Yolo-digit-detector/save-files", "model.h5")
DEFAULT_THRESHOLD = 0.3



argparser = argparse.ArgumentParser(
    description='Predict digits driver')

argparser.add_argument(
    '-c',
    '--conf',
    default=DEFAULT_CONFIG_FILE,
    help='path to configuration file')

argparser.add_argument(
    '-t',
    '--threshold',
    default=DEFAULT_THRESHOLD,
    help='detection threshold')

argparser.add_argument(
    '-w',
    '--weights',
    default=DEFAULT_WEIGHT_FILE,
    help='trained weight files')

argparser.add_argument(
    '-p',
    '--path',
    default='/content/Yolo-digit-detector/tests/images',
    help='path to images')

def create_ann(filename, image, boxes, right_label, label_list):
    copyfile(os.path.join(args.path,filename), '/content/Yolo-digit-detector/tests/imgs/'+filename)
    writer = Writer(os.path.join(args.path,filename), 224, 224)
    print(right_label)
    for i in range(len(right_label)):
    	writer.addObject(label_list[right_label[i]], boxes[i][0], boxes[i][1], boxes[i][2], boxes[i][3])
    name = filename.split('.')
    writer.save('/content/Yolo-digit-detector/tests/ann/'+name[0]+'.xml')

if __name__ == '__main__':
    # 1. extract arguments
    args = argparser.parse_args()
    with open(args.conf) as config_buffer:
        config = json.loads(config_buffer.read())
    if config['train']['is_only_detect']:
        labels = ['']
    else:
        if config['model']['labels']:
            labels = config['model']['labels']
        else:
            labels = get_object_labels(config['train']['train_annot_folder'])
    print(labels)
    # 2. create yolo instance & predict
    yolo = create_yolo(config['model']['architecture'],
                       labels,
                       config['model']['input_size'],
                       config['model']['anchors'])
    yolo.load_weights(args.weights)

    # 3. read image
    write_dname = "/content/Yolo-digit-detector/tests/detected"
    if not os.path.exists(write_dname): os.makedirs(write_dname)
    annotations = parse_annotation(config['train']['valid_annot_folder'],
                                   config['train']['valid_image_folder'],
                                   config['model']['labels'],
                                   is_only_detect=config['train']['is_only_detect'])

    n_true_positives = 0
    n_truth = 0
    n_pred = 0
    for filename in os.listdir('/content/Yolo-digit-detector/tests/images'):
        img_path = os.path.join('/content/Yolo-digit-detector/tests/images',filename)
        img_fname = os.path.basename(img_path)
        suffix=filename.split(".")
        if suffix[1]== "jpg" or suffix[1]== "png" or suffix[1]== "JPEG" :
            image = cv2.imread(img_path)
            boxes, probs = yolo.predict(image, float(args.threshold))
            labels = np.argmax(probs, axis=1) if len(probs) > 0 else [] 
            # 4. save detection result
            image = draw_scaled_boxes(image, boxes, probs, config['model']['labels'])
            output_path = os.path.join(write_dname, os.path.split(img_fname)[-1])
            label_list = config['model']['labels']
            cv2.imwrite(output_path, image)
            print("{}-boxes are detected. {} saved.".format(len(boxes), output_path))
            if len(probs) > 0:
                create_ann(filename,image,boxes,labels,label_list)
                cv2.imwrite(output_path, image)
                print(label_list[labels[0]], " with a certainty of",probs[0][0])
