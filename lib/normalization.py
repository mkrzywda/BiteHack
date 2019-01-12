import os, re


def normalize_srt(path):
    with open(path) as file:
        srt = file.read()
        results = []
        for record in srt.split("\n\n"):
            lines = record.split("\n")
            assert re.match("\d+", lines[0])
            assert re.match("\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}", lines[1])
            utt = ' '.join(lines[2:])
            results.append(utt)
        return results


if __name__ == '__main__':
    x = normalize_srt(os.path.join(os.path.dirname(__file__), '..', 'data', 'Shrek (2001) DVDRiP KvCD Hockney(TUS Release).en.srt'))
    print(x)
