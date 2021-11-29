"""
855. Exam Room
In an exam room, there are N seats in a single row, numbered 0, 1, 2, ..., N-1.-

When a student enters the room, they must sit in the seat that maximizes the distance to the closest person.
If there are multiple such seats, they sit in the seat with the lowest number.
(Also, if no one is in the room, then the student sits at seat number 0.)

Return a class ExamRoom(int N) that exposes two functions: ExamRoom.seat()
returning an int representing what seat the student sat in, and ExamRoom.leave(int p) representing
that the student in seat number p now leaves the room.
It is guaranteed that any calls to ExamRoom.leave(p) have a student sitting in seat p.


Example 1:
Input: ["ExamRoom","seat","seat","seat","seat","leave","seat"], [[10],[],[],[],[],[4],[]]
Output: [null,0,9,4,2,null,5]
Explanation:
ExamRoom(10) -> null
seat() -> 0, no one is in the room, then the student sits at seat number 0.
seat() -> 9, the student sits at the last seat number 9.
seat() -> 4, the student sits at the last seat number 4.
seat() -> 2, the student sits at the last seat number 2.
leave(4) -> null
seat() -> 5, the student sits at the last seat number 5.

Note:

1 <= N <= 10^9
ExamRoom.seat() and ExamRoom.leave() will be called at most 10^4 times across all test cases.
Calls to ExamRoom.leave(p) are guaranteed to have a student currently sitting in seat number p.
"""
import heapq
import bisect


class ExamRoom:
    """
    Google OA Problem
    Uber OA Problem
    """
    def __init__(self, N: int):
        self.N = N
        self.students = []
        self.distance = 0

    def seat(self) -> int:
        if not self.students:
            self.students = [0]
            return 0

        # initial the room and the student
        self.distance, student = self.students[0], 0

        for idx in range(1, len(self.students)):
            left, right = self.students[idx - 1], self.students[idx]
            if (right - left) // 2 > self.distance:
                self.distance, student = (right - left) // 2, (right + left) // 2

        if self.students[-1] != self.N - 1:
            if self.N - 1 - self.students[-1] > self.distance:
                student = self.N - 1

        # This module provides support for maintaining a list in sorted order
        # without having to sort the list after each insertion
        # ------------------------------------------------------------------------
        # The purpose of Bisect algorithm is to find a position in list
        # where an element needs to be inserted to keep the list sorted.
        # O(n)
        bisect.insort(self.students, student)
        return student

    def leave(self, p: int) -> None:
        self.students.remove(p)


class ExamRoomSolution:
    """
    heapq is min heap, if want to start with large we call max heap, can input -x,
    let x = -x after pop up.
    """
    def __init__(self, N: int):
        self.N = N
        self.students_maxheap = [(self.dist_check(-1, self.N), -1, self.N)]

    def dist_check(self, left, right):
        if left == -1 or right == self.N:
            return -(right - left - 1)
        else:
            return -((right - left) // 2)

    def seat(self) -> int:
        dist, left, right = heapq.heappop(self.students_maxheap)
        dist = -dist

        if left == -1:
            student = 0
        elif left == self.N:
            student = self.N - 1
        else:
            student = left + dist

        heapq.heappush(self.students_maxheap, (self.dist_check(left, student), left, student))
        heapq.heappush(self.students_maxheap, (self.dist_check(student, right), student, right))
        return student

    def leave(self, p: int) -> None:
        remove = []
        start = end = 0
        for idx in range(len(self.students_maxheap)):
            dist, left, right = self.students_maxheap[idx]
            if left == p:
                end = right
                remove.append((dist, left, right))
            if right == p:
                start = left
                remove.append((dist, left, right))
        for rm in remove:
            self.students_maxheap.remove(rm)

        self.students_maxheap.append((self.dist_check(start, end), start, end))
        heapq.heapify(self.students_maxheap)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)

"""
------------------------------------------------------------
bisect maintain the list.
------------------------------------------------------------
"""

# initializing list
li = [1, 3, 4, 4, 4, 6, 7]
# ----- Search: O(log(n)) -> Bisect method works on the concept of binary search
# using bisect() to find index to insert new element
# returns 5 ( right most possible index )
print("The rightmost index to insert, so list remains sorted is", end=" - ")
print(bisect.bisect(li, 4))
print(bisect.bisect_right(li, 4))

# using bisect_left() to find index to insert new element
# returns 2 ( left most possible index )
print("The leftmost index to insert, so list remains sorted is", end=" - ")
print(bisect.bisect_left(li, 4))

# using bisect_right() to find index to insert new element
# returns 4 ( right most possible index )
print("The rightmost index to insert, so list remains sorted is", end=" - ")
print(bisect.bisect_right(li, 4, 0, 4))

#  ----- insert: O(n) -> Inserting an element in sorted array requires traversal
# initializing list
li1 = [1, 3, 4, 4, 4, 6, 7]

# initializing list
li2 = [1, 3, 4, 4, 4, 6, 7]

# initializing list
li3 = [1, 3, 4, 4, 4, 6, 7]

# using insort() to insert 5 at appropriate position
# inserts at 6th position
bisect.insort(li1, 5)

print("The list after inserting new element using insort() is : ")
for i in range(0, 7):
    print(li1[i], end=" ")

# using insort_left() to insert 5 at appropriate position
# inserts at 6th position
bisect.insort_left(li2, 5)

print("\r")

print("The list after inserting new element using insort_left() is : ")
for i in range(0, 7):
    print(li2[i], end=" ")

print("\r")

# using insort_right() to insert 5 at appropriate position
# inserts at 5th position
bisect.insort_right(li3, 5, 0, 4)

print("The list after inserting new element using insort_right() is : ")
for i in range(0, 7):
    print(li3[i], end=" ")


"""
------------------------------------------------------------
heapq:  the property of this data structure in Python is that each time the smallest of heap element is popped(min heap)
whenever elements are pushed or popped, the heap structure in maintained. the heap[0] element also returns the smallest
element each time
------------------------------------------------------------
"""
