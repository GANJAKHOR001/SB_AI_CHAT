from flask import Flask, request
import os

from flask import Flask

app Flask (__name__)

port = int(os.environ.get('PORT', 8000))


def index(): 
return 'Hello' 

if __name__ == '__main__': app.run(host='0.0.0.0', port=port)

