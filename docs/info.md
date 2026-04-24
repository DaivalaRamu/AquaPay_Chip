How it works

The AquaPay Chip is a coin-based smart water dispensing controller designed for water ATM systems.

The chip accepts coin inputs and dispenses a predefined amount of water using a hybrid control mechanism:

Flow-based control: Counts water using a flow sensor (1 pulse = 1 unit of water)
Time-based control: Limits dispensing duration to prevent overflow or sensor failure
💡 Coin to Water Mapping
₹1 → 2 Liters
₹2 → 5 Liters
₹5 → 20 Liters
₹10 → 40 Liters
⚙️ Working Steps
User inserts a coin (input signal)
Chip sets target water amount and time limit
Valve turns ON
Water flow is counted using the flow sensor
Valve turns OFF when:
Target liters reached, OR
Time limit exceeded (safety feature)

This ensures accurate and safe water dispensing, even under low pressure or sensor faults.

How to test
🔌 Inputs (ui_in)
ui_in[0] → ₹1 coin
ui_in[1] → ₹2 coin
ui_in[2] → ₹5 coin
ui_in[3] → ₹10 coin
ui_in[4] → Flow sensor pulse
📤 Outputs (uo_out)
uo_out[0] → Valve ON/OFF
uo_out[1:7] → Water dispensed (binary count)
🧪 Test Procedure
Apply reset (rst_n = 0 → 1)
Insert coin by setting corresponding input HIGH for 1 clock cycle
Generate flow pulses using ui_in[4]
Observe:
Valve turns ON
Water count increases
Valve turns OFF at correct limit
✅ Example Test (₹5 coin)
Set ui_in[2] = 1 (₹5)
Provide 20 flow pulses on ui_in[4]
Output:
Valve ON during flow
Turns OFF after 20 pulses
External hardware

This design is fully digital and does not require external hardware for simulation.

However, for real-world deployment, the following components can be connected:

Water flow sensor (pulse output type)
Solenoid valve (controlled via driver circuit)
Coin detection module
Power supply and control circuitry
