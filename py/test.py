from konlpy.tag import Okt
import re
from typing import List
from lexrankr import LexRank
from konlpy.tag import Kkma

from pykospacing import Spacing

kkma = Kkma()


class OktTokenizer:
    okt: Okt = Okt()

    def __call__(self, text: str) -> List[str]:
        tokens: List[str] = self.okt.pos(text, norm=True, stem=True, join=True)
        return tokens


def preprocessing(input_sentence):
    total_review = ''
    okt = Okt()

    input_sentence = re.sub('[\n]', '', input_sentence)

    # 형태소 분석이 필요할까?
    for sentence in kkma.sentences(input_sentence):
        sentence = re.sub('([a-zA-Z])', '', sentence)
        sentence = re.sub('[ㄱ-ㅎㅏ-ㅣ]+', '', sentence)
        sentence = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', sentence)

        total_review += (okt.normalize(sentence) + ". ")
    return total_review


# 1. init
mytokenizer: OktTokenizer = OktTokenizer()
lexrank: LexRank = LexRank(mytokenizer)

while True:
    print("입력해주세요: ")
    summarize_text = str(input())

    # 2. summarize (like, pre-computation)

    summarize_text = preprocessing(summarize_text)
    lexrank.summarize(summarize_text)  # 이 부분 디버깅 하면서 확인하기

    # 3. probe (like, query-time)
    summaries: List[str] = lexrank.probe(4)

    for summary in summaries:
        print(summary)


    print("--------------------------------------------","\n")
h