# Lobex Luz — Catálogo Unificado — Convenções do Projeto

## Visão geral
Site de busca (`index.html`) que consolida catálogos de fornecedores de iluminação
em um único dataset JSON embutido. Já processados: **Opus** (1094 itens),
**Gaya** (1422 itens), **Save Energy** (496 itens). Faltam ~69 fornecedores.

## Arquivos deste pacote
- `master_catalog.json` — itens da Opus
- `gaya_catalog.json` — itens da Gaya
- `save_catalog.json` — itens da Save Energy
- `build_html.py` — gera o `index.html` a partir dos 3 JSONs acima (embutindo o JSON combinado no HTML)
- `index.html` — o site publicado atualmente (referência do resultado esperado)

## Esquema de dados (campos usados por item)
Nem todo item usa todos os campos. Campos-chave:

- `nome`, `marca`, `secao` (categoria macro do catálogo do fornecedor)
- `codigo` (referência do fornecedor), `cor`, `potencia`, `voltagem`, `temp_cor`,
  `lumens`, `angulo`, `dimensoes`, `irc`, `ip`, `garantia`, `composicao`, `recursos`
- `subtipo` — descrição mais específica dentro da seção
- `sistema` — tag de compatibilidade com sistema/trilho (ex: "Sistema Trilho Mag",
  "Sistema LLS Flex"). Usado pra "spot para trilho X" funcionar na busca.
- `acessorio_de` — para acessórios, descreve pra qual produto/sistema serve
  (ex: "Acessório para Perfil Connect")
- `apelidos` — nomes populares/alternativos, separados por `; ` (ex: "Lâmpada Pera"
  pra lâmpadas ST64; "Downlight" pra linha Soul da Opus)
- `montagem` — "Embutir" / "Sobrepor" / "No Frame"
- `face` — "Recuada" / "Plana" (acabamento do spot, independente da montagem)
- `formato` — "Redondo" / "Quadrado" / "Retangular" / "Oval" / "Orgânico".
  **Só preencher quando o catálogo deixa isso claro** (nome do produto ou desenho
  técnico) — nunca "chutar" a partir da foto sem confirmação.
- `marcenaria` — literal "Ideal para Marcenaria" para produtos de uso em móveis
  (perfis mini, sensores, spots pequenos). Regra: linhas inteiras (ex: Gaya
  "Linha Mini Mag", "Linha Leya", "Linha Woody") ou itens específicos confirmados
  pelo usuário (Fita COB 3mm, Fita Mini Hai, Perfis RN/Duplos da Gaya).
- `fonte_luz` — SÓ para categorias ambíguas entre LED integrado e lâmpada trocável
  (Plafom, Pendente, Arandela). Regra automática: se o item tem campo `soquete`
  preenchido (E27/GU10/etc.) → "[Categoria] com Lâmpada"; senão → "[Categoria] de LED".
  **Spots NUNCA usam esse campo** — mesmo que usem soquete de lâmpada, um spot
  continua sendo "Spot", não "Plafom".

## Regras de nomenclatura (aprendidas com o usuário)
- Fornecedores usam nomes diferentes pro mesmo tipo de produto. Convenção adotada:
  - "Spot de Embutir" / "Spot de Sobrepor" — SEMPRE que o produto for um spot,
    mesmo que o fornecedor chame de "Plafom" (caso da Save Energy: Tower/Boxit
    eram "Plafom" no catálogo, mas são spots de sobrepor pra nós).
  - "Downlight" = apelido popular pra linha Soul (Opus) — mas é a *linha*, não o
    tipo de montagem; um Soul pode ser embutir ou sobrepor.
- **Sempre que um produto de um catálogo novo parecer visualmente igual/parecido
  a um já catalogado (Opus/Gaya/Save) mas com nome diferente do fornecedor,
  PARE e pergunte ao usuário qual nomenclatura seguir antes de cadastrar.**
  Não decidir isso sozinho.
- Perfis de LED sempre em **mm** (dimensões de seção). Todo o resto em **cm**
  (convenção pedida pelo usuário pra facilitar a busca).
- Sempre incluir o campo de composição/material do produto quando o catálogo
  informar.
- **NÃO incluir campo de EAN** (removido a pedido do usuário a partir da Save Energy).
- Potência, ângulo, temperatura de cor etc. devem ficar em formato exato e
  pesquisável (ex: "4,8W", "24°") — são usados em buscas tipo "MR16 4,8W".

## Extração de cada catálogo novo (processo já validado)
1. Ler o PDF, mapear a estrutura (índice, seções, offset de página impressa vs física).
2. Percorrer página a página, visualmente (renderizar com pymupdf + `view`),
   extraindo cada produto e suas variantes (cor/temperatura/tamanho).
3. Construir uma planilha `.xlsx` de checkpoint por seção grande, mostrar ao
   usuário antes de seguir pra próxima seção.
4. Ao final do catálogo, consolidar todas as planilhas num JSON com a mesma
   convenção de campos acima (`secao` = nome da seção do fornecedor,
   `marca` = nome do fornecedor).
5. Aplicar as tags (sistema, marcenaria, formato, fonte_luz, apelidos) onde
   fizer sentido, confirmando com o usuário os casos ambíguos.
6. Juntar com os JSONs dos fornecedores já feitos e rodar `build_html.py`
   pra gerar o `index.html` atualizado.

## Sobre fotos de produto (pendência aberta)
Ainda NÃO há fotos no dataset. Plano combinado com o usuário:
- Extrair **uma foto por família de produto** (não por variante de cor — a cor
  não muda a foto de referência) direto da página do PDF, como arquivo separado
  (não embutido em base64 no HTML — isso não cabe no limite de 16MB por muito tempo).
- Guardar as fotos numa pasta do repositório (ex: `images/<marca>/<slug-do-produto>.jpg`)
  e referenciar no JSON com um campo `imagem` (caminho relativo).
- Site real (GitHub Pages) não tem a limitação de 16MB nem a restrição de
  "sem imagem externa" que os Artifacts do Claude têm — por isso a migração
  pra hospedagem própria é necessária pra esse recurso funcionar bem em escala.
- Busca "por imagem" (upload de foto → achar parecido) é uma funcionalidade de
  IA separada (embeddings/similaridade visual) — não é busca de texto. Ainda não
  implementada; ideia é usar os campos estruturados (formato, tipo_luz, etc.)
  como substituto prático no curto prazo.
