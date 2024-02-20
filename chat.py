import os
import sys
import json
import random
import numpy as np
import socketserver
import tensorflow as tf
from nltk import LancasterStemmer
from chatbot_dependencies import *
from face_recog import *
from http.server import SimpleHTTPRequestHandler
from urllib.parse import parse_qs
import pygments
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
import cgi
import shutil
from pygments.util import ClassNotFound
import google.generativeai as genai
import PIL.Image


def chat(input_text, v_t):

    print("API KEY HERE")

    safety_settings = [
        {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
        {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"}
    ]

    ### ENTER YOUR GOOGLE_API_KEY BELOW ###
    
    os.environ['GOOGLE_API_KEY'] = ""
    genai.configure(api_key = os.environ['GOOGLE_API_KEY'])
    v_t = v_t.lower()
    if v_t == "t":
        model = genai.GenerativeModel('gemini-pro', safety_settings=safety_settings)

        chat = model.start_chat(history=[])

        response = chat.send_message(input_text.lower())
        return (str(response.text))

    elif v_t == "v":

        ### ENTER YOUR GOOGLE_API_KEY ###

        google_api_key = "" 
        os.environ['GOOGLE_API_KEY'] = google_api_key
        genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

        safety_settings = [
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"}
        ]

        img = PIL.Image.open('data.png')

        model_gemini_pro_vision = genai.GenerativeModel('gemini-pro-vision', safety_settings=safety_settings)

        response = model_gemini_pro_vision.generate_content(contents=[input_text, img])

        return str(response.text)


def extract_type(input_dict, input_text):
    try:
        data = json.loads(input_dict)

        name = data.get(input_text)

        return str(name)
    except:
        return None



class WebChatHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        super().do_GET()

    def do_POST(self):
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode('utf-8')

        print("POST_DATA:", post_data)

        u_input = extract_type(post_data, "userInput")
        print("INPUT:", u_input)

        f_name = extract_type(post_data, "fileName")
        print("FILE NAME:", f_name)

        contents = extract_type(post_data, "fileContents")
        contents = uri_to_image(contents)
        string = "None"

        if str(u_input.strip()) != string and str(f_name.strip()) != string:
            answer = chat(u_input, "v")
        elif str(f_name.strip()) != string and str(u_input) != string:
            answer = "Text input is required along with the image."
        elif str(u_input) != string and str(f_name.strip()) == string:
            answer = chat(u_input, "t")

        print(answer)

        self.send_response(200)
        self.end_headers()

        try:
            code_start = answer.find('```') + 3
            code_end = answer.rfind('```')
            code_content = answer[code_start:code_end].strip()

            lang_start = code_content.find('\n') + 1
            language = code_content[:lang_start].strip()
            code_content_without_lang = code_content[lang_start:]

            lexer = get_lexer_by_name(language, stripall=True)
            formatter = HtmlFormatter(style='colorful')
            formatted_code = highlight(code_content_without_lang, lexer, formatter)

            final_response = formatted_code if '```' in answer else answer
        except ClassNotFound:
            final_response = answer

        bot_response_with_links = re.sub(r'\*\*(.*?)\*\*', r'<b>\1</b>', final_response)
        bot_response_with_links = re.sub(r'(https?://\S+)', r'<a href="\1" target="_blank">\1</a>', bot_response_with_links)
        formatted_response = "<html><body>{}</body></html>".format(bot_response_with_links.replace('\n', '<br>'))
                    
        self.wfile.write(bytes(formatted_response, 'utf-8'))

if __name__ == "__main__":
    port = 8001
    try:
        with socketserver.TCPServer(("", port), WebChatHandler) as httpd:
            print(f"Serving on port {port}")
            open_incognito_window("Chrome")
            url_1 = f"http://127.0.0.1:{port}/webchat.html"
            open_in_incognito_tab("Google Chrome", url_1)
            httpd.serve_forever()
    except OSError:
        with socketserver.TCPServer(("", port+1), WebChatHandler) as httpd:
            print(f"Serving on port {port+1}")
            open_incognito_window("Chrome")
            url_1 = f"http://127.0.0.1:{port+1}/webchat.html"
            open_in_incognito_tab("Google Chrome", url_1)
            httpd.serve_forever()