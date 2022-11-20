from konlpy.tag import Okt
import re

okt = Okt()

def bag_of_words(text):
    document = re.sub(r"[^\uAC00-\uD7A30-9a-zA-Z\s]", "", text)
    words = okt.morphs(document)

    word_to_index = {}
    bow = []

    for word in words:
        if word not in word_to_index.keys():
            word_to_index[word] = len(word_to_index)
            bow.insert(len(word_to_index)-1, 1)
        else:
            index = word_to_index.get(word)
            bow[index] = bow[index] + 1

    return word_to_index, bow


if __name__ == '__main__':
    text = '나는 자연어 처리를 배운다! 자연어 처리는 !@$ ## {} 재미있다. aplle is good.'
    word_to_index, bow = bag_of_words(text)

    print('vocabulary :', word_to_index)
    print('bag of words vector :', bow)