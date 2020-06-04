## Links
OneDrive: https://liveplymouthac-my.sharepoint.com/:f:/r/personal/kamel_adjei_students_plymouth_ac_uk/Documents/PROJECT?csf=1&web=1&e=UdppDc
Github: https://github.com/KamelAdjei
Youtube: https://www.youtube.com/channel/UCOUrASPLv0as6m6N5cgQQcA

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
 


//the first prediction will also take a while (apprx 15 minutes)

## How to use:
- Once the chatbot is active
- You type in a question
- The trump chatbot will analyze the question and based on its trained data
- It will reply with the best matched answer.


## Build Process
- Train in chatbot in train.py on a corpus of words Donald Trump mostly uses (files).
- After the bot has finished training, dbsqlite files will be created.
- Using these files, go to chatbot.py and open terminal
- run "python chatbot.py", this will open a development server using Flask
- You can start chatting with the bot.

If you would like to train it yourself then delete the following:
- file.txt
- db.sqlite and all db files
- sentence_tokenizer



## How to Deploy

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






