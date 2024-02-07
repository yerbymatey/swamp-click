
hey, these are the population dynamics in this ecosystem game im making. here are some of the relationships between specific species--here are some existing dynamics that are modeled out.

time	algae	bugs	birbs	fish	alligators	log_algae	log_bugs	log_fish	algae_multiplier	bug_multiplier	birb muliplier	fish multipler	alligator multiplier
0	5	1	0	0	0	=LOG(C5)			2	2	1.12	3	2
1	=(C5*K6) - (D6 + (F6 * 10))	=(D5*L6) - (E6 * 10)	0	=(F5*N6) - ((G6 * 25) + (E6 * 5))	=G5*O6	=LOG(C6)	=LOG(D6)		2	2	1.12	3	2
2	=(C6*K7) - (D7 + (F7 * 10))	=(D6*L7) - (E7 * 10)	0	=(F6*N7) - ((G7 * 25) + (E7 * 5))	=G6*O7	=LOG(C7)	=LOG(D7)		5	2	1.12	3	2
3	=(C7*K8) - (D8 + (F8 * 10))	=(D7*L8) - (E8 * 10)	0	1	=G7*O8	=LOG(C8)	=LOG(D8)	=log(F8)	5	2	1.12	3	2
4	=(C8*K9) - (D9 + (F9 * 10))	=(D8*L9) - (E9 * 10)	=E8*M9	=(F8*N9) - ((G9 * 25) + (E9 * 5))	=G8*O9	=LOG(C9)	=LOG(D9)	=log(F9)	5	2	1.12	3	2
5	=(C9*K10) - (D10 + (F10 * 10))	=(D9*L10) - (E10 * 10)	=E9*M10	=(F9*N10) - ((G10 * 25) + (E10 * 5))	=G9*O10	=LOG(C10)	=LOG(D10)	=log(F10)	5	2	1.12	3	2
6	=(C10*K11) - (D11 + (F11 * 10))	=(D10*L11) - (E11 * 10)	=E10*M11	=(F10*N11) - ((G11 * 25) + (E11 * 5))	=G10*O11	=LOG(C11)	=LOG(D11)	=log(F11)	5	2	1.12	3	2
7	=(C11*K12) - (D12 + (F12 * 10))	=(D11*L12) - (E12 * 10)	=E11*M12	=(F11*N12) - ((G12 * 25) + (E12 * 5))	1	=LOG(C12)	=LOG(D12)	=log(F12)	5	2	1.12	3	2
8	=(C12*K13) - (D13 + (F13 * 10))	=(D12*L13) - (E13 * 10)	=E12*M13	=(F12*N13) - ((G13 * 25) + (E13 * 5))	=G12*O13	=LOG(C13)	=LOG(D13)	=log(F13)	5	2	1.12	3	2
9	=(C13*K14) - (D14 + (F14 * 10))	=(D13*L14) - (E14 * 10)	=E13*M14	=(F13*N14) - ((G14 * 25) + (E14 * 5))	=G13*O14	=LOG(C14)	=LOG(D14)	=log(F14)	5	2	1.12	3	2
10	=(C14*K15) - (D15 + (F15 * 10))	=(D14*L15) - (E15 * 10)	20	=(F14*N15) - ((G15 * 25) + (E15 * 5))	=G14*O15	=LOG(C15)	=LOG(D15)	=log(F15)	5	2	1.12	3	2
11	=(C15*K16) - (D16 + (F16 * 10))	=(D15*L16) - (E16 * 10)	=E15*M16	=(F15*N16) - ((G16 * 25) + (E16 * 5))	=G15*O16	=LOG(C16)	=LOG(D16)	=log(F16)	10	2	1.12	3	2
12	=(C16*K17) - (D17 + (F17 * 10))	=(D16*L17) - (E17 * 10)	=E16*M17	=(F16*N17) - ((G17 * 25) + (E17 * 5))	=G16*O17	=LOG(C17)	=LOG(D17)	=log(F17)	10	2	1.12	3	2
13	=(C17*K18) - (D18 + (F18 * 10))	=(D17*L18) - (E18 * 10)	=E17*M18	=(F17*N18) - ((G18 * 25) + (E18 * 5))	=G17*O18	=LOG(C18)	=LOG(D18)	=log(F18)	10	2	1.12	3	2
14	=(C18*K19) - (D19 + (F19 * 10))	=(D18*L19) - (E19 * 10)	=E18*M19	=(F18*N19) - ((G19 * 25) + (E19 * 5))	=G18*O19	=LOG(C19)	=LOG(D19)	=log(F19)	10	2	1.12	3	2
15	=(C19*K20) - (D20 + (F20 * 10))	=(D19*L20) - (E20 * 10)	=E19*M20	=(F19*N20) - ((G20 * 25) + (E20 * 5))	=G19*O20	=LOG(C20)	=LOG(D20)	=log(F20)	10	2	1.12	3	2
16	=(C20*K21) - (D21 + (F21 * 10))	=(D20*L21) - (E21 * 10)	=E20*M21	=(F20*N21) - ((G21 * 25) + (E21 * 5))	=G20*O21	=LOG(C21)	=LOG(D21)	=log(F21)	20	2	1.12	3	2
17	=(C21*K22) - (D22 + (F22 * 10))	=(D21*L22) - (E22 * 10)	=E21*M22	=(F21*N22) - ((G22 * 25) + (E22 * 5))	=G21*O22	=LOG(C22)	=LOG(D22)	=log(F22)	20	2	1.12	3	2
18	=(C22*K23) - (D23 + (F23 * 10))	=(D22*L23) - (E23 * 10)	=E22*M23	=(F22*N23) - ((G23 * 25) + (E23 * 5))	=G22*O23	=LOG(C23)	=LOG(D23)	=log(F23)	20	2	1.12	3	2
19	=(C23*K24) - (D24 + (F24 * 10))	=(D23*L24) - (E24 * 10)	=E23*M24	=(F23*N24) - ((G24 * 25) + (E24 * 5))	=G23*O24	=LOG(C24)	=LOG(D24)	=log(F24)	20	2	1.12	3	2
20	=(C24*K25) - (D25 + (F25 * 10))	=(D24*L25) - (E25 * 10)	=E24*M25	=(F24*N25) - ((G25 * 25) + (E25 * 5))	=G24*O25	=LOG(C25)	=LOG(D25)	=log(F25)	20	2	1.12	3	2
21	=(C25*K26) - (D26 + (F26 * 10))	=(D25*L26) - (E26 * 10)	=E25*M26	=(F25*N26) - ((G26 * 25) + (E26 * 5))	=G25*O26	=LOG(C26)	=LOG(D26)	=log(F26)	20	2	1.12	3	2
22	=(C26*K27) - (D27 + (F27 * 10))	=(D26*L27) - (E27 * 10)	=E26*M27	=(F26*N27) - ((G27 * 25) + (E27 * 5))	=G26*O27	=LOG(C27)	=LOG(D27)	=log(F27)	20	2	1.12	3	2
23	=(C27*K28) - (D28 + (F28 * 10))	=(D27*L28) - (E28 * 10)	=E27*M28	=(F27*N28) - ((G28 * 25) + (E28 * 5))	=G27*O28	=LOG(C28)	=LOG(D28)	=log(F28)	20	2	1.12	3	2
24	=(C28*K29) - (D29 + (F29 * 10))	=(D28*L29) - (E29 * 10)	=E28*M29	=(F28*N29) - ((G29 * 25) + (E29 * 5))	=G28*O29	=LOG(C29)	=LOG(D29)	=log(F29)	20	2	1.12	3	2
25	=(C29*K30) - (D30 + (F30 * 10))	=(D29*L30) - (E30 * 10)	=E29*M30	=(F29*N30) - ((G30 * 25) + (E30 * 5))	=G29*O30	=LOG(C30)	=LOG(D30)	=log(F30)	40	2	1.12	3	2
26	=(C30*K31) - (D31 + (F31 * 10))	=(D30*L31) - (E31 * 10)	=E30*M31	=(F30*N31) - ((G31 * 25) + (E31 * 5))	=G30*O31	=LOG(C31)	=LOG(D31)	=log(F31)	40	2	1.12	3	2
27	=(C31*K32) - (D32 + (F32 * 10))	=(D31*L32) - (E32 * 10)	=E31*M32	=(F31*N32) - ((G32 * 25) + (E32 * 5))	=G31*O32	=LOG(C32)	=LOG(D32)	=log(F32)	40	2	1.12	3	2
28	=(C32*K33) - (D33 + (F33 * 10))	=(D32*L33) - (E33 * 10)	=E32*M33	=(F32*N33) - ((G33 * 25) + (E33 * 5))	=G32*O33	=LOG(C33)	=LOG(D33)	=log(F33)	40	2	1.12	3	2
29	=(C33*K34) - (D34 + (F34 * 10))	=(D33*L34) - (E34 * 10)	=E33*M34	=(F33*N34) - ((G34 * 25) + (E34 * 5))	=G33*O34	=LOG(C34)	=LOG(D34)	=log(F34)	40	2	1.12	3	2
30	=(C34*K35) - (D35 + (F35 * 10))	=(D34*L35) - (E35 * 10)	=E34*M35	=(F34*N35) - ((G35 * 25) + (E35 * 5))	=G34*O35	=LOG(C35)	=LOG(D35)	=log(F35)	40	2	1.12	3	2
31	=(C35*K36) - (D36 + (F36 * 10))	=(D35*L36) - (E36 * 10)	=E35*M36	=(F35*N36) - ((G36 * 25) + (E36 * 5))	=G35*O36	=LOG(C36)	=LOG(D36)	=log(F36)	40	2	1.12	3	2
32	=(C36*K37) - (D37 + (F37 * 10))	=(D36*L37) - (E37 * 10)	=E36*M37	=(F36*N37) - ((G37 * 25) + (E37 * 5))	=G36*O37	=LOG(C37)	=LOG(D37)	=log(F37)	40	2	1.12	3	2
33	=(C37*K38) - (D38 + (F38 * 10))	=(D37*L38) - (E38 * 10)	250	=(F37*N38) - ((G38 * 25) + (E38 * 5))	=G37*O38	=LOG(C38)	=LOG(D38)	=log(F38)	40	2	1.12	3	2
34	=(C38*K39) - (D39 + (F39 * 10))	=(D38*L39) - (E39 * 10)	250	=(F38*N39) - ((G39 * 25) + (E39 * 5))	=G38*O39	=LOG(C39)	=LOG(D39)	=log(F39)	40	2	1.12	3	2
35	=(C39*K40) - (D40 + (F40 * 10))	=(D39*L40) - (E40 * 10)	250	=(F39*N40) - ((G40 * 25) + (E40 * 5))	=G39*O40	=LOG(C40)	=LOG(D40)	=log(F40)	40	2	1.12	3	2
36	=(C40*K41) - (D41 + (F41 * 10))	=(D40*L41) - (E41 * 10)	250	=(F40*N41) - ((G41 * 25) + (E41 * 5))	=G40*O41	=LOG(C41)	=LOG(D41)	=log(F41)	40	2	1.12	3	2
37	=(C41*K42) - (D42 + (F42 * 10))	=(D41*L42) - (E42 * 10)	250	=(F41*N42) - ((G42 * 25) + (E42 * 5))	=G41*O42	=LOG(C42)	=LOG(D42)	=log(F42)	40	2	1.12	3	2
38	=(C42*K43) - (D43 + (F43 * 10))	=(D42*L43) - (E43 * 10)	250	=(F42*N43) - ((G43 * 25) + (E43 * 5))	=G42*O43	=LOG(C43)	=LOG(D43)	=log(F43)	40	2	1.12	3	2
39	=(C43*K44) - (D44 + (F44 * 10))	=(D43*L44) - (E44 * 10)	250	=(F43*N44) - ((G44 * 25) + (E44 * 5))	=G43*O44	=LOG(C44)	=LOG(D44)	=log(F44)	40	2	1.12	3	2
40	=(C44*K45) - (D45 + (F45 * 10))	=(D44*L45) - (E45 * 10)	250	=(F44*N45) - ((G45 * 25) + (E45 * 5))	=G44*O45	=LOG(C45)	=LOG(D45)	=log(F45)	40	2	1.12	3	2
41	=(C45*K46) - (D46 + (F46 * 10))	=(D45*L46) - (E46 * 10)	250	=(F45*N46) - ((G46 * 25) + (E46 * 5))	=G45*O46	=LOG(C46)	=LOG(D46)	=log(F46)	40	2	1.12	3	2
42	=(C46*K47) - (D47 + (F47 * 10))	=(D46*L47) - (E47 * 10)	250	=(F46*N47) - ((G47 * 25) + (E47 * 5))	=G46*O47	=LOG(C47)	=LOG(D47)	=log(F47)	40	2	1.12	3	2
43	=(C47*K48) - (D48 + (F48 * 10))	=(D47*L48) - (E48 * 10)	250	=(F47*N48) - ((G48 * 25) + (E48 * 5))	=G47*O48	=LOG(C48)	=LOG(D48)	=log(F48)	40	2	1.12	3	2
44	=(C48*K49) - (D49 + (F49 * 10))	=(D48*L49) - (E49 * 10)	250	=(F48*N49) - ((G49 * 25) + (E49 * 5))	=G48*O49	=LOG(C49)	=LOG(D49)	=log(F49)	40	2	1.12	3	2
45	=(C49*K50) - (D50 + (F50 * 10))	=(D49*L50) - (E50 * 10)	250	=(F49*N50) - ((G50 * 25) + (E50 * 5))	=G49*O50	=LOG(C50)	=LOG(D50)	=log(F50)	40	2	1.12	3	2
46	=(C50*K51) - (D51 + (F51 * 10))	=(D50*L51) - (E51 * 10)	250	=(F50*N51) - ((G51 * 25) + (E51 * 5))	=G50*O51	=LOG(C51)	=LOG(D51)	=log(F51)	40	2	1.12	3	2
47	=(C51*K52) - (D52 + (F52 * 10))	=(D51*L52) - (E52 * 10)	250	=(F51*N52) - ((G52 * 25) + (E52 * 5))	=G51*O52	=LOG(C52)	=LOG(D52)	=log(F52)	40	2	1.12	3	2
48	=(C52*K53) - (D53 + (F53 * 10))	=(D52*L53) - (E53 * 10)	250	=(F52*N53) - ((G53 * 25) + (E53 * 5))	=G52*O53	=LOG(C53)	=LOG(D53)	=log(F53)	40	2	1.12	3	2


