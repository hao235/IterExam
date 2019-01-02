# This is a specification definition file for the LTLMoP toolkit.
# Format details are described at the beginning of each section below.


======== SETTINGS ========

Actions: # List of action propositions and their state (enabled = 1, disabled = 0)
x, 1

CompileOptions:
convexify: True
parser: ltl
symbolic: False
use_region_bit_encoding: True
synthesizer: jtlv
fastslow: False
decompose: True

Customs: # List of custom propositions

RegionFile: # Relative path of region description file
patrol.regions

Sensors: # List of sensor propositions and their state (enabled = 1, disabled = 0)
c_B, 1
a_A, 1


======== SPECIFICATION ========

RegionMapping: # Mapping between region names and their decomposed counterparts
r4 = p1
others = 
r1 = p4
r2 = p3
r3 = p2

Spec: # Specification in structured English
! e.a_A
[](! e.a_A -> ! next (e.a_A) )
! e.c_B
[](! e.c_B -> next (e.c_B))
[]( e.c_B -> next (e.c_B))
--
r1
! s.x
[]( next (e.c_B) -> next (s.x))
[]( next (e.a_A) -> ! next(s.x))

