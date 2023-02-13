## Hashing

### What is the point of a hash function?
We know that arrays have **O(1)** random access. The main constraint with arrays is that they are a fixed size, and their indices have to be integers. Because hash functions can convert any input into an integer, if we combine an array with a hash function, we can create what is known as a hash map, also known as a hash table or dictionary. Then, we can essentially have the **O(1)** random access of an array without the constraint of integers as indices. With arrays, we map indices to values. With hash maps, we map keys to values, and a key can be almost anything. The only constraint on a hash map's key is that it has to be immutable (this is language dependent but generally a good rule of thumb). Values can be anything.

A hash map is probably the most important concept in all of algorithm interviewing. It is extremely powerful and allows you to reduce the time complexity of an algorithm by a factor of 
**O(n)** for a huge amount of problems. Every major language has a built-in implementation of a hash map. For example, in Python they're called dictionaries and declaring one is as simple as **dic = {}**. If you could only take one thing from this course, it should be to learn and master the hash map operations for the programming language you use.

To summarize, a hash map is an unordered data structure that stores key-value pairs. A hash map can add and remove elements in **O(1)**, as well as update values associated with a key and check if a key exists, also in  **O(1)**. You can iterate over both the keys and values of a hash map, but a hash map isn't necessarily an ordered data structure (there are many implementations and this is language dependent for the built-in types).

>An ordered data structure is one where the insertion order is "remembered". An unordered data structure is one where the insertion order is not relevant.

### Comparison with arrays
In terms of time complexity, hash maps blow arrays out of the water. The following operations are all **O(1)** for a hash map:
- Add an element and associate it with a value
- Delete an element if it exists
- Check if an element exists

A hash map also has many of the same useful properties as an array with the same time complexity:
- Find length/number of elements
- Updating values
- Iterate over elements

>Hash maps are also just easier/cleaner to work with. Even if your keys are integers and you could get away with using an array, if you don't know what the max size of your key is, then you don't know how large you should size your array. With hash maps, you don't need to worry about that, since your key can be anything.

However, from a practical perspective, there are some disadvantages to using hash maps, and it's important to know them as it is common in interviews to talk about tradeoffs.

The biggest disadvantage of hash maps is that for smaller input sizes, they can be slower because of overhead. Because big O ignores constants, the **O(1)** time complexity can sometimes be deceiving - it's usually something more like **O(10)** because every key needs to go through the hash function, and there can also be **collisions(碰撞)**, which we will talk about in the next section.

>When talking about the time complexity of hash map operations, they are constant relative to the size of the hash map. However, some keys can be very expensive to hash. For example, it may take O(m) time to hash a string, where m is the length of the string. If you want to store a huge string as a key, then the time complexity can be deceiving.


Hash tables can also take up more space. Recall that dynamic arrays are actually fixed-size arrays that resize themselves when they go beyond their capacity. Hash tables are also implemented using a fixed size array - remember that the size is a limit set by the programmer. The problem is, resizing a hash table is much more expensive because every existing key needs to be re-hashed, and also a hash table may use an array that is significantly larger than the number of elements stored, resulting in a huge waste of space. Let's say you chose your limit as 10,000 items, but you only end up storing 10. Okay, you could argue that 10,000 is too large, but then what if your next test case ends up needing to store 100,000 elements? The point is, when you don't know how many elements you need to store, arrays are more flexible with resizing and not wasting space.

>Note: remember that time complexity functions only care about the variables you give it. When we say that hash map operations are O(1), the variable we are concerned with is usually n, which is the size of the hash map. However, this may be misleading. For example, hashing a string requires  O(m) time, where m is the length of the string. The constant time operations are only "constant" relative to the size of the map.

### Collisions

When different keys convert to the same integer, it is called a collision. Without handling collisions, older keys will get overridden and data will be lost. There are [multiple ways](https://en.wikipedia.org/wiki/Hash_table#Collision_resolution) to handle collisions, but here we'll talk about a common one called chaining.

If you don't know what a linked list is, don't worry, they are the focus of the next chapter. For now, you can imagine them as a data structure similar to an array.

When using chaining, we store linked lists inside the hash map's array instead of the elements themselves. The linked list nodes store both the key and the value. If there are collisions, the collided key-value pairs are linked together in a linked list. Then, when trying to access one of these key-value pairs, we traverse through the linked list until the key matches.

>If this part is confusing to you, don't worry. Every major programming language's hash map implementation will handle collisions automatically. The only reason to understand the inner workings of a hash map is that an interviewer may ask you trivia or want to discuss tradeoffs of using a hash map, but this is rare.

Collisions are problematic because handling them is necessary, and handling them takes time, slowing down the overall speed and efficiency of the hash map. How can we design our hash map to minimize collisions? The most important thing is that the size of your hash table's array and modulus is a prime number. Prime numbers near significant magnitudes that are common to use are:

- 10,007
- 1,000,003
- 1,000,000,007


### Sets
A set is another data structure that is very similar to a hash table. It uses the same mechanism for hashing keys into integers. The difference between a set and hash table is that sets do not map their keys to anything. Sets are more convenient to use when you only care about checking if elements exist. You can add, remove, and check if an element exists in a set all in **O(1)**.

An important thing to note about sets is that they don't track frequency. If you have a set and add the same element 100 times, the first operation adds it and the next 99 do nothing.

### Arrays as keys?
We said that being immutable is a requirement for being a hash map key. Arrays are mutable, so how do we store an ordered collection of elements as a key? Depending on the language you're using, there are several ways to convert an array into a unique immutable key. In Python, tuples are immutable, so it's as easy as doing tuple(arr). Another trick is to convert the array into a string, delimited by some character that is guaranteed to not show up in any element. For example, use a comma to separate integers. [1, 51, 163] --> "1,51,163".