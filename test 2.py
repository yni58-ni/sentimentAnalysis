data = []
list_in_eastern = []
list_in_central = []
list_in_mountain = []
list_in_pacific = []
count_of_tweets_e = 0
count_of_tweets_c = 0
count_of_tweets_m = 0
count_of_tweets_p = 0
count_of_keyword_tweets_e = 0
count_of_keyword_tweets_c = 0
count_of_keyword_tweets_m = 0
count_of_keyword_tweets_p = 0

for line in open("tweets.txt","r"):
    data.append(line)
for line2 in data:
    if 24.660845 < float(line2[1:8]) < 49.189787:
        if -87.518395 < float((line2[(int(line2.find(","))+1):(int(line2.find(","))+11)])) < -67.444574:  # eastern
            list_in_eastern.append(line2)
            count_of_tweets_e += 1
        if -101.998892 < float((line2[(int(line2.find(","))+1):(int(line2.find(","))+11)])) < -87.518395:  # central
            list_in_central.append(line2)
            count_of_tweets_c += 1
        if -115.236428 < float((line2[(int(line2.find(","))+1):(int(line2.find(","))+11)])) < -101.998892:  # mountain
            list_in_mountain.append(line2)
            count_of_tweets_m += 1
        if -125.242264 < float((line2[(int(line2.find(","))+1):(int(line2.find(","))+11)])) < -115.236428:  # pacific
            list_in_pacific.append(line2)
            count_of_tweets_p += 1
print(count_of_tweets_e)
a = []
c = []
for line4 in list_in_eastern:
    #print(line4)
    for item1 in line4:
        if item1.isalpha() == True and item1.isspace() == True:
            a.append(item1)
            b = "".join(a)
            b.lower()
            c.append(b)



file_eastern = open('file_eastern.txt','w')
for items in list_in_eastern:
    file_eastern.write(items)
    file_eastern.write("")
file_eastern.close()
a = open('file_eastern.txt','r')
b = a.readlines()
print(b)
#print(count_of_tweets_e)
#print(count_of_tweets_c)
#print(count_of_tweets_m)
#print(count_of_tweets_p)

list_new = []
def move_punc (tweetsName):
    with open(tweetsName) as t:
        f = t.readlines()
        m = f.strip().split(" ",5)
#print(move_punc("file_eastern.txt"))


dic = {}  # create an empty dictionary to store both keywords and values
keywords = []  # create an empty list to store only sentiment keywords
with open('keywords.txt') as k:
    for line in k:
        split_Line = line.split(",")  # split each line from keywords.txt by comma
        list = line.split(",")[0]  # specify maxsplit
        keywords.append(list)  # a list which contains only sentiment keywords
        dic[str(split_Line[0])] = int(split_Line[1])  # a dictionary which contains both keywords and values


for line3 in list_in_eastern:
    for keyword in keywords:
        if keyword in line3:
           count_of_keyword_tweets_e += 1
    continue
#print(count_of_keyword_tweets_e)

    #print(line2[1:10])
# print((line2[(int(line2.find(","))+1):(int(line2.find(","))+13)]))
#print(data[0][1:10])
#print(data[0][(int(data[1].find(","))+1):(int(data[0].find(","))+13)])


