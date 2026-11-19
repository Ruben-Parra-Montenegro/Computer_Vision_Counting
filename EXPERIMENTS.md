# Experiments

Notes on experiments to run for the project. These are plans, not results.

## Experiment 1: Lighting robustness

Capture parts under bright, dim, and uneven illumination. Compare the fixed threshold of 200 against Otsu's automatic thresholding.

Question: does adaptive threshold selection improve accuracy?

## Experiment 2: Touching objects

Compare separated nuts against nuts touching one another. Show where connected components fail.

Optional: investigate distance transforms and watershed segmentation to separate touching parts. The placeholder for this is [functions/separate_touching.py](./functions/separate_touching.py).

## Experiment 3: Algorithm performance

Compare the Python-loop thresholding against NumPy vectorization. Measure processing latency and frames per second.

This gives the project a computational-performance section.
