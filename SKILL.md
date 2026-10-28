---
name: hsh-report-theme
description: House theme distilled from a corporate business-plan deck ("BAO CAO KINH DOANH", 88 slides) — red + navy corporate report style with exact hex colors, Arial Bold caps typography, measured paddings, and component specs (slide header, two-tone title, KPI tiles, numbered cards, stat cards, red-header tables, BSC panels, bar/line charts, vision slide). Load whenever the user wants a business report, kế hoạch kinh doanh, báo cáo, slide deck, dashboard or one-pager "theme đỏ navy", "giống file báo cáo kinh doanh", or reuses this look in PPTX, HTML, charts (matplotlib/Chart.js) or Excel. Trigger (VI+EN): "hsh theme", "phong cách báo cáo kinh doanh", "slide đỏ xanh navy", "report theme", "làm slide giống file pdf báo cáo".
---

# HSH Report Theme

Source: `~/Downloads/ssss (1).pdf` (PowerPoint → "Microsoft Print to PDF", 88 slides, section 03 "Giải pháp & định hướng hoạt động", plan 2026–2027). Colors sampled from pixels; sizes measured on a 960×540 pt (13.33×7.5 in, 16:9) slide.

Ready-made files:
- `references/components.md`: **full inventory of ~60 components (frame, navigation, KPI, lists, image cards, tables, charts, timelines, special slides) with exact specs + the page numbers to look at.** Read it before building any slide.
- `assets/theme.css`: CSS tokens + components.
- `assets/pptx_theme.py`: python-pptx constants + builders.
- `assets/chart_theme.py`: matplotlib rc.

## 1. Character of the style
- Corporate, dense, information-first. White canvas, **red = brand/emphasis, navy = text/structure**.
- Everything in **UPPERCASE Arial Bold** for titles, labels, table headers. Body sentence-case Arial Regular.
- Big numbers are the hero: huge red (or blue) digits with a small navy unit next to them ("7.586 khách hàng").
- Numbered everything: `01 02 03…` badges in each card.
- Soft rounded cards (light tint fills, faint shadow), short red underline accents, one thick red band at the bottom of section/agenda slides.
- Photo-heavy slides: product/store photos in rounded tiles with a numbered caption strip.

## 2. Color tokens (exact hex)

### Core
| Token | Hex | Use |
|---|---|---|
| `--red` | `#FF0000` | brand word "BRAND NAME", title emphasis part, big KPI numbers, section number "03" |
| `--red-deep` | `#D00018` (alt `#CB001C`, `#CE0017`, `#D40B16`) | badges 01–05, table header fill, bottom band, icon circles |
| `--red-bar` | `#CB282D` | thin top rule on cover/summary slides |
| `--red-chart` | `#E62601` | solid bars in bar charts |
| `--navy` | `#002060` | all body titles, labels, numbers in footers, breadcrumb |
| `--navy-chart` | `#001D5C` | bar series in combo charts |
| `--blue` | `#0871D0` (Office `#0070C0`) | secondary KPI numbers, "VẬN HÀNH" panel, blue tiles |
| `--white` | `#FFFFFF` | canvas |

### Tints (card fills)
| Token | Hex | Use |
|---|---|---|
| `--tint-red` | `#FDEDEC` | KPI tile (red family) |
| `--tint-rose` | `#FBF1F0` | wide highlight band card |
| `--tint-red-icon` | `#FCD8DA` | circle behind line icons |
| `--tint-blue` | `#E7F1FB` | KPI tile (blue family) |
| `--tint-sky` | `#CCECFF` | table total row |
| `--card-gray` | `#F6F7F8` (alt `#F5F7F9`) | neutral cards (agenda, stat cards) |
| `--beige` | `#EEECE1` | side summary box next to charts |
| `--line` | `#BFC9D9` | table grid, dividers |

### 8-color category set (agenda "Giải pháp thực hiện" 01–08, always in this order)
| # | Topic | Hex |
|---|---|---|
| 01 | Giải pháp kinh doanh | `#D00018` red |
| 02 | Phát triển cửa hàng | `#0871D0` blue |
| 03 | Tối ưu hệ thống cung ứng | `#D85A00` orange |
| 04 | Phát triển đa dạng sản phẩm | `#008E52` green |
| 05 | Hoạt động marketing | `#87329D` purple |
| 06 | Đầu tư công nghệ | `#0098A5` teal |
| 07 | Phát triển nguồn nhân lực | `#D7A000` gold |
| 08 | Nâng cao hoạt động kiểm soát | `#334D64` slate |

