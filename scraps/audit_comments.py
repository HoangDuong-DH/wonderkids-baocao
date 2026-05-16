"""
Audit AFTER FIX — kiểm tra lại 4 mock profiles với logic mới
(dynamic tone + threshold + grammar fix).
"""

PROFILES = {
    'excellent': {
        'name': 'XUẤT SẮC',
        'kt': [('Các số đến 9',10,10),('Phép cộng & phép trừ',10,9),('Phân loại',6,6),('Đo lường',8,7),('Các kiến thức toán tư duy khác',6,5)],
        'kq': [('Bài toán có lời văn',14,13),('Bài toán cơ bản',6,6)],
        'ss': [('Dễ',8,8),('Trung bình',10,9),('Khó',4,4)],
        'qscore': [5,5,5,5,5,5,5,7,6,10],
        'qscore_max': [5,5,5,5,5,5,5,7,7,11],
        'nl_labels': ['Giải quyết vấn đề','Logic và quan sát','Phân tích và phân loại','Số và ký hiệu','Không gian và hình học','Suy luận toán học'],
        'nl': [(30,28),(25,24),(35,33),(30,27),(25,23),(20,18)],
        'cd': [('Dễ',15,14),('Trung bình',20,18),('Khó',25,23)],
    },
    'good': {
        'name': 'KHÁ',
        'kt': [('Các số đến 9',10,7),('Phép cộng & phép trừ',10,6),('Phân loại',6,4),('Đo lường',8,5),('Các kiến thức toán tư duy khác',6,3)],
        'kq': [('Bài toán có lời văn',14,8),('Bài toán cơ bản',6,4)],
        'ss': [('Dễ',8,7),('Trung bình',10,6),('Khó',4,1)],
        'qscore': [5,4,3,5,4,3,4,5,4,7],
        'qscore_max': [5,5,5,5,5,5,5,7,7,11],
        'nl_labels': ['Giải quyết vấn đề','Logic và quan sát','Phân tích và phân loại','Số và ký hiệu','Không gian và hình học','Suy luận toán học'],
        'nl': [(30,18),(25,17),(35,22),(30,19),(25,16),(20,12)],
        'cd': [('Dễ',15,11),('Trung bình',20,13),('Khó',25,14)],
    },
    'weak': {
        'name': 'CẦN CỐ GẮNG',
        'kt': [('Các số đến 9',10,4),('Phép cộng & phép trừ',10,3),('Phân loại',6,2),('Đo lường',8,3),('Các kiến thức toán tư duy khác',6,1)],
        'kq': [('Bài toán có lời văn',14,4),('Bài toán cơ bản',6,3)],
        'ss': [('Dễ',8,5),('Trung bình',10,2),('Khó',4,0)],
        'qscore': [2,1,3,2,1,2,1,2,1,3],
        'qscore_max': [5,5,5,5,5,5,5,7,7,11],
        'nl_labels': ['Giải quyết vấn đề','Logic và quan sát','Phân tích và phân loại','Số và ký hiệu','Không gian và hình học','Suy luận toán học'],
        'nl': [(30,8),(25,9),(35,10),(30,8),(25,7),(20,3)],
        'cd': [('Dễ',15,8),('Trung bình',20,5),('Khó',25,2)],
    },
    'imbalanced': {
        'name': 'MẤT CÂN ĐỐI',
        'kt': [('Các số đến 9',10,9),('Phép cộng & phép trừ',10,9),('Phân loại',6,5),('Đo lường',8,6),('Các kiến thức toán tư duy khác',6,3)],
        'kq': [('Bài toán có lời văn',14,9),('Bài toán cơ bản',6,5)],
        'ss': [('Dễ',8,7),('Trung bình',10,8),('Khó',4,2)],
        'qscore': [3,3,2,2,1,2,1,2,1,1],
        'qscore_max': [5,5,5,5,5,5,5,7,7,11],
        'nl_labels': ['Giải quyết vấn đề','Logic và quan sát','Phân tích và phân loại','Số và ký hiệu','Không gian và hình học','Suy luận toán học'],
        'nl': [(30,9),(25,12),(35,14),(30,8),(25,6),(20,4)],
        'cd': [('Dễ',15,9),('Trung bình',20,6),('Khó',25,3)],
    },
}

