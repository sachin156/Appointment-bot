from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
import datefinder
import pickle
from apiclient.discovery import build
import dateparser
from datetime import datetime,timedelta

# db_connect = create_engine('sqlite:///chinook.db')
credentials=pickle.load(open('token.pkl','rb'))
service=build("calendar","v3",credentials=credentials)
result=service.calendarList().list().execute()
calendar_id=result['items'][0]['id']
now = datetime.utcnow().isoformat() + 'Z'

app = Flask(__name__)
api = Api(app)
# global events_result
# events_result=service.events().list(calendarId=calendar_id, timeMin=now,
#                                            maxResults=500, singleEvents=True,
#                                            orderBy='startTime').execute()

def get_events():
#     print(now)
    events_result = service.events().list(calendarId=calendar_id, timeMin=now,
                                               maxResults=500, singleEvents=True,
                                               orderBy='startTime').execute()
    # print(events_result.get('items',[]))
    return events_result.get('items', [])

def create_event(new_event):
    if already_exists(new_event):
        return event_suggest()
    else:
        events_result = service.events().list(calendarId=calendar_id, timeMin=now,
                                                       maxResults=500, singleEvents=True,
                                                       orderBy='startTime').execute()
        events=events_result['items']
        # events_result=events_result.get('items', [])
        event_id=""
        date=new_event['start']['dateTime']+'+05:30'
        events_result=events_result.get('items', [])
        for event in events_result:
            if date==event['start']['dateTime']:
                event_id=event['id']
        if event_id=="":
            return event_suggest()
        else:
            return update_event(new_event,event_id)

def event_suggest():
    events_result = service.events().list(calendarId=calendar_id, timeMin=now,
                                               maxResults=500, singleEvents=True,
                                               orderBy='startTime').execute()
    events=events_result['items']
#         print(events)
    eventsforappointment=[]
    suggested_times=[]
    for event in events:
        if event['summary'].lower()=='noappointment':
            eventsforappointment.append(event)
            x=(dateparser.parse(event['start']['dateTime']))
            x=x.strftime('%B%d-%H:%M')
            suggested_times.append(x)
    suggested_times=','.join(suggested_times)

    return " Bot: Pick from the suggested timings:" +'\n'+suggested_times+ '''<form method="POST">
              Input: <input type="text" name="appoint"><br>'''+'''<input type="submit" value="Submit"><br>
              </form>'''
def update_event(newevent,event_id):
    event = service.events().get(calendarId=calendar_id,eventId=event_id).execute()
    event['summary']='Appointment'
    updated_event = service.events().update(calendarId=calendar_id, eventId=event['id'], body=event).execute()
    # Print the updated date.
    print(updated_event['updated'])
    return "Appointmet added"


def already_exists(new_event):
    events = get_date_events(new_event['start']['dateTime'],get_events())
    event_list = [new_event['summary'] for new_event in events]
    if new_event['summary'] not in event_list:
        return False
    else:
        return True


def get_date_events(date, events):
    lst = []
    i=0
    date = date+'+05:30'
    for event in events:
        i+=1
        if event.get('start').get('dateTime'):
#             print(event['start']['dateTime'])
            d1 = event['start']['dateTime']
            if d1 == date:
                lst.append(event)
    print(i)
    return lst

def new_eve(text):
    matches=list(datefinder.find_dates(text))
    print(matches)
    if len(matches)==0:
        return "null"
    else:
        start_time=matches[0]
    end_time=start_time+timedelta(minutes=30)

    event = {
      'summary': 'Appointment',
      'location': 'Hyderabad',
      'description': 'Appointment with the doctor',
      'start': {
        'dateTime': start_time.strftime("%Y-%m-%dT%H:%M:%S"),
        'timeZone': 'Asia/Kolkata',
      },
      'end': {
        'dateTime': end_time.strftime("%Y-%m-%dT%H:%M:%S"),
        'timeZone': 'Asia/Kolkata',
      },
      'reminders': {
        'useDefault': False,
        'overrides': [
          {'method': 'email', 'minutes': 24 * 60},
          {'method': 'popup', 'minutes': 10},
        ],
      },
    }
    return event

# print("Hi! book an Appointment")
# text=input()

@app.route('/')
def index():
    return "Main Page (Dashboard)"

def getfuncval():
    event=new_eve(request.form.get('appoint'))
    print(event)
    if event=="null":
        return '''<form method="POST">
                  Bot:Sorry,I can book an appointment only if date and time are provided <br>
                  Input: <input type="text" name="appoint"><br>'''+'''<input type="submit" value="Submit"><br>
                  </form>'''
    else:
        return create_event(event)
    # x='You:'+ request.form.get('appoint') + '''<form method="POST">
    #           Bot: Hi book an appointment<br>
    #           Input: <input type="text" name="appoint"><br>
    #           <input type="submit" value="Submit"><br>
    #       </form>'''
    # return x


@app.route('/bot',methods=['POST','GET'])
def getvalue():
    if request.method=='POST':
        return getfuncval()
    else:
        tempx="newvalue"
        return '''<form method="POST">
                  Bot: Hi!! Book an Appointment<br>
                  Input: <input type="text" name="appoint"><br>'''+'''<input type="submit" value="Submit"><br>
                  </form>'''



if __name__ == '__main__':
     app.run(port=5000)
