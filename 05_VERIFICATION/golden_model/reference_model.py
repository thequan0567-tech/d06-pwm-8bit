def pwm_step(cnt, ui_in, enable=True, phase_invert=False):
    if not enable:
        return 0, 0
    raw_pwm = 1 if cnt < ui_in else 0
    pwm_out = raw_pwm ^ (1 if phase_invert else 0)
    uo_out = ((cnt >> 1) << 1) | pwm_out
    return uo_out, pwm_out

def simulate_period(duty, enable=True, phase_invert=False):
    high_cycles = 0
    for cnt in range(256):
        uo_out, pwm_out = pwm_step(cnt, duty, enable, phase_invert)
        if enable:
            assert (uo_out >> 1) == (cnt >> 1), "Position bits mismatch"
        else:
            assert uo_out == 0, "Disable must force uo_out to 0"
        high_cycles += pwm_out
    return high_cycles

def run():
    for d in range(256):
        assert simulate_period(d, enable=True, phase_invert=False) == d
        assert simulate_period(d, enable=True, phase_invert=True) == 256 - d
        assert simulate_period(d, enable=False, phase_invert=False) == 0
        assert simulate_period(d, enable=False, phase_invert=True) == 0

    dyn_high = 0
    for cnt in range(256):
        duty = 32 if cnt < 64 else 200
        _, pwm_out = pwm_step(cnt, duty, enable=True, phase_invert=False)
        dyn_high += pwm_out
    assert dyn_high == 168
    print("D06 reference model PASS")

if __name__ == "__main__":
    run()
