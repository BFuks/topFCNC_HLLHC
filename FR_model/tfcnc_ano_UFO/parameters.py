# This file was automatically created by FeynRules 2.4.87
# Mathematica version: 12.3.0 for Mac OS X x86 (64-bit) (May 10, 2021)
# Date: Mon 12 Sep 2022 16:13:25



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
NPl = Parameter(name = 'NPl',
                nature = 'external',
                type = 'real',
                value = 1000,
                texname = '\\Lambda',
                lhablock = 'EFT',
                lhacode = [ 1 ])

atcL = Parameter(name = 'atcL',
                 nature = 'external',
                 type = 'real',
                 value = 0.101,
                 texname = 'g_L^{\\text{$\\gamma $tc}}',
                 lhablock = 'FCNCCHARM',
                 lhacode = [ 1 ])

atcR = Parameter(name = 'atcR',
                 nature = 'external',
                 type = 'real',
                 value = 0.102,
                 texname = 'g_R^{\\text{$\\gamma $tc}}',
                 lhablock = 'FCNCCHARM',
                 lhacode = [ 2 ])

gtcL = Parameter(name = 'gtcL',
                 nature = 'external',
                 type = 'real',
                 value = 0.103,
                 texname = 'g_L^{\\text{gtc}}',
                 lhablock = 'FCNCCHARM',
                 lhacode = [ 3 ])

gtcR = Parameter(name = 'gtcR',
                 nature = 'external',
                 type = 'real',
                 value = 0.104,
                 texname = 'g_R^{\\text{gtc}}',
                 lhablock = 'FCNCCHARM',
                 lhacode = [ 4 ])

ztcL1 = Parameter(name = 'ztcL1',
                  nature = 'external',
                  type = 'real',
                  value = 0.105,
                  texname = 'g_L^{\\text{Ztc$\\_$dip}}',
                  lhablock = 'FCNCCHARM',
                  lhacode = [ 5 ])

ztcR1 = Parameter(name = 'ztcR1',
                  nature = 'external',
                  type = 'real',
                  value = 0.106,
                  texname = 'g_R^{\\text{Ztc$\\_$dip}}',
                  lhablock = 'FCNCCHARM',
                  lhacode = [ 6 ])

ztcL2 = Parameter(name = 'ztcL2',
                  nature = 'external',
                  type = 'real',
                  value = 0.107,
                  texname = 'g_L^{\\text{Ztc$\\_$vec}}',
                  lhablock = 'FCNCCHARM',
                  lhacode = [ 7 ])

ztcR2 = Parameter(name = 'ztcR2',
                  nature = 'external',
                  type = 'real',
                  value = 0.108,
                  texname = 'g_R^{\\text{Ztc$\\_$vec}}',
                  lhablock = 'FCNCCHARM',
                  lhacode = [ 8 ])

htcL = Parameter(name = 'htcL',
                 nature = 'external',
                 type = 'real',
                 value = 0.109,
                 texname = 'g_L^{\\text{htc}}',
                 lhablock = 'FCNCCHARM',
                 lhacode = [ 9 ])

htcR = Parameter(name = 'htcR',
                 nature = 'external',
                 type = 'real',
                 value = 0.11,
                 texname = 'g_R^{\\text{htc}}',
                 lhablock = 'FCNCCHARM',
                 lhacode = [ 10 ])

atuL = Parameter(name = 'atuL',
                 nature = 'external',
                 type = 'real',
                 value = 0.201,
                 texname = 'g_L^{\\text{$\\gamma $tu}}',
                 lhablock = 'FCNCUP',
                 lhacode = [ 1 ])

atuR = Parameter(name = 'atuR',
                 nature = 'external',
                 type = 'real',
                 value = 0.202,
                 texname = 'g_R^{\\text{$\\gamma $tu}}',
                 lhablock = 'FCNCUP',
                 lhacode = [ 2 ])

gtuL = Parameter(name = 'gtuL',
                 nature = 'external',
                 type = 'real',
                 value = 0.203,
                 texname = 'g_L^{\\text{gtu}}',
                 lhablock = 'FCNCUP',
                 lhacode = [ 3 ])

gtuR = Parameter(name = 'gtuR',
                 nature = 'external',
                 type = 'real',
                 value = 0.204,
                 texname = 'g_R^{\\text{gtu}}',
                 lhablock = 'FCNCUP',
                 lhacode = [ 4 ])

ztuL1 = Parameter(name = 'ztuL1',
                  nature = 'external',
                  type = 'real',
                  value = 0.205,
                  texname = 'g_L^{\\text{Ztu$\\_$dip}}',
                  lhablock = 'FCNCUP',
                  lhacode = [ 5 ])

ztuR1 = Parameter(name = 'ztuR1',
                  nature = 'external',
                  type = 'real',
                  value = 0.206,
                  texname = 'g_R^{\\text{Ztu$\\_$dip}}',
                  lhablock = 'FCNCUP',
                  lhacode = [ 6 ])

ztuL2 = Parameter(name = 'ztuL2',
                  nature = 'external',
                  type = 'real',
                  value = 0.207,
                  texname = 'g_L^{\\text{Ztu$\\_$vec}}',
                  lhablock = 'FCNCUP',
                  lhacode = [ 7 ])

ztuR2 = Parameter(name = 'ztuR2',
                  nature = 'external',
                  type = 'real',
                  value = 0.208,
                  texname = 'g_R^{\\text{Ztu$\\_$vec}}',
                  lhablock = 'FCNCUP',
                  lhacode = [ 8 ])

htuL = Parameter(name = 'htuL',
                 nature = 'external',
                 type = 'real',
                 value = 0.209,
                 texname = 'g_L^{\\text{htu}}',
                 lhablock = 'FCNCUP',
                 lhacode = [ 9 ])

