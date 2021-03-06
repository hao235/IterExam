# This is a specification definition file for the LTLMoP toolkit.
# Format details are described at the beginning of each section below.


======== SETTINGS ========

Actions: # List of action propositions and their state (enabled = 1, disabled = 0)
a, 1
b, 1

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
patrol.regions

Sensors: # List of sensor propositions and their state (enabled = 1, disabled = 0)
f, 1
d_B, 1


======== SPECIFICATION ========

RegionMapping: # Mapping between region names and their decomposed counterparts
r4 = p1
others = 
r1 = p4
r2 = p3
r3 = p2

Spec: # Specification in structured English
! (e.f) & [] (! next (e.f))
! e.d_B
[](! e.d_B -> next (e.d_B))
[]( e.d_B -> next (e.d_B))
--
r1
! s.a & ! s.b
[](next (e.f) <-> next (s.a))
[](next (e.d_B) <-> next (s.b))

[]<>(s.a -> r1)
[]<>(s.a -> r2)
[]<>(s.a -> r3)
[]<>(s.a -> r4)

