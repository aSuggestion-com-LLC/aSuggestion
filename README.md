# aSuggestion Landing Page

Static project with multiple HTML pages.

## Requirements

- Node.js 18+
- npm

## asdf (recommended)

This project pins the runtime version via `.tool-versions`:

```bash
nodejs 24.12.0
```

If needed:

```bash
asdf plugin add nodejs
asdf install
asdf current
```

## Run Locally

```bash
npm install
npm run dev
```

Default local server: `http://localhost:5173`

## Structure

- `index.html`, `about.html`, `community.html`, `contact.html`, `payment.html`: pages
- `assets/css/base.css`: shared global styles
- `assets/css/index.css`: Home page styles
- `assets/css/about.css`: About page styles
- `assets/css/community.css`: Community page styles
- `assets/css/contact.css`: Contact page styles
- `assets/css/payment.css`: Payment page styles

## Local Images (Figma Migration)

Place files in `assets/images/` with the asset UUID in the filename (example: `a82a50da-00bb-491e-a426-5ceb06d215f2.png`) and run:

```bash
./scripts/sync-figma-assets.sh
```

The script:
- normalizes file names to `UUID.ext`
- replaces `figma.com/api/mcp/asset/UUID` URLs in HTML files with `assets/images/UUID.ext`
- lists remaining Figma links