htuR = Parameter(name = 'htuR',
                 nature = 'external',
                 type = 'real',
                 value = 0.21,
                 texname = 'g_R^{\\text{htu}}',
                 lhablock = 'FCNCUP',
                 lhacode = [ 10 ])

aEWM1 = Parameter(name = 'aEWM1',
                  nature = 'external',
                  type = 'real',
                  value = 127.9,
                  texname = '\\text{aEWM1}',
                  lhablock = 'SMINPUTS',
                  lhacode = [ 1 ])

Gf = Parameter(name = 'Gf',
               nature = 'external',
               type = 'real',
               value = 0.0000116637,
               texname = 'G_f',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

aS = Parameter(name = 'aS',
               nature = 'external',
               type = 'real',
               value = 0.1184,
               texname = '\\alpha _s',
               lhablock = 'SMINPUTS',
               lhacode = [ 3 ])

ymb = Parameter(name = 'ymb',
                nature = 'external',
                type = 'real',
                value = 4.7,
                texname = '\\text{ymb}',
                lhablock = 'YUKAWA',
                lhacode = [ 5 ])

ymt = Parameter(name = 'ymt',
                nature = 'external',
                type = 'real',
                value = 172,
                texname = '\\text{ymt}',
                lhablock = 'YUKAWA',
                lhacode = [ 6 ])

ymtau = Parameter(name = 'ymtau',
                  nature = 'external',
                  type = 'real',
                  value = 1.777,
                  texname = '\\text{ymtau}',
                  lhablock = 'YUKAWA',
                  lhacode = [ 15 ])

MZ = Parameter(name = 'MZ',
               nature = 'external',
               type = 'real',
               value = 91.1876,
               texname = '\\text{MZ}',
               lhablock = 'MASS',
               lhacode = [ 23 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

MT = Parameter(name = 'MT',
               nature = 'external',
               type = 'real',
               value = 172,
               texname = '\\text{MT}',
               lhablock = 'MASS',
               lhacode = [ 6 ])

MB = Parameter(name = 'MB',
               nature = 'external',
               type = 'real',
               value = 4.7,
               texname = '\\text{MB}',
               lhablock = 'MASS',
               lhacode = [ 5 ])

MH = Parameter(name = 'MH',
               nature = 'external',
               type = 'real',
               value = 125,
               texname = '\\text{MH}',
               lhablock = 'MASS',
               lhacode = [ 25 ])

WZ = Parameter(name = 'WZ',
               nature = 'external',
               type = 'real',
               value = 2.4952,
               texname = '\\text{WZ}',
               lhablock = 'DECAY',
               lhacode = [ 23 ])

WW = Parameter(name = 'WW',
               nature = 'external',
               type = 'real',
               value = 2.085,
               texname = '\\text{WW}',
               lhablock = 'DECAY',
               lhacode = [ 24 ])

WT = Parameter(name = 'WT',
               nature = 'external',
               type = 'real',
               value = 1.50833649,
               texname = '\\text{WT}',
               lhablock = 'DECAY',
               lhacode = [ 6 ])

WH = Parameter(name = 'WH',
               nature = 'external',
               type = 'real',
               value = 0.00407,
               texname = '\\text{WH}',
               lhablock = 'DECAY',
               lhacode = [ 25 ])

aEW = Parameter(name = 'aEW',
                nature = 'internal',
                type = 'real',
                value = '1/aEWM1',
                texname = '\\alpha _{\\text{EW}}')

G = Parameter(name = 'G',
              nature = 'internal',
              type = 'real',
              value = '2*cmath.sqrt(aS)*cmath.sqrt(cmath.pi)',
              texname = 'G')

MW = Parameter(name = 'MW',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(MZ**2/2. + cmath.sqrt(MZ**4/4. - (aEW*cmath.pi*MZ**2)/(Gf*cmath.sqrt(2))))',
               texname = 'M_W')

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEW)*cmath.sqrt(cmath.pi)',
               texname = 'e')

sw2 = Parameter(name = 'sw2',
                nature = 'internal',
                type = 'real',
                value = '1 - MW**2/MZ**2',
                texname = '\\text{sw2}')

cw = Parameter(name = 'cw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(1 - sw2)',
               texname = 'c_w')

sw = Parameter(name = 'sw',
               nature = 'internal',
               type = 'real',
               value = 'cmath.sqrt(sw2)',
               texname = 's_w')

g1 = Parameter(name = 'g1',
               nature = 'internal',
               type = 'real',
               value = 'ee/cw',
               texname = 'g_1')

gw = Parameter(name = 'gw',
               nature = 'internal',
               type = 'real',
               value = 'ee/sw',
               texname = 'g_w')

vev = Parameter(name = 'vev',
                nature = 'internal',
                type = 'real',
                value = '(2*MW*sw)/ee',
                texname = '\\text{vev}')

lam = Parameter(name = 'lam',
                nature = 'internal',
                type = 'real',
                value = 'MH**2/(2.*vev**2)',
                texname = '\\text{lam}')

yb = Parameter(name = 'yb',
               nature = 'internal',
               type = 'real',
               value = '(ymb*cmath.sqrt(2))/vev',
               texname = '\\text{yb}')

yt = Parameter(name = 'yt',
               nature = 'internal',
               type = 'real',
               value = '(ymt*cmath.sqrt(2))/vev',
               texname = '\\text{yt}')

ytau = Parameter(name = 'ytau',
                 nature = 'internal',
                 type = 'real',
                 value = '(ymtau*cmath.sqrt(2))/vev',
                 texname = '\\text{ytau}')

muH = Parameter(name = 'muH',
                nature = 'internal',
                type = 'real',
                value = 'cmath.sqrt(lam*vev**2)',
                texname = '\\mu')

