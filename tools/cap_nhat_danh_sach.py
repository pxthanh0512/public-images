#!/usr/bin/env python3
"""Cap nhat danh_sach_anh.txt cua kho public-images (Platinum).

Cach chay (o thu muc goc cua kho):
  python3 tools/cap_nhat_danh_sach.py            # cap nhat danh sach
  python3 tools/cap_nhat_danh_sach.py --kiem-tra # chi kiem tra, khong ghi; thoat ma 1 neu co loi

Nguyen tac:
- Dong da co trong danh sach GIU NGUYEN (ke ca phan Jake da sua tay), chi cap nhat kich thuoc.
- Anh moi: lay kenh tu ten thu muc, doan cac cot con lai tu TEN FILE theo quy uoc (xem HUONG_DAN_UP_HINH.md).
- Ten file khong theo quy uoc: dip_dung = chua_phan_loai (quy trinh AI se bo qua anh nay).
- Anh sai ti le 2:1 hoac qua nang: ghi_chu bat dau bang KHONG_DUNG (AI khong chon).
- Anh bi xoa khoi kho: dong tuong ung bi bo.
- File ghi_chu_anh.txt (tuy chon): moi dong "ten_file | ghi chu", ghi de cot ghi_chu.
"""
import os, re, sys, glob
from PIL import Image

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LIST = os.path.join(REPO, 'danh_sach_anh.txt')
NOTES = os.path.join(REPO, 'ghi_chu_anh.txt')
KENH = ['nhahang', 'oem', 'privateparty', 'chung']
EXT = ('.jpg', '.jpeg', '.png')
RAW = 'https://raw.githubusercontent.com/pxthanh0512/public-images/main/'
MAX_KB = 200
KIND = {'khongkhi': 'khong_khi', 'sanpham': 'san_pham', 'nhanvat': 'nhan_vat', 'gianhang': 'gian_hang'}
COLOR = {'vang': 'vang', 'hophach': 'ho_phach', 'den': 'den', 'nhieumau': 'nhieu_mau', 'khongapdung': 'khong_ap_dung'}
HEADER_FALLBACK = ['# DANH SACH ANH - kho public-images (Platinum, bo khung email B2B)',
 '# Moi dong = 1 anh. Cac cot cach nhau bang dau " | ".',
 '# Cot: ten_file | duong_dan | link_truc_tiep | kenh | dip_dung | mau_dong_bia | co_chu_tren_anh | kich_thuoc | ghi_chu']


def read_list():
    header, rows = [], {}
    if os.path.exists(LIST):
        for line in open(LIST, encoding='utf8').read().splitlines():
            if line.startswith('#') or not line.strip():
                if not rows:
                    header.append(line)
                else:
                    header.append(line)  # chu thich cuoi tep giu nguyen
                continue
            c = [x.strip() for x in line.split(' | ')]
            if len(c) == 9:
                rows[c[1]] = c
    return header or HEADER_FALLBACK, rows


def read_notes():
    d = {}
    if os.path.exists(NOTES):
        for line in open(NOTES, encoding='utf8').read().splitlines():
            if '|' in line and not line.startswith('#'):
                a, b = line.split('|', 1)
                d[a.strip()] = b.strip()
    return d


def scan():
    def nat(x):
        return [int(t) if t.isdigit() else t.lower() for t in re.split(r'(\d+)', x)]
    out = []
    for k in KENH + ['.']:
        for p in sorted(glob.glob(os.path.join(REPO, k, '*')), key=nat):
            if p.lower().endswith(EXT):
                out.append(os.path.relpath(p, REPO).replace(os.sep, '/'))
    return out


def guess(name):
    stem = os.path.splitext(name)[0].lower()
    toks = re.split(r'[_\-]', stem)
    kind = next((KIND[t] for t in toks if t in KIND), None)
    col = next((COLOR[t] for t in toks if t in COLOR), None)
    text = 'logo_tren_anh' if 'cochu' in toks else 'khong'
    return kind, col, text


def main():
    check = '--kiem-tra' in sys.argv
    header, old = read_list()
    notes = read_notes()
    errors, warns, rows, new = [], [], [], 0
    for rel in scan():
        name = os.path.basename(rel)
        full = os.path.join(REPO, rel)
        bad_name = bool(re.search(r'[^A-Za-z0-9._\-]', name))
        if bad_name:
            errors.append(f'{rel}: ten file co dau, khoang trang hoac ky tu la (chi dung a-z, 0-9, _ va -); hay doi ten file')
        try:
            with Image.open(full) as im:
                w, h = im.size
        except Exception as e:
            errors.append(f'{rel}: khong doc duoc anh ({e})'); continue
        kb = os.path.getsize(full) / 1024
        size = f'{w}x{h} px, {kb:.0f} KB'
        problems = []
        if bad_name:
            problems.append('ten_file_sai')
        if w * 1 != h * 2:
            problems.append('sai_ti_le_2_1')
        if w < 1200:
            problems.append('rong_duoi_1200')
        if kb > MAX_KB:
            problems.append(f'nang_tren_{MAX_KB}KB')
        if problems:
            warns.append(f'{rel}: {size} -> ' + ', '.join(problems))
        if rel in old:
            c = old[rel][:]
            c[7] = size
            if rel not in old or True:
                if any(p in ('sai_ti_le_2_1', 'ten_file_sai') for p in problems) and not c[8].startswith('KHONG_DUNG'):
                    c[8] = 'KHONG_DUNG_' + '_'.join(p for p in problems if p in ('sai_ti_le_2_1', 'ten_file_sai'))
            if name in notes:
                c[8] = notes[name]
        else:
            new += 1
            kind, col, text = guess(name)
            kenh = rel.split('/')[0] if '/' in rel else 'chua_phan_loai'
            if kind and col:
                dip = f'{kind}_{os.path.splitext(name)[0].lower()}'
            else:
                dip, col = 'chua_phan_loai', col or 'chua_phan_loai'
                warns.append(f'{rel}: chua phan loai (ten file thieu kieu anh hoac mau bia); AI se bo qua cho den khi doi ten hoac sua dong trong danh sach')
            note = notes.get(name, '-')
            if any(p in ('sai_ti_le_2_1', 'rong_duoi_1200', 'ten_file_sai') for p in problems):
                note = 'KHONG_DUNG_' + '_'.join(problems)
            c = [name, rel, RAW + rel, kenh, dip, col, text, size, note]
        rows.append(c)
    out = '\n'.join(header) + '\n' + '\n'.join(' | '.join(c) for c in rows) + '\n'
    for m in warns:
        print('LUU Y:', m)
    for m in errors:
        print('LOI:', m)
    print(f'{len(rows)} anh trong danh sach ({new} anh moi).')
    if check:
        sys.exit(1 if errors else 0)
    cur = open(LIST, encoding='utf8').read() if os.path.exists(LIST) else ''
    if cur != out:
        open(LIST, 'w', encoding='utf8').write(out)
        print('Da cap nhat danh_sach_anh.txt')
    else:
        print('Danh sach khong doi.')
    sys.exit(0)


if __name__ == '__main__':
    main()
