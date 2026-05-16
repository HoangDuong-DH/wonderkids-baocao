import sys, io, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open(r'C:\Users\Admin\Downloads\wks\scraps\atomic_l3.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

ABILITY_MAP = {
    'Chú ý':'attention', 'Quan sát':'observation',
    'Kiên nhẫn/Quan sát':'observation', 'Ghi nhớ':'memory',
    'Số & tính toán':'number', 'Hình học KG':'geometry',
    'Đo lường':'measurement', 'Kiểu mẫu':'pattern', 'Dữ liệu':'data',
    'Hiểu biết':'understanding', 'Ứng dụng':'application',
    'Phân tích':'analysis', 'Tổng hợp':'synthesis',
    'Trôi chảy':'fluency', 'Linh hoạt':'flexibility',
    'Độc đáo':'originality', 'Chính xác':'precision',
}

def jss(s):
    """JS-safe string: double quotes, escape backslash and double quote"""
    s = str(s)
    s = s.replace(chr(92), chr(92)+chr(92))  # backslash → double-backslash
    s = s.replace(chr(34), chr(92)+chr(34))  # double-quote → escaped
    return chr(34) + s + chr(34)

lines = []
lines.append('/* ═══════════════════════════════════════════════════════════════')
lines.append('   ATOMIC SCORING L3 — 63 tiêu chí + 315 mô tả tham chiếu')
lines.append('   Source: Atomic_Excel_L3.xlsx')
lines.append('   Formula: điểm đạt = trọng số × hệ số nhân')
lines.append('     5→1.00 | 4→0.75 | 3→0.50 | 2→0.25 | 0→0.00')
lines.append('   Tổng max: 170 điểm — 4 lĩnh vực (24+61+32+53)')
lines.append('   Ngưỡng: S≥80 | A 65-79 | B 50-64 | C 30-49 | L<30')
lines.append('   ═══════════════════════════════════════════════════════════════ */')
lines.append('const __ATOMIC_MULTIPLIER_L3 = {5:1.0, 4:0.75, 3:0.5, 2:0.25, 0:0.0};')
lines.append('')
lines.append('const __ATOMIC_CRITERIA_L3 = [')
for c in data['criteria']:
    skill_key = ABILITY_MAP.get(c['ability'], 'observation')
    lines.append('  {cau:' + str(c['cau']) + ', ma:' + jss(c['ma']) + ', label:' + jss(c['label']) + ', weight:' + str(c['weight']) + ', skill:' + jss(skill_key) + '},')
lines.append('];')
lines.append('')
lines.append('const __ATOMIC_DESCRIPTIONS_L3 = {')
for ma, descs in data['descriptions'].items():
    parts = []
    for lvl in [5, 4, 3, 2, 0]:
        desc = descs.get(str(lvl), '')
        parts.append(str(lvl) + ':' + jss(desc))
    lines.append('  ' + jss(ma) + ':{' + ','.join(parts) + '},')
lines.append('};')

content = '\n'.join(lines)
with open(r'C:\Users\Admin\Downloads\wks\scraps\atomic_l3_data.js', 'w', encoding='utf-8') as f:
    f.write(content)

print('File size:', len(content), 'bytes')
print('Lines:', len(lines))
print('Criteria:', len(data['criteria']))
print('Descriptions:', len(data['descriptions']))