here are also some existing populations with some definitions and relationships:

species_info = {
    "bobcat": {"population": 30, "growth_rate": 0.04, "predator": True},
    "snapping_turtle": {"population": 50, "growth_rate": 0.03, "predator": True},
    "river_otter": {"population": 40, "growth_rate": 0.035, "predator": True},
    "great_blue_heron": {"population": 35, "growth_rate": 0.03, "predator": True},
    "raccoon": {"population": 70, "growth_rate": 0.025, "predator": True},
    "water_moccasin": {"population": 45, "growth_rate": 0.04, "predator": True},
    "red_tailed_hawk": {"population": 25, "growth_rate": 0.03, "predator": True},
    "eagle": {"population": 20, "growth_rate": 0.02, "predator": True},
    "coyote": {"population": 30, "growth_rate": 0.03, "predator": True},
    "rabbits": {"population": 150, "growth_rate": 0.1},
    "rodents": {"population": 200, "growth_rate": 0.12},
    "fish": {"population": 300, "growth_rate": 0.08},
    "frogs": {"population": 250, "growth_rate": 0.07},
    "insects": {"population": 500, "growth_rate": 0.15},
    "grass": {"population": 1000, "growth_rate": 0.2},
    "berries": {"population": 500, "growth_rate": 0.1},
    "water_plants": {"population": 400, "growth_rate": 0.09}
}

relationships = {
    "bobcat": ["rabbits", "rodents"],
    "snapping_turtle": ["fish", "frogs"],
    "river_otter": ["fish"],
    "great_blue_heron": ["fish", "frogs"],
    "raccoon": ["berries", "insects"],
    "water_moccasin": ["fish", "frogs"],
    "red_tailed_hawk": ["rodents", "small_birds"],
    "eagle": ["red_tailed_hawk", "rabbits"],
    "coyote": ["rabbits", "rodents"]
}

can you write a simulation for this ecosystem that takes into account the existing dynamics and population growth rates? assume carrying capacity to be related to what a species preys on. if the species doesn't prey on anything, set the carrying capacity for prey to a reasonable number. 
we're going to be running alot of simulations to see what the best starting populations and growth rates will be, so please make sure to include that in your response, as we need to see how the populations change over time. 

#things that need to be included for population mechanics
# plant and insect recovery rate, rates of predation, inter-species competition, player actions, environmental factors, symbiotic relationships
# need to amend species and ecosystem class







