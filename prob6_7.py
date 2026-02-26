# prob6_7.py
# I compute the Rayleigh MLE a_hat = sqrt( (1/(2n)) * sum(h_i^2) ) for the given wave heights.

from __future__ import annotations

import math

def main() -> None:
    h = [1.50, 2.80, 2.50, 3.20, 1.90, 4.10, 3.60, 2.60, 2.90, 2.30]
    n = len(h)

    sum_sq = sum(x * x for x in h)
    a_hat = math.sqrt(sum_sq / (2.0 * n))

    print(f"n = {n}")
    print(f"sum(h_i^2) = {sum_sq:.4f}")
    print(f"a_hat = sqrt(sum(h_i^2)/(2n)) = {a_hat:.6f} m")

if __name__ == "__main__":
    main()