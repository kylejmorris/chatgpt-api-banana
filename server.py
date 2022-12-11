"""Make some requests to OpenAI's chatbot"""

import time
import os
import flask

from flask import g

from playwright.sync_api import sync_playwright

APP = flask.Flask(__name__)
PLAY = sync_playwright().start()
BROWSER = PLAY.chromium.launch_persistent_context(
    user_data_dir="/tmp/playwright",
    headless=True,
)
PAGE = BROWSER.new_page()

def get_input_box():
    """Get the child textarea of `PromptTextarea__TextareaWrapper`"""
    return PAGE.query_selector('.PromptTextarea__TextareaWrapper-sc-4snkpf-0 textarea')

def is_logged_in():
    # See if we have a textarea with data-id="root"
    return get_input_box() is not None

def send_message(message):
    # Send the message
    box = get_input_box()
    # print css info about box
    print(str(box.inner_html))
    box.fill(message) # click seems to freeze up on headless, so just fill textarea by force
    box.press("Enter")

def get_last_message():
    """Get the latest message"""
    page_elements = PAGE.query_selector_all("div[class*='ConversationItem__Message']")
    last_element = page_elements[-1]
    return last_element.inner_text()

@APP.route("/chat", methods=["GET"])
def chat():
    message = flask.request.args.get("q")
    print("Sending message: ", message)
    send_message(message)
    time.sleep(10) # TODO: there are about ten million ways to be smarter than this
    response = get_last_message()
    print("Response: ", response)
    return response

def start_browser():
    PAGE.goto("https://chat.openai.com/")

    if not is_logged_in():
        print(" attempting to login to openai")
        # Find the "Log in" button on the page
        login_button = PAGE.get_by_role("button")
        print(login_button)

        # Click the button
        login_button.click()

        print("Clicked login button")

        # fill in login form
        # Enter your login information
        email_field = PAGE.locator('label')
        continue_button = PAGE.locator("button[name=\"action\"]")

        email_field.fill("kyle@banana.dev")
        continue_button.click()

        print("filled in email")
        try:
            # Submit the login form
            password_field = PAGE.locator("label")
            password_field.fill("bananabanana12")
            continue_button = PAGE.locator("button[name=\"action\"]")
            continue_button.click()
        except Exception as e:
            print("Failed to login: ", e)
            return

        if not is_logged_in():
            # if you still aren't logged in well i got bad news for you son. i got 99 problems and auth is one
            return 

        print("Logged in")
        APP.run(port=5001, threaded=False)

if __name__ == "__main__":
    start_browser()
    APP.run(port=5001, threaded=False)

