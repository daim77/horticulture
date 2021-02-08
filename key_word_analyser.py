# =====  Analysis key words for hortycurtularist =====
from pprint import pprint as pp


with open('tables/result.txt') as all_web_text:
    TEXTS = all_web_text.read()

# definitions for variables
word_count = {}
numerosity_count = {}
texts = TEXTS.lower()

# text clean up
text_list = TEXTS.split()
for num, char in enumerate(text_list):
    word = char.strip('[]#$%&*?(©),.:+/;\\-@1234567890')
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
numerosity_count = {
    numerosity: []
    for numerosity in sorted(list(set(word_count.values())))
}

for word in word_count:
    numerosity_count[word_count.get(word)].append(word)


# FINAL OUTPUT
pp(word_count)
pp(numerosity_count)
pp(numerosity_count.keys())
