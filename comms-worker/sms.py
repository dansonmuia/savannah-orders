''' Send AT smses from here '''

import os

import africastalking


username = os.environ['AT_USERNAME']
api_key = os.environ['AT_API_KEY']

africastalking.initialize(username, api_key)

sms = africastalking.SMS


def send_sms(message, phone):
    sms.send(message, [phone])
