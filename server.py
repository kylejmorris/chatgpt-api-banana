"""Make some requests to OpenAI's chatbot"""

import time
import os
from sanic import Sanic, response

from pyChatGPT import ChatGPT

app = Sanic("my_app")


@app.route('/healthcheck', methods=["GET"])
def healthcheck(request):
    return response.json({"state": "healthy"})

@app.route('/', methods=["POST"]) # Do not edit - POST requests to "/" are a required interface
def inference(request):
    try:
        model_inputs = response.json.loads(request.json)
    except:
        model_inputs = request.json

    # Parse out your arguments
    prompt = model_inputs.get('prompt', None)
    if prompt == None:
        return response.json({'message': "No prompt provided"})

    session_id = model_inputs.get('session_id', None)
    if session_id == None:
        return response.json({'message': "No session ID provided"})

    conversation_id = model_inputs.get('conversation_id', None)
    if conversation_id == None:
        print("This is a new conversation.")
    
    api = ChatGPT(session_id, conversation_id)  # auth with session token
    resp = api.send_message(prompt)
    print(resp['message'], resp['conversation_id'])

    return response.json({"message": resp['message'], "conversation_id": resp['conversation_id']}) # Do not edit - returning a dictionary as JSON is a required interface


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, workers=1)