from flask import Flask, render_template, request, redirect, url_for
import db_utils
from argon2 import PasswordHasher
from collections import defaultdict
import map
import greencover
import cv2
import os
from flask_dropzone import Dropzone

#basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config.update(
    UPLOADED_PATH='static/images',
    # Flask-Dropzone config:
    DROPZONE_ALLOWED_FILE_TYPE='image',
    DROPZONE_MAX_FILE_SIZE=3,
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
            print(data)
            hashedPassword = ph.hash(data["password"])
            conn.insert('users',username=data["username"],passwd=hashedPassword,firstname=data["firstname"],lastname=data["lastname"],email=data["emailid"],phone=data["phone"])
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
    data = conn.query('properties',pid=pid)
    tags = conn.query('tags',pid=pid)
    print(data)
    print(tags)
    address = " ".join([data[0]["address"],data[0]["city"],str(data[0]["pincode"])])
    location = map.get_latitude_and_longitude(address)
    print(location)
    l = []
    for place in map.place_types:
        l.append(map.get_closest_places(location,place,num=2,radius=2000))
    print(l)
    distances = []
    for item in l:
        if item:
            distances.append([map.get_distance_and_time(location,item[0][1]),map.get_distance_and_time(location,item[1][1])])
        else:
            distances.append([])
    print(distances)
    green = greencover.green_index(location["lat"],location["lng"])
    if(not(os.path.isdir("static/images/properties/"+pid))):
        os.mkdir("static/images/properties/"+pid)
    cv2.imwrite("static/images/properties/"+pid+"/input.png",green[1])
    cv2.imwrite("static/images/properties/"+pid+"/hsv.png",green[2])
    cv2.imwrite("static/images/properties/"+pid+"/threshold.png",green[3])
    cv2.imwrite("static/images/properties/"+pid+"/green.png",green[4])
    return render_template('listings_single.html', data = data, tags = tags, proximity = l, distances = distances, green = green[0],prop_id=pid)

@app.route('/listings.html', methods=['GET','POST'])
def listings():
    if request.method == 'POST':
        data = request.form
        cur.execute("select * from users where username = '" + data['username'] + "';")
        if(cur.rowcount == 1):
            print('Success: valid username')
            cur.execute("select passwd from users where username = '" + data['username'] + "';")
            passwordHash = cur.fetchall()[0][0]
            try:
                if(ph.verify(passwordHash,data['password'])):
                    print('Success: valid password')
            except:
                print('Failure: invalid password')
                return redirect(url_for('login'))
        else:
            print('Failure: invalid username')
    data = conn.query('properties')
    print(data)
    tags = conn.query('tags')
    print(tags)
    d = defaultdict(list)
    for tag in tags:
        d[tag["pid"]].append(tag["tag"])
    print(d)
    for elem in data:
        print(elem,' ',type(elem))
        elem.append(d[elem[0]])
    print(data)
    return render_template('listings.html', data = data)

@app.route('/login.html')
def login():
    return render_template('login.html')

@app.route('/post-ad.html')
def post_ad_page():
    return render_template('post-ad.html')

@app.route('/upload', methods=['POST'])
def handle_upload():
    for key, f in request.files.items():
        if key.startswith('file'):
            f.save(os.path.join(app.config['UPLOADED_PATH'], f.filename))
    return '', 204

@app.route('/register.html')
def register_page():
    return render_template('register.html')

@app.route('/process_post_ad', methods=['POST'])
def process_post_ad():
    data = request.form
    print(data)
    address_for_geocoding = ' '.join([data['address'],data['locality'],data['city'],data['pincode']])
    location = map.get_latitude_and_longitude(address_for_geocoding)
    lat,long = location['lat'], location['lng']
    conn.insert('properties',title='Property for '+data['type']+' at ' + data['address'] ,type=data['type'],locality=data['locality'],city=data['city'],pincode=data['pincode'], address=data['address'],short_description=data['short_description'],bedrooms=int(data['bedrooms']),bathrooms=int(data['bathrooms']), patio=int(data['patio']),area=float(data['area']),cost=float(data['cost']),latitude=float(lat),longitude=float(long))
    return redirect(url_for('listings'))

if __name__ == '__main__':
    conn = db_utils.dbconnection(database="forsale", user="root", password="root", host="localhost")
    ph = PasswordHasher()
    app.run()
