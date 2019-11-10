### [#Quora-and-Ebay-OA]

* product sum
* valid word


```python
# Product Sum
# Input: 230
# Output: -6
# Explaination: 2 * 3 * 0 - (2 + 3 + 0) = -5

def product_sum(num):
    product = 1
    addition = 0
    while num:
        i = num % 10
        product *= i
        addition += i
        num //= 10
    return product - addition


num = 230
print(product_sum(num))
```

[Go Top](#Quora-and-Ebay-OA)

