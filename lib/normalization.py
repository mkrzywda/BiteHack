import os, re


def normalize_srt(path):
    print(path)
    try:
        srt = open(path).read()
    except UnicodeDecodeError:
        srt = open(path, encoding='ISO-8859-1').read()

    results = []
    for record in srt.split("\n\n"):
        lines = record.split("\n")

        # assert re.match(r"\d+", lines[0].strip()), f"|{lines[0]}|"
        assert re.match(r"\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}", lines[1])

        utt = ' '.join(lines[2:])
        utt = re.sub('<([^>]+)>(.*)</\1>', '\1', utt)

        results.append(utt)
    return results


if __name__ == '__main__':
    x = normalize_srt(os.path.join(os.path.dirname(__file__), '..', 'data', 'Shrek (2001) DVDRiP KvCD Hockney(TUS Release).en.srt'))
    print(x)
