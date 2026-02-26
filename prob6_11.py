# prob6_11.py
# I compute sample means and standard errors for b1, b2, and B (converted to degrees),
# then estimate A = 0.5*b1*b2*sin(B) and propagate uncertainty with a first-order (FOSM) approximation.

from __future__ import annotations

import math
import statistics


def main() -> None:
    b1 = [120.4, 119.8, 120.2, 120.3, 119.6]
    b2 = [89.8, 89.6, 90.4, 90.2, 89.5]
    B_deg = [
        60.0 + 20.0 / 60.0,
        60.0 + 10.0 / 60.0,
        59.0 + 45.0 / 60.0,
        59.0 + 35.0 / 60.0,
        60.0 + 5.0 / 60.0,
    ]

    n = len(b1)

    b1_bar = sum(b1) / n
    b2_bar = sum(b2) / n
    B_bar_deg = sum(B_deg) / n

    s_b1 = statistics.stdev(b1)
    s_b2 = statistics.stdev(b2)
    s_B_deg = statistics.stdev(B_deg)

    se_b1 = s_b1 / math.sqrt(n)
    se_b2 = s_b2 / math.sqrt(n)
    se_B_deg = s_B_deg / math.sqrt(n)
    se_B_min = se_B_deg * 60.0

    # Area estimate
    B_bar_rad = math.radians(B_bar_deg)
    A_hat = 0.5 * b1_bar * b2_bar * math.sin(B_bar_rad)

    # FOSM standard error for A_hat (assuming independence)
    var_b1 = se_b1**2
    var_b2 = se_b2**2
    se_B_rad = math.radians(se_B_deg)
    var_B = se_B_rad**2

    dA_db1 = 0.5 * b2_bar * math.sin(B_bar_rad)
    dA_db2 = 0.5 * b1_bar * math.sin(B_bar_rad)
    dA_dB = 0.5 * b1_bar * b2_bar * math.cos(B_bar_rad)

    var_A = (dA_db1**2) * var_b1 + (dA_db2**2) * var_b2 + (dA_dB**2) * var_B
    se_A = math.sqrt(var_A)

    # 90% CI uses z_{0.95}
    z_095 = 1.6448536269514722
    ci_lo = A_hat - z_095 * se_A
    ci_hi = A_hat + z_095 * se_A

    print("Part (a) means")
    print(f"  b1_bar = {b1_bar:.2f} m")
    print(f"  b2_bar = {b2_bar:.2f} m")
    print(f"  B_bar  = {B_bar_deg:.6f} deg")
    print("Part (b) standard errors")
    print(f"  SE(b1_bar) = {se_b1:.6f} m")
    print(f"  SE(b2_bar) = {se_b2:.6f} m")
    print(f"  SE(B_bar)  = {se_B_min:.3f} arcmin")
    print("Part (c) area + SE")
    print(f"  A_hat  = {A_hat:.6f} m^2")
    print(f"  SE(A)  = {se_A:.6f} m^2")
    print("Part (d) 90% CI")
    print(f"  90% CI = [{ci_lo:.6f}, {ci_hi:.6f}] m^2")


if __name__ == "__main__":
    main()