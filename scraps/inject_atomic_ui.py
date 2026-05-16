"""Inject Atomic Workspace UI (HTML + CSS + JS init) vào mau-giao.html"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

target = r'C:/Users/Admin/Downloads/wks/mau-giao.html'
with open(target, 'r', encoding='utf-8') as f:
    html = f.read()

# 1. CSS chèn trước </style> đầu tiên (style chính)
CSS = '''
/* ═══════════════════════════════════════════════════════════════
   ATOMIC WORKSPACE — Floating panel cho GV chấm 63 tiêu chí
   ═══════════════════════════════════════════════════════════════ */
#atomic-workspace{
  position:fixed;top:60px;left:50%;transform:translateX(-50%);
  width:96%;max-width:1100px;max-height:88vh;
  background:#fffbf0;border:2px solid var(--orange);border-radius:18px;
  box-shadow:0 20px 60px rgba(120,60,10,.25);
  z-index:200;display:none;flex-direction:column;overflow:hidden;
}
#atomic-workspace.open{display:flex}
.atomic-header{
  padding:14px 22px;background:linear-gradient(90deg,#ffe5ad,#fcd685);
  display:flex;align-items:center;gap:14px;flex-wrap:wrap;
  border-bottom:2px solid #f3c66e;
}
.atomic-header h2{
  margin:0;font:800 17px/1.2 var(--font-display);color:var(--orange-deep);
  flex:1;min-width:200px;
}
.atomic-header .atomic-actions{display:flex;gap:8px}
.atomic-header button{
  appearance:none;border:1.5px solid var(--orange);background:#fff;
  color:var(--orange-deep);font:700 12.5px/1 var(--font-body);
  padding:8px 14px;border-radius:99px;cursor:pointer;
  transition:all .15s ease;
}
.atomic-header button:hover{background:var(--orange);color:#fff}
.atomic-header button.primary{background:var(--orange);color:#fff}
.atomic-header button.primary:hover{background:var(--orange-deep)}
.atomic-legend{
  padding:10px 22px;background:#fff;border-bottom:1px solid var(--hair-soft);
  font:600 11.5px/1.4 var(--font-body);color:var(--ink-soft);
  display:flex;flex-wrap:wrap;gap:14px;align-items:center;
}
.atomic-legend .lvl{display:inline-flex;align-items:center;gap:5px}
.atomic-legend .lvl b{
  display:inline-flex;align-items:center;justify-content:center;
  width:22px;height:22px;border-radius:50%;color:#fff;font-weight:900;
}
.atomic-legend .lvl[data-l="5"] b{background:var(--g-S)}
.atomic-legend .lvl[data-l="4"] b{background:var(--g-A)}
.atomic-legend .lvl[data-l="3"] b{background:var(--g-B)}
.atomic-legend .lvl[data-l="2"] b{background:var(--g-C)}
.atomic-legend .lvl[data-l="0"] b{background:var(--g-L)}
.atomic-legend label{margin-left:auto;cursor:pointer;display:inline-flex;align-items:center;gap:6px}
.atomic-content{
  flex:1;overflow-y:auto;padding:14px 22px;
}
.atomic-cau{
  margin-bottom:14px;border:1.5px solid var(--hair-soft);
  border-radius:12px;background:#fff;overflow:hidden;
}
.atomic-cau-header{
  padding:8px 14px;background:#fff7e2;border-bottom:1px solid var(--hair-soft);
  display:flex;align-items:center;gap:12px;
  font:700 13px/1.2 var(--font-display);color:var(--ink);
}
.atomic-cau-header .cau-num{
  width:26px;height:26px;border-radius:50%;background:var(--orange);
  color:#fff;display:flex;align-items:center;justify-content:center;
  font:800 13px/1 var(--font-display);flex-shrink:0;
}
.atomic-cau-header .cau-title{flex:1}
.atomic-cau-header .cau-total{
  font:700 12.5px/1 var(--font-display);
  padding:5px 11px;border-radius:99px;background:#f3e7c5;color:var(--ink-soft);
}
.atomic-cau-header .cau-total.ok{background:#dff5d6;color:#2d7d2d}
.atomic-cau-header .cau-total.partial{background:#fdecc7;color:#9a6e10}
.atomic-table{width:100%;border-collapse:collapse}
.atomic-table th{
  font:700 9.5px/1 var(--font-body);color:var(--ink-mute);
  letter-spacing:.06em;text-transform:uppercase;text-align:left;
  padding:7px 10px;border-bottom:1px solid var(--hair-soft);background:#fffaf0;
}
.atomic-table th.center{text-align:center}
.atomic-table td{
  padding:7px 10px;border-bottom:1px solid #f5e9c8;
  font:500 12px/1.4 var(--font-body);color:var(--ink);vertical-align:middle;
}
.atomic-table tr:last-child td{border-bottom:0}
.atomic-table .ma{font:800 11px/1 var(--font-display);color:var(--orange-deep);width:42px;text-align:center}
.atomic-table .label{font-weight:600;min-width:200px}
.atomic-table .weight{width:60px;text-align:center;color:var(--ink-mute);font-size:11px;display:none}
.atomic-table.show-weights .weight{display:table-cell}
.atomic-table .ability-tag{
  display:inline-block;padding:2px 7px;border-radius:99px;
  font:700 9.5px/1.4 var(--font-body);background:#eef6fb;color:#1f4f7a;
  white-space:nowrap;
}
.atomic-table .info-btn{
  width:20px;height:20px;border-radius:50%;border:1.5px solid var(--hair);
  background:#fff;color:var(--ink-mute);font:800 10px/1 var(--font-body);
  cursor:pointer;transition:all .15s ease;
}
.atomic-table .info-btn:hover{background:var(--orange);color:#fff;border-color:var(--orange)}
.atomic-table .levels{display:inline-flex;gap:5px}
.atomic-table .levels button{
  width:32px;height:32px;border-radius:8px;
  border:1.5px solid var(--hair-soft);background:#fffaf0;
  color:var(--ink-soft);font:800 13px/1 var(--font-display);
  cursor:pointer;transition:all .15s ease;
}
.atomic-table .levels button:hover{transform:scale(1.08);filter:brightness(1.05)}
.atomic-table .levels button.active[data-lvl="5"]{background:var(--g-S);color:#fff;border-color:var(--g-S)}
.atomic-table .levels button.active[data-lvl="4"]{background:var(--g-A);color:#fff;border-color:var(--g-A)}
.atomic-table .levels button.active[data-lvl="3"]{background:var(--g-B);color:#fff;border-color:var(--g-B)}
.atomic-table .levels button.active[data-lvl="2"]{background:var(--g-C);color:#fff;border-color:var(--g-C)}
.atomic-table .levels button.active[data-lvl="0"]{background:var(--g-L);color:#fff;border-color:var(--g-L)}
.atomic-status{
  position:sticky;bottom:0;padding:10px 22px;
  background:#fffaf0;border-top:2px solid var(--hair-soft);
  font:600 12px/1.4 var(--font-body);color:var(--ink-soft);
  display:flex;justify-content:space-between;align-items:center;gap:14px;
}
.atomic-status .progress{
  flex:1;height:12px;background:#f3e7c5;border-radius:99px;overflow:hidden;
}
.atomic-status .progress .fill{height:100%;background:var(--orange);width:0%;transition:width .3s ease}
.atomic-status .total{font:800 14px/1 var(--font-display);color:var(--orange-deep)}
@media print{#atomic-workspace{display:none !important}}
'''

# 2. HTML workspace shell + toolbar button
TOOLBAR_BTN = '''
  <button onclick="toggleAtomicWorkspaceMG()" id="atomic-toggle-btn" title="Mở bảng chấm chi tiết 63 tiêu chí (chỉ GV thấy, phụ huynh không lưu vào PDF)">
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M9 2v6m6-6v6M9 14h6M3 6h18M5 22h14a2 2 0 0 0 2-2V6a2 2 0 0 0-2-2H5a2 2 0 0 0-2 2v14a2 2 0 0 0 2 2z"/></svg>
    Chấm 63 tiêu chí
  </button>'''

# Workspace shell
WORKSPACE_HTML = '''
<!-- ATOMIC WORKSPACE — GV-only, chỉ hiện khi toggle ON, ẩn hoàn toàn khi print -->
<div id="atomic-workspace">
  <div class="atomic-header">
    <h2>🎓 Chấm chi tiết 63 tiêu chí</h2>
    <div class="atomic-actions">
      <button onclick="resetAtomicMG();_buildAtomicUI_MG();" title="Xóa hết điểm đã chấm">↻ Reset</button>
      <button class="primary" onclick="applyAtomicToReportMG();_showToastMG('Đã áp dụng vào báo cáo','#5fb74f')" title="Tổng hợp 63 → 16 năng lực → cập nhật báo cáo">✓ Áp dụng vào báo cáo</button>
      <button onclick="toggleAtomicWorkspaceMG()" title="Đóng workspace">✕ Đóng</button>
    </div>
  </div>
  <div class="atomic-legend">
    <span>Thang điểm:</span>
    <span class="lvl" data-l="5"><b>5</b> Hoàn hảo</span>
    <span class="lvl" data-l="4"><b>4</b> Tốt</span>
    <span class="lvl" data-l="3"><b>3</b> Khá</span>
    <span class="lvl" data-l="2"><b>2</b> Hỗ trợ</span>
    <span class="lvl" data-l="0"><b>0</b> Chưa</span>
    <label><input type="checkbox" id="atomic-show-weights" onchange="document.querySelectorAll('.atomic-table').forEach(t=>t.classList.toggle('show-weights',this.checked))"> Hiện trọng số</label>
  </div>
  <div class="atomic-content" id="atomic-content">
    <!-- 14 câu groups render bằng _buildAtomicUI_MG() -->
  </div>
  <div class="atomic-status">
    <span>Tiến độ: <span id="atomic-filled-count">0</span>/63 tiêu chí</span>
    <div class="progress"><div class="fill" id="atomic-progress-fill"></div></div>
    <span class="total" id="atomic-total-display">0/170 — 0%</span>
  </div>
</div>'''

# 3. JS UI builder + toggle logic
JS_UI = '''

/* ═══════════════════════════════════════════════════════════════
   ATOMIC WORKSPACE UI — render 14 câu groups + handle input
   ═══════════════════════════════════════════════════════════════ */
function toggleAtomicWorkspaceMG(){
  const ws = document.getElementById('atomic-workspace');
  if(!ws) return;
  const opening = !ws.classList.contains('open');
  if(opening){
    _buildAtomicUI_MG();
    ws.classList.add('open');
    document.body.style.overflow = 'hidden';
  } else {
    ws.classList.remove('open');
    document.body.style.overflow = '';
  }
}

function _buildAtomicUI_MG(){
  const content = document.getElementById('atomic-content');
  if(!content) return;
  // Group criteria by câu
  const byCau = {};
  __ATOMIC_CRITERIA_L3.forEach(c => {
    if(!byCau[c.cau]) byCau[c.cau] = [];
    byCau[c.cau].push(c);
  });
  const cauTitles = {
    1:'Vẽ hình lục giác',
    2:'Nối quy luật chẵn/lẻ',
    3:'Ghi nhớ chuỗi yếu tố',
    4:'Phân loại người tuyết',
    5:'Phân nhóm 2 tiêu chí',
    6:'Xếp thứ tự câu chuyện',
    7:'Đặt đồ vào tủ lạnh',
    8:'Phép cộng tổng = 6',
    9:'Khoanh hình phù hợp',
    10:'So sánh cao thấp',
    11:'Nhận diện quy luật',
    12:'Đếm + biểu đồ bánh',
    13:'Sáng tạo từ 6 hình tròn',
    14:'Sáng tạo từ 6 hình vuông',
  };
  let html = '';
  Object.keys(byCau).sort((a,b)=>+a-+b).forEach(cau => {
    const criteria = byCau[cau];
    const maxSum = criteria.reduce((a,c)=>a+c.weight,0);
    html += '<div class="atomic-cau">';
    html += '  <div class="atomic-cau-header">';
    html += '    <span class="cau-num">'+cau+'</span>';
    html += '    <span class="cau-title">Câu '+cau+' — '+(cauTitles[cau]||'')+'</span>';
    html += '    <span class="cau-total" data-cau-total="'+cau+'">0/'+maxSum+'</span>';
    html += '  </div>';
    html += '  <table class="atomic-table"><thead><tr>';
    html += '    <th class="center">Mã</th>';
    html += '    <th>Tiêu chí</th>';
    html += '    <th class="weight">Trọng số</th>';
    html += '    <th>Năng lực đo</th>';
    html += '    <th class="center">Hướng dẫn</th>';
    html += '    <th class="center">Chấm</th>';
    html += '  </tr></thead><tbody>';
    criteria.forEach(c => {
      const skillLabel = __ATOMIC_SKILL_LABELS_MG[c.skill] || c.skill;
      html += '<tr>';
      html += '  <td class="ma">'+c.ma+'</td>';
      html += '  <td class="label">'+c.label+'</td>';
      html += '  <td class="weight">'+c.weight+'</td>';
      html += '  <td><span class="ability-tag">'+skillLabel+'</span></td>';
      html += '  <td class="center"><button class="info-btn" onclick="_showAtomicHelp_MG(\\''+c.ma+'\\')" title="Xem chi tiết 5 mức">ⓘ</button></td>';
      html += '  <td class="center"><div class="levels" data-ma="'+c.ma+'">';
      [5,4,3,2,0].forEach(lvl => {
        const active = __atomicScoresMG[c.ma] === lvl ? 'active' : '';
        html += '<button class="'+active+'" data-lvl="'+lvl+'" onclick="_pickAtomicLevel_MG(\\''+c.ma+'\\','+lvl+')">'+lvl+'</button>';
      });
      html += '  </div></td>';
      html += '</tr>';
    });
    html += '</tbody></table></div>';
  });
  content.innerHTML = html;
  _updateAtomicProgress_MG();
}

// Skill labels (Vietnamese) — mapping cho UI
const __ATOMIC_SKILL_LABELS_MG = {
  attention:'Chú ý', observation:'Quan sát', memory:'Ghi nhớ',
  number:'Số & tính toán', geometry:'Hình học KG', measurement:'Đo lường',
  pattern:'Kiểu mẫu', data:'Dữ liệu',
  understanding:'Hiểu biết', application:'Ứng dụng', analysis:'Phân tích', synthesis:'Tổng hợp',
  fluency:'Trôi chảy', flexibility:'Linh hoạt', originality:'Độc đáo', precision:'Chính xác',
};

function _pickAtomicLevel_MG(ma, level){
  // Toggle: nếu đang active mức này → unselect
  const curr = __atomicScoresMG[ma];
  if(curr === level){
    delete __atomicScoresMG[ma];
  } else {
    __atomicScoresMG[ma] = level;
  }
  // Update buttons in this row
  const row = document.querySelector('[data-ma="'+ma+'"]');
  if(row){
    row.querySelectorAll('button').forEach(btn => {
      btn.classList.toggle('active', __atomicScoresMG[ma] === +btn.dataset.lvl);
    });
  }
  _updateAtomicProgress_MG();
}

function _updateAtomicProgress_MG(){
  const agg = aggregateAtomicMG();
  const filled = Object.keys(__atomicScoresMG).length;
  const total = __ATOMIC_CRITERIA_L3.length;
  document.getElementById('atomic-filled-count').textContent = filled;
  const pct = total ? Math.round(filled/total*100) : 0;
  document.getElementById('atomic-progress-fill').style.width = pct + '%';
  document.getElementById('atomic-total-display').textContent =
    (Math.round(agg.total.score*10)/10) + '/' + agg.total.max + ' — ' + agg.total.pct + '%';
  // Update mỗi câu total
  for(const cau in agg.cauSum){
    const el = document.querySelector('[data-cau-total="'+cau+'"]');
    if(el){
      const c = agg.cauSum[cau];
      const filled = c.filled === c.total ? '✓' : (c.filled > 0 ? '⚠' : '');
      el.innerHTML = (Math.round(c.score*10)/10) + '/' + c.max + ' ' + filled;
      el.className = 'cau-total ' + (c.filled === c.total ? 'ok' : (c.filled > 0 ? 'partial' : ''));
    }
  }
}

function _showAtomicHelp_MG(ma){
  const c = __ATOMIC_CRITERIA_L3.find(x => x.ma === ma);
  const d = __ATOMIC_DESCRIPTIONS_L3[ma];
  if(!c || !d) return;
  const lines = [];
  lines.push('═══ ' + c.ma + '. ' + c.label + ' ═══');
  lines.push('Trọng số: ' + c.weight + ' điểm · Năng lực đo: ' + (__ATOMIC_SKILL_LABELS_MG[c.skill] || c.skill));
  lines.push('');
  [5,4,3,2,0].forEach(lvl => {
    lines.push('Mức ' + lvl + ': ' + (d[lvl] || '—'));
  });
  alert(lines.join('\\n'));
}
'''

# Insert CSS before closing </style> (first occurrence of major style block — end around line ~900)
# Find the largest <style>...</style> block
style_end = html.find('</style>')
if style_end < 0:
    print('ERROR: </style> not found'); sys.exit(1)
html = html[:style_end] + CSS + html[style_end:]

# Insert toolbar button after print button or before sep
# Find "Cập nhật" button (forceRefreshMG)
needle1 = '<button onclick="forceRefreshMG()"'
idx1 = html.find(needle1)
if idx1 < 0:
    print('ERROR: forceRefresh button not found'); sys.exit(1)
# Insert atomic toggle button before forceRefresh
html = html[:idx1] + TOOLBAR_BTN + '\n  ' + html[idx1:]

# Insert workspace HTML right after toolbar </div>
needle2 = '</div>\n\n<div class="page"'
idx2 = html.find(needle2)
if idx2 < 0:
    print('ERROR: insertion point for workspace not found')
    sys.exit(1)
html = html[:idx2] + '</div>\n' + WORKSPACE_HTML + '\n\n<div class="page"' + html[idx2+len('</div>\n\n<div class="page"'):]

# Insert JS at end of script (before </script>)
last_script_close = html.rfind('</script>')
if last_script_close < 0:
    print('ERROR: </script> not found'); sys.exit(1)
html = html[:last_script_close] + JS_UI + html[last_script_close:]

with open(target, 'w', encoding='utf-8') as f:
    f.write(html)

print('UI injection done. New size:', len(html))
