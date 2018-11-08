# Pokedex

# Summary
An image classifier that can detect and recognize which Pokemon is in an image

This project is still a work in progress.

Planning to improve the accuracy of the model, add more types of Pokemon datasets, and publishing this on the Google Play Store.

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
- achieves 96.43% accuracy for classifying pokemon images
- currently classifies 6 different Pokemon (Pikachu, Charmander, Squirtle, Bulbasaur, Gyarados, Rayquaza)
- deep learning dataset consists of 2225 images of Pokemon

# Screenshots:
![Alt text](/screenshots/train.PNG)

![Alt text](/screenshots/plot.png)

![Alt text](/screenshots/pikachu.PNG)

![Alt text](/screenshots/charmander.PNG)

![Alt text](/screenshots/charmander2.PNG)
