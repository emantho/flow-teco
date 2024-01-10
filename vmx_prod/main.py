import requests
from xml.etree import ElementTree

# Defining SOAP endpoint URL, user and password
url = 'https://10.200.181.30:8099/services/AdminMgmtService'
name = 'emanjarres'
prod_password = 'emanjarres2404'

# Defining the SOAP Envelope
envelope = '''
<?xml version="1.0" encoding="utf-8"?>
<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:omi="http://www.verimatrix.com/omi" xmlns:omit="http://www.verimatrix.com/schemas/OMItypes.xsd" >
    <soapenv:Header/>
    <soapenv:Body>
        <omi:signOn>
            <userAttributes>
                <omit:userName>{{name}}</omit:userName>
                <omit:password>{{prod_password}}</omit:password>
            </userAttributes>
        </omi:signOn>
    </soap:Body>
</soap:Envelope>
'''

# Defining SOAP Header
headers = {
    'Content-Type': 'text/xml; charset=utf-8',
    'SOAPAction': 'http://www.verimatrix.com/omi/signOn'
}

# Send the SOAP request
response = requests.post(url, data=envelope, headers=headers)

# Print the response
print(response.content)