# Food Classification

This model tells the users the names of food in the photo such as burger, pizza, or sushi, by using image classification.
This model may be especially helpful for tourists to understand foods even if they don’t know that food.
![add image descrition here](direct image link here)

## The Algorithm

Add an explanation of the algorithm and how it works. Make sure to include details about how the code works, what it depends on, and any other relevant info. Add images or other descriptions for your project here. 

This re-trained resNet-18 model was created on Jetson Nano and trained on a dataset of many kinds of food images.


## Running this project

1. 
2. 

[View a video explanation here](video link)




imagenet --model=$NET/resnet18.onnx --input_blob=input_0 --output_blob=output_0 --labels=$DATASET/labels.txt /dev/video0 webrtc://@:8554/output
imagenet --model=$NET/resnet18.onnx --input_blob=input_0 --output_blob=output_0 --labels=$DATASET/labels.txt            $DATASET/test/burger $DATASET/test_output/burger