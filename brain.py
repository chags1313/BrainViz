# -*- coding: utf-8 -*-
"""
Created on Wed May 11 21:24:06 2022

@author: chags
"""

import streamlit as st
#from nilearn import plotting 
import streamlit.components.v1 as components

st.sidebar.header("BrainViz 🧠")
st.sidebar.subheader("3D Brain Visualization Tool for Exploration of Brain Regions and MNI Coordinates")

st.header("BrainViz 🧠")
rprimsens = (41, -27, 47)
lprimsnes = (-40 , -27, 44)
rprimmotor = (38,-18,45)
lprimmotor = (-36,-19,48)
rsensass = (15,-33,48)
lsensass = (-14, -33, 48)
rpremotsupmot = (28,-1,51)
lpremotsupmot = (-28,-2,52)
rvismotor = (23, -60, 61)
lvismotor = (-18,-61,55)
rfronteye = (22, 26, 45)
lfronteye = (-23, 24, 44)
rdlpfc = (35, 39, 31)
ldlpfc = (-39, 34, 37)
rantpfc = (23, 55, 7)
lantpfc = (-23, 55, 4)
rorbfront = (12, 37, -19)
lorbfront = (-11, 38, -19)
rinsula = (44, 4, 0)
linsula = (-42, 4, -1)
rprimvisual = (11, -78, 9)
lprimvisual = (-11, -81, 7)
rsecvisual = (29, -92, 2)
lsecvisual = (-19, -92, 2)
rvisasso = (44, -75, 5)
lvisasso = (-45, -75, 11)
rinftempgyrus = (48, -17, -31)
linftempgyrus = (-47, -14, -34)
rmedtempgyrus = (60, -27, -9)
lmedtempgyrus = (-59, -25, -13)
rsuptempgyrus = (54, -19, 1)
lsuptempgyrus = (-57, -20, 1)
rventpostcing = (9, -45, 24)
lventpostcing = (-10, -45, 24)
rventantcing = (5, 5, 31)
lventantcing = (-5, 1, 32)
rsubgenual = (7, 17, -14)
lsubgenual = (-5, 17, -13)
rdorsalpcc = (8,-48,39)
ldorsalpcc = (-8, -49,38)
rdorsalacc =  (6, 33, 16)
ldorsalacc = (-5, 39, 20)
rparahip = (26, -19, -25)
lparahip = (-26, -20, -22)
rfusiform = (47, -51, -14)
lfusiform = (-47, -52, -12)
ranggyrus = (46, -59, 31)
langgyrus = (-46, -60, 33)
lhypothalamus = (-4, -2, -11)
rhypothalamus = (3, -1, -11)
lhippocampus = (-29, -19, -15)
rhippocampus = (28,-22, -14)
lamygdala = (-24, 0, -21)
ramygdala = (21, -1, -22)
lnucaccumb = (-11, 9, -11)
rnuccaccumb = (10, 10, -12)
lglobpal = (-20, 0, -2)
rglobpal = (19, 0, -2)
lthalamus = (-9, -17, 6)
rthalamus = (10, -19, 6)
lputamen = (-26, 3, -1)
rputamen = (25, 3, -1)
lcaudate = (-11, 13, 10)
rcaudate = (14, 13, 11)

sel_coords = st.sidebar.selectbox('Select a Brain Region to Plot',
     [' ', 'Right Caudate', 'Left Caudate', "Right Putamen", "Left Putamen", "Right Thalamus", "Left Thalamus",
      "Right Globus Paladus","Left Globus Paladus","Right Nucleus Accumbens","Left Nucleus Accumbens","Right Amygdala",
      "Left Amygdala"])


if sel_coords == "Right Caudate":
    sel_coords1 = rcaudate
    st.sidebar.write("MNI Coordinates: ", rcaudate)
if sel_coords == "Left Caudate":
    sel_coords1 = lcaudate
    st.sidebar.write("MNI Coordinates: ", lcaudate)
if sel_coords == "Right Putamen":
    sel_coords1 = rputamen
    st.sidebar.write("MNI Coordinates: ", rputamen)
if sel_coords == "Left Putamen":
    sel_coords1 = lputamen
    st.sidebar.write("MNI Coordinates: ", lputamen)
if sel_coords == "Right Thalamus":
    sel_coords1 = rthalamus
    st.sidebar.write("MNI Coordinates: ", rthalamus)
if sel_coords == "Left Thalamus":
    sel_coords1 = lthalamus
    st.sidebar.write("MNI Coordinates: ", lthalamus)    
if sel_coords == "Right Globus Paladus":
    sel_coords1 = rglobpal
    st.sidebar.write("MNI Coordinates: ", rglobpal)
if sel_coords == "Left Globus Paladus":
    sel_coords1 = lglobpal
    st.sidebar.write("MNI Coordinates: ", lglobpal)
if sel_coords == "Right Nucleus Accumbens":
    sel_coords1 = rnuccaccumb
    st.sidebar.write("MNI Coordinates: ", rnuccaccumb)
if sel_coords == "Left Nucleus Accumbens":
    sel_coords1 = lnucaccumb
    st.sidebar.write("MNI Coordinates: ", lnucaccumb)
if sel_coords == "Right Amygdala":
    sel_coords1 = ramygdala
    st.sidebar.write("MNI Coordinates: ", ramygdala)
if sel_coords == "Left Amygdala":
    sel_coords1 = lamygdala
    st.sidebar.write("MNI Coordinates: ", lamygdala)



btn = st.sidebar.button("Plot")
if btn:
    dmn_coords = [sel_coords1]
    #view = plotting.view_markers(
     #   dmn_coords, ['red'], marker_size=30)
    #view.save_as_html(sel_coords+".html") 
    HtmlFile = open(sel_coords+".html", 'r', encoding='utf-8')
    source_code = HtmlFile.read() 
    components.html(source_code, height = 1000, width = 800)


