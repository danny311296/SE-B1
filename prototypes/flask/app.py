from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/contact')
def contact_page():
    return render_template('contact.html')
    
@app.route('/listings_single')
def listings_single():
    return render_template('listings_single.html')

@app.route('/listings')
def listings():
    return render_template('listings.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/post-ad')
def post_ad_page():
    return render_template('post-ad.html')

@app.route('/register')
def register_page():
    return render_template('register.html')

if __name__ == '__main__':
    app.run()