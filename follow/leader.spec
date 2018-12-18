# This is a specification definition file for the LTLMoP toolkit.
# Format details are described at the beginning of each section below.


======== SETTINGS ========

Actions: # List of action propositions and their state (enabled = 1, disabled = 0)

CompileOptions:
convexify: True
parser: ltl
symbolic: False
use_region_bit_encoding: True
synthesizer: jtlv
fastslow: False
decompose: True

CurrentConfigName:
Untitled configuration

Customs: # List of custom propositions

RegionFile: # Relative path of region description file
follow.regions

Sensors: # List of sensor propositions and their state (enabled = 1, disabled = 0)


======== SPECIFICATION ========

RegionMapping: # Mapping between region names and their decomposed counterparts
living = p4
porch = p3
deck = p7
others = 
dining = p6
bedroom = p8
kitchen = p5

Spec: # Specification in structured English
--
! living & [](! living)

[]<> porch
[]<> bedroom

