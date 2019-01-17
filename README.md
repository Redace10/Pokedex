# Pokedex

# Summary
An image classifier that can detect and recognize which Pokemon is in an image

Disclaimer: Adrian Rosebrock's tutorial (See reference section below for the original article) was used and incredibly helpful in making this model.

# How to Run:
If you are interested in running this application, you need to run the command 
`python classify.py --model pokedex.model --labelbin lb.pickle --image <path to image that you want to classify>`

Since the model has already been trained and stored in pokedex.model, you do not need to waste time to train the model.

Keep in mind that you need to install the required libraries before running the command above: python, tensorflow, Keras, openCV, imutils, argparse, and numpy. These can simply be installed by using `pip install <module that you want installed>`
It is recommend that you install these in a virtual environment.

# Features:
- created image dataset by using Microsoft’s Bing Image Search API to programmatically download images via a query
- added more images to the dataset by taking existing images and applying transformations to generate more image data
- constructed a Keras model by following VGGNet CNN architecture
- uses Adam Optimizer and Categorical Cross-entropy loss
- achieves 97.49% training accuracy and 88.76% validation accuracy for classifying pokemon images
- currently classifies 12 different Pokemon (Pikachu, Charmander, Charmeleon, Charizard, Squirtle, Wartortle, Blastoise, Bulbasaur, Ivysaur, Venusaur, Gyarados, Rayquaza)
- deep learning dataset consists of 4112 images of Pokemon (these images are not stored in github because they take up too much space)
- takes around 5-6 hours to train using CPU. Takes only around 40 minutes to train using GPU.

# Screenshots:
![Alt text](/screenshots/train.PNG)

![Alt text](/screenshots/plot.png)

![Alt text](/screenshots/pikachu.PNG)

![Alt text](/screenshots/pikachu2.png)

![Alt text](/screenshots/pikachu3.png)

![Alt text](/screenshots/charmander.PNG)

![Alt text](/screenshots/charmander2.PNG)

![Alt text](/screenshots/charizard.png)

![Alt text](/screenshots/venusaur.png)

![Alt text](/screenshots/blastoise.png)

![Alt text](/screenshots/gyarados.png)

# References
Adrian Rosebrock, Keras and Convolutional Neural Networks (CNNs), (2018), pyimagesearch, https://www.pyimagesearch.com/2018/04/16/keras-and-convolutional-neural-networks-cnns/
