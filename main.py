import streamlit as st
from PIL import Image
from math import ceil,sin,cos,tan,atan

st.set_page_config(layout="wide")

def discharge(x):
    tabla = [
        [0,39,5,10],
        [40,99,10,15],
        [100,189,15,20],
        [190,460,20,30]
    ]
    for a,b,c,d in tabla:
        if a <= x <= b:
            q = c + (d-c)/(b-a) * (x-a)
            return q

with st.sidebar:
    st.header("TRABAJO ESCALONADO 2")
    st.write("**Departamento Académico de Hidráulica e Hidrología**")
    st.write("**HH413G - IRRIGACIÓN**")
    image= Image.open("/app/irrigacion/img/UNI.PNG")
    st.image(image,width=200)
    st.write("**Integrantes:**")
    "- Caballero Lazarte Leidy Letzy"
    "- Cano Pacheco Ludwig Luiggi"
    "- Pariona Colos Erika"
    "- Quispe Leguía Carlofrancisco"
    "- Villegas Condemaita Niccolas"

st.title("BAFFLED APRON DROPS")

T1,T2,T3,T4,T5,T6 = st.tabs(["[ DATOS ]","[ PLANTA ]","[ PERFIL ]","[ DETALLE ]","[ AGUAS ARRIBA ]","[ AGUAS ABAJO ]"])

with T1:
    c1,c2,c3,c4,c5,c6 = st.columns([1,2,1,2,1,2],gap="medium")
    with c1: "$Q (cfs):$"
    with c2: Q = st.number_input("Q",min_value=0.0,value=120.0,label_visibility="collapsed")
    with c3: "$b (ft):$"
    with c4: b = st.number_input("b",min_value=0.0,value=8.0,label_visibility="collapsed")
    with c5: "$d_1 (ft):$"
    with c6: d_1 = st.number_input("d_1",min_value=0.0,value=4.10,label_visibility="collapsed")
    c1,c2,c3,c4,c5,c6 = st.columns([1,2,1,2,1,2],gap="medium")
    with c1: "$A_1 (sq ft):$"
    with c2: A_1 = st.number_input("A_1",min_value=0.0,value=58.02,label_visibility="collapsed")
    with c3: "$v_1 (fps):$"
    with c4: v_1 = st.number_input("v_1",min_value=0.0,value=2.08,label_visibility="collapsed")
    with c5: "$h_{v_1} (ft):$"
    with c6: h_v1 = st.number_input("h_v_1",min_value=0.0,value=0.07,label_visibility="collapsed")
    c1,c2,c3,c4,c5,c6 = st.columns([1,2,1,2,1,2],gap="medium")
    with c1: "$r:$"
    with c2: r = st.number_input("r",min_value=0.0,value=2.55,label_visibility="collapsed")
    with c3: "$n:$"
    with c4: n = float(st.text_input("n",value=0.025,label_visibility="collapsed"))
    with c5: "$s:$"
    with c6: s = float(st.text_input("s",value=0.00035,label_visibility="collapsed"))
    c1,c2,c3,c4,c5,c6 = st.columns([1,2,1,2,1,2],gap="medium")
    with c1: "$ss:$"
    with c2: ss = st.number_input("ss",min_value=0.0,value=1.5,label_visibility="collapsed")
    with c3: "$f_b (ft):$"
    with c4: f_b = st.number_input("v_1",min_value=0.0,value=2.0,label_visibility="collapsed")
    with c5: "$h_B (ft):$"
    with c6: h_B = st.number_input("h_v_1",min_value=0.0,value=6.1,label_visibility="collapsed")
    c1,c2,c3,c4,c5,c6 = st.columns([1,2,1,2,1,2],gap="medium")
    with c1: "$F (ft):$"
    with c2: F = st.number_input("F",min_value=0.0,value=6.0,label_visibility="collapsed")
    image= Image.open("img/GENERAL.png")
    st.image(image,use_column_width=True)


# Paso 1

