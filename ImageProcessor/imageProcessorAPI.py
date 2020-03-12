from flask import Flask, request, render_template, url_for, send_from_directory
from PIL import Image, ImageOps
import os
from flask.json import jsonify
import json
import random
import string
import config

app = Flask(__name__)
APP_ROOT = os.path.dirname(os.path.abspath(__file__))



@app.route('/')
@app.route('/home')
def home():
    print(request)
    return render_template('home.html')

@app.route('/upload', methods=["POST"])
def processing():
    target = os.path.join(APP_ROOT, 'images/')

    # create image directory if not found
    if not os.path.isdir(target):
        os.mkdir(target)
    
     # retrieve file from html file-picker
    upload = request.files.getlist("file")[0]
    print(upload)
    print("File name: {}".format(upload.filename))
    filename = upload.filename
    config.Filename = filename
    print(config.Filename)
    # file support verification
    ext = os.path.splitext(filename)[1]
    if (ext == ".jpg") or (ext == ".png") or (ext == ".bmp") or (ext == ".jpeg"):
        print("File accepted")
    else:
        return render_template("error.html", title="Error Page", message="The file type is not supported. Please upload a jpg/png/bmp image"), 400
    
    # save file
    destination = "/".join([target, filename])
    print("File saved to to:", destination)
    upload.save(destination)
    return render_template('processing.html', title="Processing Page", image_name=filename)

