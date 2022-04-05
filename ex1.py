import random


class MySeq:
    
    def __init__(self,seq,seq_type="DNA"):
        self.seq=seq
        self.seq_type=seq_type
    
    def print_sequence(self):
        print("Sequence: " + self.seq)
    
    def get_seq_biotype(self):
        return self.seq_type

    def show_info_seq (self):
        print ("Sequence: " + self.seq + " biotype: " + self.seq_type)

    def count_occurrences(self, seq_search):
        return self.seq.count(seq_search)

    # safer alternative: class method to validate update
    def set_seq_biotype(self , bt):
        biotype = bt.upper()
        if biotype == "DNA" or biotype == "RNA" or biotype == "PROTEIN":
            self.seq_type = biotype
        else:
            print("Non biological sequence type!")
    
    def __len__(self):
        return len(self.seq)

    def __str__(self):
        return self.seq_type + ":" + self.seq

    def __getitem__(self,n):
        return self.seq[n]

    def __getslice__(self,i,j):
        return self.seq[i:j]


class MyNumSeq(MySeq):
    def _init__(self,num_seq,seq_type="numeric"):
        super().__init__(num_seq,seq_type)

    def set_seq_biotype (self,st):
        seq_type = st.upper()
        if seq_type == "DNA" or seq_type == "RNA" or seq_type == "PROTEIN":
            self.seq_type = seq_type
        elif seq_type == "NUMERIC" or seq_type == "NUM":
            self.seq_type = seq_type
        else:
            print ("Non-biological or Non-numeric sequence type")



s1 = MySeq("MKKVSJEMSSVPYW", "PROTEIN")
print(s1)
print(len(s1))
print(s1[4])
print(s1[2:5])

s1 = MySeq("ATAATGATAGATAGATGAT")
print(s1.seq)
print(s1.seq_type)
s1.print_sequence()
print (s1.get_seq_biotype())

#s1.set_seq_biotype("time series")
s1.set_seq_biotype("dna")



a = MyNumSeq("123456789")
print(a.seq_type)
a.set_seq_biotype("numeric")
a.seq_type
a.print_sequence()

#create 100 objects of MyNumSeq and store them in a list
list_of_NumSeq=[]
for i in range(100):
    list_of_NumSeq.append(MyNumSeq(str(int(random.random()*1000000))))

for i in range(len(list_of_NumSeq)):
    list_of_NumSeq[i].print_sequence()

seq = 'AATAGATCGA'
print(len(seq))
print(seq[5])
print(seq[4:7])
print(seq.count('A'))

seq2="ATAGATCTAT"
print(seq+seq2)

print(seq)
seq1=seq.replace('T','U')
print(seq1)
print(seq[::2])
print(seq[::-2])
print(seq[5:1:-2])
print(seq.lower())
print(seq.lower()[2:])
print(seq.lower()[2:].count('a'))

c = seq.count("C")
g = seq.count("G")
print(float (c + g)/len(seq)*100)

seq = "ATGATATATGA"
print(seq.find("TAT"))
print(seq.find("TATC"))
print(seq.count("TA"))

text = "Restriction enzymes work by recognizing a particular sequence of bases on the DNA."
text_tokens = text.split(" ")
print(text_tokens)
print(text_tokens.count("the"))
print(text_tokens.index("sequence"))


seq = "ATGCTAATGTACATGCA"
seq_words = tuple ([(seq[x:x+3]) for x in range(0, len (seq)-3)])
print(seq_words)

print(seq_words.count("ATG"))
print(seq_words.count("CAT"))
print(seq_words.count("TAA"))
print(seq_words.index("TAA"))
print(seq_words.index("ATG"))





#sets
A = set([2, 3, 5, 7, 11, 13])
B = set([2, 4, 6, 8, 10])
print(A | B)
print(A & B)
print(A - B)

C = set([17, 19, 23, 31, 37])
print(A)
A.update(C)
print(A)

A.add(35)

print(A)
print(A.pop())
print(A)

A.discard(35)
print(A)




def validate_dna (dna_seq):
    """ Checks if DNA sequence is valid. Returns True is sequence is valid, or False otherwise. """
    seqm = dna_seq.upper()
    valid = seqm.count("A") + seqm.count("C") + seqm.count("G") + seqm.count("T")
    if valid == len (seqm):
        return True
    else:
        return False

print(validate_dna("atagagagatctcg"))
print(validate_dna("ATAGAXTAGAT"))


def frequency (seq):
    """ Calculates the frequency of each symbol in the sequence. Returns a dictionary. """
    dic = {}
    for s in seq.upper():
        if s in dic:
            dic[s] += 1
        else:
            dic[s] = 1
    return dic

print(frequency("atagataactcgcatag"))
print(frequency("MVVMKKSHHVLHSQSLIK"))


def gc_content (dna_seq):
    """ Returns percentage of G and C nucleotides in a DNA sequence."""
    gc_count = 0
    for s in dna_seq:
        if s in "GCgc":
            gc_count += 1
    return gc_count / len (dna_seq)

def gc_content_subseq (dna_seq , k=100):
    """ Returns GC content of non-overlapping sub-sequences of size k. The result is a list. """
    res = []
    for i in range(0, len (dna_seq)-k+1, k):
        subseq = dna_seq[i:i+k]    
        gc = gc_content(subseq)
        res.append(gc)
    return res

def transcription (dna_seq):
    """ Function that computes the RNA corresponding to the transcription of the DNA sequence provided. """
    assert validate_dna(dna_seq), "Invalid DNA sequence"
    return dna_seq.upper().replace("T","U")


def reverse_complement (dna_seq):
    """ Computes the reverse complement of the DNA sequence. """
    assert validate_dna(dna_seq), "Invalid DNA sequence"
    comp = ""
    for c in dna_seq.upper():
        if c == 'A':
            comp = "T" + comp
        elif c == "T":
            comp = "A" + comp
        elif c == "G":
            comp = "C" + comp
        elif c == "C":
            comp = "G" + comp
    return comp

