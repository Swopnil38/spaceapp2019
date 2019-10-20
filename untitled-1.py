from twilio.rest import Client

account_sid = 'AC5a4a87bfbace59ef81e8f0d2b871d62e'
auth_token = '385dd141e51f9e2518744e53e0955984'
client = Client(account_sid, auth_token)
message = client.messages \
                    .create(
                         body='You Reported A Fire.Contact 100 and 102 foremergency ',
                         from_='+17078791851',
                         to= '+9779804008243'
                     )
print(message.sid)
