"""
30. Substring with Concatenation of All Words
You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.
Example 1:
Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]
Output: [0,9]
Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
The output order does not matter, returning [9,0] is fine too.

Example 2:

Input:
  s = "wordgoodgoodgoodbestword",
  words = ["word","good","best","word"]
Output: []

Problem solving： !!!!this is very bad solution.!!!!
this problem divides to two parts:
1. take care of the edge cases, make sure the range: [−2**31,  2**31 − 1], and test them at the edge of them,
eg: 2147483648, -2147483648, 2147483647, -2147483647, -1, 1. when the dividend reach to 2147483647, the maximum.
2. take care of the basic logic, but make sure the large number brings the performance issue.
"""

from itertools import permutations


class Solution:
    def findSubstring(self, s: str, words: list) -> list:
        pos_list = []
        substr_list = self.order_sub_string(words, s)
        if len(substr_list) == 0:
            return pos_list
        for sub in substr_list:
            start = 0
            while True:
                index = s.find(sub, start)
                if index < len(s):
                    start = index + 1
                if index >= 0:
                    pos_list.append(index)
                if index == -1:
                    break
        return pos_list

    def order_sub_string(self, words: list, s:str) -> set:
        word_len = len(words[0])
        words_list_len = len(words)
        substring_list = []

        words = [w for w in words if w is not "" or None]
        if words_list_len == 0:
            return substring_list
        if words_list_len == 1:
            return words
        match_item_list = [words.copy()]
        self.loop_substr(match_item_list, s, words_list_len - 1, 0)
        try:
            if len(final_match_list):
                substring_list = [v[0] for v in final_match_list if len(v[0]) == (words_list_len * word_len)]
                return set(substring_list)
            else:
                return []
        except:
            return []

    def loop_substr(self, match_item_list, main_str, loop_num, cur_loop) -> list:

        for match in match_item_list:
            if len(match) == 1:
                global final_match_list
                final_match_list = match_item_list
                return
            if cur_loop >= loop_num:
                return

            permutation_list = list(permutations(match, 2))
            match_item_list = []
            for item in permutation_list:
                new_words = match.copy()
                sub_str = "".join(item)
                if main_str.find(sub_str) >= 0:
                    for i in item:
                        new_words.remove(i)

                    new_list = [sub_str] + new_words
                    match_item_list.append(new_list)

        if len(match_item_list) == 0:
            return

        cur_loop += 1

        self.loop_substr(match_item_list, main_str, loop_num, cur_loop)


if __name__ == "__main__":
    # s = "pjzkrkevzztxductzzxmxsvwjkxpvukmfjywwetvfnujhweiybwvvsrfequzkhossmootkmyxgjgfordrpapjuunmqnxxdrqrfgkrsjqbszgiqlcfnrpjlcwdrvbumtotzylshdvccdmsqoadfrpsvnwpizlwszrtyclhgilklydbmfhuywotjmktnwrfvizvnmfvvqfiokkdprznnnjycttprkxpuykhmpchiksyucbmtabiqkisgbhxngmhezrrqvayfsxauampdpxtafniiwfvdufhtwajrbkxtjzqjnfocdhekumttuqwovfjrgulhekcpjszyynadxhnttgmnxkduqmmyhzfnjhducesctufqbumxbamalqudeibljgbspeotkgvddcwgxidaiqcvgwykhbysjzlzfbupkqunuqtraxrlptivshhbihtsigtpipguhbhctcvubnhqipncyxfjebdnjyetnlnvmuxhzsdahkrscewabejifmxombiamxvauuitoltyymsarqcuuoezcbqpdaprxmsrickwpgwpsoplhugbikbkotzrtqkscekkgwjycfnvwfgdzogjzjvpcvixnsqsxacfwndzvrwrycwxrcismdhqapoojegggkocyrdtkzmiekhxoppctytvphjynrhtcvxcobxbcjjivtfjiwmduhzjokkbctweqtigwfhzorjlkpuuliaipbtfldinyetoybvugevwvhhhweejogrghllsouipabfafcxnhukcbtmxzshoyyufjhzadhrelweszbfgwpkzlwxkogyogutscvuhcllphshivnoteztpxsaoaacgxyaztuixhunrowzljqfqrahosheukhahhbiaxqzfmmwcjxountkevsvpbzjnilwpoermxrtlfroqoclexxisrdhvfsindffslyekrzwzqkpeocilatftymodgztjgybtyheqgcpwogdcjlnlesefgvimwbxcbzvaibspdjnrpqtyeilkcspknyylbwndvkffmzuriilxagyerjptbgeqgebiaqnvdubrtxibhvakcyotkfonmseszhczapxdlauexehhaireihxsplgdgmxfvaevrbadbwjbdrkfbbjjkgcztkcbwagtcnrtqryuqixtzhaakjlurnumzyovawrcjiwabuwretmdamfkxrgqgcdgbrdbnugzecbgyxxdqmisaqcyjkqrntxqmdrczxbebemcblftxplafnyoxqimkhcykwamvdsxjezkpgdpvopddptdfbprjustquhlazkjfluxrzopqdstulybnqvyknrchbphcarknnhhovweaqawdyxsqsqahkepluypwrzjegqtdoxfgzdkydeoxvrfhxusrujnmjzqrrlxglcmkiykldbiasnhrjbjekystzilrwkzhontwmehrfsrzfaqrbbxncphbzuuxeteshyrveamjsfiaharkcqxefghgceeixkdgkuboupxnwhnfigpkwnqdvzlydpidcljmflbccarbiegsmweklwngvygbqpescpeichmfidgsjmkvkofvkuehsmkkbocgejoiqcnafvuokelwuqsgkyoekaroptuvekfvmtxtqshcwsztkrzwrpabqrrhnlerxjojemcxel"
    # words = ["dhvf", "sind", "ffsl", "yekr", "zwzq", "kpeo", "cila", "tfty", "modg", "ztjg", "ybty", "heqg", "cpwo", "gdcj", "lnle", "sefg", "vimw", "bxcb"]
    # s = "wordgoodgoodgoodbestword"
    # words = ["word","good","best","word"]
    # s = "barfoothefoobarman"
    # words = ["foo","bar"]
    s = "barfoofoobarthefoobarman"
    words = ["bar", "foo", "the"]
    print(Solution().findSubstring(s, words))

