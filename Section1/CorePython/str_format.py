# from math import pi

# sentence = 'pi is equal to {:.2f}'.format(pi)
# print(sentence)

#  To add commas to big numbers
# sentence = '1 MB is equal to {:,} bytes'.format(1000**2)

# To format dates
import datetime

my_date = datetime.datetime(2016, 9, 24, 12, 30, 45)

sentence_1 = "{:%B, %d, %Y}".format(my_date)
print(sentence_1)

sentence_2 = "{0:%B %d, %Y} fell on a {0:%A} and was the {0:%j} day of the year".format(
    my_date
)
