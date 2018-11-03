from flask import Flask, render_template, request, redirect, url_for
import db_utils
from argon2 import PasswordHasher
from collections import defaultdict
import map
import greencover 
import os
from flask_dropzone import Dropzone

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

@app.route('/process_post_ad', methods=['POST'])
def process_post_ad():
    data = request.form
    #print(data)
    address_for_geocoding = ' '.join([data['address'],data['locality'],data['city'],data['pincode']])
    location = map.get_latitude_and_longitude(address_for_geocoding)
    lat,long = location['lat'], location['lng']
    db.insert('properties',title='Property for '+data['type']+' at ' + data['address'] ,type=data['type'],locality=data['locality'],city=data['city'],pincode=data['pincode'], address=data['address'],short_description=data['short_description'],bedrooms=int(data['bedrooms']),bathrooms=int(data['bathrooms']), patio=int(data['patio']),area=float(data['area']),cost=float(data['cost']),latitude=float(lat),longitude=float(long))
    print('yes')
    print(location)
    l = []
    for place in map.place_types:
        l.append(map.get_closest_places(location,place,num=2,radius=2000))
    #print(l)
    distances = []
    print(l)
    for item in l:
        if item:
            distances.append([map.get_distance_and_time(location,item[0][1]),map.get_distance_and_time(location,item[1][1])])
        else:
            distances.append([])
    pid = db.query('properties',cols=['max(pid)'])[0][0]
    img_processor = greencover.Image_Processor(lat,long)
    img_processor.store_images_for_pid(pid)
    db.insert('property_analytics',pid=pid, hospital1=l[0][0][0]+distances[0][0][0], hospital2=l[0][1][0]+distances[0][1][0], bank1=l[1][0][0]+distances[1][0][0] , bank2=l[1][1][0]+distances[1][1][0] , book_store1=l[2][0][0]+distances[2][0][0] , book_store2=l[2][1][0]+distances[2][1][0] , bus_station1=l[3][0][0]+distances[3][0][0] , bus_station2=l[3][1][0]+distances[0][1][0] , school1=l[4][0][0]+distances[4][0][0] , school2=l[4][1][0]+distances[4][1][0] , clothing_store1=l[5][0][0]+distances[5][0][0] , clothing_store2=l[5][1][0]+distances[5][1][0] , restaurant1=l[6][0][0]+distances[6][0][0] , restaurant2=l[6][1][0]+distances[6][1][0] , gym1=l[7][0][0]+distances[7][0][0] , gym2=l[7][1][0]+distances[7][1][0] , gas_station1=l[8][0][0]+distances[8][0][0] , gas_station2=l[8][1][0]+distances[8][1][0] , doctor1=l[9][0][0]+distances[9][0][0] , doctor2=l[9][1][0]+distances[9][1][0] , electronics_store1=l[10][0][0]+distances[10][0][0] , electronics_store2=l[10][1][0]+distances[10][1][0] , pharmacy1=l[11][0][0]+distances[11][0][0] , pharmacy2=l[11][1][0]+distances[11][1][0], green_cover=img_processor.green_percent);

    return redirect(url_for('listings'))

if __name__ == '__main__':
    db = db_utils.db(database="forsale", user="root", password="root", host="localhost")
    ph = PasswordHasher()
    app.run()
