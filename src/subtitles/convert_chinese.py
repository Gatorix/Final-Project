import opencc

converter = opencc.OpenCC('s2t.json')
s = converter.convert('汉字')  # 漢字

print(s)
