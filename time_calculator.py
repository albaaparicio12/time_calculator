def add_time(start, duration, day=""):
    tardeODia = start.split(' ')[1]
    duration = duration.split(':')
    start = start.split(' ')[0].split(':')

    daysLater = 0
    hours = int(start[0])
    minutes = int(duration[1]) + int(start[1])
    if (minutes >= 60):
        minutes -= 60
        hours += 1
    hours += int(duration[0])
    while (hours > 12):
        tardeODia = contrario(tardeODia)
        hours -= 12
        if (tardeODia == 'AM'):
            daysLater += 1
    if (hours > 11):
        tardeODia = contrario(tardeODia)
        if (tardeODia == 'AM'):
            daysLater += 1
    if (minutes < 10):
        minutes = "0" + str(minutes)
    new_time = str(hours) + ":" + str(minutes) + " " + tardeODia
    if (day != ""):
        week = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        day = day.capitalize()
        new_time += ", " + getDay(week, daysLater, day)
    if (daysLater == 1):
        new_time += " (next day)"
    elif (daysLater > 1):
        new_time += " (" + str(daysLater) + " days later)"

    return new_time


def contrario(AMoPM):
    if (AMoPM == 'AM'):
        return 'PM'
    else:
        return 'AM'

def getDay(week, daysLater, day):
    position = week.index(day)
    daysLater += position
    while (daysLater >= len(week)):
        daysLater -= len(week)
    return week[daysLater]
