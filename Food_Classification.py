#!/usr/bin/python3
import jetson_inference
import jetson_utils
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("input_filename", type=str, help="filename of the image to process")
parser.add_argument("output_filename",type=str, help="Path to save ")
parser.add_argument("--labels",type=str,default="jetson-inference/python/training/classification/data/Food-Classification-dataset/labels.txt",help="path to text file containing the labels for each class")
parser.add_argument("--model",type=str,default="jetson-inference/python/training/classification/models/Food-Classification/resnet18.onnx",help="path to custom model to load (caffemodel, uff, or onnx)")
parser.add_argument("--input-blob", type=str, default="input_0", help="Name of the input blob.")
parser.add_argument("--output-blob", type=str, default="output_0", help="Name of the output blob.")

opt = parser.parse_args()

#get the image and network
img = jetson_utils.loadImage(opt.input_filename)
net = jetson_inference.imageNet(
    model=opt.model,
    labels=opt.labels,
    input_blob=opt.input_blob,
    output_blob=opt.output_blob
)

#classify input image by custom model
class_idx, confidence = net.Classify(img)
class_description = net.GetClassDesc(class_idx)

#save the output imamge
jetson_utils.saveImage(opt.output_filename,img)

#print results
print("The image is classified as a " + class_description + " at class " +str(class_idx) + " with a confidence of " + str(confidence * 100) + "%")