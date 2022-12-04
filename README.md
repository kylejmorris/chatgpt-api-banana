# ChatGPT api

* It uses playwright and chromium to open browser and parse html.

# How to install

* Make sure that python and virual environment is installed.

* Create a new virtual environment

```python
# one time
virtualenv -p $(which python3) pyenv

# everytime you want to run the server
source pyenv/bin/activate
```

* Now install the requirements

```
pip install -r requirements.txt
```

* If you are installing playwright for the first time, it will ask you to run this command for one time only.

```
playwright install && playwright install-deps
```
* Set env vars so login works
export EMAIL="your openai email"
export PASSWORD="your openai password"

* Note: you need to use email/password login for this to work, gmail auth isn't supported. 

* Now run the server

```
python server.py
```

* The server runs at port `5001`. If you want to change, you can change it in server.py


# Api Documentation

* There is a single end point only. It is available at `/chat`

```sh
curl -XGET http://localhost:5001/chat?q=Write%20a%20python%20program%20to%20reverse%20a%20list
```

# Credit

* thanks to [Daniel Gross's whatsapp gpt](https://github.com/danielgross/whatsapp-gpt) package. + [Tarans cleanuped installation](https://github.com/taranjeet/chatgpt-api) for making this easier + Chat-GPT for advising me on how to access openai programatically. 