# Cálculo de caudal por pie
q = discharge(Q) # con tabla
# Cálculo de ancho
B = ceil(12*Q/q)/12 # aproximado

# Paso 2

# Cálculo de profundidad crítica dc
g = 32.2 #ft/s²
d_c = round(q**(2/3) / g**(1/3),2)
# Altura de bloque
h_b = ceil(12*0.9*d_c)/12
# Ancho de bloque y espacio, w:
Min_w = h_b
Max_w = 1.5 * h_b

# Paso 3
Min_wp = (1/3) * h_b
Max_wp = (2/3) * h_b

with T2:
    c1,c2,cc,c3,c4 = st.columns([1,2,1,1,2])
    with c1: "$w\ (ft):$"
    with c2: w = st.slider("w",min_value=Min_w,max_value=Max_w,value=1.0*round(h_b),label_visibility="collapsed")
    with c3: "$w_p\ (ft):$"
    with c4: wp = st.slider("wp",min_value=Min_wp,max_value=Max_wp,value=1.0*round(h_b/2),label_visibility="collapsed")

n = 3 #Cantidad de espacios o bloques en una fila
B = 2 * wp + n * w
q = Q/B
d_c = round(q**(2/3) / g**(1/3),2)
h_b = round(12 * 0.9 * d_c)/12

with T4:
    c1,c2 = st.columns([1,5])
    with c1: "$T (in):$"
    with c2: T = st.slider("T",min_value=8.0,max_value=10.0,value=9.0,step=0.25,label_visibility="collapsed")

# Paso 4
L_1 = ceil(12*2*d_1)/12

# Paso 5
v_c = (q*g)**(1/3)
h_vc = v_c ** 2 / (2*g)
E_s1 = d_1 + h_v1
E_sc = d_c + h_vc
h_i = 0.5 * (v_c**2 - v_1**2) / (2*g)
h_s = E_s1 - E_sc - h_i
h_s = round(12*h_s)/12

# Paso 7
phi = atan(0.5)
R = 6 #INPUT
L_2 = R * sin(phi)
y = R - R*cos(phi)
e = h_s - y

# Paso 8
S_min = 2 * h_b
S = 6 #INPUT


# Paso 9
Sy = S * sin(phi)
hy = h_b * cos(phi)
j = Sy + hy

# Paso 10
Ly = e + F + j
rows = Ly / Sy
rows = ceil(rows)
Ls = rows * S
Ly = rows * Sy
Sx = S * cos(phi)
L_3 = rows * Sx

# Paso 11
L = L_1 + L_2 + L_3

# Paso 12
h_1 = d_1 + 1
h_1 = ceil(12*h_1)/12
h_2 = h_1 - h_s
h_3 = 3 * h_b

# Paso 13
C_1 = 2.5 #ft
M_1 = 1.5 * h_1 + C_1

# Paso 14
C_3 = 2.5  #ft
h_3p = h_3 / cos(phi)
M_3 = 1.5 * h_3p + C_3
M_3 = ceil(12*M_3)/12
L_b = T/12 + h_b * tan(phi)


with T2:
    c1,c2,cc,c3,c4 = st.columns([1,2,1,1,2])
    with c1: "$M_1:$"
    with c2: f"${int(M_1)}\ ft\ \ {12*(M_1-int(M_1)):.1f}\ in$"
    with c3: "$B:$"
    with c4: f"${int(B)}\ ft\ \ {12*(B-int(B)):.1f}\ in$"
    c1,c2,cc,c3,c4 = st.columns([1,2,1,1,2])
    with c1: "$L:$"
    with c2: f"${int(L)}\ ft\ \ {12*(L-int(L)):.1f}\ in$"
    with c3: "$M_3:$"
    with c4: f"${int(M_3)}\ ft\ \ {12*(M_3-int(M_3)):.1f}\ in$"
    image= Image.open("img/PLANTA.png")
    st.image(image,use_column_width=True)

