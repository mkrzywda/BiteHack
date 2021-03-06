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
            # time.sleep(10)
            try:
                with tempfile.TemporaryDirectory() as tmp_dir:

                    os.chdir(tmp_dir)
                    outfile = os.path.join(tmp_dir, 'srt.zip')
                    # os.system(f"wget -O {outfile} https://dl.opensubtitles.org/en/download/sub/{id}")
                    cmd = f"curl 'https://dl.opensubtitles.org/en/download/sub/{id}' -H 'referer: https://www.opensubtitles.org/en/subtitles/{id}'  --compressed --output {outfile}"
                    print('>>>>', cmd)
                    os.system(cmd)
                    assert os.path.exists(outfile)
                    print()
                    os.system(f"unzip {outfile}")
                    srts = glob.glob(os.path.join(tmp_dir, '*.srt'))
                    print("ASDAAAADDS"*100)

                    time.sleep(15)
                    if len(srts) != 1:
                        continue
                    shutil.move(srts[0], os.path.join(srt_dir, os.path.basename(srts[0])))
                    print('OK')
            except:
                # print('>>>>>>>', e)
                time.sleep(30)

            else:
                break


if __name__ == '__main__':
    # ids = get_ids(200)
    # print(ids)
    ids = ['7343963', '6878391', '6163690', '6429776', '6181260', '6874371', '6701427', '6822622', '6434467', '7477437', '7389345', '4641722', '7022250', '6989084', '4450863', '5926334', '6232700', '6886229', '7215550', '5830520', '6624234', '7308298', '7482119', '6919147', '6789105', '6001168', '7008689', '7024930', '6865126', '6451334', '6617497', '7369564', '6876068', '6441816', '6563473', '7456643', '6127842', '6631293', '5906818', '6825339', '6753841', '7434756', '4255108', '6855884', '6192263', '6688613', '6682985', '6030439', '7036651', '6232676', '6500090', '6722828', '6241206', '7282469', '6793020', '7171313', '6553108', '6284037', '7343111', '6178332', '6230492', '3378584', '6709384', '3925608', '6654719', '7326460', '6672811', '7200504', '7113642', '7354632', '6792726', '6795172', '7252679', '6620882', '6720968', '6864906', '6562563', '4938109', '7078525', '3097840', '7585243', '7487104', '3545076', '7263489', '6631559', '7028158', '6873925', '6766909', '5145524', '6549923', '6909235', '7035776', '6438150', '6811109', '7349358', '6298023', '6732790', '7257146', '7061198', '7412115', '6726459', '6267567', '6934864', '3635474', '7035433', '6941443', '7475046', '6757160', '6863855', '6713099', '6700911', '3358132', '7272615', '5972050', '5248172', '6990398', '7520991', '6388455', '4673734', '3384181', '6832242', '6174075', '7007801', '6857947', '7535804', '7066255', '6730013', '6769086', '6615484', '7126404', '7430820', '6622066', '7555843', '6775162', '6811112', '6838591', '6942608', '6998801', '3582795', '6388610', '6298024', '6647636', '5143645', '7320779', '6721820', '7200261', '7470647', '6683337', '7008173', '6838899', '6249074', '6775083', '5993578', '3182984', '6785801', '6839802', '7297952', '7093859', '5561246', '7113685', '6670251', '7426649', '7220480', '6344627', '6285156', '6871406', '7333993', '6729376', '6558206', '6368454', '6833102', '6721239', '6159793', '7379245', '7105514', '7577999', '6968875', '6865913', '6696875', '6349955', '6029434', '6832259', '6245048', '6949884', '7181186', '5202711', '6871699', '7527068', '6527732', '5499597', '5815200', '5519048', '7418483', '7120813', '6937679', '7495962', '6636504', '3937720', '6264282', '6609521']

    download_ids(ids[50:])
