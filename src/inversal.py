# Nome: Yan Rodrigues da Silva
# Matrícula: 495532

def merge(a: list, b: list) -> list:
    i, j = 0, 0
    max = []

    while i < len(a) and j < len(b):
        if a[i] > b[j]:
            max.append(a[i])
            i += 1
        else:
            max.append(b[j])
            j += 1

    while i < len(a):
        max.append(a[i])
        i += 1

    while j < len(b):
        max.append(b[j])
        j += 1

    return max


def inversal_sort(arr: list) -> list:
    if len(arr) < 2:
        return arr
    left = inversal_sort(arr[: len(arr) // 2])
    right = inversal_sort(arr[len(arr) // 2 :])
    return merge(left, right)
