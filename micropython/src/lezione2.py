# Lezione 2
#
# 0) Variabili
# 1) Operazioni matematiche (*, /, +, -)
# 2) Funzioni con parametri
# 3) Funzioni predefinite (print, type, int, float, str, bool)

# Esercizio 1
# Implementare la formula per resistenze in parallelo

def parallelo(r1, r2):
    return 1 / (1 / r1 + 1 / r2)

print(parallelo(100, 200))

# Esercizio 2
# Implementare Legge di Ohm canonica U=RI

def ohm_u(r, i):
    return r * i

print(ohm_u(200, 0.1))

# Esercizi aggiuntivi
# Leggo di Ohm inverse

def ohm_i(r, u):
    return u / r

def ohm_r(u, i):
    return u / i

# Corrente che scorre in un resistore di 2 Ohm con una tensione di 3 Volt
print(ohm_i(2, 3))

# Valore del resistore che ha una corrente di 0.5 Ampere con una tensione di 3 Volt
print(ohm_r(3, 0.5))


