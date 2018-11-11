from flask import Flask, render_template, request, redirect, url_for, session
import db_utils
from argon2 import PasswordHasher
from collections import defaultdict
import map
import greencover 
import os
import price
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

app.config['SECRET_KEY'] = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

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
    print(type(pid))
    data = db.query('properties',pid=pid)[0]
    tags = db.query('tags',pid=pid)
    print(data)
    #print(tags)
    images = db.query('property_images',cols=['image'],pid=pid)
    address = " ".join([data["address"],data["city"],str(data["pincode"])])
    places = db.query('property_analytics',pid=pid)[0]
    #print(distances)
    ward = db.query('ward_mapping',cols=['ward'],locality=data["locality"])[0]['ward']
    print(ward)
    complaints = db.query('complaints',cols=['complaint'],ward=ward)
    print(complaints)
    return render_template('listings_single.html', images = images, data = data, tags = tags, places = places,prop_id=pid, complaints= complaints)

@app.route('/process_login',methods=['POST'])
def process_login():
    if request.method == 'POST':
        data = request.form
        user = db.query('users',username=data['username'])
        if(len(user) == 1):
            print('Success: valid username')
            password = user[0]['passwd']
            try:
                if(ph.verify(password,data['password'])):
                    print('Success: valid password')
                    print(user[0]['username'])
                    session['username'] = user[0]['username']
                    print(session['username'])
                    return redirect(url_for('listings'))
            except:
                print('Failure: invalid password')
                return redirect(url_for('login'))
        else:
            print('Failure: invalid username')
            return redirect(url_for('login'))
            
@app.route('/listings.html')
def listings():
    data = db.query('properties')
    #print(data)
    tags = db.query('tags')
    #print(tags)
    images = db.query('property_images')
    d1 = defaultdict(list)
    d2 = defaultdict(list)
    for tag in tags:
        d1[tag["pid"]].append(tag["tag"])
    for image in images:
        d2[image["pid"]].append(image["image"])
    print(d1)
    print(d2)
    for elem in data:
        elem['tags'] = d1[elem['pid']]
        elem['images'] = d2[elem['pid']]
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
    pid = 0 if pid[0]['max']==None else pid[0]['max']
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
    questions = db.query('questions')
    return render_template('news.html',questions=questions)

@app.route('/question.html')
def question_page():
    return render_template('question.html')

@app.route('/discuss.html')
def discuss_page():
    qid = request.args.get('qid')
    question = db.query('questions',qid=qid)[0]
    print(question)
    comments = db.query('comments',qid=qid)
    return render_template('discuss.html',question=question,comments=comments)

@app.route('/process_question',methods=['POST'])
def process_question():
    data = request.form
    db.insert('questions',username=session['username'],title=data['title'],body=data['description'],category=data['category'])
    return redirect(url_for('question_page'))


@app.route('/process_comment',methods=['POST'])
def process_comment():
    data = request.form
    db.insert('comments',username=session['username'],body=data['comment'],qid=data['qid'])
    return redirect(url_for('discuss_page',qid=data['qid']))


@app.route('/reco.html')
def reco():
	return render_template('reco.html')

@app.route('/vastu.html')
def vastu():
	return render_template('vastu.html')
		    
@app.route('/process_price', methods =['POST'])
def process_price():
	data = request.form
	print(data)
	pred = []
	for k in data:
		pred.append(data[k])
	
	print(pred)	
	p = price.price_est(pred)
	res = p.est(pred)[0]
	print(res) 
	return render_template('reco.html', data = res)


@app.route('/process_post_ad', methods=['POST'])
def process_post_ad():
    data = request.form
    map_services = map.MapServices()
    map_services.geocode_address(' '.join([data['address'],data['locality'],data['city'],data['pincode']]))
    db.insert_from_dict('properties',generate_property_dict(data,map_services.lat,map_services.long))
    pid = db.query('properties',cols=['max(pid)'])[0]['max']
    print(pid)
    map_services.generate_top_two_closest_places()
    map_services.generate_distances()
    img_processor = greencover.Image_Processor(map_services.lat,map_services.long)
    img_processor.store_images_for_pid(pid)
    tags = data['tags'].split(',')
    for tag in tags:
        db.insert('tags',pid=pid,tag=tag)
    db.insert_from_dict_and_kw('property_analytics',generate_property_analytics_dict(map_services.places,map_services.distances),pid=pid,green_cover=img_processor.green_percent)
    return redirect(url_for('listings'))

@app.route('/filtering_properties',methods=['POST'])
def filtering_properties():
    data = request.form
    print(data)
    properties = db.query('properties',locality=data['locality'],area=float(data['area']),bedrooms=int(data['bedrooms']),bathrooms=int(data['bathrooms']))
    print(properties)
    tags = db.query('tags')
    #print(tags)
    images = db.query('property_images')
    d1 = defaultdict(list)
    d2 = defaultdict(list)
    for tag in tags:
        d1[tag["pid"]].append(tag["tag"])
    for image in images:
        d2[image["pid"]].append(image["image"])
    print(d1)
    print(d2)
    for elem in properties:
        elem['tags'] = d1[elem['pid']]
        elem['images'] = d2[elem['pid']]
    
    return render_template('listings.html', data = properties[::-1])

@app.route('/traffic',methods=['POST'])
def get_traffic_details():
    data = request.form
    m = map.MapServices()
    traffic_details = m.get_distance_metrics(data['origin'],data['destination'])
    return ' '.join([traffic_details[0],traffic_details[1]])

@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home_page'))

if __name__ == '__main__':
    db = db_utils.db(database="forsale", user="root", password="root", host="localhost")
    ph = PasswordHasher()
    app.run()
