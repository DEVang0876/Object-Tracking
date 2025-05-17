import pywhatkit as pwk
phone_number = "+9925456609"  # Replace with the recipient's phone number
message = "Hello, this is a test message!"  # Replace with your message
time_hour = 18  # Replace with the hour you want to send the message (24-hour format)
time_minute = 10  # Replace with the minute you want to send the message
# Send the message using pywhatkit
pwk.sendwhatmsg(phone_number, message, time_hour, time_minute)
