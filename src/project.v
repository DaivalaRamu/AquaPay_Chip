/*
 * AquaPay Chip - Smart Water ATM
 * Coin-based water dispensing with flow + time control
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_um_aquapay_chip (
    input  wire [7:0] ui_in,    // Inputs
    output wire [7:0] uo_out,   // Outputs
    input  wire [7:0] uio_in,   // Not used
    output wire [7:0] uio_out,  
    output wire [7:0] uio_oe,   
    input  wire       ena,      
    input  wire       clk,      
    input  wire       rst_n     
);

  // ---------------- INPUT MAPPING ----------------
  wire coin_1      = ui_in[0];
  wire coin_2      = ui_in[1];
  wire coin_5      = ui_in[2];
  wire coin_10     = ui_in[3];
  wire flow_sensor = ui_in[4];

  wire rst = ~rst_n;

  // ---------------- INTERNAL REGS ----------------
  reg valve_on;
  reg [7:0] liters;

  reg [1:0] state;
  reg [7:0] target;
  reg [7:0] coin_reg;
  reg [7:0] coin_value;

  reg [15:0] timer;
  reg [15:0] time_limit;

  localparam IDLE=0, SET=1, DISP=2, DONE=3;

  // ---------------- FSM LOGIC ----------------
  always @(posedge clk or posedge rst) begin
    if (rst) begin
        state <= IDLE;
        liters <= 0;
        valve_on <= 0;
        coin_reg <= 0;
        target <= 0;
        coin_value <= 0;
        timer <= 0;
        time_limit <= 0;
    end else begin

        case(state)

        // -------- IDLE --------
        IDLE: begin
            liters <= 0;
            valve_on <= 0;
            timer <= 0;

            if (coin_1)      begin coin_reg <= 1;  state <= SET; end
            else if (coin_2) begin coin_reg <= 2;  state <= SET; end
            else if (coin_5) begin coin_reg <= 5;  state <= SET; end
            else if (coin_10)begin coin_reg <= 10; state <= SET; end
        end

        // -------- SET --------
        SET: begin
            case(coin_reg)
                1:  begin target <= 2;  time_limit <= 20;  end
                2:  begin target <= 5;  time_limit <= 50;  end
                5:  begin target <= 20; time_limit <= 200; end
                10: begin target <= 40; time_limit <= 400; end
                default: begin target <= 0; time_limit <= 0; end
            endcase

            coin_value <= coin_reg;
            timer <= 0;

            state <= DISP;
        end

        // -------- DISP --------
        DISP: begin
            valve_on <= 1;
            timer <= timer + 1;

            if (flow_sensor) begin
                liters <= liters + 1;
            end

            if ((liters >= target && target != 0) || (timer >= time_limit)) begin
                valve_on <= 0;
                state <= DONE;
            end
        end

        // -------- DONE --------
        DONE: begin
            state <= IDLE;
        end

        endcase
    end
  end

  // ---------------- OUTPUT MAPPING ----------------
  assign uo_out[0] = valve_on;

  // liters as binary output
  assign uo_out[1] = liters[0];
  assign uo_out[2] = liters[1];
  assign uo_out[3] = liters[2];
  assign uo_out[4] = liters[3];
  assign uo_out[5] = liters[4];
  assign uo_out[6] = liters[5];
  assign uo_out[7] = liters[6];

  // ---------------- UNUSED ----------------
  assign uio_out = 8'b0;
  assign uio_oe  = 8'b0;

  wire _unused = &{ena, uio_in, liters[7]};

endmodule
