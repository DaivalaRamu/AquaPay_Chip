# AquaPay Chip

## Description
AquaPay chip is a simple digital design that processes input signals and produces outputs based on predefined logic.

---

## How it works
The chip reads input signals from input pins and processes them using internal digital logic.

- Inputs are given through ui pins
- Logic block processes signals
- Output is produced on uo pins

Example:
- Valid input → Output HIGH
- Invalid input → Output LOW

---

## How to test

### Step 1
Provide inputs using testbench or simulator.

### Step 2
Run simulation using TinyTapeout tools.

### Step 3
Check outputs.

Test Cases:
- Input = 0001 → Output = 1
- Input = 0000 → Output = 0

---

## Author
Ramu