KTCB_UNIT_ABILITY = {
    'các số đến 9':'thực hiện phép tính và các bài toán số học',
    'phép cộng & phép trừ':'xử lý bài toán số học nhanh và chính xác',
    'phân loại':'tư duy logic, nhận ra điểm giống – khác và sắp xếp thông tin có hệ thống',
    'đo lường':'quan sát, so sánh và ước lượng',
    'các kiến thức toán tư duy khác':'quan sát, liên kết thông tin và tiếp cận bài toán mới',
}
KTCB_UNIT_IMPACT = {
    'các số đến 9':'ảnh hưởng đến khả năng thực hiện phép toán cơ bản và phức tạp',
    'phép cộng & phép trừ':'ảnh hưởng đến khả năng tính toán chính xác và giải bài toán',
    'phân loại':'ảnh hưởng đến khả năng tổ chức và xử lý thông tin',
    'đo lường':'cần củng cố khả năng sử dụng và chuyển đổi đơn vị đo trong các tình huống thực tế',
    'các kiến thức toán tư duy khác':'ảnh hưởng đến khả năng linh hoạt giải quyết các bài toán nâng cao',
}
KTCB_DIFFICULTY = {
    'khó':'bài toán khó, cần suy luận logic rõ rệt hoặc tư duy nhiều bước',
    'trung bình':'bài toán cần suy luận ngắn hoặc 2 bước xử lý',
    'dễ':'bài toán cơ bản, nhận biết trực quan, chỉ 1 bước xử lý',
}
TUDUY_GROUP_ABILITY = {
    'giải quyết vấn đề':'áp dụng kiến thức đã học, lập luận để giải quyết những bài toán mới',
    'logic và quan sát':'tìm ra mối quan hệ hoặc bản chất sự vật thông qua trực quan',
    'phân tích và phân loại':'thu thập, phân loại thông tin để giải quyết vấn đề',
    'số và ký hiệu':'vận dụng và công thức hóa khái niệm, ký hiệu toán học để giải quyết vấn đề',
    'không gian và hình học':'phát hiện và giải quyết những bài toán về hình học phẳng và không gian',
    'suy luận toán học':'sử dụng các phương pháp như quy nạp hay diễn dịch',
}

def pct_to_level(p):
    if p>=0.85: return 'Xuất sắc'
    if p>=0.65: return 'Tốt'
    if p>=0.50: return 'Khá'
    if p>=0.35: return 'Đạt'
    return 'Cần cố gắng'

def diff_label(s):
    n = s.lower().strip()
    if 'khó' in n: return 'khó'
    if 'trung' in n: return 'trung bình'
    if 'dễ' in n: return 'dễ'
    return ''

def tone_for(p):
    if p>=0.85: return 'rất tốt'
    if p>=0.65: return 'khá tốt'
    if p>=0.50: return 'tương đối ổn'
    return 'chưa thực sự rõ rệt'

def diff_tone_for(p):
    if p>=0.85: return 'rất tốt'
    if p>=0.65: return 'khá tốt'
    if p>=0.50: return 'ở mức tạm ổn'
    return 'còn hạn chế'

def fmt_int(x):
    return int(x) if x == int(x) else round(x,1)

