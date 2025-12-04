import sys

if len(sys.argv) > 1:
    script_name = sys.argv[0]
    websitename = sys.argv[1]
    weburl = sys.argv[2]
    username = sys.argv[3]
    password = sys.argv[4]

else:
    script_name = sys.argv[0]
    websitename = "abc limited"
    weburl = "abc.com"
    username = "king"
    password = "12345"

print(f"Script Name : {script_name}")
print(f"Website Name: {websitename}")
print(f"Website URL : {weburl}")
print(f"User Name   : {username}")
print(f"Password    : {password}")
