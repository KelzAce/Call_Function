from twilio.rest import Client

def place_call_and_read_text(phone_number, text):
    # Replace these variables with your Twilio account SID and Auth Token
    account_sid = 'YOUR_TWILIO_ACCOUNT_SID'
    auth_token = 'YOUR_TWILIO_AUTH_TOKEN'
    # Replace this with your Twilio phone number
    twilio_phone_number = 'YOUR_TWILIO_PHONE_NUMBER'

    # Initialize the Twilio client
    client = Client(account_sid, auth_token)

    try:
        # Make the call
        call = client.calls.create(
            to=phone_number,
            from_=twilio_phone_number,
            url='http://twimlets.com/echo?Twiml=' + text
        )
        print(f"Call placed to {phone_number}. Call SID: {call.sid}")
    except Exception as e:
        print(f"Error occurred: {str(e)}")

# Example usage
if __name__ == "__main__":
    phone_number = '+1234567890'  # Replace with the desired phone number
    text_to_read = 'Hello, this is a test call from Twilio. Thank you for listening.'  # Replace with the desired text
    place_call_and_read_text(phone_number, text_to_read)
