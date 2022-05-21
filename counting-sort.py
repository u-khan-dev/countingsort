def countSort(arr, out, maximum):
    count = [0] * (maximum + 1)

    for i in range(len(arr)):
        count[arr[i]] += 1

    for i in range(1, maximum + 1):
        count[i] = count[i - 1] + count[i]

    for j in reversed(range(len(arr))):
        out[count[arr[j]] - 1] = arr[j]
        count[arr[j]] -= 1

    return out


def main():
    arr = [5, 10, 2, 12, 5, 9, 0, 0, 0, 11, 17, 4, 3, 37, 20, 91]
    max_element = int(max(arr))
    output_arr = [0] * len(arr)
    print("\nOriginal array is " + str(arr))
    ans = countSort(arr, output_arr, max_element)
    print("\nSorted array is " + str(ans))


if __name__ == '__main__':
    main()
