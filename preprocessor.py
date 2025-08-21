import pandas as pd
import re
from datetime import datetime

def preprocess(data):
    # Step 1: Clean invisible Unicode characters
    def clean_unicode(text):
        return re.sub(r'[\u202f\u200e\u200b]', '', text)

    data = clean_unicode(data)

    # Step 2: Pattern to extract [date, time] and message content
    pattern = r"\[(\d{2}/\d{2}/\d{2}),\s(\d{1,2}:\d{2}:\d{2})\s?(AM|PM)\]\s(.*)"

    # Split data into lines
    lines = data.split("\n")

    messages = []
    dates = []

    for line in lines:
        match = re.match(pattern, line)
        if match:
            date = match.group(1)
            time = match.group(2)
            ampm = match.group(3)
            message = match.group(4).strip()
            datetime_obj = datetime.strptime(f"{date} {time} {ampm}", "%d/%m/%y %I:%M:%S %p")
            dates.append(datetime_obj)
            messages.append(message)
        elif messages:  # it's a continuation of the previous message
            messages[-1] += "\n" + line.strip()

    # Step 3: Create DataFrame
    df = pd.DataFrame({'user_message': messages, 'date': dates})

    # Step 4: Separate users from messages
    users = []
    content = []
    for msg in df['user_message']:
        entry = re.split(r'([\w~\s]+?):\s', msg, maxsplit=1)
        if len(entry) == 3:
            users.append(entry[1])
            content.append(entry[2])
        else:
            users.append("group_notification")
            content.append(entry[0])

    df['user'] = users
    df['message'] = content
    df.drop(columns=['user_message'], inplace=True)

    # Step 5: Extract temporal features
    df['only_date'] = df['date'].dt.date
    df['year'] = df['date'].dt.year
    df['month_num'] = df['date'].dt.month
    df['month'] = df['date'].dt.month_name()
    df['day'] = df['date'].dt.day
    df['day_name'] = df['date'].dt.day_name()
    df['hour'] = df['date'].dt.hour
    df['minute'] = df['date'].dt.minute

    # Step 6: Create time period buckets
    period = []
    for hour in df['hour']:
        if hour == 23:
            period.append("23-00")
        elif hour == 0:
            period.append("00-01")
        else:
            period.append(f"{hour:02}-{hour+1:02}")
    df['period'] = period

    return df
