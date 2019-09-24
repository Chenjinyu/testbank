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

Problem solving：
Everytime, when we deal with data, must think about the memory performance, not only in the leetCode, also in our work.
based on this, first time, my thoughts were permutation all the possible, it works well for small size of list, but when the words list is larger than 10 items.
it has tons of permutations, my computer's memeory was full. so bad. right?
if we could not detect what the size of words list could have, we shouldn't try to make large data.

we have to jump out of this logic. try another way. even we never think about it. below example is someone, I copied and read from him/her.
this solution is very efficient, and less memory consumes.

the logic of below solution:

"""
from collections import Counter


class Solution:
    def findSubstring(self, s: str, words:list) -> list:
        if not s or not words or len(s) < len(words) * len(words[0]):
            return []
        words_dict = Counter(words)
        pos_list = []
        length = len(words[0])
        for start in range(length):
            matched_s_dict = {}
            for i in range(start, len(s), length):
                word = s[i:i + length]
                if word not in words_dict:
                    start = i + length
                    matched_s_dict = {}  # if could not match, empty matched_s_dict.
                    continue
                matched_s_dict[word] = matched_s_dict.get(word, 0) + 1
                # curr value move back to start, and remove it from the matched_s_dict.
                # for the wordgoodgoodgoodbestword scenario. if good only has one in words list,
                # it will move the first three `good` words. and keep to matching.
                while matched_s_dict[word] > words_dict[word]:
                    curr = s[start:start + length]
                    start += length
                    matched_s_dict[curr] -= 1
                if matched_s_dict == words_dict:
                    pos_list.append(start)
        return pos_list


if __name__ == "__main__":
    # s = "pjzkrkevzztxductzzxmxsvwjkxpvukmfjywwetvfnujhweiybwvvsrfequzkhossmootkmyxgjgfordrpapjuunmqnxxdrqrfgkrsjqbszgiqlcfnrpjlcwdrvbumtotzylshdvccdmsqoadfrpsvnwpizlwszrtyclhgilklydbmfhuywotjmktnwrfvizvnmfvvqfiokkdprznnnjycttprkxpuykhmpchiksyucbmtabiqkisgbhxngmhezrrqvayfsxauampdpxtafniiwfvdufhtwajrbkxtjzqjnfocdhekumttuqwovfjrgulhekcpjszyynadxhnttgmnxkduqmmyhzfnjhducesctufqbumxbamalqudeibljgbspeotkgvddcwgxidaiqcvgwykhbysjzlzfbupkqunuqtraxrlptivshhbihtsigtpipguhbhctcvubnhqipncyxfjebdnjyetnlnvmuxhzsdahkrscewabejifmxombiamxvauuitoltyymsarqcuuoezcbqpdaprxmsrickwpgwpsoplhugbikbkotzrtqkscekkgwjycfnvwfgdzogjzjvpcvixnsqsxacfwndzvrwrycwxrcismdhqapoojegggkocyrdtkzmiekhxoppctytvphjynrhtcvxcobxbcjjivtfjiwmduhzjokkbctweqtigwfhzorjlkpuuliaipbtfldinyetoybvugevwvhhhweejogrghllsouipabfafcxnhukcbtmxzshoyyufjhzadhrelweszbfgwpkzlwxkogyogutscvuhcllphshivnoteztpxsaoaacgxyaztuixhunrowzljqfqrahosheukhahhbiaxqzfmmwcjxountkevsvpbzjnilwpoermxrtlfroqoclexxisrdhvfsindffslyekrzwzqkpeocilatftymodgztjgybtyheqgcpwogdcjlnlesefgvimwbxcbzvaibspdjnrpqtyeilkcspknyylbwndvkffmzuriilxagyerjptbgeqgebiaqnvdubrtxibhvakcyotkfonmseszhczapxdlauexehhaireihxsplgdgmxfvaevrbadbwjbdrkfbbjjkgcztkcbwagtcnrtqryuqixtzhaakjlurnumzyovawrcjiwabuwretmdamfkxrgqgcdgbrdbnugzecbgyxxdqmisaqcyjkqrntxqmdrczxbebemcblftxplafnyoxqimkhcykwamvdsxjezkpgdpvopddptdfbprjustquhlazkjfluxrzopqdstulybnqvyknrchbphcarknnhhovweaqawdyxsqsqahkepluypwrzjegqtdoxfgzdkydeoxvrfhxusrujnmjzqrrlxglcmkiykldbiasnhrjbjekystzilrwkzhontwmehrfsrzfaqrbbxncphbzuuxeteshyrveamjsfiaharkcqxefghgceeixkdgkuboupxnwhnfigpkwnqdvzlydpidcljmflbccarbiegsmweklwngvygbqpescpeichmfidgsjmkvkofvkuehsmkkbocgejoiqcnafvuokelwuqsgkyoekaroptuvekfvmtxtqshcwsztkrzwrpabqrrhnlerxjojemcxel"
    # words = ["dhvf","sind","ffsl","yekr","zwzq","kpeo","cila","tfty","modg","ztjg","ybty","heqg","cpwo","gdcj","lnle","sefg","vimw","bxcb"]
    # s = "wordgoodgoodgoodbestword"
    # words = ["word", "good", "best", "word"]
    s = "barfoofoobarthefoobarman"
    words = ["bar", "foo", "the"]
    print(Solution().findSubstring(s, words))


