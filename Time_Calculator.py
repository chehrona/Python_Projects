weekdaysListResult = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday","Sunday"]
weekdaysListLower = [x.lower() for x in weekdaysListResult]

def add_time(usTime, duration, weekday = None):
    usTimesSplit = usTime.split()
    usTimeToList = usTimesSplit[0].split(":")
    usTimeHourInt = int(usTimeToList[0])
    usTimeMinutesInt = int(usTimeToList[1])
    usTimeLetters = usTimesSplit[1]
    if weekday != None:
        weekday = str.lower(weekday)

    durationSplit = duration.split(":")

    durationHourInt = int(durationSplit[0])
    durationMinutesInt = int(durationSplit[1])

    # Convert to 24 hours
    if usTimeLetters == "PM":
        usTimeHourInt = usTimeHourInt + 12


    addedHoursInt = durationHourInt + usTimeHourInt
    addedMinutes = usTimeMinutesInt + durationMinutesInt

    # divisibleByTwelve = (addedHoursInt/12)%2
    extraHoursFromMinutes = int(addedMinutes/60)
    remainingMinutes = int(addedMinutes%60)
    # Get remaining hours from min
    newHours = addedHoursInt + extraHoursFromMinutes

    newDays = int(newHours/24)
    remainingHours = int(newHours%24)

    newUsTimeLetters = ""
    # print(newDays)
    if remainingHours == 12 and usTimeLetters == "AM":
        newUsTimeLetters = "PM"

    # PM
    elif remainingHours > 12:
        remainingHours = abs(remainingHours - 12)
        newUsTimeLetters = "PM"
    # AM
    elif remainingHours == 0:
        remainingHours = remainingHours + 12
        newUsTimeLetters = "AM"
    else:
        newUsTimeLetters = "AM"
    new_time = ""
    if weekday == None:
        if newDays == 1:
            new_time = str(remainingHours) + ":" + str(remainingMinutes).zfill(2) + " " + newUsTimeLetters + " (next day)"
        elif newDays > 1:
            new_time = str(remainingHours) + ":" + str(remainingMinutes).zfill(2) + " " + newUsTimeLetters + " (" + str(newDays) + " days later)"
        else:
            new_time = str(remainingHours) + ":" + str(remainingMinutes).zfill(2) + " " + newUsTimeLetters
    else:
        weekdayIndex = (weekdaysListLower.index(weekday) + newDays%7)%7
        newWeekday = weekdaysListResult[weekdayIndex]
        if newDays == 1:
            new_time = str(remainingHours) + ":" + str(remainingMinutes).zfill(2) + " " + newUsTimeLetters + ", " + newWeekday + " (next day)"
        elif newDays > 1:
            new_time = str(remainingHours) + ":" + str(remainingMinutes).zfill(2) + " " + newUsTimeLetters + ", " + newWeekday + " (" + str(newDays) + " days later)"
        else:
            new_time = str(remainingHours) + ":" + str(remainingMinutes).zfill(2) + " " + newUsTimeLetters + ", " + newWeekday
    return new_time
print(add_time("11:06 PM", "2:02"))
