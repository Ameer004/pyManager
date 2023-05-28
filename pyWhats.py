from datetime import datetime
import json
from whatsapp_api_client_python import API
id = '1101778445'
token = 'cb49bdc0829841e092771f4ad059ed277784102bdaba4bbe93'
greenAPI = API.GreenApi(id, token)

def main():
   greenAPI.webhooks.startReceivingNotifications(onEvent)

def onEvent(typeWebhook, body):
   if typeWebhook == 'incomingMessageReceived':
      onIncomingMessageReceived(body)      
   elif typeWebhook == 'deviceInfo':   
      onDeviceInfo(body)              
   elif typeWebhook == 'incomingCall':
      onIncomingCall(body)

def onIncomingMessageReceived(body):
        idMessage = body['idMessage']
        eventDate = datetime.fromtimestamp(body['timestamp'])
        senderData = body['senderData']
      #  sender = json.loads(senderData)
        messageData = body['messageData']
        if senderData["chatId"] == "2348143109904@c.us":
           send = greenAPI.sending.sendMessage(senderData["chatId"], "Hello")
           print(idMessage + ': ' 
            + 'At ' + str(eventDate) + ' Incoming from ' \
            + json.dumps(senderData, ensure_ascii=False) \
            + ' message = ' + json.dumps(messageData, ensure_ascii=False))
            
def onIncomingCall(body):
   idMessage = body['idMessage']
   eventDate = datetime.fromtimestamp(body['timestamp'])
   fromWho = body['from']
   print(idMessage + ': ' 
      + 'Call from ' + fromWho 
      + ' at ' + str(eventDate))


if __name__ == "__main__":
    main()