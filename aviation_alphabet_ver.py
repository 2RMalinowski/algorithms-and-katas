"""
The International Civil Aviation Organization (ICAO) alphabet assigns code words to the letters of the
English alphabet acrophonically (Alfa for A, Bravo for B, etc.) so that critical combinations of letters
(and numbers) can be pronounced and understood by those who transmit and receive voice messages by radio
or telephone regardless of their native language. Especially useful when the safety of navigation
or persons is essential. Here is a Python dictionary covering one version of the ICAO alphabet:

d = {'a':'alfa', 'b':'bravo', 'c':'charlie', 'd':'delta', 'e':'echo', 'f':'foxtrot',
    'g':'golf', 'h':'hotel', 'i':'india', 'j':'juliett', 'k':'kilo', 'l':'lima',
    'm':'mike', 'n':'november', 'o':'oscar', 'p':'papa', 'q':'quebec', 'r':'romeo',
    's':'sierra', 't':'tango', 'u':'uniform', 'v':'victor', 'w':'whiskey',
    'x':'x-ray', 'y':'yankee', 'z':'zulu'}

Your task in this exercise is to write a procedure speak_ICAO() able to translate any text
(i.e. any string) into spoken ICAO words.

You need to import at least two libraries: os and time:
- On a Mac, you have access to the system TTS (Text-To-Speech) as follows: os.system('say ' + msg),
where msg is the string to be spoken.
- Under UNIX/Linux and Windows, something similar might exist.

Apart from the text to be spoken, your procedure also needs to accept two additional parameters:
a float indicating the length of the pause between each spoken ICAO word, and a float indicating
the length of the pause between each word spoken.
"""
import os
import time


def speak_ICAO(sentence, pause_between_word, pause_between_ICAO):
    d = {'a': 'alfa', 'b': 'bravo', 'c': 'charlie', 'd': 'delta', 'e': 'echo', 'f': 'foxtrot',
         'g': 'golf', 'h': 'hotel', 'i': 'india', 'j': 'juliett', 'k': 'kilo', 'l': 'lima',
         'm': 'mike', 'n': 'november', 'o': 'oscar', 'p': 'papa', 'q': 'quebec', 'r': 'romeo',
         's': 'sierra', 't': 'tango', 'u': 'uniform', 'v': 'victor', 'w': 'whiskey',
         'x': 'x-ray', 'y': 'yankee', 'z': 'zulu'}
    words_list = sentence.split()
    for word in words_list:
        os.system(f"'spd-say' '{word}'")
        time.sleep(pause_between_word)
    for letter in sentence.lower().replace(' ', ''):
        icao_word = d[letter]
        os.system(f"'spd-say' '{icao_word}'")
        time.sleep(pause_between_ICAO)


speak_ICAO('The quick brown fox jumped over the lazy dog', 0.7, 0.6)
# speak_ICAO("I m sorry Dave I m afraid I cant do that", 0.7, 0.6)
