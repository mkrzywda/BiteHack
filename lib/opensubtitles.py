import urllib.request
import re, tempfile
import glob, os
import shutil, time
from tqdm import tqdm

def get_ids(top):
    links = re.compile('href="/en/subtitleserve/sub/(\d+)')
    ids = []
    i = 0
    while True:
        url = "https://www.opensubtitles.org/en/search/sublanguageid-eng/searchonlymovies-on/subformat-srt/sort-7/asc-0"
        if i > 0:
            url += f"/offset-{40*i}"

        with urllib.request.urlopen(url) as f:
            content = f.read().decode("utf8")

            ids.extend(links.findall(content))
        i += 1
        print(i)

        if len(ids) >= top:
            break
        time.sleep(10)
    return ids[:top]


def download_ids(ids):
    srt_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', 'data'))

    print(srt_dir)
    for id in tqdm(ids):
        print(id)

        while True:
            print(f"Downloading {id}")
            try:
                with tempfile.TemporaryDirectory() as tmp_dir:

                    os.chdir(tmp_dir)
                    outfile = os.path.join(tmp_dir, 'srt.zip')
                    # os.system(f"wget -O {outfile} https://dl.opensubtitles.org/en/download/sub/{id}")
                    os.system(f"curl 'https://dl.opensubtitles.org/en/download/sub/{id}'  --compressed --output {outfile}")
                    assert os.path.exists(outfile)

                    os.system(f"unzip {outfile}")
                    srts = glob.glob(os.path.join(tmp_dir, '*.srt'))
                    if len(srts) != 1:
                        continue
                    shutil.move(srts[0], os.path.join(srt_dir, os.path.basename(srts[0])))
                    time.sleep(15)
            except Exception as e:
                print(e)
                time.sleep(30)
            else:
                break


if __name__ == '__main__':
    ids = get_ids(200)
    print(ids)
    download_ids(ids)
