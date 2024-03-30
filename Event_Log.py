def get_event_date(event):
  return event.date

def current_users(events):
  events.sort(key=get_event_date)
  machines = {}
  for event in events:
    if event.machine not in machines:
      machines[event.machine] = set()
    if event.type == "login":
      machines[event.machine].add(event.user)
    elif event.type == "logout" and event.user in machines[event.machine]:
      machines[event.machine].remove(event.user)
  return machines

def generate_report(machines):
  for machine, users in machines.items():
    if len(users) > 0:
      user_list = ", ".join(users)
      print("{}: {}".format(machine, user_list))


class Event:
  def __init__(self, event_date, event_type, machine_name, user):
    self.date = event_date
    self.type = event_type
    self.machine = machine_name
    self.user = user



# Create instances of Event class
event1 = Event("2023-01-01", "login", "Machine1", "User1")
event2 = Event("2023-01-01", "login", "Machine2", "User2")
event3 = Event("2023-01-01", "logout", "Machine1", "User1")
event4 = Event("2023-01-01", "logout", "Machine2", "User2")

# Call functions
events = [event1, event2, event3, event4]
machines = current_users(events)
generate_report(machines)
