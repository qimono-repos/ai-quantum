# Hybrid Quantum and Classical Computing in the NISQ Era

## Introduction

This document summarizes key concepts related to Support Vector Machines (SVM), Quantum Support Vector Machines (QSVM), Neural Networks (NN), Quantum Neural Networks (QNN), and hybrid quantum-classical approaches using Qiskit and PyTorch. The context is the current technological stage known as the NISQ (Noisy Intermediate-Scale Quantum) era.

---

## 1. Support Vector Machines (SVM)

A Support Vector Machine is a supervised learning algorithm used for classification tasks. Its main goal is to find a **decision boundary** that separates different classes of data.

- In 2D, the decision boundary is a line.
- In higher dimensions, it is called a **hyperplane**.

### Key Idea: Maximum Margin

SVM does not just separate classes—it maximizes the margin between the boundary and the closest data points. These closest points are called **support vectors**.

---

## 2. The Kernel Trick

Real-world data is often **not linearly separable**.

Example: the **make_moons dataset**, where two classes form interleaving crescent shapes.

### Solution: Kernel Trick

Instead of transforming data explicitly into higher dimensions, SVM uses a **kernel function**:

- It computes similarity between points as if they were in a higher-dimensional space.
- The actual transformation is never computed explicitly.

### Common Kernels

- Linear Kernel
- Polynomial Kernel (e.g., quadratic: x²-like behavior)
- Radial Basis Function (RBF) Kernel

Important insight:
> The dimensionality of the transformed space can be very high—even infinite (as in RBF).

---

## 3. Decision Boundary vs Hyperplane

- **Decision boundary**: general term for separation surface.
- **Hyperplane**: technical term used in higher dimensions.

They refer to the same concept depending on dimensionality.

---

## 4. Neural Networks (NN)

Neural networks are models composed of layers of interconnected neurons.

### Key Characteristics

- Learn **nonlinear transformations explicitly**
- Use **weights and biases**
- Trained using **backpropagation**

### Parameter Adjustment

- Loss function measures error
- Gradients are computed
- Weights updated via optimization (e.g., gradient descent)

---

## 5. SVM vs Neural Networks

### SVM

- Uses kernel (implicit transformation)
- Optimizes margin
- Fewer parameters

### Neural Networks

- Learn transformations explicitly
- Highly flexible
- Large number of parameters

Both are capable of solving **nonlinear classification problems** like make_moons.

---

## 6. Quantum Support Vector Machines (QSVM)

QSVM extends SVM into the quantum domain.

### Core Idea

- Use a **quantum feature map**
- Encode classical data into quantum states
- Compute similarities using quantum circuits

This replaces the classical kernel with a **quantum kernel**.

---

## 7. Quantum Neural Networks (QNN)

QNNs are analogous to classical neural networks but use **quantum circuits**.

### Structure

- Data encoding layer
- Parameterized quantum circuit (variational circuit)
- Measurement output

### Training

- Parameters adjusted using classical optimization
- Hybrid loop:
  - Quantum circuit computes output
  - Classical optimizer updates parameters

---

## 8. Hybrid Quantum-Classical Approach

This is the dominant paradigm in the **NISQ era**.

### Why Hybrid?

Quantum hardware is:

- Noisy
- Limited in qubits
- Not fault-tolerant

### Strategy

Combine:

- Classical computation (optimization, control)
- Quantum computation (state transformation, feature space)

---

## 9. Qiskit + PyTorch Integration

### Workflow

1. Classical preprocessing (PyTorch / NumPy)
2. Quantum circuit (Qiskit)
3. Output fed back into PyTorch model
4. Loss computed
5. Gradients update parameters

This enables:

- End-to-end differentiable hybrid models
- Integration with modern ML pipelines

---

## 10. Why Use the Same Dataset (make_moons)?

The make_moons dataset is used because:

- It is **nonlinear**
- It is **visually intuitive**
- It highlights differences in model capabilities

Using the same dataset across:

- SVM
- QSVM
- NN
- QNN

Allows understanding how different models solve the **same structural problem**.

---

## Final Insight

The unifying concept is:

> All models attempt to construct a decision boundary in a transformed space.

- SVM → implicit transformation via kernel
- NN → explicit learned transformation
- QSVM → quantum kernel
- QNN → quantum circuit as learnable transformation

---

## Conclusion

In the NISQ era, hybrid quantum-classical models are essential. Understanding classical methods like SVM and neural networks provides the foundation to understand their quantum counterparts.

The key learning is not just about quantum advantage, but about:

- Representation of data
- Transformation of feature spaces
- Construction of decision boundaries

This conceptual bridge is critical for advancing in quantum machine learning.
