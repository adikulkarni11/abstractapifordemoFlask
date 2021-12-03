# Email Validation and Verification through Abstract API's Email Verification API (https://www.abstractapi.com/email-verification-validation-api)
# Reasons: 1) Checking a misspelled email 2) Checking a malformed email

import os
import json
import time
from abstractapikey import api_keygen

import requests


#print(response.status_code)
#print(response.content)

def t1():

    lookupEmail = 'dff@cs.columbia.edu'       #email to verify and validate
    apiKey = api_keygen()                   # our api key is called via an other file to ensure security
    
    response = requests.get("https://emailvalidation.abstractapi.com/v1/?api_key=" + api_keygen() + "&email=" + lookupEmail)


    print("T1 result = \n", "Status Code:", response.status_code, "\n", "Content:",  response.content.decode('utf-8'))

def t2():
    time.sleep(1)
    # EUD instead of EDU

    lookupEmail = 'dff@cs.columbia.eud'       #email to verify and validate
    apiKey = api_keygen()                   # our api key is called via an other file to ensure security
    
    response = requests.get("https://emailvalidation.abstractapi.com/v1/?api_key=" + api_keygen() + "&email=" + lookupEmail)


    print("T2 result = \n", "Status Code:", response.status_code, "\n", "Content:",  response.content.decode('utf-8'))


def t3():
    # WRONG EMAIL DOMAIN columiba instead of columbia
    time.sleep(1)
    lookupEmail = 'dff@cs.columiba.edu'       #email to verify and validate
    apiKey = api_keygen()                   # our api key is called via an other file to ensure security
    
    response = requests.get("https://emailvalidation.abstractapi.com/v1/?api_key=" + api_keygen() + "&email=" + lookupEmail)

    print("T3 result = \n", "Status Code:", response.status_code, "\n", "Content:",  response.content.decode('utf-8'))

t1()
print('------------------------------')
t2()
print('------------------------------')
t3()
