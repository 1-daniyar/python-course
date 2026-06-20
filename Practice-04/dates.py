# dates.py
# Working with dates and time

from datetime import datetime, date, timedelta, timezone

# ---------- CURRENT DATE AND TIME ----------
now = datetime.now()
print("Now:", now)
print("Year:", now.year, "Month:", now.month, "Day:", now.day)
print("Weekday name:", now.strftime("%A"))


# ---------- CREATING DATE OBJECTS ----------
# Specify year, month, day (and optionally time)
birthday = datetime(2004, 5, 15)
print("Birthday:", birthday)

just_date = date(2026, 1, 1)
print("New Year:", just_date)


# ---------- DATE FORMATTING (strftime) ----------
# Turn a datetime into a formatted string
formatted = now.strftime("%d/%m/%Y %H:%M:%S")
print("Formatted:", formatted)

# Common codes: %Y year, %m month, %d day, %H hour, %M minute, %A weekday
print("Readable:", now.strftime("%A, %d %B %Y"))


# ---------- PARSING A STRING INTO A DATE (strptime) ----------
text = "2026-03-21 14:30"
parsed = datetime.strptime(text, "%Y-%m-%d %H:%M")
print("Parsed from string:", parsed)


# ---------- CALCULATING TIME DIFFERENCES ----------
# Subtracting two dates gives a timedelta
start = datetime(2026, 1, 1)
end = datetime(2026, 12, 31)
difference = end - start
print("Days between:", difference.days)

# Adding/subtracting time with timedelta
in_ten_days = now + timedelta(days=10)
print("In 10 days:", in_ten_days.strftime("%d/%m/%Y"))

week_ago = now - timedelta(weeks=1)
print("A week ago:", week_ago.strftime("%d/%m/%Y"))


# ---------- WORKING WITH TIMEZONES ----------
# A timezone-aware datetime in UTC
utc_now = datetime.now(timezone.utc)
print("UTC now:", utc_now)

# Create a custom timezone (Kazakhstan is UTC+5)
kz_time = timezone(timedelta(hours=5))
kz_now = datetime.now(kz_time)
print("Kazakhstan time (UTC+5):", kz_now.strftime("%d/%m/%Y %H:%M"))
