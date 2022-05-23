# DNA-sequencing-by-hybridization
It is my solution for a hackerrank task using tree search. It reffers to the problem of finding a DNA sequence from available oligonucleotides.


This is the description of the task from Hackerrank:

The hybridization process of the DNA return information about short DNA parts occurring in the input sequence. Such pieces of DNA are called oligonucleotides and can be represented as short strings with the same length and builds from A, C, G, and T chars (standing for Adenine, Cytosine, Guanine, and Thymine).
Basing on the fact that the oligonucleotides overlap one another, the algorithm can reproduce the input DNA sequence.

Input Format

Input is a list of oligonucleotides, i.e., short strings of the same length based on the ACGT alphabet. Each oligonucleotide comes in a separate line.
Before the list of oligonucleotides comes some additional optional information. These lines start with the # sign followed by the key of information.
There are the following keys:
- length: input DNA sequence length
- start: the first oligonucleotide in the DNA sequence
- probe: the oligonucleotide length
Example input:

#length 7
#start ACGT
#probe 4
ACGT
CGTT
GTTT
TTTT
Constraints

The input list in each task may have a different size and contain oligonucleotides of varying lengths, but the same for every single task.

Output Format

Reconstructed input DNA sequence, e.g.,
ACGTTTTT

Sample Input 0

#length 7
#start ACGT
#probe 4
ACGT
CGTT
GTTT
TTTT
Sample Output 0

ACGTTTT
Explanation 0

The input sequence ACGTTTT is split into four parts of length 4: ACGT, CGTT, GTTT, and TTTT.
Can be reconstructed by overlapping parts in following way:

ACGT
 CGTT
  GTTT
   TTTT
↓↓↓↓↓↓↓
ACGTTTT
