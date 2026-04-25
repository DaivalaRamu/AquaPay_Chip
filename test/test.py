import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def test_project(dut):
    dut._log.info("Start AquaPay Chip Test")

    # Reset
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.ena.value = 1

    await Timer(10, units="ns")

    # Input ₹1
    dut.ui_in.value = 1

    await Timer(100, units="ns")

    # Convert LogicArray → int
    output_val = dut.uo_out.value.integer

    # Extract liters
    liters = (output_val >> 1) & 0x7F

    dut._log.info(f"Output liters = {liters}")

    # Check result
    assert liters == 2, f"Expected 2 liters, got {liters}"
