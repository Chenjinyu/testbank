def fn(i):
    if i > 3:
        return

    print(i)
    fn(i + 1)
    print(f"End of call where i = {i}")
    return

fn(1)

"""
Output: 

// 1
// 2
// 3
// End of call where i = 3
// End of call where i = 2
// End of call where i = 1

"""