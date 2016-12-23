import time, requests, sys
from requests import post
from json import dumps
from getopt import getopt, GetoptError

def main(argv):
    flags = "h:p:"
    options = ["host", "port"]
    headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
    host = ""
    port = ""
    devices = getDevices()
    waitTime = 5

    try:
        opts, args = getopt(sys.argv[1:], flags, options)
    except GetoptError as e:
        print("Error: " + str(e))
        sys.exit(2)

    for opt, args in opts:
        if opt in ("-h", "--host"):
            host = args
        elif opt in ("-p", "--port"):
            port = ''.join(c for c in args if c.isdigit())

    destination = host + ":" + port if port != '' else host
    for device in devices:
        json = dumps(device)
        request = post(destination, json, headers)
        time.sleep(waitTime)


def getDevices():
    return [
        {
            "eventType": "E",
            "deviceId": "1",
            "localId": "3"
        },
        {
            "eventType": "E",
            "deviceId": "2",
            "localId": "4"
        },
        {
            "eventType": "S",
            "deviceId": "1",
            "localId": "3"
        },
        {
            "eventType": "E",
            "deviceId": "4",
            "localId": "1"
        },
        {
            "eventType": "E",
            "deviceId": "3",
            "localId": "2"
        },
        {
            "eventType": "S",
            "deviceId": "2",
            "localId": "4"
        },
        [
            {
                "eventType": "S",
                "deviceId": "3",
                "localId": "2"
            },
            {
                    "eventType": "S",
                    "deviceId": "4",
                    "localId": "1"
            }
        ]
    ]



if __name__ == '__main__':
    main(sys.argv[1:])
