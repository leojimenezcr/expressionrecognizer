## Project desired structure

With data directories

.
├── README.md

├── resources
│   ├── project-article.pdf
│   └── sources.md
└── src
    ├── facerecognition
    │   ├── dataset
    │   │   ├── test
    │   │   │   ├── anger
    │   │   │   │   └── files.png
    │   │   │   ├── contempt
    │   │   │   │   └── files.png
    │   │   │   ├── disgust
    │   │   │   │   └── files.png
    │   │   │   ├── fear
    │   │   │   │   └── files.png
    │   │   │   ├── happy
    │   │   │   │   └── files.png
    │   │   │   ├── sadness
    │   │   │   │   └── files.png
    │   │   │   └── surprise
    │   │   │       └── files.png
    │   │   └── train
    │   │       ├── anger
    │   │       │   └── files.png
    │   │       ├── contempt
    │   │       │   └── files.png
    │   │       ├── disgust
    │   │       │   └── files.png
    │   │       ├── fear
    │   │       │   └── files.png
    │   │       ├── happy
    │   │       │   └── files.png
    │   │       ├── sadness
    │   │       │   └── files.png
    │   │       └── surprise
    │   │           └── files.png
    │   ├── facerecognition.py
    │   ├── haarcascades
    │   │   ├── haarcascade_files.xml
    │   ├── image.jpg
    │   ├── __init__.py
    │   ├── neuralnetwork.py
    ├── main.py
    ├── postprocessing
    │   ├── __init__.py
    │   └── postprocessing.py
    ├── preprocessing
    │   ├── __init__.py
    │   ├── kmeans_segmentation.py
    └── signrecognition
        ├── dataset
        │   ├── test
        │   │   ├── 1
        │   │   │   └── files.png
        │   │   ├── 2
        │   │   │   └── files.png
        │   │   ├── 3
        │   │   │   └── files.png
        │   │   ├── 4
        │   │   │   └── files.png
        │   │   ├── 5
        │   │   │   └── files.png
        │   │   ├── a
        │   │   │   └── files.png
        │   │   ├── e
        │   │   │   └── files.png
        │   │   ├── i
        │   │   │   └── files.png
        │   │   ├── o
        │   │   │   └── files.png
        │   │   └── u
        │   │       └── files.png
        │   └── train
        │       ├── 1
        │       │   └── files.png
        │       ├── 2
        │       │   └── files.png
        │       ├── 3
        │       │   └── files.png
        │       ├── 4
        │       │   └── files.png
        │       ├── 5
        │       │   └── files.png
        │       ├── a
        │       │   └── files.png
        │       ├── e
        │       │   └── files.png
        │       ├── i
        │       │   └── files.png
        │       ├── o
        │       │   └── files.png
        │       └── u
        │           └── files.png
        ├── __init__.py
        └── signrecognition.py
