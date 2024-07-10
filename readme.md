## Links
- Youtube: https://www.youtube.com/channel/UCOUrASPLv0as6m6N5cgQQcA

## Folder Structure:
FYP DAT 611 – project folder
- Samplephotos ( photo examples for testing)
- Static ( contains css,javascript and img file)
- Templates (contains all the pages for the web application)
- Job_list.py ( extensive occupation list used for the random job generator.)
- App.py ( main python file)

Idea development – sketch file

 ## Install the required packages:
Type in cmd : pip install -r requirements.txt

## Local Setup:
 1. Ensure that Python, Flask, Flask-uploads and Deepface are installed (either manually, or run `pip install -r requirements.txt`).
 2. Run *app.py* with `python app.py`.
 3. The demo will be live at [http://localhost:5000/](http://localhost:5000/)

## How to Deploy:

- It will be deployed using Flask which is a framework written in Python used to build web applications.
- Simply type in cmd in folder "python app.py" and a development server will be live.

## Once the flask server is running:
- You will be able to upload an image.
- You will be able to analyze the image.
- Based on the results from the analysis, a random job title will be generated from the specified group.

## Recommended
- You will need to have pip and atleast Python version 3.7 64 bit to install python packages
- Ensure your python is installed correctly in PATH


## Note
Installing Deepface will take more than 15 minutes, and an additional 15 minutes when you analyze for the first time.
