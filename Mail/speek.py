  def speek(retuen_msg):
    out_msg =  {
        'version': '1.0',
        'sessionAttributes': '',
        'response': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': retuen_msg
            },
            'card': {
                'type': 'Simple',
                'title': "SessionSpeechlet - " + 'Hotel booking',
                'content': "SessionSpeechlet - " + retuen_msg
            },
            'reprompt': {
                'outputSpeech': {
                    'type': 'PlainText',
                    'text': 'Please enter the city'
                }
            },
            'shouldEndSession': 'false'
        }
    }
    return out_msg
    
    
def session(session,retuen_msg):
    out_msg =  {
        'version': '1.0',
        'sessionAttributes': session,
        'response': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': retuen_msg
            },
            'card': {
                'type': 'Simple',
                'title': "SessionSpeechlet - " + 'Hotel booking',
                'content': "SessionSpeechlet - " + retuen_msg
            },
            'reprompt': {
                'outputSpeech': {
                    'type': 'PlainText',
                    'text': 'Please enter the city'
                }
            },
            'shouldEndSession': 'true'
        }
    }
    return out_msg