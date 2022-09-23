# import os
# import flask
# import werkzeug
# import time

# UPLOAD_FOLDER = './uploadedImages'
# ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# app = flask.Flask(__name__)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# @app.route('/', methods=["GET","POST"])
# def upload():
#     print("Upload method called\n")
#     if flask.request.method == 'POST':
#         print("req received\n")
#         if 'image' not in flask.request.files:
#             print("Inside if\n")
#             flask.flash('No file part')
#             return flask.redirect(flask.request.url)
#         fileid = flask.request.files['image']
#         print("saving image/n")
#         imagefile = flask.request.files[fileid]
#         filename = werkzeug.utils.secure_filename(imagefile.filename)
#         print("filename: " + imagefile.filename)
#         timestr = time.strftime("%Y%m%d-%H%M%S")
#         #imagefile.save("./uploadedImages/"+ timestr + '_' + filename)
#         imagefile.save(os.path.join(app.config['UPLOAD_FOLDER'], timestr+'_'+filename))
#         return "Image(s) Uploaded Successfully. Come Back Soon."
#     return '''
#     <!doctype html>
#     <title>Upload new File</title>
#     <h1>Upload new File</h1>
#     '''

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000, debug=True)




import flask
import werkzeug
import time
import os

UPLOAD_FOLDER = './uploadedImages'

app = flask.Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def handle_request():
    if flask.request.method == 'POST':
        imagefile = flask.request.files['image']
        textmsg = flask.request.values['text']
        print("\nText recieved " + textmsg)
        filename = werkzeug.utils.secure_filename(imagefile.filename)
        print("\nReceived image File name : " + imagefile.filename)
        timestr = time.strftime("%Y%m%d_%H%M%S")
        imagefile.save(os.path.join("./uploadedImages/" + textmsg, timestr+'_'+filename))
        return "Image Uploaded Successfully"
    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>'''

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2929, debug=True)