import string
def count_of_keyTweet(name_format_keyword,name_format_tweet):
    number = 0
    for i in range(len(name_format_tweet)):
        isKeyword = 0
        for x in name_format_keyword:
            if x in (name_format_tweet[i]):
                isKeyword = 1
                break
        if isKeyword == 1:
            number += 1
    return number


def move_punc (tweetsName):
    with open(tweetsName) as t:
        punct = string.punctuation
        New_tweet2 = []
        for Line in t:
            m = Line.strip().split(" ", 5)  # use maxsplit to get tweet contents
            new_tweet = m[-1]
            new_tweet = new_tweet.split()
            for i in range(len(new_tweet)):
                new_tweet[i] = new_tweet[i].strip()
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


def happiness_score(name_format_keyword,name_format_tweet,number):
    keywords_dic = compute_keywords(name_format_keyword)[0]
    keywords_list = compute_keywords(name_format_keyword)[1]
    happiness_score_sum = []
    average_score = 0
    for tweet in name_format_tweet:  # each tweet in file_eastern
        count_keyword = 0
        happiness_score = 0
        value = 0
        for character in tweet:  # each word in every tweet
            if character in keywords_list:
                value = int(keywords_dic[character]) + value
                count_keyword += 1
            if character == tweet[-1] and count_keyword != 0:
                happiness_score = (value / count_keyword)
                happiness_score_sum.append(happiness_score)
                average_score = (sum(happiness_score_sum)/number)
    return average_score


def compute_tweets(tweetsName, keywordName):
    try:
        tweetsFile = open(tweetsName,"r", errors='ignore')
        keywordFile = open(keywordName,"r", errors='ignore')
    except IOError:
        print("The file name does not exist")
        exit()

    keywords_list = compute_keywords(keywordName)[1]

    count_of_keyword_tweets_e = 0
    count_of_keyword_tweets_c = 0
    count_of_keyword_tweets_m = 0
    count_of_keyword_tweets_p = 0
    data = []
    list_in_eastern = []
    list_in_central = []
    list_in_mountain = []
    list_in_pacific = []
    count_of_tweets_e = 0
    count_of_tweets_c = 0
    count_of_tweets_m = 0
    count_of_tweets_p = 0

    # select tweets that belong to certain timezone
    for line in open(tweetsName, "r"):
        data.append(line)
    for line2 in data:
        if 24.660845 < float(line2[1:8]) < 49.189787:
            if -87.518395 < float((line2[(int(line2.find(",")) + 1):(int(line2.find(",")) + 11)])) < -67.444574:  # eastern
                list_in_eastern.append(line2)
                count_of_tweets_e += 1
            if -101.998892 < float((line2[(int(line2.find(",")) + 1):(int(line2.find(",")) + 11)])) < -87.518395:  # central
                list_in_central.append(line2)
                count_of_tweets_c += 1
            if -115.236428 < float((line2[(int(line2.find(",")) + 1):(int(line2.find(",")) + 11)])) < -101.998892:  # mountain
                list_in_mountain.append(line2)
                count_of_tweets_m += 1
            if -125.242264 < float((line2[(int(line2.find(",")) + 1):(int(line2.find(",")) + 11)])) < -115.236428:  # pacific
                list_in_pacific.append(line2)
                count_of_tweets_p += 1

    # cover selected tweets into file
    file_eastern = open('file_eastern.txt', 'w')
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

    # format selected tweets from each timezone
    format_eastern = move_punc('file_eastern.txt')
    format_central = move_punc('file_central.txt')
    format_mountain = move_punc('file_mountain.txt')
    format_pacific = move_punc('file_pacific.txt')
    # count of keyword tweets from each timezone
    count_of_keyTweet_eastern = count_of_keyTweet(keywords_list, format_eastern)
    count_of_keyTweet_central = count_of_keyTweet(keywords_list, format_central)
    count_of_keyTweet_mountain = count_of_keyTweet(keywords_list, format_mountain)
    count_of_keyTweet_pacific = count_of_keyTweet(keywords_list, format_pacific)

    # Average happiness score from each timezone
    average_eastern = happiness_score(keywordName, format_eastern, count_of_keyTweet_eastern)
    average_central = happiness_score(keywordName, format_central, count_of_keyTweet_central)
    average_mountain = happiness_score(keywordName, format_mountain, count_of_keyTweet_mountain)
    average_pacific = happiness_score(keywordName, format_pacific, count_of_keyTweet_pacific)


    result_eastern = [average_eastern, count_of_keyTweet_eastern, count_of_tweets_e]
    result_central = [average_central, count_of_keyTweet_central, count_of_tweets_c]
    result_mountain = [average_mountain, count_of_keyTweet_mountain, count_of_tweets_m]
    result_pacific = [average_pacific, count_of_keyTweet_pacific, count_of_tweets_p]

    final_result = []
    final_result.append(result_eastern)
    final_result.append(result_central)
    final_result.append(result_mountain)
    final_result.append(result_pacific)

    return final_result






