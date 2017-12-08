# Readapted from Tensor For Poets Overview
This repo contains code for the "TensorFlow for Poets" series, adapted for our final project 
of artificial intelligence. The idea here is to create a similar thing but integrating a 
webcam and using the Need for speed game.


## Requirements:
If you want to run this project you will need to have **TensorFlow,numpy,pygame and keyboard**.
then press: 

`user@host $ python run.py`


# References:

* For [TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/) the new, ground up rewrite targeted at mobile devices
  use [this version of the codelab](https://codelabs.developers.google.com/codelabs/tensorflow-for-poets-2-tflite) 
* For the more mature [TensorFlow Mobile](https://www.tensorflow.org/mobile/mobile_intro) use 
  [this version of the codealab](https://codelabs.developers.google.com/codelabs/tensorflow-for-poets-2).
* https://colah.github.io/posts/2014-10-Visualizing-MNIST/ 
* Idea from [OpenCV Python Webcam Hand Gesture Detection API](https://www.youtube.com/watch?v=oH0ZkfFoeYU)

* The TensorFlow Lite version, in `android/tflite`, comes from [tensorflow/contrib/lite/](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/contrib/lite).
* The Tensorflow Mobile version, in `android/tfmobile`, comes from [tensorflow/examples/android/](https://github.com/tensorflow/tensorflow/tree/master/tensorflow/examples/android).

The `scripts` directory contains helpers for the codelab. Some of these come from the main TensorFlow repository, and are included here so you can use them without also downloading the main TensorFlow repo (they are not part of the TensorFlow `pip` installation).

