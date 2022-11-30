"""
Every valid email consists of a local name and a domain name, separated by the '@' sign. Besides lowercase letters, the email may contain one or more '.' or '+'.

For example, in "alice@leetcode.com", "alice" is the local name, and "leetcode.com" is the domain name.
If you add periods '.' between some characters in the local name part of an email address, mail sent there will be forwarded to the same address without dots in the local name. Note that this rule does not apply to domain names.

For example, "alice.z@leetcode.com" and "alicez@leetcode.com" forward to the same email address.
If you add a plus '+' in the local name, everything after the first plus sign will be ignored. This allows certain emails to be filtered. Note that this rule does not apply to domain names.

For example, "m.y+name@email.com" will be forwarded to "my@email.com".
It is possible to use both of these rules at the same time.

Given an array of strings emails where we send one email to each emails[i], return the number of different addresses that actually receive mails.

 

Example 1:

Input: emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
Output: 2
Explanation: "testemail@leetcode.com" and "testemail@lee.tcode.com" actually receive mails.
Example 2:

Input: emails = ["a@leetcode.com","b@leetcode.com","c@leetcode.com"]
Output: 3

"""
from typing import List
import unittest

class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        # runtime: 133ms
        res = []
        for email in emails:
            ln, dn = email.split('@')
            ln_idx = len(ln) if ln.find('+') == -1 else ln.find('+')
            ln = ln[0:ln_idx]
            ln = ''.join(ln.split('.'))
            res.append(ln + "@" + dn)
        return len(set(res))
    
    def numUniqueEmails2(self, emails: List[str]) -> int:
        res = set()
        for email in emails:
            ln, dn = email.split('@')
            res.add(ln.split('+')[0].repliace('.', '') + '@' + dn) # 72ms
            res.add(''.join(ln.split('+')[0].split('.')) + "@" + dn) # 86ms

        return len(res)

class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_numUniqueEmails(self):
        emails = ["test.email+alex@leetcode.com","test.email.leet+alex@code.com"]
        result = self.solution.numUniqueEmails(emails)
        expect = 2
        self.assertEqual(result, expect)
        
if __name__ == "__main__":
    emails = ["test.email+alex@leetcode.com","test.email.leet+alex@code.com"]
    print(Solution().numUniqueEmails(emails))
    unittest.main()
