# =====  Analysis key words for hortycurtularist =====
from pprint import pprint as pp
with open('/Users/martindanek/Documents/na_luka_cz/all_text.txt') as all_web_text:
    TEXTS = all_web_text.read()

# definitions for variables
word_count = {}
numerosity_count = {}
LIST_OF_WWW_KEYW = ['Na luka', 'naluka', 'zahradníci', 'realizace zahrad', 'veřejná zeleň', 'soukromé zahrady']
list_of_www_keyw = [char.lower() for char in LIST_OF_WWW_KEYW]
list_of_www_keyw_numerosity = []
texts = TEXTS.lower()

# text clean up
text_list = TEXTS.split()
for num, char in enumerate(text_list):
    word = char.strip('(©),.:+/;\\-@1234567890')
    if len(word) < 4:
        text_list[num] = ''
        continue
    text_list[num] = word.lower()
while '' in text_list:
    text_list.remove('')

# stats for text
# words count total
for char in text_list:
    word_count[char] = word_count.get(char, 0) + 1

# count numerosity of the words
numerosity_count = {numerosity: [] for numerosity in sorted(list(set(word_count.values())))}
for word in word_count:
    numerosity_count[word_count.get(word)].append(word)

for char in list_of_www_keyw:
    index = 0
    counter = 0
    while texts.find(char, index) != -1:
        counter += 1
        index = texts.find(char, index) + 1
    list_of_www_keyw_numerosity.append(counter)
list_of_www_keyw_result = zip(list_of_www_keyw, list_of_www_keyw_numerosity)

# FINAL OUTPUT
pp(word_count)
pp(numerosity_count)
pp(numerosity_count.keys())
pp(len(TEXTS.split()))
pp(len(text_list))
pp(list(list_of_www_keyw_result))
