import cv2
import face_recognition
import time

import subprocess
import platform
import os

def open_incognito_window(browser='chrome'):
    # Detect the operating system
    system = platform.system()

    # Browser commands for incognito mode
    browser_commands = {
        'chrome': {
            'Windows': 'start chrome --incognito',
            'Darwin': 'open -a "Google Chrome" --args --incognito',
            'Linux': 'google-chrome --incognito'
        },
        'brave': {
            'Windows': 'start brave --incognito',
            'Darwin': 'open -a "Brave Browser" --args --incognito',
            'Linux': 'brave-browser --incognito'
        }
    }

    # Check if the browser and system are supported
    browser_lower = browser.lower()
    if browser_lower not in browser_commands or system not in browser_commands[browser_lower]:
        print(f"Unsupported combination of browser '{browser}' and operating system '{system}'")
        return

    # Open the specified browser in incognito mode
    subprocess.run(browser_commands[browser_lower][system], shell=True)


def open_in_incognito_tab(browser_name, url):
    # AppleScript command to open a new incognito tab in an existing browser window
    applescript = f'''
    tell application "{browser_name}"
        if it is running then
            make new tab at end of tabs of window 1 with properties {{URL:"{url}"}}
        else
            open location "{url}"
        end if
        activate
    end tell
    '''

    # Run the AppleScript using subprocess
    subprocess.run(['osascript', '-e', applescript])

def run_website_opener():
    if __name__ == "__main__":
        # Specify the URL of the website you want to open
        url = "https://"
        url_1 = url+'accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ifkv=ASKXGp2kqCqAlHRr8gEV3wQRGCU1roK3np0cX8xrpksHldeNigOLVaJrFG-sC7-U__JBT21xA7tbAg&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-787815589%3A1701304875703537&theme=glif'
        url_2 = url+'arms.esuhsd.org'
        url_3 = url + "accounts.google.com/v3/signin/identifier?continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ifkv=ASKXGp2kqCqAlHRr8gEV3wQRGCU1roK3np0cX8xrpksHldeNigOLVaJrFG-sC7-U__JBT21xA7tbAg&rip=1&sacu=1&service=mail&flowName=GlifWebSignIn&flowEntry=ServiceLogin&dsh=S-787815589%3A1701304875703537&theme=glif"
        url_4 = url+"sso.sjeccd.edu/_layouts/PG/login.aspx?ReturnUrl=%2f"
        url_5 = url+"account.cengage.com/login?SAMLRequest=fZLLTsMwEEV%2FJfI%2BDztN0lpNUUWFVAkqxEuIneVMU4tkHDxOS%2F%2BekFIEC9haM%2BdenfH84r1tgj04MhZLxqOEBYDaVgbrkj0%2BXIVTdrGYk2ob0cll73d4B289kA%2BWROD8sHZpkfoW3D24vdHweHddsp33Hck4VsNGpAFrVUOkbRsT2XikxYlVIs%2BmfIu0ec429TLNChasBrRB5cc63xStbY%2F%2BF6ixtUEWXFmnYexVsq1qCFiwXpXMVJMkzURR5AXnRZbPknSWZmmeZfkwQNTDGskr9CUTiUhDLsJk8iBSmU4lLyIuZi8seDprEZ9aBlFI8mSiZL1DaRUZkqhaIOm1vF%2FeXMthVHbOeqttw77EyTHQ%2FST8D1BntWxxVnA4HCL76tVJ4iiQTr7DIW5vKnAxdXusWkB1tJ2r31R1rPw8%2Flnh%2B5KbIXO9urWN0cdPh63yf1fiER9fTBVux1HZI3WgzdZAxeLFV8bv%2F7H4AA%3D%3D&RelayState=%252Foauth2%252Fv1%252Fauthorize%252Fredirect%253Fokta_key%253DWAdXX6-mFtzB7oNdeE52fc0AaClA5PHpnR7tGKKNn_0&SigAlg=http%3A%2F%2Fwww.w3.org%2F2001%2F04%2Fxmldsig-more%23rsa-sha256&Signature=ZvoHRsb6%2BoQ4u%2BZSmXnuYV9eD5W%2B6Dw9n6loM%2BKyu2DfbUieX48yjEVZF%2FOFv4Qj%2FEYxYkWbQXRG5Ac06cEanhHj2yijJEO5UCtXHSG7ZSrmP7L%2FeweEJ6AxvATWjLGGBHmSsmF8R8FzAHT8cCB%2BiV0RNm05y9cxcrv5QJ62EG5rMf6O7OdPVLz2kEAWeWigx1PokUIuchO4Rln%2BkVW2NvCtJt6q5GMS%2FPzjGzrDwOOB3h8c5sdlFuyzyQ4RZOHf2g2e1mHnlqq9RkKgGaqgNTu4NiUVAEViA%2BccZgpU5oOmHKSmIm5K1WnolDWXM1oTuqOoypbfD0Kbw5gGdn5zzA%3D%3D"
        url_6 = url+"auth0.openai.com/u/login/identifier?state=hKFo2SAxTmVnYVI1T01TSGdDbnhkX2ExTHZPUFpaLXRhbE90VqFur3VuaXZlcnNhbC1sb2dpbqN0aWTZIFV4enpQTlp5dXI3WGhlZjBuRFFoU25KcGtOY1NBTDVlo2NpZNkgVGRKSWNiZTE2V29USHROOTVueXl3aDVFNHlPbzZJdEc"
        # Open incognito window in Google Chrome
        subprocess.run(['open', '-a', "Discord"])
        subprocess.run(["open", "-a", "WhatsApp"])
        open_incognito_window("Chrome")
        open_in_incognito_tab("Google Chrome", url_1)
        open_in_incognito_tab("Google Chrome", url_2)
        open_in_incognito_tab("Google Chrome", url_5)
        open_incognito_window("Brave")
        open_in_incognito_tab("Brave Browser", url_3)
        open_in_incognito_tab("Brave Browser", url_4)
        open_in_incognito_tab("Brave Browser", url_6)
        