def gen_ktcb(p):
    cur = sum(r[2] for r in p['kt'])
    mx  = sum(r[1] for r in p['kt'])
    pct = cur/mx if mx else 0
    level = pct_to_level(pct)
    items = [(lbl, c/m if m else 0) for lbl,m,c in p['kt']]
    items_sorted = sorted(items, key=lambda x: -x[1])
    top = items_sorted[0]
    bot = items_sorted[-1]
    top_ability = KTCB_UNIT_ABILITY.get(top[0].lower(), 'tiếp thu kiến thức cơ bản')
    bot_impact  = KTCB_UNIT_IMPACT.get(bot[0].lower(), 'ảnh hưởng đến nền tảng')

    ss = sorted([(s[0], s[2]/s[1] if s[1] else 0) for s in p['ss']], key=lambda x: -x[1])
    strong = ss[0]; weak = ss[-1]

    kq = [(r[0], r[2]/r[1] if r[1] else 0) for r in p['kq']]
    colVan = next((x for x in kq if 'có lời' in x[0].lower()), None)
    coBan  = next((x for x in kq if 'cơ bản' in x[0].lower() or 'không' in x[0].lower()), None)

    txt = f"Học viên đạt {fmt_int(cur)}/{fmt_int(mx)} điểm, tương đương {round(pct*100)}%, thuộc mức {level}."

    # Top sentence by pct band
    if top[1] >= 0.65:
        txt += f" Con có điểm mạnh ở {top[0]}, cho thấy khả năng {top_ability} {tone_for(top[1])}."
    elif top[1] >= 0.50:
        txt += f" Trong các đơn vị KTCB, {top[0]} là nội dung con nắm tương đối khá nhất, khả năng {top_ability} đang ở mức tạm ổn."
    else:
        txt += f" Hiện tại các đơn vị KTCB đều ở mức cần cải thiện, {top[0]} là phần con tiếp cận khá nhất nhưng vẫn cần luyện thêm."

    # Bottom sentence
    if top != bot and bot[1] < 0.65 and (top[1]-bot[1]) >= 0.15:
        txt += f" Tuy nhiên, {bot[0]} còn yếu — điều này {bot_impact}."
    elif top != bot and bot[1] >= 0.80:
        txt += f" Các đơn vị còn lại đều ở mức tốt — con đã xây được nền tảng KTCB vững."

    # Difficulty
    if strong:
        dl = diff_label(strong[0])
        if strong[1] >= 0.65:
            txt += f" Xét theo cấp độ, con xử lý {diff_tone_for(strong[1])} các bài ở mức {dl}."
        elif strong[1] >= 0.50:
            txt += f" Xét theo cấp độ, con xử lý các bài ở mức {dl} tạm ổn — chưa thực sự vững."
        else:
            txt += f" Xét theo cấp độ, con còn chật vật ngay cả ở mức {dl}, cần xây nền tảng vững hơn."
    if weak and strong != weak and weak[1] < 0.50:
        wl = diff_label(weak[0])
        desc = KTCB_DIFFICULTY.get(wl, '')
        if desc:
            txt += f" Cần ưu tiên rèn thêm với {desc}."

    # Bài toán có lời
    if colVan and coBan:
        if colVan[1] >= 0.65 and coBan[1] >= 0.65:
            txt += " Con xử lý tốt cả bài toán có lời văn lẫn bài toán cơ bản — đã có khả năng chuyển dữ kiện sang phép toán."
        elif colVan[1] >= coBan[1] and colVan[1] >= 0.50:
            txt += " Con xử lý tốt hơn với bài toán có lời văn — đã có khả năng đọc hiểu đề và chuyển dữ kiện thành phép toán."
        elif coBan[1] >= colVan[1] and coBan[1] >= 0.50:
            txt += " Con làm bài toán cơ bản tốt hơn, nhưng còn yếu ở bài toán có lời văn — cần rèn thêm kỹ năng đọc hiểu đề và chuyển dữ kiện thành phép toán."
        else:
            txt += f" Kết quả bài toán có lời văn ({round(colVan[1]*100)}%) và bài toán cơ bản ({round(coBan[1]*100)}%) đều còn thấp — cần rèn cả kỹ năng đọc hiểu lẫn tính toán trực tiếp."
    return txt

