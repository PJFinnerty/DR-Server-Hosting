from flask import Flask

app = Flask(__name__, static_url_path='', static_folder='.')

@app.route('/', methods=['GET'])
def printHello():
    return "Hello, are ya well?"

if __name__ == '__main__' :
    app.run(debug= True)
    
