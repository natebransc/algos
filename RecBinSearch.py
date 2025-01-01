import argparse
import typing

def RecBinSearch(A: list[int], x: int) -> bool:
    n = len(A)

    if n == 0:
        return False
    if n == 1 and A[0] == x:
        return True

    # Ceil division by double negation
    # Then reindex
    m = - (- n // 2) - 1
    
    if A[m] == x:
        return True
    if x < A[m]:
        return RecBinSearch(A[0:m-1], x)
    else:
        return RecBinSearch(A[m+1:], x)



if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-a", "--array", nargs = "+", help="<Required> Sorted integer array")
    parser.add_argument("-t", "--target", help="<Required> The target integer to search for")
    args = parser.parse_args()

    A = args.array
    x = args.target
    
    found = RecBinSearch(A, x)
    print(f"Result: {found} for {x} in array {A}")
