import argparse
from Combine import Combine
from typing import List

def MergeSort(A: List[int]) -> List[int]:
    n = len(A)

    if n == 1:
        return A

    m = n // 2
    B1 = MergeSort(A[0:m])
    B2 = MergeSort(A[m:])

    return Combine(B1, B2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-A",
        "--Array",
        required=True,
        nargs="+",
        help="<Required> Integer array to be sorted",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Verbosity flag",
    )
    args = parser.parse_args()

    A = list(map(int, args.Array))
    sorted_A = MergeSort(A)
    
    print(f"Original: {A}\nSorted: {sorted_A}" if args.verbose else f"A: {sorted_A}")
