# Image-Processor API
Image Processing API written in Python, using the Pillow library for image manipulation and exposing the functions with the Flask framework. The API has been tested with jpg, png, jpeg and bmp formats and is able to perform following operations on the image:
* `Flip Horizontal`
* `Flip Vertical`
* `Rotate Left`
* `Rotate Right`
* `Greyscale`
* `Thumbnail`
* `Resize`
* `Rotate` to different angle

## Getting started
The API Python file:
* `imageProcessorAPI.py`: a web application to test the functionality that serves as a proof of concept. Run it, navigate to `localhost:5000` and follow the instructions. For more details please refer to the documentation section in this file.

## Dependencies
Python installation needs the `PIL` library (image processing), `flask` with its dependencies (`werkzeug`, `jinja2`, `markupsafe`, `itsdangerous`). It is recommended to use the provided `requirements.txt` file:
```
sudo pip install -r requirements.txt
```

## Documentation
To test the app locally, run `imageProcessorAPI.py` and navigate to `localhost:5000`.

Use the `CHOOSE FILE` button to upload the desired image file. 

![image](https://github.com/F-Zainab/Image-Processor/blob/master/Screenshot%20(152)_LI.jpg)

If successful, the browser will redirect to the processing page.

![image](https://github.com/F-Zainab/Image-Processor/blob/master/Screenshot%20(141).png)

Click on checkbox and input the desired parameters to apply the corresponding transformation. The modified image will be opened with your default image viewing program. The parameters are now sent through the `AJAX` request with a `POST` method.
The transformations would be performed and image would be displayed.

![image](https://github.com/F-Zainab/Image-Processor/blob/master/Screenshot%20(143).png)

### Refer to [Documentation](https://github.com/F-Zainab/Image-Processor/blob/master/Image-ProcessorDocumentation.pdf) for more details.
