# import Counter

from collections import Counter

str_1, str_2, str_3 = "acbde", "abced", "abcda"
cnt_1, cnt_2, ctn_3 = Counter(str_1), Counter(str_2), Counter(str_3)

if cnt_1 == cnt_2:
    print('1 va 2 dao chu')
if cnt_1 == ctn_3:
    print('1 va 3 dao chu')