@app.route('/createList', methods=["POST"])
def createList():
    #filename = request.form['file']
    print("entered createList")
    array1 = request.get_json()
    print("printing array:::::::::::::::::::::")
    print(array1)
    array = array1["key1"]
    print("print order list::::::::::::::::::::")
    print(array)
    dictOrder = array1["key2"]
    print("print other inputa::::::::::::::::::::")
    print(dictOrder)
    #print(array)
    
    name = randomString(stringLength=5)
    image_name = (name + '.png')
    print(image_name)
    
    #transformationList = request.form.getlist('transformation[]')
    #print(transformationList)
    
    # open and process image
    target = os.path.join(APP_ROOT, 'images')
    destination = "/".join([target, config.Filename])
    print(destination)
    img = Image.open(destination)
    print("image opened")
    for item in array:
        print("entered in the loop")
        if item == "FlipH":
            v = dictOrder["timesFH"]
            if not v or int(v) == 1:
                img = img.transpose(Image.FLIP_LEFT_RIGHT)
                # save and return image
                destination = "/".join([target, image_name])
                if os.path.isfile(destination):
                    os.remove(destination)
                img.save(destination)
            elif int(v) > 1:
                for value in range(0, int(v)):
                    img = img.transpose(Image.FLIP_LEFT_RIGHT)
                    # save and return image
                    destination = "/".join([target, image_name])
                    if os.path.isfile(destination):
                        os.remove(destination)
                    img.save(destination)
            print("transformation performed")

        if item == "FlipV":
            v = dictOrder["timesFV"]
            print(v)
            #print("value = [{}]".format(v))
            if not v or int(v) == 1:
                img = img.transpose(Image.FLIP_TOP_BOTTOM)
                # save returned image
                destination = "/".join([target, image_name])
                if os.path.isfile(destination):
                    os.remove(destination)
                img.save(destination)
                print("flipV")
            elif int(v) > 1:
                for value in range(0, int(v)):
                    img = img.transpose(Image.FLIP_TOP_BOTTOM)
                    # save returned image
                    destination = "/".join([target, image_name])
                    if os.path.isfile(destination):
                        os.remove(destination)
                    img.save(destination)
            print("transformation performed")

        if item == "Greyscale":
            v = dictOrder["timesGrey"]
            print(v)
            #print("value = [{}]".format(v))
            if not v or int(v) == 1:
                img = ImageOps.grayscale(img)
                # save returned image
                destination = "/".join([target, image_name])
                if os.path.isfile(destination):
                    os.remove(destination)
                img.save(destination)
                print("grey")
            elif int(v) > 1:
                for value in range(0, int(v)):
                    img = ImageOps.grayscale(img)
                    # save returned image
                    destination = "/".join([target, image_name])
                    if os.path.isfile(destination):
                        os.remove(destination)
                    img.save(destination)
            print("transformation performed")
                    
        if item == "RotateL":
            v = dictOrder["timesRL"]
            #print("value = [{}]".format(v))
            if not v or int(v) == 1:
                img = img.rotate(90)
                # save returned image
                destination = "/".join([target, image_name])
                if os.path.isfile(destination):
                    os.remove(destination)
                img.save(destination)
            elif int(v) > 1:
                for value in range(0, int(v)):
                    img = img.rotate(90)
                    # save returned image
                    destination = "/".join([target, image_name])
                    if os.path.isfile(destination):
                        os.remove(destination)
                    img.save(destination)
            print("transformation performed")

        if item == "RotateR":
            v = dictOrder["timesRR"]
            #print("value = [{}]".format(v))
            if not v or int(v) == 1:
                img = img.rotate(270)
                # save returned image
                destination = "/".join([target, image_name])
                if os.path.isfile(destination):
                    os.remove(destination)
                img.save(destination)
            elif int(v) > 1:
                for value in range(0, int(v)):
                    img = img.rotate(270)
                    # save returned image
                    destination = "/".join([target, image_name])
                    if os.path.isfile(destination):
                        os.remove(destination)
                    img.save(destination)
            print("transformation performed")

        if item == "Thumbnail":
            v = dictOrder["timesThumb"]
           # print("value = [{}]".format(v))
            if not v or int(v) == 1:
                img.thumbnail((200,200))
                # save returned image
                destination = "/".join([target, image_name])
                if os.path.isfile(destination):
                    os.remove(destination)
                img.save(destination)
            elif int(v) > 1:
                for value in range(0, int(v)):
                    img.thumbnail((200,200))
                    # save returned image
                    destination = "/".join([target, image_name])
                    if os.path.isfile(destination):
                        os.remove(destination)
                    img.save(destination)
            print("transformation performed")

        if item == "Rotate":
            v = dictOrder["timesR"]
            #print("value = [{}]".format(v))
            if not v or int(v) == 1:
                angle = dictOrder["angle"]
                img = img.rotate(-1*int(angle))
                # save returned image
                destination = "/".join([target, image_name])
                if os.path.isfile(destination):
                    os.remove(destination)
                img.save(destination)
            elif int(v) > 1:
                angle = dictOrder["angle"]
                for value in range(0, int(v)):
                    img = img.rotate(-1*int(angle))
                    # save returned image
                    destination = "/".join([target, image_name])
                    if os.path.isfile(destination):
                        os.remove(destination)
                    img.save(destination)
            print("transformation performed")

        if item == "Resize":
            x = int(dictOrder["x"])
            y = int(dictOrder["y"])
            #print(x)
            #print(y)
            # check for valid resize parameters
            width = img.size[0]
            height = img.size[1]

            resize_possible = True
            if not 0 <= x < width:
                resize_possible = False
            if not 0 <= y < height:
                resize_possible = False

            #resize the image
            if resize_possible:
                v = dictOrder["timesR"]
                print("value = [{}]".format(v))
                if not v or int(v) == 1:
                    img = img.resize((x, y))
                    # save returned image
                    destination = "/".join([target, image_name])
                    if os.path.isfile(destination):
                        os.remove(destination)
                    img.save(destination)
                elif int(v) > 1:
                    for value in range(0, int(v)):
                        img = img.resize((x, y))
                        # save returned image
                        destination = "/".join([target, image_name])
                        if os.path.isfile(destination):
                            os.remove(destination)
                        img.save(destination)
            else:
                return render_template("error.html", message="Resize dimensions not valid"), 400
            print("transformation performed")

    return render_template("display.html", image=image_name)       
    #return send_image('temp.png')

# retrieve file from 'images' directory
@app.route('/images/<filename>')
def send_image(filename):
    print("entered the send image")
    print(request)
    return send_from_directory("images", filename)

def randomString(stringLength=5):
    """Generate a random string of fixed length """
    letters = string.ascii_lowercase
    nameList = []
    name = ''.join(random.choice(letters) for i in range(stringLength))
    if name in nameList:
        return randomString(stringLength=5)
    else:
        nameList.append(name)
        print(name)
        return name



if __name__ == "__main__":
    app.run(debug=True)
