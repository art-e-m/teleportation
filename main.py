import numpy as np
from qiskit import(
  QuantumCircuit,
  ClassicalRegister,
  QuantumRegister,
  execute,
  BasicAer,
  )
from qiskit.visualization import plot_histogram
from qiskit.result import marginal_counts

cr1 = ClassicalRegister(1)
cr2 = ClassicalRegister(1)
cr3 = ClassicalRegister(1)
qr = QuantumRegister(3)
circuit = QuantumCircuit(qr, cr1, cr2, cr3)

circuit.h(1)
circuit.cx(1, 2)

circuit.barrier()
circuit.cx(1, 0)
circuit.h(0)

circuit.barrier()
circuit.measure(0, 0)
circuit.measure(1, 1)

circuit.barrier()
circuit.x(2).c_if(cr2, 1)
circuit.z(2).c_if(cr1, 1)

circuit.barrier()
circuit.measure(2, 2)

backend = BasicAer.get_backend('qasm_simulator')
job = execute(circuit, backend, shots=4321)
counts = job.result().get_counts(circuit)
qubit_counts = [marginal_counts(counts, [qubit]) for qubit in range(3)]

print(qubit_counts)
print(circuit.draw())
