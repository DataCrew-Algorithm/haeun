# Most common word

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

from typing import List
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower().split() # 대소문자 상관없고, 공백으로 구분
        
        return paragraph

# Sol = Solution()
# Sol.mostCommonWord(paragraph, banned)


# 정답 풀이
# 're' 모듈의 re.sub 함수를 통해 특정문자열만 치환: re.sub(치환하고 싶은 문자열(정규표현), 새로운 문자열（정규표현）, 대상변수 [,치환횟수])
# 'Count' 모듈의 most_common 메소드로 Count 객체에서 가장 빈도 수가 높은 요소를 추출

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]',' ',
                                         paragraph).lower().split()
                if word not in banned]

        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]


# 예빈님 코드 참고: 
# 구두점을 공백으로 변환한 문장으로부터 단어만 추출
# 금지된 단어가 있는지 확인 없는 것만 따로 리스트에 담고,
# 원소 별로 카운트한 값을 인덱스 리스트로 별도로 넣어서 최댓값을 구하고, 그 최댓값인 인덱스의 단어를 출력

class Solution:
    def mostCommonWord(self, paragraph, banned):
        punc = ",.!'?;`'" 
        for punc in punc:
            paragraph = (paragraph.lower()).replace(punc," ")
        word = paragraph.split()
        r_word = [x for x in word if x not in banned]
        lst = []
        for i in r_word:
            n = r_word.count(i)
            lst.append(n)
        return r_word[lst.index(max(lst))]

# paragraph = "a, a, a, a, b,b,b,c, c"
# banned = ["a"]
# sol = Solution()
# print(sol.mostCommonWord(paragraph, banned))