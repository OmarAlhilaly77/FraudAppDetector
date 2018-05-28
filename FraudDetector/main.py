import requests
from bs4 import BeautifulSoup

url = ""
r = requests.get(url)

soup = BeautifulSoup(r.content, "html5lib")
str_soup = str(soup)
newtext = str_soup.splitlines()
file  = open("file.txt", "w",encoding="utf-8")
for i in range (1,len(newtext)):
    seperating = newtext[i]
    seperating = seperating.split("\"")
    if len(seperating) == 3:
        part = seperating[0]
        seperatingtwo = part.split(",")
        if len(seperatingtwo) == 4 :
            if seperatingtwo[2] == "null":
                new = seperating[1]
                new = str(new)
                if new[0] == '/' or new[0] == 'h' and new[1] == 't'or new[0:2]=="CB":
                    continue
                else :
                    file.writelines("\n")
                    file.writelines(seperating[1])          
file.close()
file  = open("file.txt", "r")
file1  = open("negative.txt", "r")
file2  = open("positive.txt", "r")
Data = file.readlines()
negative = file1.readlines()
positive = file2.readlines()
Negativecount = 0
positivecount = 0
newp = ''.join(positive)
newp = newp.splitlines()
newn = ''.join(negative)
newn = newn.splitlines()
for i in range (1,len(Data)):
    parts = Data[i]
    parts = parts.split(" ")
    for k in range (1,len(parts)):
        for d in range (1,len(newp)):
            if ( newp[d] == parts[k]):
                    positivecount = positivecount + 1
                    break;
        for j in range (1,len(newn)):
            if (parts[k] ==  newn[j]):
                Negativecount = Negativecount + 1
rate = Negativecount + positivecount
rateneg = (Negativecount / rate)*100
ratepos = (positivecount/rate)*100
rateof5 = 5 * (ratepos / 100)
print("Neg = " + str(Negativecount) )
print("pos = " + str(positivecount) )
print("Neg = " + str(rateneg) )
print("pos = " + str(ratepos) )
print("pos = " + str(rateof5) ) 
file.close()




        


