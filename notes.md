# Lecture 2 NMS

## Representation av decimaltal 
Maskin epsilon = maximala relativa fel mellan två tal som existerar.

maskinepsilon ~= 10^-16 

## IEEE flyttalsstandard

IEEE (institute for Electrical and Electronics Engineering) standard

- Konsistent flyttalsrepresentation
- Korrekta avrundningsregler
- Konsistent hantering av "exceptions" (t.ex. division med noll, 0/0 etc.)


Tre standardtyper:
- Enkel precision
- Dubbel precision
- Utökad precision

IEEE enkel precision (32-bits)
$$+- e_1, e_2, ..., e_8, d_0, d_1, d_2, ..., d_22$$
IEEE dubbel precision (64-bits)
$$+- e_1, e_2, ..., e_8, d_0, d_1, d_2, ..., d_51$$
tecken 1 bit, exponent 11 bits, mantissa 52-bits

**Hidden bit**:
- behöver vi lagra $d_0$?
- Nej, $d_0 = 1$ alltid p.g.a normalisering $=> hidden bit$
- Vi får då: Enkel precision $$+- e_1 e_2 ... e_11 d_0 d_1 d_2 ... d_23$$
- IEEE dubbel precision $$+- e_1 e_2 ... e_11 d_0 d_1 d_2 ... d_52$$
$(\beta, p, l, u)$ i IEEE flyttalsstandard


|a - b| / | a | < tolerans

|a-b| /|a| < tolerans * |a|

tolerans är ett litet tal, runt 100_maskinepsilon

# Ordinära differentialekvationer, ODEer

misstag, det ska vara: -> {y'(t) = f(t, y), t >= a 
                          {y_a = y_0

när det kommer till att använda solve_ivp för högre ordningends ode, 
måste göra om för hand till en första ordningens ODE

**höger ordningens ODE**
skriv om till 1:a ordningens

EX):
    y'' = -cy'-g*sin(y) = f(t, y, y')
    y(0) = a
    y(0) = b

Skriv om på formen y'(t) = f(t, y)
Sätt t.ex 
    u_1 = y     => u_1' = y'
    u_2 = y'    => u_2' = y'' 
    
Nu är 
    y' = u_2 
och 
    y'' = -cy'-g*sin(y)            
=> 
    u_1' = u_2
    u_2' = -cu_2-g*sin(u_1)

Sätt 

u       = (u_1, 
            u_2), 
f(t, u) = (u_2,
            -cu_2-gsin(u_1)) 
=>
    [u'(t) = f(t,u)]

Rätt form för ``solve_ivp``
