### Sorted

func: sorted(iterable, *, key=func, reverse=False)
eg. 
* sorted(strs, key=len)
* sorted(strs, key=lambda x: x*2)
* sorted(strs, key=str.lower)
* sorted(student_objects, key=attrgetter('age'))
* sorted(student_objects, key=attrgetter('age'), reverse=True)

        
```
>>>from operator import itemgetter, attrgetter
>>>sorted(student_tuples, key=itemgetter(2))
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]
>>> sorted(student_objects, key=attrgetter('age'))
[('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]


# order by grade and age.
>>> sorted(student_tuples, key=itemgetter(1,2))
[('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]
>>> sorted(student_objects, key=attrgetter('grade', 'age'))
[('john', 'A', 15), ('dave', 'B', 10), ('jane', 'B', 12)]
```

#### Ascending and Descending
Both list.sort() and sorted() accept a reverse parameter with a boolean value. This is used to flag descending sorts. For example, to get the student data in reverse age order:
```
>>> sorted(student_tuples, key=itemgetter(2), reverse=True)
[('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]

>>> sorted(student_objects, key=attrgetter('age'), reverse=True)
[('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]
```
