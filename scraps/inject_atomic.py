"""Inject atomic L3 data + aggregation engine vào mau-giao.html
   Insertion point: trước /* ─── Excel insight analytics
"""
import sys, io
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

target_path = r'C:/Users/Admin/Downloads/wks/mau-giao.html'
atomic_path = r'C:/Users/Admin/Downloads/wks/scraps/atomic_l3_data.js'

with open(target_path, 'r', encoding='utf-8') as f:
    html = f.read()

with open(atomic_path, 'r', encoding='utf-8') as f:
    atomic_data = f.read()

# Aggregation engine — chèn sau atomic data
engine = '''

/* ═══════════════════════════════════════════════════════════════
   ATOMIC AGGREGATION ENGINE — atomic scores → 16 năng lực + 4 lĩnh vực
   ═══════════════════════════════════════════════════════════════ */

// State: atomic scores object {ma: mức (0/2/3/4/5)}
let __atomicScoresMG = {};

// Tính điểm đạt cho 1 atomic: trọng số × hệ số nhân
function _atomicPointMG(ma, level){
  const c = __ATOMIC_CRITERIA_L3.find(x => x.ma === ma);
  if(!c) return 0;
  const mult = __ATOMIC_MULTIPLIER_L3[level];
  if(mult == null) return 0;
  return Math.round(c.weight * mult * 100) / 100;
}

// Aggregate atomic scores → 16 skills (per dataKey)
function aggregateAtomicMG(scores){
  scores = scores || __atomicScoresMG;
  const skillSum = {};   // {observation: {score: X, max: Y}}
  const cauSum = {};     // {1: {score: X, max: 10}, ...}
  __ATOMIC_CRITERIA_L3.forEach(c => {
    const lvl = scores[c.ma];
    const point = lvl != null ? _atomicPointMG(c.ma, lvl) : 0;
    // Per-skill aggregate
    if(!skillSum[c.skill]) skillSum[c.skill] = {score:0, max:0};
    skillSum[c.skill].score += point;
    skillSum[c.skill].max += c.weight;
    // Per-câu aggregate
    if(!cauSum[c.cau]) cauSum[c.cau] = {score:0, max:0, filled:0, total:0};
    cauSum[c.cau].score += point;
    cauSum[c.cau].max += c.weight;
    cauSum[c.cau].total++;
    if(lvl != null) cauSum[c.cau].filled++;
  });

  // Convert skillSum → grade letter
  const skillGrades = {};
  for(const k in skillSum){
    const s = skillSum[k];
    s.pct = s.max ? Math.round(s.score / s.max * 100) : 0;
    s.grade = _pctToGradeMG(s.pct);
    skillGrades[k] = s;
  }
  // Per-lĩnh vực aggregate (4 nhóm)
  const fieldMap = {
    'basic':['attention','observation','memory'],
    'math':['number','geometry','measurement','pattern','data'],
    'logic':['understanding','application','analysis','synthesis'],
    'creative':['fluency','flexibility','originality','precision'],
  };
  const fields = {};
  for(const f in fieldMap){
    let sc=0, mx=0;
    fieldMap[f].forEach(sk => {
      if(skillSum[sk]){ sc += skillSum[sk].score; mx += skillSum[sk].max; }
    });
    fields[f] = {score:sc, max:mx, pct: mx ? Math.round(sc/mx*100) : 0};
    fields[f].grade = _pctToGradeMG(fields[f].pct);
  }
  // Total
  const totalScore = Object.values(skillSum).reduce((a,s)=>a+s.score,0);
  const totalMax = Object.values(skillSum).reduce((a,s)=>a+s.max,0);
  return {
    skillSum, skillGrades, cauSum, fields,
    total: {score: totalScore, max: totalMax, pct: totalMax ? Math.round(totalScore/totalMax*100) : 0},
  };
}

// Apply atomic aggregation → fill 16 skill spans in section 2
function applyAtomicToReportMG(){
  const agg = aggregateAtomicMG();
  // Fill từng .ability tbody td:last-child span[data-skill]
  document.querySelectorAll('.ability tbody td:last-child span[data-skill]').forEach(span => {
    const skill = span.dataset.skill;
    const s = agg.skillGrades[skill];
    if(s){
      const g = s.grade;
      span.textContent = __GRADE_NAME[g] || g;
      span.className = 'g' + g;
    }
  });
  // Trigger recompute (radar + mini radars + s1-cards)
  if(typeof recomputeAllMG === 'function') recomputeAllMG();
  if(typeof scheduleSaveMG === 'function') scheduleSaveMG();
  return agg;
}

// Set score cho 1 atomic + cập nhật DOM
function setAtomicScoreMG(ma, level){
  if(level === null || level === undefined || level === ''){
    delete __atomicScoresMG[ma];
  } else {
    __atomicScoresMG[ma] = Number(level);
  }
  // Update cau total display
  const agg = aggregateAtomicMG();
  for(const cau in agg.cauSum){
    const el = document.querySelector('[data-cau-total="' + cau + '"]');
    if(el){
      const c = agg.cauSum[cau];
      const filled = c.filled === c.total ? '✓' : '⚠';
      el.innerHTML = (Math.round(c.score*10)/10) + '/' + c.max + ' ' + filled;
      el.className = 'cau-total ' + (c.filled === c.total ? 'ok' : 'partial');
    }
  }
}

// Reset all atomic scores
function resetAtomicMG(){
  __atomicScoresMG = {};
}

'''

# Find insertion point
needle = '/* ─── Excel insight analytics: units, abstraction, channel, Bloom ─── */'
idx = html.find(needle)
if idx < 0:
    print('ERROR: insertion point not found')
    sys.exit(1)

new_html = html[:idx] + atomic_data + engine + '\n' + html[idx:]

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(new_html)

print('Injection done.')
print('Original size:', len(html))
print('Atomic data size:', len(atomic_data))
print('Engine size:', len(engine))
print('New size:', len(new_html))
