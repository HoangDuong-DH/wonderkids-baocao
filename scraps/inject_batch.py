"""Inject BATCH IMPORT/EXPORT cho mau-giao.html
   - Multi-file upload
   - Bé navigator (prev/next)
   - Export current bé / Export ALL với confirm
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

target = r'C:/Users/Admin/Downloads/wks/mau-giao.html'
with open(target, 'r', encoding='utf-8') as f:
    html = f.read()

# CSS for batch panel
CSS = '''
/* ═══════════════════════════════════════════════════════════════
   BATCH MODE — Upload nhiều file Excel + export tuần tự
   ═══════════════════════════════════════════════════════════════ */
#batch-panel{
  position:fixed;top:60px;right:14px;width:380px;max-height:80vh;
  background:#fffbf0;border:2px solid var(--orange);border-radius:14px;
  box-shadow:0 18px 50px rgba(120,60,10,.22);
  z-index:180;display:none;flex-direction:column;overflow:hidden;
}
#batch-panel.open{display:flex}
.batch-header{
  padding:12px 16px;background:linear-gradient(90deg,#ffe5ad,#fcd685);
  display:flex;align-items:center;gap:8px;border-bottom:2px solid #f3c66e;
}
.batch-header h3{margin:0;flex:1;font:800 14px/1.2 var(--font-display);color:var(--orange-deep)}
.batch-header .close-btn{
  appearance:none;border:0;background:transparent;color:var(--orange-deep);
  font:800 18px/1 var(--font-body);cursor:pointer;padding:0 6px;
}
.batch-header .close-btn:hover{color:var(--ink)}
.batch-empty{
  padding:24px 16px;text-align:center;color:var(--ink-mute);
  font:500 12px/1.5 var(--font-body);
}
.batch-empty .upload-btn{
  display:inline-block;margin-top:10px;padding:9px 20px;
  background:var(--orange);color:#fff;font:700 13px/1 var(--font-body);
  border-radius:99px;cursor:pointer;transition:background .15s ease;
}
.batch-empty .upload-btn:hover{background:var(--orange-deep)}
.batch-list{
  flex:1;overflow-y:auto;padding:6px 8px;
}
.batch-item{
  display:flex;align-items:center;gap:8px;padding:8px 10px;
  border-radius:8px;cursor:pointer;transition:background .15s ease;
  border-bottom:1px solid var(--hair-soft);
}
.batch-item:hover{background:#fff7e2}
.batch-item.active{background:#ffe5ad;font-weight:700}
.batch-item .status-ico{
  width:22px;height:22px;border-radius:50%;flex-shrink:0;
  display:flex;align-items:center;justify-content:center;
  font:700 11px/1 var(--font-body);color:#fff;background:var(--ink-mute);
}
.batch-item .status-ico.done{background:var(--g-S)}
.batch-item .status-ico.active{background:var(--orange)}
.batch-item .item-info{flex:1;min-width:0}
.batch-item .item-name{font:600 12.5px/1.3 var(--font-body);color:var(--ink);
  overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
.batch-item .item-meta{font:500 10px/1.3 var(--font-body);color:var(--ink-mute)}
.batch-toolbar{
  padding:8px 12px;border-top:1px solid var(--hair-soft);
  display:flex;gap:6px;flex-wrap:wrap;background:#fff;
}
.batch-toolbar button{
  appearance:none;border:1.5px solid var(--orange);background:#fff;
  color:var(--orange-deep);font:700 11.5px/1 var(--font-body);
  padding:7px 10px;border-radius:8px;cursor:pointer;transition:all .15s ease;
  flex:1;
}
.batch-toolbar button:hover{background:var(--orange);color:#fff}
.batch-toolbar button.primary{background:var(--orange);color:#fff}
.batch-toolbar button.primary:hover{background:var(--orange-deep)}
.batch-toolbar button:disabled{opacity:.5;cursor:not-allowed}
.batch-progress{padding:8px 12px;background:#fffaf0;font:600 11px/1.4 var(--font-body);color:var(--ink-soft)}
.batch-progress .bar{height:6px;background:#f3e7c5;border-radius:99px;overflow:hidden;margin-top:5px}
.batch-progress .bar i{display:block;height:100%;background:var(--orange);transition:width .3s ease}
@media print{#batch-panel{display:none !important}}
'''

# HTML — batch panel
BATCH_HTML = '''
<!-- BATCH IMPORT/EXPORT panel — GV only -->
<input type="file" id="batch-files-input" accept=".xlsx,.xls" multiple style="position:absolute;width:1px;height:1px;opacity:0;pointer-events:none" onchange="_loadBatchFilesMG(event)"/>
<div id="batch-panel">
  <div class="batch-header">
    <h3>📦 Batch import</h3>
    <button class="close-btn" onclick="toggleBatchModeMG()" title="Đóng">✕</button>
  </div>
  <div id="batch-body">
    <div class="batch-empty" id="batch-empty">
      <div>Chưa có file nào tải</div>
      <div style="margin-top:6px;font-size:11px">Chấm xong 63 tiêu chí trong Excel → upload nhiều file cùng lúc</div>
      <label class="upload-btn" for="batch-files-input">📂 Chọn file Excel...</label>
    </div>
    <div class="batch-list" id="batch-list" style="display:none"></div>
  </div>
  <div class="batch-progress" id="batch-progress" style="display:none">
    <span id="batch-progress-text">Đang xuất 0/0...</span>
    <div class="bar"><i id="batch-progress-fill" style="width:0%"></i></div>
  </div>
  <div class="batch-toolbar" id="batch-toolbar" style="display:none">
    <button onclick="_navBatchMG(-1)" id="batch-prev" title="Bé trước">← Trước</button>
    <button onclick="_navBatchMG(1)" id="batch-next" title="Bé sau">Sau →</button>
    <button class="primary" onclick="exportCurrentBatchPDF()" title="In PDF bé hiện tại">🖨 In bé này</button>
    <button onclick="exportAllBatchPDF()" title="In lần lượt tất cả">📥 In ALL</button>
    <button onclick="_clearBatchMG()" title="Xóa danh sách" style="flex:0">🗑</button>
  </div>
</div>'''

# Toolbar button (insert near other tools)
TOOLBAR_BTN = '''
  <button onclick="toggleBatchModeMG()" id="batch-toggle-btn" title="Batch import nhiều file Excel + in PDF hàng loạt">
    <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M21 16V8a2 2 0 0 0-1-1.73l-7-4a2 2 0 0 0-2 0l-7 4A2 2 0 0 0 3 8v8a2 2 0 0 0 1 1.73l7 4a2 2 0 0 0 2 0l7-4A2 2 0 0 0 21 16z"/><polyline points="3.27 6.96 12 12.01 20.73 6.96"/><line x1="12" y1="22.08" x2="12" y2="12"/></svg>
    Batch
  </button>'''

# JS — batch logic
JS = '''

/* ═══════════════════════════════════════════════════════════════
   BATCH IMPORT/EXPORT — Multi-file Excel → bé navigator → print loop
   ═══════════════════════════════════════════════════════════════ */

const __batchDataMG = [];  // [{name, info, scores, fileName, exported}]
let __batchCurrentIdx = -1;

function toggleBatchModeMG(){
  const panel = document.getElementById('batch-panel');
  if(!panel) return;
  panel.classList.toggle('open');
}

async function _loadBatchFilesMG(ev){
  const files = ev.target?.files;
  if(!files || !files.length) return;
  // Wait XLSX if needed
  const ready = typeof _waitXlsxMG === 'function' ? await _waitXlsxMG() : (typeof XLSX !== 'undefined');
  if(!ready){
    _showToastMG('Thư viện XLSX chưa load, vui lòng đợi 5s rồi thử lại', '#d83c2d');
    ev.target.value = '';
    return;
  }
  let added = 0;
  for(const f of files){
    try{
      const data = await _parseBatchFileMG(f);
      if(data){
        __batchDataMG.push(data);
        added++;
      }
    }catch(err){
      console.warn('[batch] Skip file', f.name, err);
    }
  }
  ev.target.value = '';
  if(added > 0){
    _showToastMG('Đã tải ' + added + ' file (tổng ' + __batchDataMG.length + ' bé)', '#5fb74f');
    _renderBatchListMG();
    // Auto-select bé đầu tiên nếu chưa có
    if(__batchCurrentIdx < 0 && __batchDataMG.length > 0){
      _selectBatchBeMG(0);
    }
  } else {
    _showToastMG('Không đọc được file nào — kiểm tra format Atomic L3', '#d83c2d');
  }
}

async function _parseBatchFileMG(file){
  const buf = await file.arrayBuffer();
  const wb = XLSX.read(buf, {type:'array', cellDates:false});
  const info = {};
  const scores = {};

  // Sheet "2.Thông tin HS" — info fields
  const infoSheet = wb.Sheets['2.Thông tin HS'] || wb.Sheets[wb.SheetNames.find(n => /thông tin/i.test(n))];
  if(infoSheet){
    const rows = XLSX.utils.sheet_to_json(infoSheet, {header:1, defval:''});
    rows.forEach(r => {
      if(!r || !r[0] || !r[1]) return;
      const label = String(r[0]).toLowerCase().trim();
      const value = String(r[1]).trim();
      if(label.includes('họ và tên') || label === 'tên') info.name = value;
      else if(label.includes('giới tính')) info.sex = value;
      else if(label.includes('ngày sinh') || label.includes('năm sinh')){
        // Extract year
        const m = value.match(/(\\d{4})/);
        if(m) info.yob = m[1];
      }
      else if(label.includes('lớp')) info.class = value;
      else if(label.includes('ngày đánh giá')) info.date = value;
      else if(label.includes('giáo viên')) info.teacher = value;
    });
  }

  // Sheet "3.Nhập atomic" — 63 atomic scores
  const atomicSheet = wb.Sheets['3.Nhập atomic'] || wb.Sheets[wb.SheetNames.find(n => /nhập atomic/i.test(n))];
  if(atomicSheet){
    const rows = XLSX.utils.sheet_to_json(atomicSheet, {header:1, defval:''});
    rows.forEach(r => {
      if(!r || r.length < 5) return;
      const ma = String(r[1] || '').trim();
      const muc = r[4];
      if(!ma || !/^\\d+\\.\\d+$/.test(ma)) return;
      const lvl = parseInt(muc, 10);
      if([5,4,3,2,0].includes(lvl)) scores[ma] = lvl;
    });
  }

  if(Object.keys(scores).length < 30){
    return null;  // Không đủ data, skip
  }
  return {
    name: info.name || file.name.replace(/\\.[^.]+$/, ''),
    fileName: file.name,
    info, scores,
    exported: false,
  };
}

function _renderBatchListMG(){
  const empty = document.getElementById('batch-empty');
  const list = document.getElementById('batch-list');
  const toolbar = document.getElementById('batch-toolbar');
  if(__batchDataMG.length === 0){
    empty.style.display = '';
    list.style.display = 'none';
    toolbar.style.display = 'none';
    return;
  }
  empty.style.display = 'none';
  list.style.display = '';
  toolbar.style.display = '';
  let html = '';
  __batchDataMG.forEach((b, i) => {
    const status = b.exported ? 'done' : (i === __batchCurrentIdx ? 'active' : '');
    const ico = b.exported ? '✓' : (i + 1);
    html += '<div class="batch-item ' + (i === __batchCurrentIdx ? 'active' : '') + '" onclick="_selectBatchBeMG(' + i + ')">';
    html += '  <span class="status-ico ' + status + '">' + ico + '</span>';
    html += '  <span class="item-info">';
    html += '    <span class="item-name">' + (b.name || '—') + '</span>';
    html += '    <span class="item-meta">' + Object.keys(b.scores).length + '/63 tiêu chí</span>';
    html += '  </span>';
    html += '</div>';
  });
  list.innerHTML = html;
  // Add upload-more button at bottom
  list.innerHTML += '<label for="batch-files-input" class="batch-item" style="justify-content:center;color:var(--orange-deep);font-weight:700;cursor:pointer;padding:10px"><span>＋ Thêm file</span></label>';
}

function _selectBatchBeMG(idx){
  if(idx < 0 || idx >= __batchDataMG.length) return;
  __batchCurrentIdx = idx;
  const b = __batchDataMG[idx];
  // Apply data to current report
  if(typeof _cleanSlateMG === 'function') _cleanSlateMG();
  if(typeof _applyMG_InfoFields === 'function') _applyMG_InfoFields(b.info);
  // Apply atomic scores
  __atomicScoresMG = Object.assign({}, b.scores);
  if(typeof applyAtomicToReportMG === 'function') applyAtomicToReportMG();
  if(typeof fillCommentsMG === 'function') fillCommentsMG(true);
  _renderBatchListMG();
  _showToastMG('Đã hiển thị: ' + (b.name || 'bé'), '#3ea1d3');
}

function _navBatchMG(dir){
  const newIdx = __batchCurrentIdx + dir;
  if(newIdx >= 0 && newIdx < __batchDataMG.length){
    _selectBatchBeMG(newIdx);
  }
}

function exportCurrentBatchPDF(){
  if(__batchCurrentIdx < 0){
    _showToastMG('Chưa chọn bé nào', '#df5728');
    return;
  }
  const b = __batchDataMG[__batchCurrentIdx];
  // Mark exported + print
  b.exported = true;
  _renderBatchListMG();
  setTimeout(() => window.print(), 200);
}

async function exportAllBatchPDF(){
  if(__batchDataMG.length === 0) return;
  if(!confirm('Sẽ in lần lượt ' + __batchDataMG.length + ' báo cáo. Mỗi báo cáo bạn cần bấm Save trong dialog in. Tiếp tục?')) return;
  const progressEl = document.getElementById('batch-progress');
  const textEl = document.getElementById('batch-progress-text');
  const fillEl = document.getElementById('batch-progress-fill');
  progressEl.style.display = '';
  for(let i = 0; i < __batchDataMG.length; i++){
    _selectBatchBeMG(i);
    const pct = Math.round((i+1) / __batchDataMG.length * 100);
    textEl.textContent = 'Đang xuất ' + (i+1) + '/' + __batchDataMG.length + ' — ' + (__batchDataMG[i].name || '');
    fillEl.style.width = pct + '%';
    await new Promise(r => setTimeout(r, 500));  // wait render
    __batchDataMG[i].exported = true;
    _renderBatchListMG();
    window.print();
    await new Promise(r => setTimeout(r, 800));  // wait dialog
  }
  textEl.textContent = '✓ Hoàn tất ' + __batchDataMG.length + ' báo cáo';
  setTimeout(() => progressEl.style.display = 'none', 3000);
}

function _clearBatchMG(){
  if(__batchDataMG.length === 0) return;
  if(!confirm('Xóa toàn bộ danh sách ' + __batchDataMG.length + ' bé?')) return;
  __batchDataMG.length = 0;
  __batchCurrentIdx = -1;
  _renderBatchListMG();
  _showToastMG('Đã xóa danh sách batch', '#3ea1d3');
}
'''

# Insert
style_end = html.find('</style>')
html = html[:style_end] + CSS + html[style_end:]

# Toolbar button before atomic-toggle
needle1 = '<button onclick="toggleAtomicWorkspaceMG()"'
idx1 = html.find(needle1)
if idx1 < 0:
    # Fallback: before forceRefresh
    needle1 = '<button onclick="forceRefreshMG()"'
    idx1 = html.find(needle1)
html = html[:idx1] + TOOLBAR_BTN + '\n  ' + html[idx1:]

# HTML panel before <div class="page"
needle2 = '<div id="atomic-workspace">'
idx2 = html.find(needle2)
if idx2 < 0:
    needle2 = '<div class="page"'
    idx2 = html.find(needle2)
html = html[:idx2] + BATCH_HTML + '\n\n' + html[idx2:]

# JS at end of script
last_script_close = html.rfind('</script>')
html = html[:last_script_close] + JS + html[last_script_close:]

with open(target, 'w', encoding='utf-8') as f:
    f.write(html)

print('Batch injection done. Final size:', len(html))
