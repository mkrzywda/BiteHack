import normalization
import binding_words_vector
import os, sys

x = normalization.normalize_srt(sys.argv[1])
y = binding_words_vector.load_vectors(x)
