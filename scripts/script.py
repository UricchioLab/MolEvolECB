from ECBseq import ECB

seq = ECB.SeqAnalysis()

seq.ReadCode()

for seq_id in seq.sequences:
    print(seq_id)
    break
