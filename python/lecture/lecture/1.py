list = []


def binaryse(list, l, r, numbersearch):
    mid = (r+l)//2
    if l == r+1 or r == l+1:
        print("not found")
    elif list[r] == numbersearch:
        print(f"number index is {r}")
    elif list[l] == numbersearch:
        print(f"number index is {l}")
    elif list[mid] == numbersearch:
        print(f"number index is {mid}")
    elif list[mid] > numbersearch:
        return binaryse(list, l, mid-1, numbersearch)
    elif list[mid] < numbersearch:
        return binaryse(list, mid+1, r, numbersearch)
