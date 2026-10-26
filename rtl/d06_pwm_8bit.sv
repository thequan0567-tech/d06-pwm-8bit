module d06_pwm_8bit #(
    parameter int WIDTH = 8
)(
    input  logic             clk,
    input  logic             rst_n,
    input  logic             ena,
    input  logic             enable,       // uio_in[0]: 1 = bat PWM, 0 = tat & xoa dem
    input  logic             phase_invert, // uio_in[1]: 0 = pha thuan, 1 = dao pha
    input  logic [WIDTH-1:0] ui_in,        // ui_in[7:0]: do rong xung (0..255)
    output logic [WIDTH-1:0] uo_out        // uo_out[0]=PWM, uo_out[7:1]=cnt[7:1]
);
    logic [WIDTH-1:0] cnt;
    logic             raw_pwm;
    logic             inverted_pwm;
    logic             pwm_out;

    // 1. Khoi Bo dem 8-bit dong bo (Chu ky 256 xung nhip)
    always_ff @(posedge clk) begin
        if (!rst_n) begin
            cnt <= '0;
        end else if (ena) begin
            if (enable) begin
                cnt <= cnt + 1'b1;
            end else begin
                cnt <= '0;
            end
        end
    end

    // 2. Khoi Bo so sanh do lon 8-bit & Dieu khien Dao pha / Bat-Tat
    always_comb begin
        raw_pwm      = (cnt < ui_in);
        inverted_pwm = raw_pwm ^ phase_invert;
        pwm_out      = enable ? inverted_pwm : 1'b0;

        uo_out[0]         = pwm_out;
        uo_out[WIDTH-1:1] = cnt[WIDTH-1:1];
    end
endmodule
