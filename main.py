tweetsName = input("Tweets Name: ")
keywordName = input("Keyword Name:")
import sentiment_analysis

output_result = sentiment_analysis.compute_tweets(tweetsName, keywordName)

print('\nIn Eastern timezone, the average score is',output_result[0][0], 'total amount of keyword tweets is', output_result[0][1], 'total amount of keyword tweets is',
      output_result[0][2], '\n')
print('\nIn Central timezone, the average score is',output_result[1][0], 'total amount of keyword tweets is', output_result[1][1], 'total amount of keyword tweets is',
      output_result[1][2], '\n')
print('\nIn Mountain timezone, the average score is',output_result[2][0], 'total amount of keyword tweets is', output_result[2][1], 'total amount of keyword tweets is',
      output_result[2][2], '\n')
print('\nIn Pacific timezone, the average score is',output_result[3][0], 'total amount of keyword tweets is', output_result[3][1], 'total amount of keyword tweets is',
      output_result[3][2], '\n')

