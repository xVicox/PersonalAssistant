import os
import datetime
from time import sleep
import pygame


class PAAlarmClock:

    def __init__(self):
        pygame.mixer.init()

    @staticmethod
    def set_time(file_path):
        try:
            if not PAAlarmClock.check_file_path(file_path):
                raise ValueError

            alarm_time = input("Set alarm ('HH:MM'): ")
            alarm_time = PAAlarmClock.validate_time_format(alarm_time).strftime("%H:%M:%S")

            is_running = True
            while is_running:
                current_time = datetime.datetime.now().time().strftime("%H:%M:%S")
                print(current_time)
                sleep(1)
                if current_time == alarm_time:
                    is_running = False

            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play()
            input("Press any key if you want to stop the alarm: ")
            if pygame.KEYDOWN:
                pygame.mixer.music.stop()
        except ValueError:
            print("Error")

    @staticmethod
    def validate_time_format(alarm_time):
        alarm_time = alarm_time.strip()
        try:
            if not len(alarm_time) == 5 or not alarm_time[2]== ":":
                raise ValueError
            hours = int(alarm_time[0:2])
            minutes = int(alarm_time[3:5])
            if hours < 0 or hours > 23 or minutes < 0 or minutes > 59:
                raise ValueError
            return datetime.time(hours, minutes)
        except ValueError:
            print("Invalid time format. Expected format is 24h format - HH:MM")
            return False

    @staticmethod
    def check_file_path(path):
        # check extension
        if not (path.endswith(".mp3") or  path.endswith(".wav") or  path.endswith(".ogg")):
            print("Unsupported file extension. Only mp3, wav and ogg files are allowed")
            return False
        # check if file exists
        elif not os.path.exists(path) or not os.path.isfile(path):
            print("File not found.")
            return False
        # all checks passed, file is found and valid
        else:
            return True


