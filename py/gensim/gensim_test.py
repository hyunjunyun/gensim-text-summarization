from gensim.summarization.summarizer import summarize
from konlpy.tag import Kkma

kkma = Kkma()

import sys
import os
import re

sys.path.append(os.path.dirname('PyKoSpacing/'))
from pykospacing import Spacing
from konlpy.tag import Okt


def preprocessing(input_sentence):
    total_review = ''
    okt = Okt()

    # 형태소 분석이 필요할까?
    for sentence in kkma.sentences(input_sentence):
        sentence = re.sub('([a-zA-Z])', '', sentence)
        sentence = re.sub('[ㄱ-ㅎㅏ-ㅣ]+', '', sentence)
        sentence = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', sentence)
        if len(sentence) == 0:
            continue
        if len(sentence) < 198:
            spacing = Spacing()
            sentence = spacing(sentence)
        total_review += (okt.normalize(sentence) + ". ")
    return total_review


# 전처리 쪽을 조금만 잘 다듬으면 더 좋은 결과가 나올 수 있을 것 같다.


while True:
    print("텍스트를 입력해주세요: ")
    text: str = str(input())
    if text == 'end': break

    print("결과: ")
    pp = preprocessing(text)
    # print(pp)

    su = summarize(pp, word_count=45)
    # su = re.sub('\n', ' ', su)

    print(su)
