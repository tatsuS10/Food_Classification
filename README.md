# Food Classification

This model tells the users the names of food in the photo such as burger, pizza, or sushi, by using image classification with re-trained model.This model may be especially helpful for tourists to understand food even if they don’t know that food.This AI was created because I struggled with understanding the names of foods when traveling abroad, this AI helps me do that.

![Food Classification](https://github.com/user-attachments/assets/76a864cd-4d68-46f0-8483-501422e4d46e)

## The Algorithm

This project was developed using Jetson Nano. It uses a re-trained resnet18 model whose dataset consists of many foods images, each labelled by their food's name. When we run it, we use the Food-Classification.py program. 

Food-Classification.py is python file which has custom code to determine foods of an inputted image. This python file work by three sections. First, this model gets arguments from user and get image and network. In the second section, It classify the image by using re-trained model. Lastly, it make a result image and save it as an output_file which user told.

This model uses imagenet and resnet-18.  It uses imagenet to train the models. Resnet-18 is the base of the AI program. 


## Running this project

1. Make sure that both the Jetson Inference library and Python3 are installed on your Jetson Nano
2. Download the resnet18.onnx and the labels.txt from this project.
3. To classify an image, type: python3 Food_Classification.py 001.jpg test.jpg  ( You can change the input file by changing "001.jpg" to your image's path and you can also change the output filename by changing "test.jpg" as you want.)
4. Get the result in terminal and the result image in test.jpg ( you typed in upper one).

## Options

--model: change the custom model by typing its path

--labels: change the labels by tyoing its path

--input_blob: change name of the input blob

--output_blob: change name of the input blob


[View a video explanation here](video link)
