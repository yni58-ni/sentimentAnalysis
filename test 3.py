import string
def move_punc (tweetsName):
    with open(tweetsName) as t:
        punct = string.punctuation
        New_tweet2 = []
        for Line in t:
            m = Line.strip().split(" ", 5)  # use maxsplit to get tweet contents
            new_tweet = m[-1]
            new_tweet = new_tweet.split()
            for i in range(len(new_tweet)):
                #new_tweet[i] = new_tweet[i].strip()
                new_tweet[i] = new_tweet[i].strip(punct).lower()  # strip punctuation from both sides of a word and convert it into lower
            New_tweet2.append(new_tweet)
    return New_tweet2

def compute_keywords (keywordName) :
    dic = {}  # create an empty dictionary to store both keywords and values
    keywords = []  # create an empty list to store only sentiment keywords
    with open(keywordName) as k:
        for line in k:
            split_Line = line.split(",")  # split each line from keywords.txt by comma
            list = line.split(",", 1)  # specify maxsplit
            for item in list:
                if item.isalpha():
                   keywords.append(item)  # a list which contains only sentiment keywords
            dic[str(split_Line[0])] = int(split_Line[1])  # a dictionary which contains both keywords and values
    return dic, keywords

keywords_list = compute_keywords("keywords.txt")[1]
keywords_dic = compute_keywords("keywords.txt")[0]
#print(keywords_dic)


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


#print(list_in_eastern)

file_eastern = open('file_eastern.txt','w')
for items in list_in_eastern:
    file_eastern.write(items)
    file_eastern.write('')
file_eastern.close()

file_central = open('file_central.txt', 'w')
for items in list_in_central:
    file_central.write(items)
    file_central.write('')
file_central.close()

file_mountain = open('file_mountain.txt', 'w')
for items in list_in_mountain:
    file_mountain.write(items)
    file_mountain.write('')
file_mountain.close()

file_pacific = open('file_pacific.txt', 'w')
for items in list_in_pacific:
    file_pacific.write(items)
    file_pacific.write('')
file_pacific.close()

haha = move_punc("file_pacific.txt")
#print(haha)

number = 0
for i in range(len(haha)):
    isKeyword = 0
    for x in keywords_list:
        if x in (haha[i]):
            isKeyword = 1
            #print(x)
            #print(i)
            #print(haha[i])
            break
            #print(isKeyword)
    if isKeyword == 1:
        number += 1
#print(type(h))

#happiness score
happiness_score_sum = []
#total_keywords = 0
for tweet in haha: # each tweet in file_eastern
    count_keyword = 0
    happiness_score = 0
    value = 0
    #print(type(tweet))
    for character in tweet: # each word in everytweet
        if character in keywords_list:
            #print(character)
           # print(tweet)
            value = int(keywords_dic[character])+ value
            print(type(value))
            count_keyword += 1
            #total_keywords += 1
        if character == tweet[-1] and count_keyword != 0:
            happiness_score = (value/count_keyword)
            happiness_score_sum.append(happiness_score)
print(sum(happiness_score_sum)) #average_score



