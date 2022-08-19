WEEKDAY = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# MAIN
def add_time(start, add, weekday=""):
    start = start.split(" ")

    # [hours, minutes]
    time1 = start[0].split(":")
    time2 = add.split(":")

    # AM / PM
    meri = start[1]
    
    # [days, hours, minutes]
    timestamp = []
    timestamp.append(0)
    timestamp.append(int(time1[0]) + int(time2[0]) + (12 if meri == "PM" else 0))
    timestamp.append(int(time1[1]) + int(time2[1]))

    timestamp[1] += int(timestamp[2] / 60)
    timestamp[2] = timestamp[2] % 60

    timestamp[0] += int(timestamp[1] / 24)
    timestamp[1] = timestamp[1] % 24

    # Weekday 0-6
    if weekday != "":
        weekday = WEEKDAY.index(weekday.capitalize()) # Saturday = 5
        weekday += timestamp[0] # 5 + 11 = 16
        weekday %= 7 # 2

    # [hours, minutes]
    result = []
    result.append(timestamp[1])
    result.append(timestamp[2])

    # 0:00 -> 12:00 AM
    # 13:00 -> 1:00 PM
    # 12:00 -> 0:00 -> 12:00 PM
    meri = "AM"
    if result[0] >= 12:
        meri = "PM"
        result[0] -= 12

    if result[0] == 0:
        result[0] = 12

    # minutes = 1
    # format = 01
    result = "{}:{:02d}".format(result[0], result[1])
    result += " " + meri

    if weekday != "":
        result += ", " + WEEKDAY[weekday]

    if timestamp[0] == 1:
        result += " (next day)"
    elif timestamp[0] > 1:
        result += " ({} days later)".format(timestamp[0])
    return result

# TEST
print(add_time("3:00 PM", "3:10"))
print()
print(add_time("11:30 AM", "2:32", "Monday"))
print()
print(add_time("11:43 AM", "00:20"))
print()
print(add_time("10:10 PM", "3:30"))
print()
print(add_time("11:43 PM", "24:20", "tueSday"))
print()
print(add_time("6:30 PM", "205:12"))
