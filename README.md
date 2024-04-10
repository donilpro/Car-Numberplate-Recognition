# Reference

A reference article for the Numberplate Recognition application.
It provides a description of the detector package.

## Installing Packages

From python shell:

```shell
pip install -r requirements.txt
```

## Image Processing class

Open an image by passing a path or openCV image to the ImageLoader constructor:

```Python
from detector.loader import ImageLoader

img = ImageLoader('path/to/image.png')
```

or:

```Python
from detector.loader import ImageLoader
import cv2 as cv

img = ImageLoader(cv.imread('path/to/image.png'))
```

You can get a QPixmap of the original image by calling the get_image method. Similar for cropped license plates by using the get_cropped_image method:

```Python
pixmap = img.get_image()
# or
pixmap = img.get_cropped_image()
```

Use the get_symbols method for license plate instance string:

```Python
number = img.get_symbols()
```

## Model Manager

The get_available_models() function returns a list of available models for your application:

```Python
import detector.manager as manager

models = manager.get_avaible_models()
print(models)
```

Read manager.py for more info