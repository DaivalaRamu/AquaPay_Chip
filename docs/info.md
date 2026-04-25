# AquaPay Chip

## Description
AquaPay Chip is a coin-based smart water dispensing system.  
It accepts coins and controls a water valve based on the inserted amount.  
Water flow is measured using a flow sensor.

---

## How it works

- The system accepts coin inputs:
  - ui[0] → ₹1
  - ui[1] → ₹2
  - ui[2] → ₹5
  - ui[3] → ₹10

- Total amount is calculated internally.

- Based on the amount:
  - Water valve (uo[0]) turns ON
  - Water is dispensed

- Flow sensor (ui[4]) counts pulses:
  - Each pulse = small quantity of water
  - Pulses are converted into liters

- Output:
  - uo[1] to uo[7] → binary value of liters dispensed

- Reset (ui[5]) clears system.

---

## How to test

1. Apply clock (1 MHz default)

2. Insert coins:
   - Set ui[0..3] HIGH one by one

3. Check:
   - uo[0] = 1 → valve ON

4. Simulate flow sensor:
   - Toggle ui[4] to generate pulses

5. Observe:
   - uo[1..7] increasing (liters output)

6. Reset:
   - Set ui[5] = 1 → system resets

---

## Pinout

| Pin | Function |
|-----|--------|
| ui[0] | Coin ₹1 |
| ui[1] | Coin ₹2 |
| ui[2] | Coin ₹5 |
| ui[3] | Coin ₹10 |
| ui[4] | Flow Sensor |
| ui[5] | Reset |
| uo[0] | Valve Control |
| uo[1-7] | Liters Output |

---

## Notes

- Designed for TinyTapeout SKY130
- Works with simple FSM logic
- Suitable for smart water vending systems
