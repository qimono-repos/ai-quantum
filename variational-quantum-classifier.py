# Variational Quantum Classifier
# - Install the required libraries
# - Import the required libraries
# - Generate + pre-process the data
# - Define the Quantum Feature Map
# - Define the Variational Quantum Circuit
# - Define the Quantum Classifier
# - Train the VQC model
# - Evaluate the model

import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import make_classification

from qiskit_aer import Aer 
from qiskit.primitives import StatevectorSampler 
from qiskit_machine_learning.algorithms.classifiers import VQC
from qiskit_machine_learning.kernels import FidelityQuantumKernel
from qiskit.circuit.library import ZZFeatureMap, RealAmplitudes, zz_feature_map #ZZFeatureMap is deprecated
from qiskit_algorithms.optimizers import COBYLA
from qiskit.transpiler import PassManager
from qiskit.transpiler.passes import Optimize1qGatesDecomposition, CommutativeCancellation

def main():
    # Generate + pre-process the data
    x, y = make_classification(
        n_samples=200,
        n_features=2,
        n_informative=2,
        n_redundant=0,
        n_clusters_per_class=1,
        class_sep=1.5,
        random_state=42,
    )

    # Normalize the data
    scaler = StandardScaler()
    x_scaled = scaler.fit_transform(x)

    x_train, x_test, y_train, y_test = train_test_split(
        x_scaled, y, test_size=0.2, random_state=42, stratify=y
    )

    # Define a quantum feature map (ZZFeatureMap is the canonical choice)
    try:
        feature_map = ZZFeatureMap(feature_dimension=2, reps=2, entanglement="linear")
    except Exception:
        # Fallback if helper function was used in notebook runs
        from qiskit.circuit.library.data_preparation import zz_feature_map

        feature_map = zz_feature_map(feature_dimension=2, reps=2, entanglement="linear")

    # Use a fidelity quantum kernel and a classical SVM with precomputed kernel
    from qiskit.primitives import Sampler
    from qiskit_aer import Aer
    from qiskit_machine_learning.kernels import FidelityQuantumKernel
    from sklearn.svm import SVC
    from sklearn.metrics import accuracy_score, classification_report

    # Create a primitive sampler (uses Aer if available)
    try:
        sampler = Sampler()
    except Exception:
        # If qiskit runtime primitives unavailable, try StatevectorSampler
        from qiskit.primitives import StatevectorSampler

        sampler = StatevectorSampler()

    kernel = FidelityQuantumKernel(feature_map=feature_map, quantum_instance=sampler)

    print("Computing training kernel matrix...")
    K_train = kernel.evaluate(x_vec=x_train)

    # Train an SVM on the quantum kernel
    clf = SVC(kernel="precomputed")
    clf.fit(K_train, y_train)

    # Evaluate on test set
    print("Computing test kernel matrix...")
    K_test = kernel.evaluate(x_vec=x_test, y_vec=x_train)
    y_pred = clf.predict(K_test)

    acc = accuracy_score(y_test, y_pred)
    print(f"Test accuracy: {acc:.3f}")
    print(classification_report(y_test, y_pred))

    # Optional: plot data and predictions (2D only)
    try:
        import matplotlib.pyplot as plt

        # Plot training data
        plt.figure(figsize=(8, 4))
        plt.subplot(1, 2, 1)
        plt.title("Training data")
        plt.scatter(x_train[:, 0], x_train[:, 1], c=y_train, cmap="bwr", edgecolor="k")

        # Plot test predictions
        plt.subplot(1, 2, 2)
        plt.title("Test predictions")
        plt.scatter(x_test[:, 0], x_test[:, 1], c=y_pred, cmap="bwr", edgecolor="k")
        plt.tight_layout()
        plt.show()
    except Exception:
        pass


if __name__ == "__main__":
    main()

