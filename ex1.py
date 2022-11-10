try:
    user_seconds = int(input('input seconds->'))
    all_seconds_per_day = 24 * 3600
    if all_seconds_per_day < user_seconds:
        raise Exception('All seconds per day is less then user seconds!')
    diff_seconds = all_seconds_per_day - user_seconds
    uh = int(user_seconds / 3600)
    um = int((user_seconds % 3600) / 60)
    us = int((user_seconds % 3600) % 60)
    print(f'{uh}:{um}:{us} user time')
    print('#>---------<MENU>---------<#')
    print('|  h - Seconds in hour     |')
    print('|  m - Seconds in minutes  |')
    print('|  s - Seconds             |')
    print('|  other key - full time   |')
    print('#>------------------------<#')
    action = input('action->')
    if action == 'h':
        print(f'Hours to midnight = {int(diff_seconds/3600)} h')
    elif action == 'm':
        print(f'Minutes to midnight = {int(diff_seconds/60)} m')
    elif action == 's':
        print(f'Seconds to midnight = {diff_seconds} s')
    else:
        h = int(diff_seconds/3600)
        m = int((diff_seconds % 3600) / 60)
        s = int((diff_seconds % 3600) % 60)
        print(f'{h}:{m}:{s} to midnight!')
except ValueError as vl_ex:
    print(f'Value error: {vl_ex}')
except Exception as ex:
    print(f'Error: {ex}')
    print(f'Name: {ex.__class__.__name__}')
        
 
