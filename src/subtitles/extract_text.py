from pysubparser import parser

subtitles = parser.parse('./files/space-jam.srt')

for subtitle in subtitles:
    print(subtitle)
