import normalization
import binding_words_vector
import os, sys
import word_counter

VECTOR_PATH = os.path.join(os.path.dirname(__file__), '..', 'vector', 'vector.vec')


def main(path):
    print(path)
    x = normalization.normalize_srt(path)
    z = word_counter.word_counter(x)
    most_z = [word for word, _ in z.most_common(50)]
    y = binding_words_vector.load_vectors(VECTOR_PATH)


if __name__ == '__main__':
    shrek_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'Shrek (2001) DVDRiP KvCD Hockney(TUS Release).en.srt')
    main(sys.argv[1] if len(sys.argv) > 1 else shrek_path)
