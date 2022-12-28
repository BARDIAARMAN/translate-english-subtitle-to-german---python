import os
from googletrans import Translator

filepath = "E:\programing\small projects\python\subtitle"
filename1 = "Wrecker.2015.720p.BluRay.x264-REGARDS.srt"
filename2 = "Wrecker.2015.720p.BluRay.x264-REGARDS.txt"


nums = ['0','1','2','3','4','5','6','7','8','9',':',',','-','>','.','?','\'']
tarjome = Translator()

with open(os.path.join(filepath,filename1)) as f:
    sub_line = f.readlines()
 
with open(os.path.join(filepath,filename2), 'w' ,encoding="utf-8") as f:  
    for line_en in sub_line:
        if line_en[0] in nums:
            f.write(line_en)
        elif line_en=='\n':
            f.write('\n')
        else:
            if line_en:
                line_de = tarjome.translate(line_en ,src='en' ,dest='de')
                f.write(line_de.text)


        

