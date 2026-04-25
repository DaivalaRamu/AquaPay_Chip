# AquaPay Chip

## Description
This project implements the AquaPay chip design for TinyTapeout.  
It is a simple digital circuit designed for demonstration and testing purposes.

---

## How it works
The design takes input signals and processes them based on predefined logic.

- Inputs are taken through designated pins.
- Internal logic performs operations (e.g., control/payment logic).
- Output is generated accordingly.

Example:
- If input = valid signal → output = success
- If input = invalid → output = failure

---

## How to test

### Step 1: Provide Inputs
Apply test signals to the input pins using a testbench or simulator.

### Step 2: Run Simulation
Use a Verilog simulator (like Icarus Verilog or TinyTapeout test setup).

### Step 3: Verify Output
Check if output matches expected behavior.

Example test cases:
- Input = 0001 → Output = 1
- Input = 0000 → Output = 0

---

## Author
Ramu
