# Author: Ramiz Muharemovic
# https://github.com/muharemovic
import urllib.request
import os
import zipfile
URL = 'https://raw.githubusercontent.com/muharemovic/fix_fonts_wps/master/wps_symbol_fonts.zip'
downloaded_fonts = os.getenv("HOME") + '/wps_symbol_fonts.zip'

if not os.path.exists(os.getenv("HOME") + '/.fonts'):
    os.makedirs(os.getenv("HOME") + '/.fonts')
if not os.path.exists(os.getenv("HOME") + '/.local/share/fonts'):
    os.makedirs(os.getenv("HOME") + '/.local/share/fonts')


def url_fonts():
    u = urllib.request.urlopen(URL)
    data = u.read()
    u.close()
    with open(downloaded_fonts, 'wb') as f:
        f.write(data)

def unzip():
    zip_ref = zipfile.ZipFile(downloaded_fonts, 'r')
    zip_ref.extractall(os.getenv("HOME") + '/.fonts')
    zip_ref.extractall(os.getenv("HOME") +  '/.local/share/fonts')
    zip_ref.close()
    os.remove(downloaded_fonts)


url_fonts()
unzip()
print('Done!')

