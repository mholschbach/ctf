#!/usr/bin/python3

old = ">.tTscYaAhHembuUnNkKoOjrR,<dvygG'xXqilL[]$&5036!1"
new = "HhaAloFrRiIn,ctTeEdDsSmuUgGy.fvVzbBwk;:{})?374015"
                                                   

key = dict()
for i in range(len(old)):
    key[old[i]] = new[i]

message = """>tssc Yscahtem

hb. uhppn khnon Njths jhu jnhenj enroune ,nsnaeune Utouturastdcruv Rj trb. knyheuhg ehb.u try khn Utoune 'r ob.trne .txn hb. jha khn Tr,ne gnaxreknev

Hb. on.n 'qta ehb.um qto hb. uhppnm txna hb. knein no yreiuhcehnau ,te' ,ru l$

Hb. .txn trb. nhe <nkhb.u ktarnxna ,nob.ahnxneL

Acone ohek acu
Gnhsb.ne ohek xstr
Ghnsn Utouturastdcruo 'r icneene
Kto hou ob.str

Ghnsn <arnoonm
Otat.

POL hb. .txn kto .hna ,nyrekneL KX>[5!e_03103uras3d6r0_!10_3rb._era_5!e5_j6e63sp.3x5u!1b.5_1rx10!0r0!6e1b.!yya5] iteeou kr ktjhu qto teyte,ne&"""

for c in message:
    if c in key:
        print(key[c], end='')
    else:
        print(c,end='')
