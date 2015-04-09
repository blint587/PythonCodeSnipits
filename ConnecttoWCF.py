from suds.client import Client

client = None

class EstablisConnection():

    def __init__(self):
        print ("Connecting to Service...")
        wsdl = "http://localhost:8744/WcfPythonTest/?wsdl"
        global client
        client = Client(wsdl)

try:
   EstablisConnection()
except Exception as e:
    print('connection failed')


if client is not None:
    result = client.service.Add(1, 2)
    print (result)