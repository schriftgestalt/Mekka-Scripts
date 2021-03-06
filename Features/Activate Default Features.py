#MenuTitle: Activate Default Features
# -*- coding: utf-8 -*-
__doc__="""
Activates all features that should be on by default.
"""

defaultFeatures = """
abvf
abvm
abvs
akhn
blwf
blwm
blws
calt
ccmp
cfar
cjct
clig
cpsp
curs
dist
fin2
fin3
fina
half
haln
init
isol
kern
liga
ljmo
locl
lfbd
mark
med2
medi
mkmk
nukt
opbd
pref
pres
pstf
psts
rclt
rlig
rkrf
rphf
stch
tjmo
vjmo
ltra
ltrm
rtla
rtlm
valt
vrt2
dtls
flac
ssty
"""

thisFont = Glyphs.font # frontmost font
defaultFeatures = defaultFeatures.strip().splitlines()
availableDefaultFeatures = [f.name for f in thisFont.features if f.name in defaultFeatures]

editTab = Glyphs.currentDocument.windowController().activeEditViewController()
for featureName in availableDefaultFeatures:
	if not featureName in editTab.selectedFeatures():
		editTab.selectedFeatures().append(featureName)

editTab.graphicView().reflow()
editTab._updateFeaturePopup()
