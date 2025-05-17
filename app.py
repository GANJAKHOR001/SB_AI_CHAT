@ -0,0 +1,10 @@

from flask import Flask

app Flask(__name__)

@app.route('/')

def hello_world():

return 'Hello from Tamanna'

if __name__ == "__main__":

app.run()