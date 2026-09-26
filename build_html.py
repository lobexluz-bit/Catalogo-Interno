import json

with open('/home/claude/site/catalog_data.json', encoding='utf-8') as f:
    data = json.load(f)

data_json = json.dumps(data, ensure_ascii=False)

html_template = r"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>Lobex Luz — Catálogo</title>
<style>
:root {
  --bg: #16171a;
  --panel: #1e2024;
  --panel-2: #26282d;
  --line: #34363c;
  --text: #eef0f2;
  --text-dim: #9a9da4;
  --brass: #c9974f;
  --brass-soft: #6b5636;
  --focus: #e8b673;
}
* { box-sizing: border-box; }
html, body {
  margin: 0; padding: 0;
  background: var(--bg);
  color: var(--text);
  font-family: -apple-system, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
  padding-top: env(safe-area-inset-top, 0px);
  padding-bottom: env(safe-area-inset-bottom, 0px);
}
::selection { background: var(--brass-soft); color: #fff; }

.wrap { max-width: 1180px; margin: 0 auto; padding: 28px 20px 64px; }

header.top {
  position: sticky; top: env(safe-area-inset-top, 0px); z-index: 20;
  background: rgba(22,23,26,0.92);
  backdrop-filter: blur(6px);
  border-bottom: 1px solid var(--line);
}
.top-inner {
  max-width: 1180px; margin: 0 auto; padding: 18px 20px 16px;
}
.brand-row { display: flex; align-items: baseline; justify-content: space-between; gap: 12px; flex-wrap: wrap; }
.brand {
  font-size: 22px; letter-spacing: 0.01em; font-weight: 600; color: var(--text);
}
.brand span { color: var(--brass); }
.count-tag {
  font-size: 12.5px; color: var(--text-dim);
}

.search-row { margin-top: 14px; display: flex; gap: 10px; }
.search-box {
  flex: 1; position: relative;
}
.search-box input {
  width: 100%; padding: 13px 16px 13px 42px;
  background: var(--panel); border: 1px solid var(--line); border-radius: 10px;
  color: var(--text); font-size: 15.5px; outline: none;
  transition: border-color .15s ease;
}
.search-box input:focus { border-color: var(--brass); }
.search-icon {
  position: absolute; left: 14px; top: 50%; transform: translateY(-50%);
  width: 17px; height: 17px; opacity: 0.55; pointer-events: none;
}

.filters { margin-top: 12px; display: flex; gap: 8px; flex-wrap: wrap; }
.filters select {
  background: var(--panel); color: var(--text); border: 1px solid var(--line);
  border-radius: 8px; padding: 9px 10px; font-size: 13.5px; outline: none;
  max-width: 220px;
}
.filters select:focus { border-color: var(--brass); }
.clear-btn {
  background: transparent; color: var(--text-dim); border: 1px solid var(--line);
  border-radius: 8px; padding: 9px 12px; font-size: 13px; cursor: pointer;
}
.clear-btn:hover { color: var(--text); border-color: var(--text-dim); }

.results-meta {
  margin: 18px 2px 10px; color: var(--text-dim); font-size: 13px;
  display: flex; justify-content: space-between; align-items: center;
}

.grid { display: flex; flex-direction: column; gap: 8px; }

.card {
  background: var(--panel); border: 1px solid var(--line); border-radius: 10px;
  padding: 14px 16px; cursor: pointer;
  transition: border-color .12s ease, background .12s ease;
}
.card:hover { border-color: #4a4d55; background: var(--panel-2); }
.card.open { border-color: var(--brass); background: var(--panel-2); }

.card-top { display: flex; justify-content: space-between; gap: 14px; align-items: flex-start; }
.card-title { font-size: 15.5px; font-weight: 600; color: var(--text); }
.card-sub { font-size: 12.5px; color: var(--text-dim); margin-top: 2px; }
.card-code { font-size: 12.5px; color: var(--brass); white-space: nowrap; font-variant-numeric: tabular-nums; }

.chip-row { display: flex; gap: 6px; flex-wrap: wrap; margin-top: 9px; }
.chip {
  font-size: 11.5px; color: var(--text-dim); background: #2c2e33;
  border-radius: 6px; padding: 3px 8px; border: 1px solid var(--line);
}
.chip.b { color: var(--brass); border-color: var(--brass-soft); }

.detail {
  margin-top: 12px; padding-top: 12px; border-top: 1px solid var(--line);
  display: grid; grid-template-columns: repeat(auto-fill, minmax(160px, 1fr)); gap: 10px 18px;
  font-size: 13px;
}
.detail div dt { color: var(--text-dim); font-size: 11px; text-transform: none; margin-bottom: 2px; }
.detail div dd { margin: 0; color: var(--text); }

.empty {
  text-align: center; padding: 70px 20px; color: var(--text-dim);
}
.empty b { color: var(--text); }

footer.note {
  text-align: center; color: var(--text-dim); font-size: 12px; margin-top: 40px;
}

@media (prefers-color-scheme: light) {
  :root:not([data-theme="dark"]) {
    --bg: #f7f5f1;
    --panel: #ffffff;
    --panel-2: #f1ede5;
    --line: #e2ddd2;
    --text: #24211c;
    --text-dim: #7a746a;
    --brass: #a6742f;
    --brass-soft: #e6d3ae;
    --focus: #a6742f;
  }
}
:root[data-theme="dark"] { }
</style>
</head>
<body>

<header class="top">
  <div class="top-inner">
    <div class="brand-row">
      <div class="brand">Lobex <span>Luz</span> — Catálogo</div>
      <div class="count-tag" id="countTag"></div>
    </div>
    <div class="search-row">
      <div class="search-box">
        <svg class="search-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="7"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
        <input id="searchInput" type="text" placeholder="Buscar por nome, código, marca, cor, tipologia... (ex: pendente, OPS 34737, arandela indireta)" autocomplete="off">
      </div>
    </div>
    <div class="filters">
      <select id="filtroSecao"><option value="">Todas as seções</option></select>
      <select id="filtroMarca"><option value="">Todas as marcas</option></select>
      <select id="filtroTipoLuz"><option value="">Todos os tipos de luz</option></select>
      <select id="filtroMontagem"><option value="">Embutir/Sobrepor</option></select>
      <select id="filtroFormato"><option value="">Formato</option></select>
      <select id="filtroFonteLuz"><option value="">Tipo de fonte de luz</option></select>
      <select id="filtroCor"><option value="">Todas as cores</option></select>
      <button class="clear-btn" id="clearBtn">Limpar filtros</button>
    </div>
  </div>
</header>

<div class="wrap">
  <div class="results-meta">
    <span id="resultsCount"></span>
    <span id="hint" style="opacity:.7">Clique num item para ver a ficha completa</span>
  </div>
  <div class="grid" id="grid"></div>
  <div class="empty" id="emptyState" style="display:none">Nenhum item encontrado para <b id="emptyTerm"></b>.<br>Tente outro termo, código ou remova algum filtro.</div>
  <footer class="note">Lobex Luz · Base interna Opus Iluminação · __COUNT__ itens catalogados</footer>
</div>

<script id="catalog-data" type="application/json">__DATA__</script>
<script>
const RAW = JSON.parse(document.getElementById('catalog-data').textContent);

const FIELD_LABELS = {
  potencia: "Potência", voltagem: "Voltagem", temp_cor: "Temp. cor", lumens: "Lumens",
  angulo: "Ângulo", dimensoes: "Dimensões", irc: "IRC", ugr: "UGR", ip: "IP",
  garantia: "Garantia", composicao: "Composição", recursos: "Recursos", soquete: "Soquete/Base",
  sistema: "Sistema/Compatibilidade", acessorio_de: "Tipo de acessório", apelidos: "Também conhecido como",
  montagem: "Montagem", face: "Acabamento/Face", marcenaria: "Uso", marca: "Marca", formato: "Formato",
  fonte_luz: "Tipo de fonte de luz",
  categoria: "Categoria", subtipo: "Subtipo/Estilo", nicho: "Nicho", comprimento: "Comprimento",
  corte_a_cada: "Corte a cada", largura: "Largura", espessura: "Espessura", leds_m: "LEDs/m",
  tensao_saida: "Tensão de saída"
};
const DETAIL_ORDER = ["marca","montagem","formato","fonte_luz","face","marcenaria","sistema","acessorio_de","apelidos","potencia","voltagem","tensao_saida","temp_cor","lumens","leds_m","angulo","dimensoes","comprimento","corte_a_cada","largura","espessura","nicho","soquete","irc","ugr","ip","garantia","composicao","recursos"];

const secaoSel = document.getElementById('filtroSecao');
const marcaSel = document.getElementById('filtroMarca');
const tipoLuzSel = document.getElementById('filtroTipoLuz');
const montagemSel = document.getElementById('filtroMontagem');
const formatoSel = document.getElementById('filtroFormato');
const fonteLuzSel = document.getElementById('filtroFonteLuz');
const corSel = document.getElementById('filtroCor');
const searchInput = document.getElementById('searchInput');
const grid = document.getElementById('grid');
const emptyState = document.getElementById('emptyState');
const emptyTerm = document.getElementById('emptyTerm');
const resultsCount = document.getElementById('resultsCount');
const countTag = document.getElementById('countTag');

function uniqueSorted(field) {
  return [...new Set(RAW.map(d => d[field]).filter(Boolean))].sort((a,b)=>a.localeCompare(b,'pt-BR'));
}

function populateSelect(sel, values) {
  values.forEach(v => {
    const opt = document.createElement('option');
    opt.value = v; opt.textContent = v;
    sel.appendChild(opt);
  });
}

populateSelect(secaoSel, uniqueSorted('secao'));
populateSelect(marcaSel, uniqueSorted('marca'));
populateSelect(tipoLuzSel, uniqueSorted('tipo_luz'));
populateSelect(montagemSel, uniqueSorted('montagem'));
populateSelect(formatoSel, uniqueSorted('formato'));
populateSelect(fonteLuzSel, uniqueSorted('fonte_luz'));
populateSelect(corSel, uniqueSorted('cor'));

countTag.textContent = RAW.length.toLocaleString('pt-BR') + ' itens';

let openIndex = null;

function norm(s) {
  return (s||'').toString().toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'');
}

const STOPWORDS = new Set(['de','da','do','das','dos','para','com','em','e','a','o','os','as','um','uma','no','na','face','tipo','acabamento']);

function matchesSearch(item, termNorm) {
  if (!termNorm) return true;
  const haystack = norm([
    item.nome, item.codigo, item.marca, item.secao, item.categoria,
    item.subtipo, item.tipo_luz, item.cor, item.composicao, item.recursos,
    item.sistema, item.acessorio_de, item.apelidos, item.montagem, item.face, item.marcenaria,
    item.potencia, item.temp_cor, item.lumens, item.angulo, item.dimensoes, item.voltagem,
    item.ip, item.irc, item.soquete, item.nicho, item.comprimento, item.corte_a_cada,
    item.largura, item.espessura, item.leds_m, item.tensao_saida, item.garantia, item.formato, item.fonte_luz
  ].join(' | '));
  const tokens = termNorm.split(/\s+/).filter(tok => tok && !STOPWORDS.has(tok));
  if (tokens.length === 0) return true;
  return tokens.every(tok => {
    if (haystack.includes(tok)) return true;
    // naive singular/plural tolerance (acessorios -> acessorio, luminarias -> luminaria)
    if (tok.length > 3 && tok.endsWith('s') && haystack.includes(tok.slice(0, -1))) return true;
    return false;
  });
}

function render() {
  const term = norm(searchInput.value.trim());
  const secao = secaoSel.value, tipoLuz = tipoLuzSel.value, cor = corSel.value, montagem = montagemSel.value, marca = marcaSel.value, formato = formatoSel.value, fonteLuz = fonteLuzSel.value;

  const filtered = RAW.filter(item => {
    if (secao && item.secao !== secao) return false;
    if (marca && item.marca !== marca) return false;
    if (tipoLuz && item.tipo_luz !== tipoLuz) return false;
    if (montagem && item.montagem !== montagem) return false;
    if (formato && item.formato !== formato) return false;
    if (fonteLuz && item.fonte_luz !== fonteLuz) return false;
    if (cor && item.cor !== cor) return false;
    return matchesSearch(item, term);
  });

  resultsCount.textContent = filtered.length.toLocaleString('pt-BR') + ' resultado' + (filtered.length===1?'':'s');

  grid.innerHTML = '';
  if (filtered.length === 0) {
    emptyState.style.display = 'block';
    emptyTerm.textContent = searchInput.value.trim() ? '"' + searchInput.value.trim() + '"' : 'os filtros selecionados';
    return;
  }
  emptyState.style.display = 'none';

  const MAX_RENDER = 300;
  const toRender = filtered.slice(0, MAX_RENDER);

  toRender.forEach((item, i) => {
    const card = document.createElement('div');
    card.className = 'card';
    card.dataset.idx = i;

    const top = document.createElement('div');
    top.className = 'card-top';

    const left = document.createElement('div');
    const title = document.createElement('div');
    title.className = 'card-title';
    title.textContent = item.nome || '(sem nome)';
    const sub = document.createElement('div');
    sub.className = 'card-sub';
    sub.textContent = [item.marca, item.secao, item.subtipo || item.categoria].filter(Boolean).join(' · ');
    left.appendChild(title); left.appendChild(sub);

    const code = document.createElement('div');
    code.className = 'card-code';
    code.textContent = item.codigo || '';

    top.appendChild(left); top.appendChild(code);
    card.appendChild(top);

    const chipRow = document.createElement('div');
    chipRow.className = 'chip-row';
    const highlightVals = new Set([item.tipo_luz, item.sistema, item.acessorio_de, item.marcenaria].filter(Boolean));
    [item.marca, item.montagem, item.formato, item.fonte_luz, item.face, item.marcenaria, item.sistema, item.acessorio_de, item.cor, item.tipo_luz, item.potencia, item.temp_cor, item.lumens, item.ip].filter(Boolean).forEach(v => {
      const chip = document.createElement('span');
      chip.className = 'chip' + (highlightVals.has(v) ? ' b' : '');
      chip.textContent = v;
      chipRow.appendChild(chip);
    });
    card.appendChild(chipRow);

    card.addEventListener('click', () => {
      const already = card.classList.contains('open');
      grid.querySelectorAll('.card.open').forEach(c => {
        c.classList.remove('open');
        const d = c.querySelector('.detail'); if (d) d.remove();
      });
      if (!already) {
        card.classList.add('open');
        const detail = document.createElement('dl');
        detail.className = 'detail';
        DETAIL_ORDER.forEach(f => {
          if (item[f]) {
            const wrap = document.createElement('div');
            const dt = document.createElement('dt'); dt.textContent = FIELD_LABELS[f] || f;
            const dd = document.createElement('dd'); dd.textContent = item[f];
            wrap.appendChild(dt); wrap.appendChild(dd);
            detail.appendChild(wrap);
          }
        });
        card.appendChild(detail);
      }
    });

    grid.appendChild(card);
  });

  if (filtered.length > MAX_RENDER) {
    const more = document.createElement('div');
    more.style.cssText = 'text-align:center;padding:16px;color:var(--text-dim);font-size:13px';
    more.textContent = `Mostrando os primeiros ${MAX_RENDER} de ${filtered.length} resultados — refine a busca para ver itens mais específicos.`;
    grid.appendChild(more);
  }
}

searchInput.addEventListener('input', render);
secaoSel.addEventListener('change', render);
marcaSel.addEventListener('change', render);
tipoLuzSel.addEventListener('change', render);
montagemSel.addEventListener('change', render);
formatoSel.addEventListener('change', render);
fonteLuzSel.addEventListener('change', render);
corSel.addEventListener('change', render);
document.getElementById('clearBtn').addEventListener('click', () => {
  searchInput.value=''; secaoSel.value=''; marcaSel.value=''; tipoLuzSel.value=''; montagemSel.value=''; formatoSel.value=''; fonteLuzSel.value=''; corSel.value='';
  render();
});

render();
</script>
</body>
</html>
"""

html_out = html_template.replace("__DATA__", data_json).replace("__COUNT__", str(len(data)))

with open('/mnt/user-data/outputs/lobex_catalogo.html', 'w', encoding='utf-8') as f:
    f.write(html_out)

print("done, size:", len(html_out))
