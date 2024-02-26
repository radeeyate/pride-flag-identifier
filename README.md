# Pride Flag Identifier

Pride flag identifier classifies images of pride flags using maching learning.

This project is very early in making, it will not be accurate for all flags.

## Setup
```
git clone https://github.com/radeeyate/pride-flag-identifier.git
cd pride-flag-identifier
pip install -r requirements.txt
```

## Training

There is probably some libraries that it didn't install. Run `python train.py` to train it. If it complains about missing libraries, install them with `pip install <missing library>`.

Training the model will ouput a `flags.h5` file.

## Classifying

Run `python classify.py` to classify an image. You can modify the path in the file to classify a different image.