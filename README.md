# Pokedex
Pokedex: A pokemon image classifier. 

- Used Microsoft’s Bing Image Search API to programmatically download images via a query to build a deep learning image dataset.
- Constructed Keras model by utilizing the VGGNet 

Planning to implement this to Android and publish on the Google Play Store.

# Features:
- created image dataset by useing Microsoft’s Bing Image Search API to programmatically download images via a query
- constructed a Keras model by following VGGNet CNN architecture
- added more images to the dataset by taking existing images and applying transformations to generate more image data
- uses Adam Optimizer and Categorical Cross-entropy loss
- achieves 96.43% accuracy for classifying pokemon images
- currently classifies 6 different Pokemon (Pikachu, Charmander, Squirtle, Bulbasaur, Gyarados, Rayquaza)
- deep learning dataset consists of 2225 images of Pokemon
