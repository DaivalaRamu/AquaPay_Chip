# SPDX-FileCopyrightText: © 2024 Tiny Tapeout
# SPDX-License-Identifier: Apache-2.0

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    dut._log.info("Start AquaPay Chip Test")

    # Clock setup (10 us period)
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    # Reset
    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 5)
    dut.rst_n.value = 1

    # -------------------------------
    # TEST ₹1 → 2 Liters
    # -------------------------------
    dut._log.info("Testing ₹1 → 2 Liters")
    dut.ui_in.value = 1

    await ClockCycles(dut.clk, 20)

    value = dut.uo_out.value.integer
    tap = value & 0x1
    liters = (value >> 1) & 0x7F

    dut._log.info(f"Tap={tap}, Liters={liters}")
    assert liters == 2, "₹1 should give 2 liters"

    # -------------------------------
    # TEST ₹2 → 5 Liters
    # -------------------------------
    dut._log.info("Testing ₹2 → 5 Liters")
    dut.ui_in.value = 2

    await ClockCycles(dut.clk, 50)

    value = dut.uo_out.value.integer
    tap = value & 0x1
    liters = (value >> 1) & 0x7F

    dut._log.info(f"Tap={tap}, Liters={liters}")
    assert liters == 5, "₹2 should give 5 liters"

    # -------------------------------
    # TEST ₹5 → 20 Liters
    # -------------------------------
    dut._log.info("Testing ₹5 → 20 Liters")
    dut.ui_in.value = 5

    await ClockCycles(dut.clk, 200)

    value = dut.uo_out.value.integer
    tap = value & 0x1
    liters = (value >> 1) & 0x7F

    dut._log.info(f"Tap={tap}, Liters={liters}")
    assert liters == 20, "₹5 should give 20 liters"

    # -------------------------------
    # TEST ₹10 → 40 Liters
    # -------------------------------
    dut._log.info("Testing ₹10 → 40 Liters")
    dut.ui_in.value = 10

    await ClockCycles(dut.clk, 400)

    value = dut.uo_out.value.integer
    tap = value & 0x1
    liters = (value >> 1) & 0x7F

    dut._log.info(f"Tap={tap}, Liters={liters}")
    assert liters == 40, "₹10 should give 40 liters"

    dut._log.info("All tests PASSED ✅")
