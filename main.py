#!/usr/bin/python3

import videocapture
import facerecognition
import signrecognition
import postprocessing

# Workflow:
# 1. Video capture -> imgframe
# 2. imgframe -> facerecoginition -> return emotion label
# 3. imgframe -> signrecogintion -> return sing label
# 4. emotion label, sing label -> postprocessing -> return expression
