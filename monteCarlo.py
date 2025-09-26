import numpy as np
import matplotlib.pyplot as plt
from math import sqrt
import pandas as pd

def monte_carlo_uncertainty(inputs, N=200_000, confidence=95, seed=42):
    np.random.seed(seed)

    samples = np.zeros((N, len(inputs)))
    summary_rows = []

    for idx, (name, dist, u) in enumerate(inputs):
        if u == 0:
            arr = np.zeros(N)
        else:
            if dist.lower() == "normal":
                arr = np.random.normal(0.0, u, N)
            elif dist.lower() == "rect":
                a = sqrt(3) * u
                arr = np.random.uniform(-a, a, N)
            else:
                raise ValueError(f"Distribusi {dist} tidak dikenali")
        samples[:, idx] = arr
        summary_rows.append({
            "name": name,
            "dist": dist,
            "u_given": u,
            "sample_std": np.std(arr, ddof=1)
        })

    # Gabungan
    Y = np.sum(samples, axis=1)

    # Statistik
    y_mean = np.mean(Y)
    u_c = np.std(Y, ddof=1)

    alpha = (100 - confidence) / 2
    low, high = np.percentile(Y, [alpha, 100-alpha])
    halfwidth = (high - low) / 2
    k = halfwidth / u_c

    summary_df = pd.DataFrame(summary_rows)

    result = {
        "N_samples": N,
        "Y_mean": y_mean,
        "u_c (std dev)": u_c,
        f"{confidence}% interval": (low, high),
        "expanded_uncertainty": halfwidth,
        "coverage_factor k": k
    }
    return result, summary_df, Y


if __name__ == "__main__":
    inputs = [
        ("Urep", "Normal", 0),
        ("uRes", "Rect", 0.1),
        ("uUTC", "Normal", 3.58E-16),
        ("uLink", "Normal", 9.82E-16),
        ("uUTC(IDN)", "Normal", 5.73E-14),
        ("ustab", "Normal", 8.53E-14),
        ("uDA", "Rect", 1.00E-12),
        ("uCx", "Rect", 1.00E-15),
        ("uSG", "Normal", 3.19E-03),
    ]

    result, summary_df, Y = monte_carlo_uncertainty(inputs, N=200_000, confidence=95)

    print("\n=== Hasil Evaluasi Ketidakpastian Gabungan (Monte Carlo) ===")
    for k, v in result.items():
        print(f"{k}: {v}")

    print("\n=== Ringkasan Input ===")
    print(summary_df)

    # Plot distribusi Monte Carlo
    plt.figure(figsize=(10,5))
    plt.hist(Y, bins=100, density=True, alpha=0.7, color="skyblue", edgecolor="k")
    plt.axvline(result["Y_mean"], color="red", linestyle="--", label="Mean")
    plt.axvline(result["Y_mean"] - result["expanded_uncertainty"], color="green", linestyle="--", label="95% CI")
    plt.axvline(result["Y_mean"] + result["expanded_uncertainty"], color="green", linestyle="--")
    plt.title("Distribusi Ketidakpastian Gabungan (Monte Carlo)")
    plt.xlabel("Output Y")
    plt.ylabel("Kerapatan probabilitas")
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.show()
