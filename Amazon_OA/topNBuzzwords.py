"""
You work on a team whose job is to understand the most sought after toys for the holiday season.
A teammate of yours has built a webcrawler that extracts a list of quotes about toys from different articles.
You need to take these quotes and identify which toys are mentioned most frequently.
Write an algorithm that identifies the top N toys out of a list of quotes and list of toys.

Your algorithm should output the top N toys mentioned most frequently in the quotes.

Input:
The input to the function/method consists of five arguments:

numToys, an integer representing the number of toys
topToys, an integer representing the number of top toys your algorithm needs to return;
toys, a list of strings representing the toys,
numQuotes, an integer representing the number of quotes about toys;
quotes, a list of strings that consists of space-sperated words representing articles about toys

Output:
Return a list of strings of the most popular N toys in order of most to least frequently mentioned

Note:
The comparison of strings is case-insensitive. If the value of topToys is more than the number of toys,
return the names of only the toys mentioned in the quotes. If toys are mentioned an equal number of times in quotes,
sort alphabetically.

Example 1:

Input:
numToys = 6
topToys = 2
toys = ["elmo", "elsa", "legos", "drone", "tablet", "warcraft"]
numQuotes = 6
quotes = [
"Elmo is the hottest of the season! Elmo will be on every kid's wishlist!",
"The new Elmo dolls are super high quality",
"Expect the Elsa dolls to be very popular this year, Elsa!",
"Elsa and Elmo are the toys I'll be buying for my kids, Elsa is good",
"For parents of older kids, look into buying them a drone",
"Warcraft is slowly rising in popularity ahead of the holiday season"
];

Output:
["elmo", "elsa"]

Explanation:
elmo - 4
elsa - 4
"elmo" should be placed before "elsa" in the result because "elmo" appears in 3 different quotes
and "elsa" appears in 2 different quotes.
"""

import heapq

def topNBuzzwords(numToys, topToys, toys, numQuotes, quotes):
    ans_list = []

    for toy in toys:
        tmp_count = 0
        for quote in quotes:
            quote_list = quote.split(" ")
            for q in quote_list:
                if not q[~0].isalnum():
                    q = q[:~0]
                if not q[0].isalnum() and len(q) > 1:
                    q = q[1:]

                if q.lower() == toy.lower():
                    tmp_count += 1

        ans_list.append((tmp_count, toy))

    ans_list.sort(key=lambda x: -x[0])
    return [x[1] for x in ans_list[:topToys]]


numToys = 6
topToys = 2
toys = ["elmo", "elsa", "legos", "drone", "tablet", "warcraft"]
numQuotes = 6
quotes = [
"Elmo is the hottest of the season! Elmo will be on every kid's wishlist!",
"The new Elmo dolls are super high quality",
"Expect the Elsa dolls to be very popular this year, Elsa!",
"Elsa and Elmo are the toys I'll be buying for my kids, Elsa is good",
"For parents of older kids, look into buying them a drone",
"Warcraft is slowly rising in popularity ahead of the holiday season"
]
print(topNBuzzwords(numToys, topToys, toys, numQuotes, quotes))

