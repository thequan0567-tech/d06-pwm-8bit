module d06_pwm_8bit_explicit #(
    parameter int WIDTH = 8
)(
    input  logic             clk,
    input  logic             rst_n,
    input  logic             ena,
    input  logic             enable,
    input  logic             phase_invert,
    input  logic [WIDTH-1:0] ui_in,
    output logic [WIDTH-1:0] uo_out
);
    logic [WIDTH-1:0] cnt;

    always_ff @(posedge clk) begin
        if (!rst_n) begin
            cnt <= '0;
        end else if (ena) begin
            cnt <= enable ? (cnt + 1'b1) : '0;
        end
    end

    always_comb begin
        uo_out[0]         = enable ? ((cnt < ui_in) ^ phase_invert) : 1'b0;
        uo_out[WIDTH-1:1] = cnt[WIDTH-1:1];
    end
endmodule
