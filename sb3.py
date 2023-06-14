from flask import Flask, send_file
app = Flask(__name__)
@app.route('/')
def home():
    return send_file(r'D:\tour\vindyachal\VID-20230107-WA0002.mp4')
if __name__ == '__main__':

    app.run(host='0.0.0.0',port=9999, debug=True)

