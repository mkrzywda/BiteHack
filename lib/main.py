import normalization
import binding_words_vector
import os, sys
import word_counter
import plot_words
import percentage_of_words

VECTOR_PATH = os.path.join(os.path.dirname(__file__), '..', 'vector', 'vector.vec')


def main(path):
    x = normalization.normalize_srt(path)
    z = word_counter.word_counter(x)
    most_no = 50
    if len(z) > most_no:
        most_z = [word for word, _ in z.most_common(most_no)]
    else:
        most_z = list(z.keys())
    # y = binding_words_vector.load_vectors(VECTOR_PATH)
    cluster = plot_words.cluster_analysis(most_z)
    percentage_result = percentage_of_words.percentage_of_words("swear_words", x)
    print(percentage_result)


if __name__ == '__main__':
    shrek_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'Shrek (2001) DVDRiP KvCD Hockney(TUS Release).en.srt')
    main(sys.argv[1] if len(sys.argv) > 1 else shrek_path)
