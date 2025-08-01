# Food Classification

This model tells the users the names of food in the photo such as burger, pizza, or sushi, by using image classification with re-trained model.This model may be especially helpful for tourists to understand food even if they don’t know that food.This AI was created because I struggled with understanding the names of foods when traveling abroad, this AI helps me do that.

![Food Classification](https://github.com/user-attachments/assets/76a864cd-4d68-46f0-8483-501422e4d46e)

## The Algorithm

This project was developed using Jetson Nano. It uses a re-trained resnet18 model whose dataset consists of many foods images, each labelled with its food name. When we run it, we use the python file named Food-Classification.py. 

Food-Classification.py is python file which has custom code to determine foods of an inputted image. This python file work by three sections.
First, this model gets arguments from user and get image and network. 
<img width="822" height="203" alt="Screenshot (4)" src="https://github.com/user-attachments/assets/e3f47969-efc4-42bc-8655-80b0664e5e3f" />

In the second section, It classify the image by using re-trained model. 
<img width="717" height="106" alt="Screenshot (5)" src="https://github.com/user-attachments/assets/fba5c6f0-afa6-471e-bd80-3d38901ca2d1" />

Lastly, it make a result image and save it as an output_file which user told.
<img width="891" height="201" alt="Screenshot (6)" src="https://github.com/user-attachments/assets/908b482d-ccd2-4909-8338-6d6668c45279" />


## Running this project

1. Make sure that both the Jetson Inference library and Python3 are installed on your Jetson Nano
2. Download the Food_Classification file which contains resnet18.onnx and the labels.txt from this project
3. Make sure to lotate in ~/Food_Classification
4. To classify an image, type: python3 Food_Classification.py image.jpg test.jpg  ( You can change the input file by changing "image.jpg" to your image's path and you can also change the output filename by changing "test.jpg" as you want)
5. Get the result in terminal and the result image in test.jpg ( you typed in upper one)

My demonstration video: https://youtu.be/YKZm_kSHmxM

## Options

--model: change the custom model by typing its path

--labels: change the labels by tyoing its path

--input_blob: change name of the input blob

--output_blob: change name of the input blob
