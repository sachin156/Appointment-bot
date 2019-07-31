from json import dumps
import datefinder
import pickle
from apiclient.discovery import build
import dateparser
from datetime import datetime,timedelta

credentials=pickle.load(open('token.pkl','rb'))
service=build("calendar","v3",credentials=credentials)
result=service.calendarList().list().execute()
calendar_id=result['items'][0]['id']
now = datetime.utcnow().isoformat() + 'Z'



# to get all the events scheduled till now
def get_events():
    events_result = service.events().list(calendarId=calendar_id, timeMin=now,
                                               maxResults=500, singleEvents=True,
                                               orderBy='startTime').execute()
    return events_result.get('items', [])


# to add an event(appointment based on slot available)
def create_event(new_event):
    if already_exists(new_event):
        return event_suggest()
    else:
        events_result = service.events().list(calendarId=calendar_id, timeMin=now,
                                                       maxResults=500, singleEvents=True,
                                                       orderBy='startTime').execute()
        events=events_result['items']
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

# Suggesting the user available slots for the appointent
def event_suggest():
    events_result = service.events().list(calendarId=calendar_id, timeMin=now,
                                               maxResults=500, singleEvents=True,
                                               orderBy='startTime').execute()
    events=events_result['items']
    eventsforappointment=[]
    suggested_times=[]
    for event in events:
        if event['summary'].lower()=='noappointment':
            eventsforappointment.append(event)
            x=(dateparser.parse(event['start']['dateTime']))
            x=x.strftime('%B%d-%H:%M')
            suggested_times.append(x)
    suggested_times=','.join(suggested_times)

    return "Pick from the suggested timings:" +'\n'+suggested_times

# update the event based on the input from the user
def update_event(newevent,event_id):
    event = service.events().get(calendarId=calendar_id,eventId=event_id).execute()
    event['summary']='Appointment'
    updated_event = service.events().update(calendarId=calendar_id, eventId=event['id'], body=event).execute()
    print(updated_event['updated'])
    return "Appointmet created,Thanks"

# check if the event exist before
def already_exists(new_event):
    events = get_date_events(new_event['start']['dateTime'],get_events())
    event_list = [new_event['summary'] for new_event in events]
    if new_event['summary'] not in event_list:
        return False
    else:
        return True

# get events based on the date and time
def get_date_events(date, events):
    lst = []
    i=0
    date = date+'+05:30'
    for event in events:
        i+=1
        if event.get('start').get('dateTime'):
            d1 = event['start']['dateTime']
            if d1 == date:
                lst.append(event)
    print(i)
    return lst


# for creating new event template to add in the google calendar
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


def getfuncval(text):
    event=new_eve(text)
    print(event)
    if event=="null":
        message="Sorry,I can book an appointment only if date and time are provided"
        return message
    else:
        return create_event(event)
