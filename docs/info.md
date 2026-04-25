# AquaPay Chip 💧

## Overview

AquaPay Chip is a digital water dispensing system implemented using Verilog.
It simulates a smart prepaid water system where users insert coins and receive water based on the amount.

---

## How it works ⚙️

The AquaPay Chip works based on simple input-output logic:

* User inserts money using input pins
* The system processes the value
* Based on the amount, water is dispensed

### Logic:

* ₹1 → 2 Liters
* ₹2 → 5 Liters
* ₹5 → 12 Liters

The chip continuously monitors inputs and updates output accordingly.

---

## Inputs 🧾

| Signal | Description             |
| ------ | ----------------------- |
| ui_in  | User input (coin value) |
| rst_n  | Reset signal            |
| clk    | Clock                   |

---

## Outputs 🚰

| Signal | Description                    |
| ------ | ------------------------------ |
| uo_out | Output showing liters of water |

---

## How to test 🧪

You can test the design using simulation:

### Steps:

1. Provide input value through `ui_in`
2. Run simulation using cocotb
3. Observe output in `uo_out`

### Expected Results:

| Input (₹) | Output (Liters) |
| --------- | --------------- |
| 1         | 2               |
| 2         | 5               |
| 5         | 12              |

---

## Tools Used 🛠️

* Verilog HDL
* Icarus Verilog
* Cocotb
* TinyTapeout

---

## Author 👨‍💻

Ramu
