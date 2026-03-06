# """
# Given a binary array `nums` and an integer `k`, return _the maximum number of consecutive_ `1`_'s in the array if you can flip at most_ `k` `0`'s.

# **Example 1:**

# **Input:** nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
# **Output:** 6
# **Explanation:** [1,1,1,0,0,**1**,1,1,1,1,**1**]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

# **Example 2:**

# **Input:** nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
# **Output:** 10
# **Explanation:** [0,0,1,1,**1**,**1**,1,1,1,**1**,1,1,0,0,0,1,1,1,1]
# Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
# """
# from typing import List
    
# def longestOnes(nums: List[int], k: int) -> int:
#     # does not work
#     if len(nums) == 0:
#         return 0
#     ans = float("-inf")
#     left = right = 0
#     flip_count = k
#     tmp_count = 0
#     while right < len(nums):
#         if nums[right] == 1:
#             right += 1
#             continue
#         if nums[right] == 0:
#             if k > 0:
#                 right += 1
#                 k -= 1
#                 continue
#             elif k == 0:
#                 ans = max(ans, right - left + 1)
#                 while left < right and tmp_count < k:
#                     if nums[left] == 0:
#                         tmp_count += 1
#                     left += 1
#                 k = flip_count
               
#     return ans

# def longestOnes2(nums: List[int], k: int) -> int:
#     # 33ms
#     left = 0
#     for right in range(len(nums)):
#         if nums[right] == 0:
#             k -= 1
#         if k < 0:
#             if nums[left] == 0:
#                 k += 1
#             left += 1
#     return right - left + 1

# def longestOnes3(nums: List[int], k: int) -> int:
#     # 611ms
#     max_len = curr_count_zero = left = 0
#     for right, val in enumerate(nums):
#         if val == 0:
#             curr_count_zero += 1
#         if curr_count_zero > k:
#             curr_count_zero = curr_count_zero - 1 if nums[left] == 0 else curr_count_zero
#             left += 1
            
#         max_len = max(max_len, right - left + 1)
        
#     return max_len


# nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1]
# k = 3
# nums2 = [1,1,1,0,0,0,1,1,1,1,0]
# k2 = 2

# ans = longestOnes(nums, k)
# print(ans)
                
            
# import re            
# def isValid(code: str) -> bool:
#     tag_pattern = re.compile(r'<(/?\w+)[^>]*>')
#     # tag_pattern = re.compile(r'<(/?[\w|!|[|]]])[^>]*>')
#     stack = []

#     for match in tag_pattern.finditer(code):
#         tag = match.group(1)
#         if not tag.startswith('/'):
#             # Opening tag
#             stack.append(tag)
#         else:
#             if not stack or stack.pop() != tag[1:]: # remove /
#                 return False
    
#     return not stack

# code = "<DIV>This is the first line <![CDATA[<div>]]></DIV>"
# print(isValid(code))


# html = """
# <html>
# 	<head>Test</head>
# 	<body>
# 		<p>test content</p>
# 		<ol>
# 			<li>Option 1</li>
# 			<li>Option 2</li>
# 			<li>Option 3</li>
# 		</ol>
# 	</body>
# </html>
# """
# import re
# def is_valid_html(html: str) -> bool:
# 	tag_pattern = re.compile(r'<(/?\w+)[^>]*>')
# 	stack = []
# 	for matches in tag_pattern.finditer(html):
# 		tag = matches.group(1)
# 		if not tag.startswith('/'):
# 			# opening tag
# 			stack.append(tag)
# 		else:
# 			if not stack or stack.pop() != tag[1:]: # not stack to make sure stack.pop() has value
# 				return False
# 	return not stack # the stack should include nothing, if all tags are matached

# print(is_valid_html(html))

import re
code_list = [
    "<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>",
    "<DIV>This is the first line <![CDATA[<div>]]></DIV>"
]
# pattern = re.compile(r'[<!]?\[CDATA\[.*?\]\]>', re.I) 
# for code in code_list:
#     matches = pattern.findall(code)
#     print(matches)
#     replaced_code = pattern.sub('', code)
#     print("code: " + code + "\nfirst replace: " + replaced_code)
#     replaced_code = re.sub(r'\[{2,}|\]{2,}|>\[+|>\]+|<\[+|<\]+', '', replaced_code, flags=re.I)
#     print("replace [ or ]: " + replaced_code)
#     replaced_code = re.sub(r'>{2,}', '>', replaced_code, flags=re.I)
#     print("replace >: " + replaced_code)
#     replaced_code = re.sub(r'<{2,}', '<', replaced_code, flags=re.I)
#     print("replace <: " + replaced_code)
#     print("final: " + replaced_code)
#     print('-' * 20)
    
    
# new_reg_exp = r'<[A-Z]{0,9}>([^<]*(<((\/?[A-Z]{1,9}>)|(!\[CDATA\[(.*?)]]>)))?)*'

new_pattern = re.compile(r"""
    <[A-Z]{0,9}>  # Opening tag with 0 to 9 uppercase letters
    (
        [^<]*  # Any characters except '<'
        (
            <
            (
                    (
                        \/?[A-Z]{1,9}>
                    )
                |
                    (
                        !\[CDATA\[(.*?)]]>
                    )
            )
        )?
    )*  # Zero or more occurrences of the above
""", re.VERBOSE)

# new_pattern = re.compile(new_reg_exp)
# "<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>",
matches = new_pattern.findall(code_list[0])
# matches = re.fullmatch(new_reg_exp, code_list[0])
# print(matches)
# for match in matches:
#     print(match)


# sentence = "The quick brown fox jumps over the lazy dog."
# position = sentence.find("fox")
# print(sentence[:position])
# code = "<![CDATA[wahaha]]]><![CDATA[]> wahaha]]>"
# if code[1: 1 + 7] != "![CDATA":
#     print("not match")

# test = "TES<T"
# if test.islower():
#     print("is lower")
# elif test.isupper():
#     print("is upper")
    
# print(test[1:100])
from typing import List

nums = [12,23,135,1567,119]

def radix_array(nums: List) -> List:
    max_digits = max([len(str(x)) for x in nums])
        
    def sort_by_digit(nums, digit_pos):
        # cannot create the radix_array with [[]] * 10, because each sub list will assign to the first sublist at the same time
        buckets = [ [] for _ in range(10) ] # 0-9
        for num in nums:
            digit = (num // digit_pos) % 10
            buckets[digit].append(num)
        
        result = []
        for bucket in buckets:
            result.extend(bucket)
        return result
    
    digit_pos = 1
    for _ in range(max_digits):
        nums = sort_by_digit(nums, digit_pos)
        digit_pos *= 10
    return nums

print(radix_array(nums))