def add_time(start, duration, week_day_start = ''):
    
    #Create days of the week list
    week = {0: 'Sunday',
            1: 'Monday', 
            2: 'Tuesday', 
            3: 'Wednesday',
            4: 'Thursday',
            5: 'Friday', 
            6: 'Saturday'}
    
    week_lower = {'sunday': 0,
            'monday': 1, 
            'tuesday': 2, 
            'wednesday': 3,
            'thursday': 4,
            'friday': 5, 
            'saturday': 6}    
    

    #Normalize capitalization for starting weekday
    if week_day_start != '':
        week_index = week_lower[(week_day_start.lower())]

    
    #Variables for hour, minute, and AM/PM of the start time
    initial_time = start.split(' ')[0]
    am_pm = start.split(' ')[1]
    initial_hour = int(initial_time.split(':')[0])
    initial_minute = int(initial_time.split(':')[1])

    #Variables for hour, minute, and AM/PM of the duration time
    duration_time = duration.split(':')
    duration_hour = int(duration_time[0])
    duration_minute = int(duration_time[1])

    #Calculate new hour    
    new_hour = initial_hour + duration_hour
    day_count = 0
    if new_hour >= 24:
        while new_hour >= 24:
            new_hour = (new_hour - 24)
            day_count += 1
    
    #Calculate new minute
    new_minute = initial_minute + duration_minute

    if new_minute >= 60:
        new_minute = (new_minute - 60)
        new_hour += 1
    
    #Define am_pm:
    if new_hour >= 12:
        while new_hour >= 12:
            new_hour = (new_hour - 12)
            if am_pm == 'AM':
                am_pm = 'PM'
            elif am_pm == 'PM':
                am_pm = 'AM'
                day_count += 1

    #Normalize when new_hour = 0
    if new_hour == 0:
        new_hour += 12

    #Get new weekday
    if week_day_start != '':
        week_index += day_count
        while week_index >= 7:
            week_index -= 7
        
        new_weekday = week[week_index]

    #Get and concatenate new time
    #Append ZERO to single digit minutes
    #Add day count
    new_time = ''
    
    #If no initial day of the week
    if week_day_start == '':
        if day_count == 0:
            if new_minute < 10:
                new_time = f'{new_hour}:0{new_minute} {am_pm}' 
            
            else:
                new_time = f'{new_hour}:{new_minute} {am_pm}'
    
        elif day_count == 1:
            if new_minute < 10:
                new_time = f'{new_hour}:0{new_minute} {am_pm} (next day)' 
            
            else:
                new_time = f'{new_hour}:{new_minute} {am_pm} (next day)'

        elif day_count > 1:
            if new_minute < 10:
                new_time = f'{new_hour}:0{new_minute} {am_pm} ({day_count} days later)' 
            
            else:
                new_time = f'{new_hour}:{new_minute} {am_pm} ({day_count} days later)'
    
    #If initial day of the week is given
    else:
        if day_count == 0:
            if new_minute < 10:
                new_time = f'{new_hour}:0{new_minute} {am_pm}, {new_weekday}' 
            
            else:
                new_time = f'{new_hour}:{new_minute} {am_pm}, {new_weekday}'
    
        elif day_count == 1:
            if new_minute < 10:
                new_time = f'{new_hour}:0{new_minute} {am_pm}, {new_weekday} (next day)' 
            
            else:
                new_time = f'{new_hour}:{new_minute} {am_pm}, {new_weekday} (next day)'

        elif day_count > 1:
            if new_minute < 10:
                new_time = f'{new_hour}:0{new_minute} {am_pm}, {new_weekday} ({day_count} days later)' 
            
            else:
                new_time = f'{new_hour}:{new_minute} {am_pm}, {new_weekday} ({day_count} days later)'            


    print(new_time)
    return new_time

add_time('3:30 PM', '2:12')
