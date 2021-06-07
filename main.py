from datetime import datetime, date, time


#  Database definition
database = [
  {'name': 'Jack', 
   'test': 'Привет!', 
   'time': '2021-06-07 21:00:00'}, 
  {'name': 'Mary', 
   'test': 'Привет, Jack', 
   'time': '2021-06-07 21:00:01'},
]



def send_message(name, text):
  # make message
  date_time_now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
  message = {
    'name': name, 
    'test': text, 
    'time': date_time_now}
  # put message in db
  database.append(message)

send_message('admin', 'Я щас вас заблочу')

# def get_messages(filter):
  # choose from db messages
  # return messmeanges