### Channel set (slides "Giải pháp theo kênh bán hàng" 01–05)
Bán lẻ `#0076BD` · Đại lý `#E67400` · Xây dựng trọn gói `#C48A00` · Dự án `#009A51` · Thương mại điện tử `#D00913`.

### Secondary families (column / panel sets)
| Family | Solid (header, number, bullet) | Tint (body) |
|---|---|---|
| Blue | `#006FC9` / `#086ABD` / `#0070C0` | `#EAF5FF` / `#EAF4FD` / `#EEF6FD` |
| Teal | `#008C90` / `#00969B` / `#00997E` | `#E8F6F4` / `#E7F6F4` / `#EDF9F5` |
| Orange-gold | `#DF9000` / `#E87118` / `#E17E18` | `#FFF5E2` / `#FFF5EB` / `#FFF5E7` |
| Red | `#DC001B` / `#DE1D22` | `#FDF0F2` / `#FDF2F3` |
| Green (level) | `#018671` | `#EAF7F4` |
Other: navy banner `#092F54` (sub-rows `#25466B`), growth pill `#FDE5E8`, row band gray `#F6F3F3`, footer band `#EDF1F7`, timeline orange `#FD561F`, timeline dot `#B80000`, logo bar `#B01019` + wordmark yellow `#FFE600`, comparison headers red `#F32B2D→#CF0B0C` / blue `#5990D5→#417CD4` with `#FFFF00` text, check marks `#C00000`, deep blue subhead `#0441EE`.

### BSC panel headers (Office standard colors)
Tài chính `#FF0000` · Vận hành `#0070C0` · Khách hàng `#E46C0A` · Phát triển `#00B050`.

Rule: one slide = red + navy + at most one secondary hue. The 8-color set appears only where the 8 solution pillars are listed.

## 3. Typography
Font: **Arial** (fallback Helvetica, "Segoe UI", sans-serif). Vietnamese diacritics must render — Arial is safe; for web use `Arial, "Helvetica Neue", sans-serif` (Be Vietnam Pro is an acceptable Google-font substitute).

| Role | Size (pt on 960×540) | Weight | Case | Color |
|---|---|---|---|---|
| Section number "03" | 28 | Bold | – | `--red` |
| Breadcrumb line 1 (section) | 9 | Bold | UPPER | `--navy` |
| Breadcrumb line 2 (sub-topic) | 8 | Regular | UPPER | `--navy` |
| Brand tag top-right "BRAND NAME" | 12 | Bold | UPPER | `--red` |
| Slide title | 26 (24–28) | Bold | UPPER | two-tone: first phrase `--red`, rest `--navy` (or reversed) |
| Centered title (agenda/section) | 30 | Bold | UPPER | `--red` |
| Hero number | 64–72 | Bold | – | `--red`, unit 14 Regular `--navy` |
| Tile number | 54 | Bold | – | `--red` / `--blue` |
| Stat-card number | 28 | Bold | – | `--red` |
| Card number badge text "01" | 14 | Bold | – | white on `--red-deep` |
| Agenda number "01" | 28 | Bold | – | pillar color |
| Card label | 12 | Bold | UPPER | `--navy`, key words `--red` |
| Body / bullets | 10–11 | Regular | Sentence | `--navy` or `#1F2937` |
| Table header | 10 | Bold | UPPER | white |
| Table body | 9–10 | Regular (row 1 Bold) | – | `--navy`; STT column `--red-deep` |
| Footnote / unit ("Đvt: Cửa hàng") | 9 | Regular / Italic | – | `--navy` |

Line-height: titles 1.1, labels 1.25, body 1.35.

## 4. Grid, spacing, padding (pt on 960×540)
- **Slide margins**: left/right **20–24**, content top starts at **y ≈ 115** (below title), bottom free zone **≥ 20** (or the 12.7-pt red band flush to the bottom).
- **Header strip** (every content slide), baseline at y ≈ 27–50:
  - "03" at x 36, y 27, then a 1-pt vertical gray divider (`#D9D9D9`) at x ≈ 85, then the 2-line breadcrumb at x 102.
  - Brand tag right-aligned, right margin ≈ 60.