def gen_tuduy(p):
    cur = sum(p['qscore'])
    mx  = sum(p['qscore_max'])
    pct = cur/mx if mx else 0
    level = pct_to_level(pct)
    items = [(lbl, c/m if m else 0) for lbl,(m,c) in zip(p['nl_labels'], p['nl'])]
    items_sorted = sorted(items, key=lambda x: -x[1])
    top = items_sorted[0]; bot = items_sorted[-1]
    top_ab = TUDUY_GROUP_ABILITY.get(top[0].lower(), 'tư duy logic và phân tích')
    bot_ab = TUDUY_GROUP_ABILITY.get(bot[0].lower(), 'tư duy logic và phân tích')
    cd = sorted([(s[0], s[2]/s[1] if s[1] else 0) for s in p['cd']], key=lambda x: -x[1])
    strong = cd[0]; weak = cd[-1]

    txt = f"Học viên đạt {fmt_int(cur)}/{fmt_int(mx)} điểm, tương đương {round(pct*100)}%, thuộc mức {level}."

    if top[1] >= 0.65:
        txt += f" Con có thế mạnh ở nhóm {top[0]} — khả năng {top_ab} {tone_for(top[1])}."
    elif top[1] >= 0.50:
        txt += f" Trong các nhóm tư duy, {top[0]} là phần con làm khá nhất, khả năng {top_ab} đang dần hình thành."
    else:
        txt += f" Hiện tại các nhóm tư duy của con đều cần luyện thêm; {top[0]} là nhóm con xử lý khá nhất nhưng chưa thực sự vững."

    if top != bot and bot[1] < 0.65 and (top[1]-bot[1]) >= 0.10:
        txt += f" Ngược lại, {bot[0]} còn yếu — con cần rèn thêm khả năng {bot_ab}."
    elif top != bot and bot[1] >= 0.80:
        txt += " Các nhóm tư duy còn lại cũng ở mức tốt — con phát triển khá đồng đều."

    if strong:
        dl = diff_label(strong[0])
        if strong[1] >= 0.65:
            txt += f" Xét theo độ khó, con xử lý {diff_tone_for(strong[1])} các bài ở mức {dl}"
            if dl == 'khó':
                txt += " — đã hình thành khả năng tư duy logic và sáng tạo ở mức độ cao."
            elif dl == 'trung bình':
                txt += " — đang phát triển khả năng tư duy logic và sáng tạo ở mức độ khá, cần thử thách thêm với bài khó."
            else:
                txt += " — đã nắm vững nền tảng, cần thử thách thêm với bài trung bình và khó."
        elif strong[1] >= 0.50:
            txt += f" Xét theo độ khó, con xử lý các bài ở mức {dl} tạm ổn nhưng chưa thực sự vững."
        else:
            txt += f" Xét theo độ khó, con còn chật vật ngay với bài mức {dl} — cần xây nền tảng tư duy logic từ cơ bản."
    if weak and strong != weak and weak[1] < 0.50:
        wl = diff_label(weak[0])
        txt += f" Đặc biệt với bài mức {wl}, con cần được hỗ trợ và luyện tập thêm."
    return txt


print("=" * 80)
print("AUDIT v2 — SAU FIX")
print("=" * 80)
for key, prof in PROFILES.items():
    print(f"\n{'━'*80}")
    print(f"━━ PROFILE: {prof['name']}")
    print('━'*80)
    cur_kt = sum(r[2] for r in prof['kt']); mx_kt = sum(r[1] for r in prof['kt'])
    cur_td = sum(prof['qscore']); mx_td = sum(prof['qscore_max'])
    print(f"  KTCB: {cur_kt}/{mx_kt} = {round(cur_kt/mx_kt*100)}% ({pct_to_level(cur_kt/mx_kt)})")
    print(f"  TƯ DUY: {cur_td}/{mx_td} = {round(cur_td/mx_td*100)}% ({pct_to_level(cur_td/mx_td)})")
    print()
    print("[NHẬN XÉT KTCB]")
    print(gen_ktcb(prof))
    print()
    print("[NHẬN XÉT TƯ DUY]")
    print(gen_tuduy(prof))
    print()
