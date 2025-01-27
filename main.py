import os
import requests
import base64

from alarm_clock import PAAlarmClock
from pa_translator import PATranslator
from transformers import MarianMTModel, MarianTokenizer

translator = PATranslator("en", "de")

subtitle_path = "D:/Filmovi i Serije/Crtani/Ilya Murometc/Ilya Muromets i Solovey Razboynik.txt"
mp3_file = "D:/Download/SoulSeek/complete/chibiotaku/driving_backup/knight rider - theme song.mp3"
#Read the file
#subtitle_raw = translator.read_file(subtitle_path)
# Get rid of new lines and timestamps -->
#subtitle = translator.extract_text_lines(subtitle_raw)

#chunks = translator.group_lines_into_chunks(subtitle)

#alarm_clock = PAAlarmClock()
#alarm_clock.set_time(mp3_file)


output_file = "D:/Filmovi i Serije/Crtani/Ilya Murometc/ILJA TRANSLATION.srt"

the_file = translator.read_file(subtitle_path)

clear_subs = translator.process_subtitles(the_file)
chunks = translator.create_chunks(clear_subs)
translated_chunks = translator.translate_chunks(chunks, "en", "sr")
reassembled_subs = translator.reassemble_subs(translated_chunks)
translator.write_to_file(reassembled_subs, output_file)


























if __name__ == "__main__":
    print("Start")
