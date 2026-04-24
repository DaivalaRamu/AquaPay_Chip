# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start AquaPay Chip Test")

    # Clock: 100 KHz
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 5)
    dut.rst_n.value = 1

    # ---------------- ₹1 TEST ----------------
    dut._log.info("Testing ₹1 → 2 Liters")

    dut.ui_in.value = 0b00000001  # coin_1
    await ClockCycles(dut.clk, 1)
    dut.ui_in.value = 0

    # simulate 2 liters
    for i in range(2):
        dut.ui_in.value = 0b00010000  # flow_sensor
        await ClockCycles(dut.clk, 1)
        dut.ui_in.value = 0
        await ClockCycles(dut.clk, 1)

    await ClockCycles(dut.clk, 2)

    liters = (dut.uo_out.value >> 1) & 0x7F
    assert liters == 2, f"₹1 failed: got {liters}"

    # ---------------- ₹2 TEST ----------------
    dut._log.info("Testing ₹2 → 5 Liters")

    dut.ui_in.value = 0b00000010
    await ClockCycles(dut.clk, 1)
    dut.ui_in.value = 0

    for i in range(5):
        dut.ui_in.value = 0b00010000
        await ClockCycles(dut.clk, 1)
        dut.ui_in.value = 0
        await ClockCycles(dut.clk, 1)

    await ClockCycles(dut.clk, 2)

    liters = (dut.uo_out.value >> 1) & 0x7F
    assert liters == 5, f"₹2 failed: got {liters}"

    # ---------------- ₹5 TEST ----------------
    dut._log.info("Testing ₹5 → 20 Liters")

    dut.ui_in.value = 0b00000100
    await ClockCycles(dut.clk, 1)
    dut.ui_in.value = 0

    for i in range(20):
        dut.ui_in.value = 0b00010000
        await ClockCycles(dut.clk, 1)
        dut.ui_in.value = 0
        await ClockCycles(dut.clk, 1)

    await ClockCycles(dut.clk, 2)

    liters = (dut.uo_out.value >> 1) & 0x7F
    assert liters == 20, f"₹5 failed: got {liters}"

    # ---------------- ₹10 TEST ----------------
    dut._log.info("Testing ₹10 → 40 Liters")

    dut.ui_in.value = 0b00001000
    await ClockCycles(dut.clk, 1)
    dut.ui_in.value = 0

    for i in range(40):
        dut.ui_in.value = 0b00010000
        await ClockCycles(dut.clk, 1)
        dut.ui_in.value = 0
        await ClockCycles(dut.clk, 1)

    await ClockCycles(dut.clk, 2)

    liters = (dut.uo_out.value >> 1) & 0x7F
    assert liters == 40, f"₹10 failed: got {liters}"

    dut._log.info("All tests PASSED ✅")
