# Group Anagrams
# Input: 
strs = ["eat","tea","tan","ate","nat","bat"]
# Output: 
# [["bat"],["nat","tan"],["ate","eat","tea"]]

from typing import List
# class Solution:
#     def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

# 원소씩 꺼내서 새로운 리스트에 추가 => 딕셔너리 타입으로 바로 집계, 굳이 새로 지정할 필요 없음
# sorted_list = []
# for word in strs:
#     # print(''.join(sorted(word)))
#     # word = "".join.sorted(word) 
#     sorted_list.append(''.join(sorted(word)))
# print(sorted_list)

# KeyError 방지하기 위해 defaultdict로 객체 지정
# 정렬한 리스트에서 딕셔너리 값으로 들어가게 함

from collections import defaultdict
anagrams = defaultdict(list)

for word in strs:   
    anagrams[''.join(sorted(word))].append(word)
print(anagrams) 
print(list(anagrams.values()))


# 출력: 예시와 다르게 되지만 추가 정렬할 필요 없음 [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]
        