from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def home_page():
   return render_template('about.html')

if __name__ == '__main__':
   app.run()