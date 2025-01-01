# Nathaniel Branscum, 1/1/25
# Written with <3 in emacs from OKC
# Formatted by Black
# ToDo: Two pointer implementation that reduces mem usage

import argparse
from typing import List


def RecBinSearch(A: List[int], x: int) -> bool:
    n = len(A)

    # Base Cases
    if n == 0:
        return False
    if n == 1 and A[0] == x:
        return True

    m = n // 2

    if A[m] == x:
        return True

    # Recurse
    if x < A[m]:
        return RecBinSearch(A[0:m], x)
    else:
        return RecBinSearch(A[m + 1 :], x)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-a",
        "--array",
        required=True,
        nargs="+",
        help="<Required> Sorted integer array",
    )
    parser.add_argument(
        "-t",
        "--target",
        type=int,
        required=True,
        help="<Required> The target integer to search for",
    )
    args = parser.parse_args()

    A = list(map(int, args.array))
    x = args.target

    found = RecBinSearch(A, x)
    print(f"Result: {found} for {x} in array {A}")
