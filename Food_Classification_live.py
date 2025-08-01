#!/usr/bin/python3
import jetson_inference
import jetson_utils
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--input",type=str,default="/dev/video0",help="path to the device")
parser.add_argument("--labels",type=str,default="jetson-inference/python/training/classification/data/Food-Classification-dataset/labels.txt",help="path to text file containing the labels for each class")
parser.add_argument("--model",type=str,default="jetson-inference/python/training/classification/models/Food-Classification/resnet18.onnx",help="path to custom model to load (caffemodel, uff, or onnx)")
parser.add_argument("--input-blob", type=str, default="input_0", help="Name of the input blob.")
parser.add_argument("--output-blob", type=str, default="output_0", help="Name of the output blob.")

opt = parser.parse_args()

net = jetson_inference.imageNet(
    model=opt.model,
    labels=opt.labels,
    input_blob=opt.input_blob,
    output_blob=opt.output_blob
)

camera = jetson_utils.videoSource(opt.input)
display = jetson_utils.videoOutput("display://0")

while display.IsStreaming():
    img = camera.Capture()
    class_idx, confidence =net.Classify(img)
    label = net.GetClassDesc(class_idx)
    jetson_utils.cudaDrawText(img,f"{label}({confidence*100:.1f}%)")
    display.Render(img)
    display.SetStatus(f"{label}({confidence*100:.1f}%)")