# aSuggestion Landing Page

Projeto estático com múltiplas páginas HTML.

## Requisitos

- Node.js 18+
- npm

## asdf (recomendado)

Este projeto fixa a versão via `.tool-versions`:

```bash
nodejs 24.12.0
```

Se necessário:

```bash
asdf plugin add nodejs
asdf install
asdf current
```

## Executar localmente

```bash
npm install
npm run dev
```

Servidor local padrão: `http://localhost:5173`

## Estrutura

- `index.html`, `about.html`, `community.html`, `contact.html`, `payment.html`: páginas
- `assets/css/base.css`: estilos globais compartilhados
- `assets/css/index.css`: estilos da Home
- `assets/css/about.css`: estilos da About
- `assets/css/community.css`: estilos da Community
- `assets/css/contact.css`: estilos da Contact
- `assets/css/payment.css`: estilos da Payment

## Imagens locais (migração do Figma)

Coloque os arquivos em `assets/images/` com o UUID do asset no nome (ex.: `a82a50da-00bb-491e-a426-5ceb06d215f2.png`) e rode:

```bash
./scripts/sync-figma-assets.sh
```

O script:
- normaliza nomes de arquivos para `UUID.ext`
- substitui URLs `figma.com/api/mcp/asset/UUID` nos HTMLs por `assets/images/UUID.ext`
- lista quais links do Figma ainda restaram
