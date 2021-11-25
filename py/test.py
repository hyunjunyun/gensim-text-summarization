from konlpy.tag import Okt

from typing import List
from lexrankr import LexRank


class OktTokenizer:
    okt: Okt = Okt()

    def __call__(self, text: str) -> List[str]:
        tokens: List[str] = self.okt.pos(text, norm=True, stem=True, join=True)
        return tokens


# 1. init
mytokenizer: OktTokenizer = OktTokenizer()
lexrank: LexRank = LexRank(mytokenizer)

summarize_text = str(input())

# 2. summarize (like, pre-computation)
lexrank.summarize(summarize_text)

# 3. probe (like, query-time)
summaries: List[str] = lexrank.probe()

for summary in summaries:
    print(summary)
