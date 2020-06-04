from flask import Flask, render_template, request,url_for, session,redirect
from flask_uploads import UploadSet, configure_uploads, IMAGES
from deepface import DeepFace 
from datetime import timedelta
from jobs_list import white_collar_jobs, white_collar_jobs_2, blue_collar_jobs,pink_collar_jobs, pink_collar_jobs_black, old_age, under_age,teen_age, asian_jobs, asian_jobs_2, black_indv, black_indv_2, middle_eastern_jobs, asian_jobs3,  exception_collar, mdEastern_jobs
import random
# from tensorflow.keras.models import model_from_json



app = Flask(__name__,)
app.permanent_session_lifetime = timedelta(minutes=5)
app.secret_key = "Hello"


app.config['UPLOADED_PHOTOS_DEST'] = 'static'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])
photos = UploadSet('photos', IMAGES)
configure_uploads(app, photos)

@app.route("/")
def home():
    return render_template('index.html')

def allowed_file(filename):    
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        session["picture"] = filename
    return render_template('details.html', image_name=filename)
 
 

@app.route('/detect', methods=['GET', 'POST'])
def detect():
# i want to get the photo and then post, so if post has been touched then get photo
    if request.method == 'POST' and "picture" in session:
        try:
            session.permanent = True
            picture = session["picture"] 
            path = "static/"
            end = path + picture 
            
            demography = DeepFace.analyze((end)) #passing nothing as 2nd argument will find everything 
            roundAge = round(demography["age"])
        except:
            return redirect(url_for('fail'))
    

# Age Category Conditional Statement
        if demography['age'] <= 15:
            word = random.choice(under_age)
            print("This person is underage")
        
        elif demography['age'] >= 16 and demography['age'] <= 19:
            word = random.choice(teen_age) 
            print("This person is a teenager")
        
        elif demography['age'] >= 55:
            word = random.choice(old_age)
            print("This person is overage")
        
        else:
            print("Not in any of these categories")
        


# White Male Category Conditional Statement         
        if demography['dominant_race'] == 'white' and demography['gender'] == 'Man':
            if demography['dominant_emotion'] == 'angry' or demography['dominant_emotion'] == 'fear' or demography['dominant_emotion'] == 'disgust' or demography['dominant_emotion'] == 'sad':
                word = random.choice(exception_collar) 
                print("This person is white man exception")
                
            elif demography['dominant_race'] == 'white' and demography['gender'] == 'Man' and demography['age'] >= 19 and demography['age'] <= 25:
                word = random.choice(white_collar_jobs_2) 
                print("This person is a young white man")
            
            else:
                word = random.choice(white_collar_jobs) 
                print("This person is a white man")
                

# Black Male Category Conditional Statement   
        if demography['dominant_race'] == 'black' and demography['gender'] == 'Man':
            if demography['dominant_emotion'] == 'angry' or demography['dominant_emotion'] == 'fear' or demography['dominant_emotion'] == 'disgust' or demography['dominant_emotion'] == 'sad':
                word = random.choice(black_indv_2) 
                print("This person is a black man exception")
            else:
                word = random.choice(black_indv) 
                print("This person is a black man")
                
# Other Race Category Conditional Statement   
        if demography['gender'] == 'Man':
            if demography['dominant_race'] == 'latino hispanic':
                word = random.choice(blue_collar_jobs) 
                print("This person is a hispanic man")

            elif demography['dominant_race'] == 'asian' and demography['gender'] == 'Man':
                word = random.choice(asian_jobs) 
                print("This person is an asian man")
        
            elif demography['dominant_race'] == 'indian' and demography['gender'] == 'Man':
                word = random.choice(asian_jobs_2) 
                print("This person is an indian man")
        
            elif demography['dominant_race'] == 'middle eastern' and demography['gender'] == 'Man':
                word = random.choice(middle_eastern_jobs) 
                print("This person is a middle eastern man")
        

# Female Category Conditional Statement   
        if demography['gender'] == 'Woman':
            if demography['dominant_race'] == 'black':
                word = random.choice(pink_collar_jobs_black) 
                print("This person is a black woman")
                
            elif demography['dominant_race'] == 'indian' or demography['dominant_race'] == 'asian':
                word = random.choice(asian_jobs3) 
                print("This person is a middle eastern man")
                
            elif demography['dominant_race'] == 'middle eastern':
                word = random.choice(mdEastern_jobs) 
                print("This person is a middle eastern woman")
                
            # We may add other elifs for other races to fit but still predominantly caring
            else:
                word = random.choice(pink_collar_jobs) 
                print("This person is a woman")   
      
            
    return render_template('results.html', results = demography, occupation = word, age = roundAge)


@app.route('/creator')
def creator():
    return render_template('creator.html')

@app.route('/fail')
def fail():
    return render_template('error.html')

# Run the web app

# Press Ctrl + Shift + R if code is changed

if __name__ == '__main__':
    app.run(threaded=False)    

 