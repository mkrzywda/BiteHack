import os, re, nltk.data
from collections import Counter
from nltk.stem import PorterStemmer
#nltk.download()
sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')

porter_stemmer = PorterStemmer()


def normalize_srt(path):
    try:
        srt = open(path, newline="").read()
    except UnicodeDecodeError:
        srt = open(path, newline="", encoding='ISO-8859-1').read()
    results = []
    #print('>>> ', srt.count("\r\n"))
    srt = srt.replace("\r\n", "\n")
    #print('>>> ', srt.count("\t"))
    #print(srt[-100:])
    for record in re.split("\n{2,}", srt):
        lines = record.split("\n")
        if len(lines) < 3:
            continue
        #print(lines)
        # assert re.match(r"\d+", lines[0].strip()), f"|{lines[0]}|"
        assert re.match(r"\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}", lines[1]), lines[1]
        utt = re.sub('<([^>]+)>(.*)</\1>', '\1', " ".join(lines[2:]))
        results.extend(sent_detector.tokenize(utt.strip()))

    string_string = ""
    for t in results:
        t = re.sub(r'[^\w\s]', ' ', t).strip()
        string_string += " " + t[0].lower() + t[1:] if len(t) > 1 else t
    return re.sub(r'\s+', ' ', string_string).strip()


if __name__ == '__main__':
    x = normalize_srt(os.path.join(os.path.dirname(__file__), '..', 'data', 'Shrek (2001) DVDRiP KvCD Hockney(TUS Release).en.srt'))
