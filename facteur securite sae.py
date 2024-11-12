import math

S_y = 0*10**3 #kpsi
S_ut = 0*10**3 #kpsi
M_a = 0
M_m = 0
T_a = 0
T_m = 0
d = 0 #inches
D = 0
r = 0
print("r = ", r)
print("r/d = ", r/d)
print("D/d = ", D/d)
a = 2
b = -0.217
k_a = a*(S_ut/10**3)**b #machined

if 0.3 <= d <= 2:
    k_b = 0.879*(d)**(-0.107)
elif 2 < d <= 10:
    k_b = 0.91*(d)**(-0.157)
else:
    k_b = 1

S_e = k_a*k_b*S_ut/2
K_t = 2.7
K_ts = 2.2
q = 0.8
q_s = 0.85
K_f = 1 + q*(K_t - 1)
K_fs = 1 + q_s*(K_ts - 1)


n_f = ((16/(math.pi*d**3))*(((1/S_e)*(4*(K_f*M_a)**2 + 3*(K_fs*T_a)**2)**(1/2)) + (1/S_ut)*(4*(K_f*M_m)**2 + 3*(K_fs*T_m)**2)**(1/2)))**(-1)
print("n_f =", n_f)