import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA') #decription message in case of error
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence") #argument for sequence
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif") #argument for motif

if len(sys.argv) == 1: #decription message is shown if there is no sequence
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

args.seq = args.seq.upper() #all letters to capitals
if re.search('^[ACGTU]+$', args.seq): #for all the letters in the sequence
    if re.search('T', args.seq): #if the letters are from DNA, including T say its DNA
        print ('The sequence is DNA')
    elif re.search('U', args.seq): #if the letters are from RNA, including U say its RNA
        print ('The sequence is RNA')
    else:
        print ('The sequence can be DNA or RNA') #if there are both T and U its unconclusive
else:
    print ('The sequence is not DNA nor RNA') #else it cannot be identified

if args.motif:
    args.motif = args.motif.upper() #motifs to capitals
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq): #if the motif is found say found
        print("FOUND")
    else:
        print("NOT FOUND") #if the motif is not found say not found