- **Title** at x 20–24, y ≈ 94; **red underline accent** 53×1.6 pt (2 px) under the first word, 10 pt below the cap line.
- **Gaps**: between cards **12** (agenda, 4-col), **16** (KPI tiles, 3-col); between rows **13–16**.
- **Card inner padding**: **15** horizontal, **18–20** top, **14** bottom.
- **Card radius**: **12** (big tiles 14–16); shadow `0 2pt 6pt rgba(0,0,0,.12)`; no border (or 1 pt `#EEF0F3`).
- **Badge** (01–05): 52×42 rounded rect r=6, `--red-deep`, sits 8 pt inside card's left edge.
- **Agenda card**: 224×163, icon circle Ø73 at (16,26) inside card, 1-pt vertical divider after circle, number + label to the right, 62×2.4 accent bar centered at bottom (14 pt from edge) in pillar color.
- **Stat card**: 275×87, 3.2-pt `--red` bar on the left edge, number at (22,17).
- **Table**: header row **28.6** high, body rows **20–21** high, cell padding 6 horizontal; full content width minus margins (≈ 898).
- **Charts**: occupy 60–65 % slide width, value labels on bars, no gridlines (or very light `#E5E7EB`).

## 5. Components (recipes)
1. **Slide header** — `03 | BREADCRUMB L1 / l2` left, `BRAND NAME` right. Present on every content slide.
2. **Two-tone title** — `<red>TỔNG QUAN VỀ</red> <navy>NHÓM KHÁCH HÀNG ĐẠI LÝ</navy>` + short red underline.
3. **Hero band** — full-width `--tint-rose` card: badge 01 + navy caps label left; divider; icon in `--tint-red-icon` circle + giant red number + unit right.
4. **Numbered feature cards** — white/very-light cards, badge 0N top-left, line icon in pink circle, 2–3 line caps label mixing navy and red, short red underline under the label.
5. **KPI tiles (3×2)** — alternating `--tint-red` / `--tint-blue` tiles: caps label (color = family), big number, hairline divider, footer row "Lũy kế …… **93** sản phẩm" (number 28 pt navy bold).
6. **Stat cards row** — 3 gray cards with red left bar: big red number, caps navy label right, small caption below.
7. **Data table** — header fill `--red-deep` white caps; STT column red bold; first data row bold; zebra none, grid `--line` 0.75 pt; totals row `--tint-sky` bold.
8. **BSC 2×2** — panels with solid colored header strip (title left, weight % right, white bold), rows "01  text  30%" with % in `--red-deep` bold, rounded bottom corners + shadow.
9. **Agenda 4×2** — see §4, colors from the 8-color set, red bottom band.
10. **Photo grid** — 4–5 rounded photos (r=8) with number above ("01" navy bold) and caps caption below.
11. **Timeline** — circles numbered 01–05 in `--red` outline, alternating above/below a red line, month labels navy.
12. **Vision / closing slide** — full-bleed photo, center emblem red, callouts with navy caps headings and red key numbers ("1.500 ĐẠI LÝ TIÊU CHUẨN"); thank-you slide "TRÂN TRỌNG CẢM ƠN" navy over a lotus photo.

## 6. Charts
- Combo bar+line: bars `--navy-chart` (`#001D5C`), line `#C00000` 2.5 pt with round markers `#4F81BD`; data table under the chart is allowed (Excel style).
- Stacked growth bars: base `--red-chart` solid, increment = same red with diagonal hatch (`////`), totals bold navy above bars; highlight one value with a red ellipse outline.
- Pie: red slice vs `#2E75B6` blue, labels outside.
- Axis text 10–12 pt navy, no chart border, legend top with square markers.

## 7. Do / Don't
- Do keep every title UPPERCASE and two-tone; keep "BRAND NAME" red wherever it appears in text.
- Do use Vietnamese number format in content: `7.586`, `19,1%`, `40 tỷ đồng`.
- Don't introduce gradients, dark backgrounds or more than 3 hues per slide (except agenda).
- Don't use thin/light font weights — the deck is all Regular/Bold Arial.

## 8. How to apply
- **PPTX**: `python3 ~/.claude/skills/hsh-report-theme/assets/pptx_theme.py demo out.pptx` builds a sample deck; import its helpers (`header`, `title`, `kpi_tile`, `stat_card`, `table`) in new decks. Pair with the `pptx` skill for general deck mechanics.
- **HTML / artifact**: link or inline `assets/theme.css`; class names `.hsh-header`, `.hsh-title`, `.hsh-tile`, `.hsh-stat`, `.hsh-table`, `.hsh-bsc`, `.hsh-agenda`.
- **Charts**: `from chart_theme import apply; apply()` then plot with `HSH['navy_chart']`, `HSH['red_chart']`.
