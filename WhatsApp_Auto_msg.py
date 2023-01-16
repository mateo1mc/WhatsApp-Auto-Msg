import pywhatkit

phone_no = str(input("Enter phone number: "))
message = str(input("Enter message: "))
time_hour = int(input("Enter hour 0-24: "))
time_min = int(input("Enter minutes 00-59: "))
pywhatkit.sendwhatmsg(phone_no, message, time_hour, time_min, 15, True, 2)
