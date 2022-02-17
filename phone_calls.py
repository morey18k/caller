from twilio.rest import Client
import numpy as np
import time

#added comment
server_path = "/home/bfichera/mnt/SHG/Data/temp.txt"

# Twilio phone number goes here. Grab one at https://twilio.com/try-twilio
# and use the E.164 format, for example: "+12025551234"
TWILIO_PHONE_NUMBER = "+18646894581"

# list of one or more phone numbers to dial, in "+19732644210" format
DIAL_NUMBERS = ["+19194337800", "+12039136784"]

# URL location of TwiML instructions for how to handle the phone call
TWIML_INSTRUCTIONS_URL = \
  "http://static.fullstackpython.com/phone-calls-python.xml"

# replace the placeholder values with your Account SID and Auth Token
# found on the Twilio Console: https://www.twilio.com/console
client = Client("AC14187d56a371349d6f3814cdb1536513", "a7496f4e30a27ebc57889326541280d0")


def dial_numbers(numbers_list):
    """Dials one or more phone numbers from a Twilio phone number."""
    for number in numbers_list:
        print("Dialing " + number)
        # set the method to "GET" from default POST because Amazon S3 only
        # serves GET requests on files. Typically POST would be used for apps
        client.calls.create(to=number, from_=TWILIO_PHONE_NUMBER,
                            twiml='<Response><Say>Temperature Has Risen Above 80 Kelvin. Please Fix.</Say></Response>', method="GET")


if __name__ == "__main__":
    prev_temp = 90
    threshold = 80 
    while True:   
        time.sleep(1)
        try:
            temp = np.genfromtxt(server_path)
            print(temp)
        except ValueError:
            temp = prev_temp
            print('There was an error reading the temperature')
        if (prev_temp <threshold and temp > threshold):
            dial_numbers(DIAL_NUMBERS)
        prev_temp = temp

