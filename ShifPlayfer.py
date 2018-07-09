def shif(text,key):
	text=list(text)
	for i in range(len(text)):
		if i != 0:
			if text[i]==text[i-1]:
				text.insert(i,"Х")
	if len(text)%2 !=0:
	    text.append("Х")
	for i in range(len(text)):
	    if text[i] == "Ъ":
	        text[i] = "Ь"
	mas = []; k = ""
	for i in text:
	    k += i
	    if len(k) == 2:
	        mas.append(k)
	        k = ""
	print(mas)
	demas = ""
	switch = 0
	for i in range(len(mas)):
	    for k in range(2):
	        for x in range(len(key)):
	            for y in range(len(key[x])):
	                    if key[x][y] == mas[i][k]:
	                        if mas[i][0] in key[x] and mas[i][1] in key[x]:
	                            if (key[x][y] != key[x][-1]):
	                                demas+=key[x][y+1]
	                            else:
	                                demas += key[x][y-5]
	                        else:
	                            for a in range(len(key)):
	                                for b in range(len(key[a])):
	                                    if key[a][b] == mas[i][0]:
	                                        y0 = b
	                                    if key[a][b] == mas[i][1]:
	                                        y1 = b
	                            if y0 == y1:
	                                if (key[x][y] != key[-1][y]):
	                                    demas += key[x + 1][y]
	                                else:
	                                    demas += key[x - 4][y]
	                            else:
	                                if switch == 0:
	                                    demas += key[x][y1]
	                                    switch = 1
	                                else:
	                                    demas += key[x][y0]
	                                    switch = 0
	print("Закодированное сообщение: %s" %demas)
	text=demas
	return text
def deshif(text,key):
	text=list(text)
	for i in range(len(text)):
	    if text[i] == "Ъ":
	        text[i] = "Ь"
	mas = []; k = ""
	for i in text:
	    k += i
	    if len(k) == 2:
	        mas.append(k)
	        k = ""
	print(mas)
	demas = []
	switch = 0
	for i in range(len(mas)):
	    for k in range(2):
	        for x in range(len(key)):
	            for y in range(len(key[x])):
	                    if key[x][y] == mas[i][k]:
	                        if mas[i][0] in key[x] and mas[i][1] in key[x]:
	                            if (key[x][y] != key[x][0]):
	                                demas+=key[x][y-1]
	                            else:
	                                demas += key[x][y+5]
	                        else:
	                            for a in range(len(key)):
	                                for b in range(len(key[a])):
	                                    if key[a][b] == mas[i][0]:
	                                        y0 = b
	                                    if key[a][b] == mas[i][1]:
	                                        y1 = b
	                            if y0 == y1:
	                                if (key[x][y] != key[0][y]):
	                                    demas += key[x - 1][y]
	                                else:
	                                    demas += key[x + 4][y]
	                            else:
	                                if switch == 0:
	                                    demas += key[x][y1]
	                                    switch = 1
	                                else:
	                                    demas += key[x][y0]
	                                    switch = 0
	for i in range(len(demas)-1):
		if demas[i] == "Х":
			if demas[i] != demas[-1]:
				if demas[i-1] == demas[i+1]:
					demas.remove(demas[i])
			else:
				demas.remove(demas[i])
	print("Декодированное сообщение:","" .join(demas))
	text=demas
	return text

text="НПВЪЗПЖИКЛБЦРПЪПЭИЯЩЛИЗПБКФАГПШУХЭЧЖРЫВЦТУНЧТЩЧНХНЩТНЯХКДНЦВЗТЧИ"
key=[
    ['Ф','И','Л','Ь','М','А'],
    ['Б','В','Г','Д','Е','Ж'],
    ['З','К','Н','О','П','Р'],
    ['С','Т','У','Х','Ц','Ч'],
    ['Ш','Щ','Ы','Э','Ю','Я']
]
text=deshif(text,key)
text=shif(text,key)