nombres = [["$h_1:$","$y:$","$S:$"],
    ["$C_1:$","$R:$","$L_s:$"],
    ["$h_2:$","$F:$","$h_b:$"],
    ["$h_s:$","$e:$","$C_3:$"],
    ["$L_1:$","$L_3:$","$J:$"],
    ["$L_2:$","$h_3:$","$h'_3:$"],
    ["$L_y:$","",""]]

valores = [[h_1,y,S],
    [C_1,R,Ls],
    [h_2,F,h_b],
    [h_s,e,C_3],
    [L_1,L_3,j],
    [L_2,h_3,h_3p],
    [Ly,0,0]]

with T3:
    for i in range(7):
        C = list(st.columns([1,3,1,3,1,3]))
        with C[0]: nombres[i][0]
        with C[1]: f"${int(valores[i][0])}\ ft\ \ {12*(valores[i][0]-int(valores[i][0])):.1f}\ in$"
        with C[2]: nombres[i][1]
        with C[3]: f"${int(valores[i][1])}\ ft\ \ {12*(valores[i][1]-int(valores[i][1])):.1f}\ in$"
        with C[4]: nombres[i][2]
        with C[5]: f"${int(valores[i][2])}\ ft\ \ {12*(valores[i][2]-int(valores[i][2])):.1f}\ in$"
    image= Image.open("img/PERFIL.png")
    st.image(image,use_column_width=True)

with T4:
    c1,c2,cc,c3,c4 = st.columns([1,2,1,1,2])
    with c1: "$h_y:$"
    with c2: f"${int(hy)}\ ft\ \ {12*(hy-int(hy)):.1f}\ in$"
    with c3: "$L_b:$"
    with c4: f"${int(L_b)}\ ft\ \ {12*(L_b-int(L_b)):.1f}\ in$"
    c1,c2,cc,c3,c4 = st.columns([1,2,1,1,2])
    with c1: "$T:$"
    with c2: f"${T:.2f}\ in$"
    with c3: "$h_b:$"
    with c4: f"${int(h_b)}\ ft\ \ {12*(h_b-int(h_b)):.1f}\ in$"
    c1,c2 = st.columns(2)
    with c1:
        image= Image.open("img/DETALLE.png")
        st.image(image,use_column_width=True)
    with c2:
        image= Image.open("img/DETALLE2.png")
        st.image(image,use_column_width=True)

with T5:
    c1,c2,cc,c3,c4 = st.columns([1,2,1,1,2])
    with c1: "$M_1:$"
    with c2: f"${int(M_1)}\ ft\ \ {12*(M_1-int(M_1)):.1f}\ in$"
    with c3: "$C_1:$"
    with c4: f"${int(C_1)}\ ft\ \ {12*(C_1-int(C_1)):.1f}\ in$"
    c1,c2,cc,c3,c4 = st.columns([1,2,1,1,2])
    with c1: "$h_1:$"
    with c2: f"${int(h_1)}\ ft\ \ {12*(h_1-int(h_1)):.1f}\ in$"
    with c3: "$B:$"
    with c4: f"${int(B)}\ ft\ \ {12*(B-int(B)):.1f}\ in$"
    image= Image.open("img/ARRIBA.png")
    st.image(image,use_column_width=True)

with T6:
    c1,c2,cc,c3,c4 = st.columns([1,2,1,1,2])
    with c1: "$M_3:$"
    with c2: f"${int(M_3)}\ ft\ \ {12*(M_3-int(M_3)):.1f}\ in$"
    with c3: "$C_3:$"
    with c4: f"${int(C_3)}\ ft\ \ {12*(C_3-int(C_3)):.1f}\ in$"
    c1,c2,cc,c3,c4 = st.columns([1,2,1,1,2])
    with c1: "$h'_3:$"
    with c2: f"${int(h_3p)}\ ft\ \ {12*(h_3p-int(h_3p)):.1f}\ in$"
    with c3: "$B:$"
    with c4: f"${int(B)}\ ft\ \ {12*(B-int(B)):.1f}\ in$"
    image= Image.open("img/ABAJO.png")
    st.image(image,use_column_width=True)
