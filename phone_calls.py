from twilio.rest import Client


# Twilio phone number goes here. Grab one at https://twilio.com/try-twilio
# and use the E.164 format, for example: "+12025551234"
TWILIO_PHONE_NUMBER = "+18646894581"

# list of one or more phone numbers to dial, in "+19732644210" format
DIAL_NUMBERS = ["+19194337800"]

# URL location of TwiML instructions for how to handle the phone call
TWIML_INSTRUCTIONS_URL = \
  "http://static.fullstackpython.com/phone-calls-python.xml"

# replace the placeholder values with your Account SID and Auth Token
# found on the Twilio Console: https://www.twilio.com/console
client = Client("AC14187d56a371349d6f3814cdb1536513", "1a07a02936f3d4fcb348cd8c023171c9")


def dial_numbers(numbers_list):
    """Dials one or more phone numbers from a Twilio phone number."""
    for number in numbers_list:
        print("Dialing " + number)
        # set the method to "GET" from default POST because Amazon S3 only
        # serves GET requests on files. Typically POST would be used for apps
        client.calls.create(to=number, from_=TWILIO_PHONE_NUMBER,
                            twiml='<Response><Say>Temperature Has Risen Above 80 Kelvin. Please Fix.</Say></Response>', method="GET")


if __name__ == "__main__":
    dial_numbers(DIAL_NUMBERS)
