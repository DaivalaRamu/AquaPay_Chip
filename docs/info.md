## How it works

The AquaPay_Chip is a coin-based water dispensing system implemented using Verilog.

- The system accepts coin inputs (Rs 1, Rs 2, Rs 5, Rs 10)
- Based on the coin value, a predefined amount of water is released
- A timer controls how long the tap remains open
- Water flow is counted in steps until the target level is reached
- Once the required amount is dispensed, the tap automatically closes

Example:
- Rs 2 → 5 liters
- Rs 5 → 20 liters
- Rs 10 → 40 liters

---

## How to test

1. Apply clock signal to the design
2. Reset the system using `rst_n = 0`, then set `rst_n = 1`
3. Provide coin input using `ui_in`:
   - 1 → Rs 1
   - 2 → Rs 2
   - 5 → Rs 5
   - 10 → Rs 10
4. Observe output on `uo_out`:
   - Tap ON/OFF signal
   - Water level increment
5. Verify:
   - Tap opens for correct duration
   - Water stops after reaching target level

---

## External hardware

- Water valve (solenoid valve)
- Relay module
- Water flow sensor (optional)
- Microcontroller (if interfacing outside chip)
