import normalization
import io

def load_vectors(fname):
    fin = io.open(fname, 'r', encoding='utf-8', newline='\n', errors='ignore')
    data = {}
    for line in fin:
        tokens = line.lower().rstrip().split(' ')
        data[tokens[0]] = map(float, tokens[1:])
    return data
