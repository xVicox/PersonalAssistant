import os
import requests

from alarm_clock import PAAlarmClock
from pa_translator import PATranslator
from api_handler import APIHandler

translator = PATranslator()
handler = APIHandler()

subtitle_path = "D:/Filmovi i Serije/Crtani/Ilya Murometc/Ilya Muromets i Solovey Razboynik.txt"
text = "Great first attempt! Your read_file method is already functional and well-structured. It includes both reading the file and basic error handling, which is excellent. Here’s a breakdown of what you’ve done:"
mp3_file = "D:/Download/SoulSeek/complete/chibiotaku/driving_backup/knight rider - theme song.mp3"
#Read the file
#subtitle_raw = translator.read_file(subtitle_path)
# Get rid of new lines and timestamps -->
#subtitle = translator.extract_text_lines(subtitle_raw)

#chunks = translator.group_lines_into_chunks(subtitle)

#alarm_clock = PAAlarmClock()
#alarm_clock.set_time(mp3_file)



the_file = translator.read_file(subtitle_path)
extracted_subs = translator.extract_text_lines(the_file)
chunks = translator.group_lines_into_chunks(extracted_subs)
request_body = translator.prepare_request_body(chunks)

response = handler.translate_text(request_body,"sr","en")

print(response)







if __name__ == "__main__":
    print("Start")







