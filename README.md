# GenBank File Parser
Couple of scripts for parsing genbank files (.gbff).
## Author
- MSR <marcossr@uma.es>
## annotation2db.py
### Description
Using Pickle reads the GenBank file and extracts all non repeated anotations to a file in the following format:
```
Species: <species> | <start position>:<end position>(<strand>) | Product: <product> | Note: <note>
```
---
## csv_filter.py
### Description
Given an annotation file (in the format described before) and a GECKO-MGV (https://pistacho.ac.uma.es/) csv file format:
```csv
All by-Identity Ungapped Fragments (Hits based approach)
[Abr.98/Apr.2010/Dec.2011 -- <ortrelles@uma.es>
SeqX filename        : Unknown
SeqY filename        : Unknown
SeqX name            : Unknown
SeqY name            : Unknown
SeqX length          : 156040895
SeqY length          : 157771801
Min.fragment.length  : 0
Min.Identity         : 0
Tot Hits (seeds)     : 0
Tot Hits (seeds) used: 0
Total fragments      : 0
========================================================
Type,xStart,yStart,xEnd,yEnd,strand(f/r),block,length,score,ident,similarity,%ident,SeqX,SeqY
Frag,3060985,155084884,3063802,155082067,f,0,2818,9368,2580,83.11,0.92,0,0
...
```
It extracts all fragments and checks the overlapping (80%) between each fragment and each annotation, then it generates a new GECKO-MGV csv file. 

---
## models.py
### Description
Some models for better use of the libraries.
### Models
```python
class Annotation:
class Fragment:
```