global true_false
true_false = False

def take_picture():
    try: 
        video_capture = cv2.VideoCapture(1)
        video_capture.set(3, 400)  # Set width
        video_capture.set(4, 400)  # Set height

        print(f"Capturing reference image. Look directly at the camera.")

        # Capture frame-by-frame
        ret, frame = video_capture.read()

        # Save the captured reference image
        cv2.imwrite('faces/reference_image.jpg', frame)
        print("Reference image saved as reference_image.jpg")

        # Release the webcam and close the window
        video_capture.release()
        cv2.destroyAllWindows()
    except:
        video_capture = cv2.VideoCapture(0)
        video_capture.set(3, 400)  # Set width
        video_capture.set(4, 400)  # Set height

        print(f"Capturing reference image. Look directly at the camera.")

        # Capture frame-by-frame
        ret, frame = video_capture.read()

        # Save the captured reference image
        cv2.imwrite('faces/reference_image.jpg', frame)
        print("Reference image saved as reference_image.jpg")

        # Release the webcam and close the window
        video_capture.release()
        cv2.destroyAllWindows()

def capture_reference_image():
    take_picture()

def compare_faces(key_image_path, test_image_path):
    # Load the key image
    key_image = face_recognition.load_image_file(key_image_path)
    key_face_encoding = face_recognition.face_encodings(key_image)[0]

    # Load the test image
    test_image = face_recognition.load_image_file(test_image_path)
    test_face_encoding = face_recognition.face_encodings(test_image)

    if not test_face_encoding:
        print("No face found in the test image.")
        return False

    # Compare the face encodings
    results = face_recognition.compare_faces([key_face_encoding], test_face_encoding[0])

    if results[0]:
        print("Face in the test image matches the key face.")
        global true_false
        true_false = True
        return True
    else:
        print("Face in the test image does not match the key face.")
        run_website_opener()
        return False

if __name__ == "__main__":
    # Automatically capture a reference image after 3 seconds
    capture_reference_image()

    # Compare the captured reference image with a key image
    key_image_path = "faces/shiv-face.jpg"
    test_image_path = "faces/reference_image.jpg"
    compare_faces(key_image_path, test_image_path)
    if true_false == False: 
        pass
    else: 
        run_website_opener()