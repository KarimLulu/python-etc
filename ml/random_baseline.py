import argparse
import numpy as np
from typing import Union


def random_baseline(size: int = 1000, n_labels: int = 2) -> np.ndarray:
    return np.random.randint(0, n_labels, size=size)


def label_distribution_baseline(
        label_frequencies: Union[list, np.ndarray] = None,
        size: int = 100
) -> np.ndarray:
    if label_frequencies is None:
        label_frequencies = [90, 10]
    if not isinstance(label_frequencies, np.ndarray):
        label_frequencies = np.array(label_frequencies)
    label_frequencies = label_frequencies.astype(float)
    label_frequencies /= label_frequencies.sum(axis=0, keepdims=1)
    return np.random.choice(len(label_frequencies), size=size, p=label_frequencies)


def zero_baseline(label_frequencies, size: int = 100):
    ind = np.argmax(label_frequencies)
    return np.ones(size) * ind


def calculate_metrics(y_true: np.ndarray, y_pred: np.ndarray):
    tp = (y_true & y_pred).sum()
    fp = (y_pred & (~y_true)).sum()
    fn = (~y_pred & y_true).sum()
    tn = ((~y_pred) & (~y_true)).sum()
    tpr = tp / (tp + fn)
    precision = tp / (tp + fp)
    fpr = fp / (tn + fp)
    f1 = 2 * tpr * precision / (precision + tpr)
    return {
        "Recall": round(tpr, 2),
        "Precision": round(precision, 2),
        "FPR": round(fpr, 2),
        "F1": round(f1, 2)
    }


def print_metrics(metrics: dict):
    for name, value in metrics.items():
        print(f"{name}: {value}")


def main(args: argparse.Namespace):
    size, n_labels, frequencies = args.size, args.n_labels, args.freqs
    uniform = random_baseline(size, n_labels).astype(bool)
    label_dist = label_distribution_baseline(frequencies, size).astype(bool)
    zero = zero_baseline(frequencies, size).astype(bool)
    y_true = label_distribution_baseline(frequencies, size)
    for name, y_pred in [("Uniform", uniform), ("Label distribution", label_dist), ("Zero baseline", zero)]:
        metrics = calculate_metrics(y_true, y_pred)
        print(name)
        print("=" * len(name))
        print_metrics(metrics)
        print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--size", type=int, default=1_000_000)
    parser.add_argument("--n_labels", type=int, default=2)
    parser.add_argument("--freqs", nargs="+", type=int, default=[70, 30])
    args = parser.parse_args()
    main(args)
