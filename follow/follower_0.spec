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
sbit0, 1
sbit1, 1
sbit2, 1


======== SPECIFICATION ========

RegionMapping: # Mapping between region names and their decomposed counterparts
living = p4
deck = p7
porch = p3
dining = p6
bedroom = p8
others = 
kitchen = p5

Spec: # Specification in structured English

--

porch

[]<>( (!e.sbit0 & !e.sbit1 & !e.sbit2)-> (!s.bit0 & !s.bit1 & !s.bit2))
[]<>((!e.sbit0 & !e.sbit1 & e.sbit2) -> (!s.bit0 & !s.bit1 & s.bit2))
[]<>((!e.sbit0 & e.sbit1 & !e.sbit2) -> (!s.bit0 & s.bit1 & !s.bit2))
[]<>((!e.sbit0 & e.sbit1 & e.sbit2) -> (!s.bit0 & s.bit1 & s.bit2))
[]<>( (e.sbit0 & !e.sbit1 & !e.sbit2) -> (s.bit0 & !s.bit1 & !s.bit2))
[]<>((e.sbit0 & !e.sbit1 & e.sbit2) -> (s.bit0 & !s.bit1 & s.bit2))

[](! living)

