from flask import Flask
app=Flask(__name__)
@app.route('/')
def sayhello():
    return 'Hello'
@app.route('/hi')
def sayhi():
    return 'Hi'
if __name__=='__main__':
    app.debug=True
    app.run()