from flask import Flask
from flask import request
app = Flask(__name__)

@app.route('/',methods=['GET','POST'])
def hello_world():
    name = request.args.get('name')
    return name

if __name__ == '__main__':
	app.run()
