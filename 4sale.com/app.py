from flask import Flask, render_template, request, redirect, url_for
import db_utils
from argon2 import PasswordHasher
from collections import defaultdict
import map
import greencover 
import os
from flask_dropzone import Dropzone
from utils import *

#basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config.update(
    UPLOADED_PATH='static/images/properties',
    # Flask-Dropzone config:
    DROPZONE_ALLOWED_FILE_TYPE='image',
    DROPZONE_MAX_FILE_SIZE=5,
    DROPZONE_MAX_FILES=30,
    DROPZONE_IN_FORM=True,
    DROPZONE_UPLOAD_ON_CLICK=True,
    DROPZONE_UPLOAD_ACTION='handle_upload',  # URL or endpoint
    DROPZONE_UPLOAD_BTN_ID='estate_contact_send_btn',
)

dropzone = Dropzone(app)

@app.route('/')
@app.route('/index.html', methods=['GET','POST'])
def home_page():
    if request.method == 'POST':
            data = request.form
            #print(data)
            hashedPassword = ph.hash(data["password"])
            db.insert('users',username=data["username"],passwd=hashedPassword,firstname=data["firstname"],lastname=data["lastname"],email=data["emailid"],phone=data["phone"])
    return render_template('index.html')

@app.route('/about.html')
def about_page():
    return render_template('about.html')

@app.route('/contact.html')
def contact_page():
    return render_template('contact.html')

@app.route('/listings_single.html')
def listings_single():
    pid = request.args.get('id')
    data = db.query('properties',pid=pid)
    tags = db.query('tags',pid=pid)
    print(data)
    #print(tags)
    images = db.query('property_images',cols=['image'],pid=pid)
    address = " ".join([data[0]["address"],data[0]["city"],str(data[0]["pincode"])])
    places = db.query('property_analytics',pid=pid)[0]
    #print(distances)
    ward = db.query('ward_mapping',cols=['ward'],locality=data[0]["locality"])[0][0]
    #print(ward)
    complaints = db.query('complaints',cols=['complaint'],ward=ward)
    #print(complaints)
    complaints = [y for x in complaints for y in x]
    #print(complaints)
    return render_template('listings_single.html', images = images, data = data, tags = tags, places = places,prop_id=pid, complaints= complaints)

@app.route('/listings.html', methods=['GET','POST'])
def listings():
    if request.method == 'POST':
        data = request.form
        db.execute("select * from users where username = '" + data['username'] + "';")
        if(db.rowcount == 1):
            print('Success: valid username')
            db.execute("select passwd from users where username = '" + data['username'] + "';")
            passwordHash = db.fetchall()[0][0]
            try:
                if(ph.verify(passwordHash,data['password'])):
                    print('Success: valid password')
            except:
                print('Failure: invalid password')
                return redirect(url_for('login'))
        else:
            print('Failure: invalid username')
    data = db.query('properties')
    #print(data)
    tags = db.query('tags')
    #print(tags)
    images = db.query('property_images')
    d = defaultdict(list)
    for tag in tags:
        d[tag["pid"]].append(tag["tag"])
    for image in images:
        d[image["pid"]].append(image["image"])
    print(images)
    print(d)
    #print(d)
    for elem in data:
        #print(elem,' ',type(elem))
        elem.append(d[elem[0]])
    print(data)
    
    return render_template('listings.html', data = data[::-1])

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/post-ad.html')
def post_ad_page():
    return render_template('post-ad.html')

@app.route('/upload', methods=['POST'])
def handle_upload():
    pid = db.query('properties',cols=['max(pid)'])
    print(pid)
    pid = 0 if pid[0][0]==None else pid[0][0]
    if(not(os.path.isdir(os.path.join(app.config['UPLOADED_PATH'],str(pid+1))))):
        os.mkdir(os.path.join(app.config['UPLOADED_PATH'],str(pid+1)))
    if(not(os.path.isdir(os.path.join(app.config['UPLOADED_PATH'],str(pid+1),'property_pics')))):
        os.mkdir(os.path.join(app.config['UPLOADED_PATH'],str(pid+1),'property_pics'))
    for key, f in request.files.items():
        if key.startswith('file'):
            f.save(os.path.join(app.config['UPLOADED_PATH'],str(pid+1),"property_pics",f.filename))
            db.insert('property_images',pid=pid+1,image=f.filename)
    print('NNNNOOOOO')
    return '', 204

@app.route('/register.html')
def register_page():
    return render_template('register.html')

@app.route('/news.html')
def news():
    return render_template('news.html')

@app.route('/ques_ans.html')
def ques_ans():
    data = conn.query('question')
    #print(data)
    return render_template('ques_ans.html', data = data)

@app.route('/process_ques', methods=['POST'])
def process_ques():
    data = request.form
    conn.insert('posts',body=data['question_text'])
    return render_template('ques_ans.html')


@app.route('/reply.html')
def reply():
    quesid = request.args.get('id')
    data_ques = conn.query('question',qid=quesid)
    data_reply = conn.query('comments',qid=quesid)
    data_reply = data_reply[::-1]
    #print(data_ques)
    #print(data_reply)
    data = array()
    data = data.append(data_ques)
    data = data.append(data_reply)
    return render_template('reply.html', data = data)

@app.route('/process_post_ad', methods=['POST'])
def process_post_ad():
    data = request.form
    map_services = map.MapServices()
    map_services.geocode_address(' '.join([data['address'],data['locality'],data['city'],data['pincode']]))
    db.insert_from_dict('properties',generate_property_dict(data,map_services.lat,map_services.long))
    pid = db.query('properties',cols=['max(pid)'])[0][0]
    map_services.generate_top_two_closest_places()
    map_services.generate_distances()
    img_processor = greencover.Image_Processor(map_services.lat,map_services.long)
    img_processor.store_images_for_pid(pid)
    db.insert_from_dict_and_kw('property_analytics',generate_property_analytics_dict(map_services.places,map_services.distances),pid=pid,green_cover=img_processor.green_percent)
    return redirect(url_for('listings'))

if __name__ == '__main__':
    db = db_utils.db(database="forsale", user="root", password="root", host="localhost")
    ph = PasswordHasher()
    app.run()
