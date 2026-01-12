import pennylane as qml
import qiskit
import torch

print(f"✅ PennyLane version: {qml.__version__}")
print(f"✅ Qiskit version: {qiskit.__version__}")
print(f"✅ PyTorch (ML) ready: {torch.__version__}")

# Simple Quantum Circuit Test
dev = qml.device("default.qubit", wires=1)

@qml.qnode(dev)
def circuit():
    qml.Hadamard(wires=0)
    return qml.expval(qml.PauliZ(0))

print(f"✅ Quantum Circuit Result: {circuit()}")
