# Custom PRNG vs NumPy Random: LCG Comparison

[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/nazibur175/Cryptography-and-Cyber-Law/blob/main/PRNG/lcg_vs_numpy.ipynb)

This project implements a simple **Linear Congruential Generator (LCG)**-based pseudorandom number generator and compares its output to NumPy's built-in random number generator. The goal is to evaluate and visualize the statistical quality and uniformity of the custom generator.

## Features

- Implementation of a custom PRNG using the LCG method
- 2D scatter plots to visually compare randomness
- Histograms to show distribution shape
- Summary statistics (mean & standard deviation) for both generators


## LCG Formula

The Linear Congruential Generator is defined by the recurrence relation:

Xₙ₊₁ = (a × Xₙ + c) mod m


Where:
- `a` → multiplier  
- `c` → increment  
- `m` → modulus  
- `X₀` → initial seed

This generator produces pseudorandom numbers scaled to the [0, 1) range.


## Visual Outputs

- `scatter_comparison.pdf`: Side-by-side scatter plots of (X, Y) points from LCG and NumPy
- `histogram_comparison.pdf`: Histogram distributions for X and Y values from both sources


## How to Run

### Option 1: Run in Google Colab (Recommended)
Just click the badge at the top of this page to open the notebook in Google Colab. No setup required.

### Option 2: Run Locally on Your Machine
1. Make sure you have Python 3.7+ installed.
2. Install the required packages:
```bash
pip install numpy matplotlib
```
Run the script:
```bash
python lcg_vs_numpy.py
```
Terminal will display the statistical summary of the generated values
