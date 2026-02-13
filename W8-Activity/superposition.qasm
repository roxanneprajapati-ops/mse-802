// This file creates a superposition using 1 qubit.
// The qubit is then measured and stored in a classical bit.

OPENQASM 2.0;
include "qelib1.inc";

//create 1 qubit register
qreg q[1];

// create 1 classical bit register
creg c[1];

// apply hadamard gate to qubit 0 to create superposition
h q[0];

//Measure qubit 0 and store result in classical bit 0
measure q[0] -> c[0];