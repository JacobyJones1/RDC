import math

S_y = 0*10**3
S_ut = 0*10**3
M_a = 0
M_m = 0
T_a = 0
T_m = 0
a = 2
b = -0.217
k_a = a*(S_ut/10**3)**b
k_b = 0.9
S_e = k_a*k_b*S_ut/2
K_t = 2.7
K_ts = 2.2
q = 0.8
q_s = 0.9
K_f = 1 + q*(K_t - 1)
K_fs = 1 + q_s*(K_ts - 1)
n = 1

for i in range(1):

    d = ((16*n/math.pi)*(((1/S_e)*(4*(K_f*M_a)**2 + 3*(K_fs*T_a)**2)**(1/2)) + (1/S_ut)*(4*(K_f*M_m)**2 + 3*(K_fs*T_m)**2)**(1/2)))**(1/3)
    print("d = ", d, "in")

    r = 0.02*d
    print("r = ", r, "in")

    if 0.3 <= d <= 2:
        k_b = 0.879*(d)**(-0.107)
    elif 2 < d <= 10:
        k_b = 0.91*(d)**(-0.157)
    else:
        k_b = 1

    print("K_t, K_ts, q et q_s")
    K_t = float(input())
    K_ts = float(input())
    q = float(input())
    q_s = float(input())

    K_f = 1 + q*(K_t - 1)
    K_fs = 1 + q_s*(K_ts - 1)
    i += 1

d = ((16*n/math.pi)*(((1/S_e)*(4*(K_f*M_a)**2 + 3*(K_fs*T_a)**2)**(1/2)) + (1/S_ut)*(4*(K_f*M_m)**2 + 3*(K_fs*T_m)**2)**(1/2)))**(1/3)
print("d = ", d, "in")