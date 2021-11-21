def fairIndexes(A, B):
    sumA = sum(A)
    sumB = sum(B)

    tmpA, tmpB, ans = 0, 0, 0

    for idx in range(len(A)):
        tmpA += A[idx]
        tmpB += B[idx]

        if sumA == 2 * tmpA and sumB == 2 * tmpA and tmpA == tmpB:
            ans += 1
    return ans


A = [1,4,2,-2,5]
B = [7,-2,-2,2,5]

print(fairIndexes(A, B))
