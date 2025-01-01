import argparse
from typing import List


def Combine(P: List[int], Q: List[int]) -> List[int]:
    # P and Q are sorted; outputs R a sorted array of elements in P and Q.
    i, j = 0, 0
    p = len(P)
    q = len(Q)
    R = []

    while i < p and j < q:
        if P[i] <= Q[j]:
            R.append(P[i])
            i += 1
        else:
            R.append(Q[j])
            j += 1
    if i >= p:
        R.extend(Q[j:])
    else:
        R.extend(P[i:])

    return R


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-P",
        required=True,
        nargs="+",
        help="<Required> First sorted integer array",
    )
    parser.add_argument(
        "-Q",
        required=True,
        nargs="+",
        help="<Required> Second sorted integer array",
    )
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        help="Verbosity flag",
    )
    args = parser.parse_args()

    P = list(map(int, args.P))
    Q = list(map(int, args.Q))

    R = Combine(P, Q)
    print(f"R: {R} Q: {Q} P:{P}" if args.verbose else f"R: {R}")
