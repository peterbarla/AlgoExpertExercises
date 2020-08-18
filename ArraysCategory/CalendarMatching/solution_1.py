# O(c1 + c2) time | O(c1 + c2) space where c1 = calendar1 and c2 = calendar2 length
def calendarMatching(calendar1: list, bounds1: list, calendar2: list, bounds2: list, meeting_Duration: int)-> list:
    i = 0
    j = 0

    new_calendar1 = [['0:00', bounds1[0]]] + calendar1 + [[bounds1[1], '23:59']]
    new_calendar2 = [['0:00', bounds2[0]]] + calendar2 + [[bounds2[1], '23:59']]

    calendar = []
    last_appended_index = -1

    while i < len(new_calendar1) and j < len(new_calendar2):
        start1 = military_time_to_minutes(new_calendar1[i][0])
        start2 = military_time_to_minutes(new_calendar2[j][0])

        end1 = military_time_to_minutes(new_calendar1[i][1])
        end2 = military_time_to_minutes(new_calendar2[j][1])

        if len(calendar) != 0:
            last_end = military_time_to_minutes(calendar[last_appended_index][1])
        else: last_end = -10


        if start1 <= start2:
            if start1 < last_end and end1 > last_end:
                calendar[last_appended_index][1] = minutes_to_military_time(end1)
                i += 1
                continue
            elif start1 < last_end and end1 < last_end:
                i += 1
                continue
            new_start = start1
            if end1 < start2:
                new_end = end1
                calendar.append([minutes_to_military_time(new_start), minutes_to_military_time(new_end)])
                last_appended_index += 1
                i += 1
            else:
                new_end = max(end1, end2)
                calendar.append([minutes_to_military_time(new_start), minutes_to_military_time(new_end)])
                last_appended_index += 1
                i += 1
                j += 1
        else:
            if start2 < last_end and end2 > last_end:
                calendar[last_appended_index][1] = minutes_to_military_time(end2)
                j += 1
                continue
            elif start2 < last_end and end2 < last_end:
                j += 1
                continue
            new_start = start2
            if end2 < start1:
                new_end = end2
                calendar.append([minutes_to_military_time(new_start), minutes_to_military_time(new_end)])
                last_appended_index += 1
                j += 1
            else:
                new_end = max(end1, end2)
                calendar.append([minutes_to_military_time(new_start), minutes_to_military_time(new_end)])
                last_appended_index += 1
                i += 1
                j += 1

    for index in range(i, len(new_calendar1)):
        calendar.append(new_calendar1[index])
    for index in range(j, len(new_calendar2)):
        calendar.append(new_calendar2[index])

    result = []
    for i in range(len(calendar) - 1):
        if military_time_to_minutes(calendar[i + 1][0]) - military_time_to_minutes(calendar[i][1]) >= meeting_Duration:
            result.append([calendar[i][1], calendar[i + 1][0]])

    return result

def military_time_to_minutes(time: str)-> int:
    hour, minute = time.split(':')
    return int(hour) * 60 + int(minute)
def minutes_to_military_time(minutes: int)-> str:
    hour = int(minutes / 60)
    minute = minutes % 60
    string_min = str(minute)
    if str(minute) == '0':
        string_min = '00'

    return str(hour) + ':' + string_min

calendar1 = [
    ["10:00", "10:30"],
    ["10:45", "11:15"],
    ["11:30", "13:00"],
    ["14:15", "16:00"],
    ["16:00", "18:00"]
  ]

calendar2 = [["10:00", "11:00"], ["10:30", "16:30"]]
bounds1 = ["9:30", "20:00"]

bounds2 = ["9:00", "22:30"]
meeting_Duration = 60

print(calendarMatching(calendar1, bounds1, calendar2, bounds2, meeting_Duration))