#!/usr/bin/python3

from signrecognition.signrecognition import run_the_signrecognition_net
from facerecognition.neuralnetwork import run_the_facerecognition_net

if __name__ == "__main__":
    print('\nRunning the sign recognition neural network')
    run_the_signrecognition_net()

    print('\nRunning the face recognition neural network')
    run_the_facerecognition_net()

    print('\nNeural networks training and testing ended\n\n')
