# prob6_9.py
# I compute (a) and (b) sample means + standard errors, then (c) H_hat = I + L*tan(B),
# and (d) the propagated standard error of H_hat using first-order error propagation.

from __future__ import annotations

import math
import statistics


def main() -> None:
    # (a) Distance measurements (ft)
    L = [124.30, 124.20, 124.40]
    nL = len(L)
    L_bar = sum(L) / nL
    sL = statistics.stdev(L)          # sample stdev (n-1 in denominator)
    se_L = sL / math.sqrt(nL)

    # (b) Angle measurements: 40 degrees + minutes
    mins = [24.6, 25.0, 25.5, 24.7, 25.2]
    deg = 40.0
    B_deg = [deg + m / 60.0 for m in mins]
    nB = len(B_deg)
    B_bar_deg = sum(B_deg) / nB
    sB_deg = statistics.stdev(B_deg)
    se_B_deg = sB_deg / math.sqrt(nB)
    se_B_min = se_B_deg * 60.0

    # (c) Height estimate
    I_hat = 3.0
    B_bar_rad = math.radians(B_bar_deg)
    H_hat = I_hat + L_bar * math.tan(B_bar_rad)

    # (d) Propagated SE for H_hat assuming independence
    sigma_I = 0.01
    var_L = se_L**2
    se_B_rad = math.radians(se_B_deg)
    var_B = se_B_rad**2
    var_I = sigma_I**2

    tanB = math.tan(B_bar_rad)
    sec2B = 1.0 / (math.cos(B_bar_rad) ** 2)

    var_H = (tanB**2) * var_L + ((L_bar * sec2B) ** 2) * var_B + var_I
    se_H = math.sqrt(var_H)

    # (e) 98% CI (two-sided): z_{0.99}
    z_099 = 2.3263478740408408
    ci_lo = H_hat - z_099 * se_H
    ci_hi = H_hat + z_099 * se_H

    print("Part (a)")
    print(f"  L_bar = {L_bar:.2f} ft")
    print(f"  SE(L_bar) = {se_L:.4f} ft")
    print("Part (b)")
    print(f"  B_bar = {B_bar_deg:.6f} deg")
    print(f"  SE(B_bar) = {se_B_min:.3f} arcmin")
    print("Part (c)")
    print(f"  H_hat = {H_hat:.6f} ft")
    print("Part (d)")
    print(f"  SE(H_hat) = {se_H:.6f} ft")
    print("Part (e)")
    print(f"  98% CI = [{ci_lo:.6f}, {ci_hi:.6f}] ft")


if __name__ == "__main__":
    main()