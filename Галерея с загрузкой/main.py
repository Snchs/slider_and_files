from flask import Flask, render_template ,request
import os

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def form_sample():
    global file_dir
    if request.method == 'GET':
        return render_template('base.html')
    elif request.method == 'POST':
        dir_img = request.files['file']
        dir_img.save('static/img/' + dir_img.filename)

        list_all_pict  = next(os.walk("static/img"))[2]

        return render_template('base.html', list_pict=list_all_pict[4:])

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')