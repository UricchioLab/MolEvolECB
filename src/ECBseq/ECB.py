import sys

class SeqAnalysis():

    def __init__(self,coding_file='/Users/marlonalejandrocalderonbalcazar/Downloads/ecb_ref_v1_genomic.supported.anno.cds.fa'):
        self.coding_file = coding_file
        self.sequences = {}

    def ReadCode(self):
        fh = open(self.coding_file,'r')
        seq_id = ''
        sequences = {}
        for i in fh:
            if i.startswith('>'):
                name = i.split()
                seq_id = name[0][1:]
                continue
            sequences[seq_id] = i.strip()
        self.sequences = sequences
