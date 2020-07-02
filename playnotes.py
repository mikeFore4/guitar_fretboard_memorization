import time
import random
import argparse


def practice(strings, notes, all_natural = False, first_wait = 1, second_wait = 4):
    while True:
        #print string
        st_idx = random.randrange(len(strings))
        string = strings[st_idx]
        print(f'STRING: {string}')
        time.sleep(first_wait)

        #print note
        nt_idx = random.randrange(len(notes))
        note = notes[nt_idx]
        if all_natural:
            natural = 2
        else:
            natural = random.randrange(3)
        
        if natural == 0:
            if note != 'F' and note != 'C':
                note = f'{note}b'
        elif natural == 1:
            if note != 'B' and note != 'E':
                note = f'{note}#'
        
        print(f'NOTE: {note}')

        time.sleep(second_wait)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-s','--strings', nargs = '+', type = int)
    parser.add_argument('-n', '--natural', action = 'store_true')
    parser.add_argument('-w', '--wait_1', default = 1, type = int)
    parser.add_argument('-e', '--wait_2', default = 4, type = int)
    
    notes = ['A','B','C','D','E','F','G']
    strings = ['E (high)', 'B', 'G', 'D', 'A', 'E (low)']
    
    args = parser.parse_args()
    if args.strings is None:
        pass
    else:
        strings = [strings[i-1] for i in args.strings]

    practice(strings, notes, args.natural, args.wait_1, args.wait_2)
