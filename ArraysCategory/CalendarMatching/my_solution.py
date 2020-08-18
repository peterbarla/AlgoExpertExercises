# not passing 1 test...:))))
def calendarMatching(calendar1: list, bounds1: list, calendar2: list, bounds2: list, meeting_Duration: int)-> list:
    calendar = []
    i = 0
    j = 0
    last_appended_index = -1
    while i < len(calendar1) and j < len(calendar2):
        print(calendar)
        if len(calendar) == 0:
            start_time = minutes_to_military_time(min(military_time_to_minutes(calendar1[i][0]), military_time_to_minutes(calendar2[j][0])))
            end_time = minutes_to_military_time(max(military_time_to_minutes(calendar1[i][1]), military_time_to_minutes(calendar2[j][1])))
            if military_time_to_minutes(calendar1[0][1]) >= military_time_to_minutes(calendar2[0][0]):
                calendar.append([start_time, end_time])
                last_appended_index += 1
            else:
                calendar.append(calendar1[i])
                calendar.append(calendar2[j])
                last_appended_index += 2
            i += 1
            j += 1
        else:
            start1 = military_time_to_minutes(calendar1[i][0])
            end1 = military_time_to_minutes(calendar1[i][1])
            start2 = military_time_to_minutes(calendar2[j][0])
            end2 = military_time_to_minutes(calendar2[j][1])

            prev_end = military_time_to_minutes(calendar[last_appended_index][1])
            prev_start = military_time_to_minutes(calendar[last_appended_index][0])

            index_for_check = -1

            if start1 <= start2: index_for_check = 0
            else: index_for_check = 1

            changed = False

            if index_for_check == 0:
                if start1 <= prev_end:
                    if start1 < prev_start:
                        calendar[last_appended_index][0] = minutes_to_military_time(start1)
                    if end1 >= start2:
                        calendar[last_appended_index][1] = minutes_to_military_time(max(end1, end2))
                    elif end1 >= prev_end:
                        calendar[last_appended_index][1] = minutes_to_military_time(end1)
                        calendar.append(calendar2[j])
                        last_appended_index += 1
                    else: 
                        #calendar[last_appended_index][1] = minutes_to_military_time(end1)
                        calendar.append(calendar2[j])
                        last_appended_index += 1
                    changed = True
            else:
                if start2 <= prev_end:
                    if start2 < prev_start:
                        calendar[last_appended_index][0] = minutes_to_military_time(start2)
                    if end2 >= start1:
                        calendar[last_appended_index][1] = minutes_to_military_time(max(end1, end2))
                    elif end2 >= prev_end:
                        calendar[last_appended_index][1] = minutes_to_military_time(end2)
                        calendar.append(calendar1[i])
                        last_appended_index += 1
                    else: 
                        #calendar[last_appended_index][1] = minutes_to_military_time(end2)
                        calendar.append(calendar1[i])
                        last_appended_index += 1
                    changed = True

            if not changed:
                start_time = minutes_to_military_time(min(military_time_to_minutes(calendar1[i][0]), military_time_to_minutes(calendar2[j][0])))
                end_time = minutes_to_military_time(max(military_time_to_minutes(calendar1[i][1]), military_time_to_minutes(calendar2[j][1])))
                calendar.append([start_time, end_time])
                last_appended_index += 1

            i += 1
            j += 1

    for index in range(i, len(calendar1)):
        if military_time_to_minutes(calendar[last_appended_index][1]) >= military_time_to_minutes(calendar1[index][1]):
            continue
        calendar.append(calendar1[index])
    for index in range(j, len(calendar2)):
        if military_time_to_minutes(calendar[last_appended_index][1]) >= military_time_to_minutes(calendar2[index][1]):
            continue
        calendar.append(calendar2[index])

    if len(calendar1) != 0 and len(calendar2) != 0:
        free_start = minutes_to_military_time(max(military_time_to_minutes(bounds1[0]), military_time_to_minutes(bounds2[0])))
        free_end = minutes_to_military_time(min(military_time_to_minutes(bounds1[1]), military_time_to_minutes(bounds2[1])))
        free_bounds = [free_start, free_end]

        free_intervalls = []
        if military_time_to_minutes(calendar[0][0]) - military_time_to_minutes(free_bounds[0]) >= meeting_Duration:
            free_intervalls.append([free_bounds[0], calendar[0][0]])

        for i in range(len(calendar) - 1):
            if military_time_to_minutes(calendar[i + 1][0]) - military_time_to_minutes(calendar[i][1]) >= meeting_Duration:
                free_intervalls.append([calendar[i][1], calendar[i + 1][0]])

        if military_time_to_minutes(free_bounds[1]) - military_time_to_minutes(calendar[len(calendar) - 1][1]) >= meeting_Duration:
            free_intervalls.append([calendar[len(calendar) - 1][1], free_bounds[1]])

    else:
        return [[minutes_to_military_time(max(military_time_to_minutes(bounds1[0]), military_time_to_minutes(bounds2[0]))), minutes_to_military_time(min(military_time_to_minutes(bounds1[1]), military_time_to_minutes(bounds2[1])))]]


    return free_intervalls
    

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

calendar2 = [
    ["9:00", "10:00"],["11:15", "11:30"],["11:45", "17:00"],["17:30", "19:00"],["20:00", "22:15"]
  ]
calendar1 = [
    ["7:00", "7:45"],["8:15", "8:30"],["9:00", "10:30"],["12:00", "14:00"],["14:00", "15:00"],["15:15", "15:30"],["16:30", "18:30"],["20:00", "21:00"]
  ]
bounds1 = ["6:30", "22:00"]

bounds2 = ["8:00", "22:30"]
meeting_Duration = 30

print(calendarMatching(calendar1, bounds1, calendar2, bounds2, meeting_Duration))
#print(military_time_to_minutes("10:30"))