# Catálogo Interno — Lobex Luz

Catálogo pesquisável da Lobex Luz que reúne, numa base única e padronizada, os produtos dos catálogos PDF dos fornecedores. Busca por marca, código, nome, tipologia, potência, medida e pelos nomes usados na loja.

## Conteúdo do repositório

| Arquivo | O que é |
|---|---|
| `index.html` | O site de busca completo (abre direto no navegador, funciona offline) |
| `dados/catalogo.json` | Base de dados completa (mesmos dados embutidos no site) |
| `dados/catalogo.csv` | A mesma base em planilha (abre no Excel, separador `;`) |

## Fornecedores integrados (5.044 itens)

| Marca | Itens |
|---|---|
| Gaya | 1.422 |
| Opus (piloto) | 1.094 |
| Pix Iluminação | 700 |
| JR Perfis | 684 |
| Brilia | 648 |
| Save Energy | 496 |

**Em andamento:** Romalux (catálogo 2026 + "by Waldir Júnior"). Ainda não está no site.
**Pendentes:** cerca de 60+ fornecedores restantes.

## Ficha padrão da peça

Marca/fornecedor, código, nome, tipologia, tamanho, cor(es) de fábrica, cor(es) personalizável(is), imagem e observações técnicas (potência, voltagem, temperatura de cor, lúmens, ângulo, IRC, IP, garantia, composição).

## Convenções de nomenclatura

- **Unidades:** Perfis de LED em **mm**; todos os demais produtos em **cm**.
- **Downlight:** Linha Soul (Opus), Linha Focco (Gaya) e Linha Vigo (Pix) levam "Downlight" no nome.
- **Spot:** usado só em embutidos e direcionais, nunca junto de "Downlight". "Embutido" vira "Spot de Embutir".
- **Painéis:** "Painel de LED Embutir/Sobrepor [formato]".
- **Linha Battery** (Pix e Brilia): "Luminária de Mesa [nome]".
- **Projetor** passa a ser "Refletor de LED" em todas as marcas.
- **Save Energy Tower/Boxit:** tratados como Spot de Sobrepor (não plafon).
- **Fonte = Driver:** buscar qualquer um dos termos retorna os dois.
- **Marcenaria:** busca "marcenaria" traz as linhas destinadas a esse uso (ex.: Gaya Mini Mag, Leya, Woody, Sensi; sensores da Pix).
- **Potência** buscável de forma exata (ex.: "MR16 4,8W").
- **JR Perfis:** buscáveis pela medida exata (ex.: "24x14") no campo "Medida (mm)".

## Próximas etapas

1. Concluir Romalux e seguir com os demais fornecedores.
2. Fotos por família de produto.
3. Busca por imagem semelhante.
