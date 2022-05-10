

# def power(r, n):
#     value = 1
#     for i in range(1, n + 1):
#         value = r * value
#     return value

# print("result", power(2, 3))


# def power(r, n):
#     if n == 1:
#         return r
#     return r * power(r, n - 1)

# print("result", power(2, 3))

def power(r, n):
    return r if n == 1 else r * power(r, n - 1)


print("result", power(2, 3))
