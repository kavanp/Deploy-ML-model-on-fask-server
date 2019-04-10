# Deploy-ML-model-on-fask-server
This project builds a simple ML model ins sci-kit learn and deploys it on a flask app. 

## model.py
File model.py builds ML model and saves it as pickle file. 

## server.py
server.py builds a flask server which loads the saved model and listens to incoming request. A request comes as JSON payload
and it is forwarded to model which makes predictions. Upon making predictions, it is sent back to client as a JSON response.

## client.py
Using python's request module this file makes http request to flask server.
