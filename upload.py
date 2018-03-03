# Import necessary dependencies
import os
from flask import Flask, flash, get_flashed_messages, request, redirect, url_for, send_from_directory, render_template
from werkzeug.utils import secure_filename

# Import the generator function
from generator import generator

# initialize Flask app
app = Flask(__name__)
app.secret_key = 'some_secret'

# Defines directory for uploaded files
UPLOAD_FOLDER = 'uploads'

# Defines directory for sitemap.xml
SITEMAP_FOLDER = 'sitemap'

# Defines allowed file extensions
ALLOWED_EXTENSIONS = set(['txt'])

# Configs directory for uploaded files
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Configs directory for sitemap.xml
app.config['SITEMAP_FOLDER'] = SITEMAP_FOLDER

# Verifies that the uploaded file is a .txt
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# route that displays index.html, calls verification function, calls the sitemap generator, and deletes the uploaded file
@app.route('/', methods=['GET', 'POST'])
def upload_file():

    # Executes if post request sent from template
    if request.method == 'POST':

        # Check if the post request includes a .file
        if 'file' not in request.files:
            flash('Please upload a .txt file')
            return render_template("index.html")

        file = request.files['file']

        # Executes if file name is blank
        if file.filename == '':
            flash('No selected file', 'error')
            return render_template("index.html")

        # Executes if uploaded file exists and has extension .txt
        if file and allowed_file(file.filename):

            # Reads in for Priority from form
            priority = request.form['priority']

            # Reads in Changefreq from form
            changefreq = request.form['changeFreq']

            # Returns a secure version of the file name
            filename = secure_filename(file.filename)

            # Saves the file in the uploads folder
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))

            # Calls the generator function to process uploaded file
            generator(UPLOAD_FOLDER + '/' + filename, changefreq, priority)

            # Deletes the uploaded user file
            os.remove(UPLOAD_FOLDER + '/' + filename)

            # Returns a redirect to the app.route associated with the Sitemap function

            return redirect(url_for('Sitemap'))

    # Renders the index.html template
    return render_template('index.html')

@app.route('/sitemap/sitemap.xml')
def Sitemap():
    # Returns the sitemap.xml file as an attachment download
    return send_from_directory(app.config['SITEMAP_FOLDER'], "sitemap.xml", as_attachment=True)
