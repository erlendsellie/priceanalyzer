# PriceAnalyzer Brand Assets

This folder contains everything you need to create and submit brand icons for the Home Assistant Brands repository.

## 📁 Files in This Folder

### Icon Designs
- **`icon_simple.svg`** - Simplified icon design (recommended)
- **`icon_design.svg`** - Detailed icon design (alternative)

### Conversion Tools
- **`convert_in_browser.html`** - 🌟 **EASIEST METHOD** - Open in browser, drag SVG, download PNGs
- **`convert_with_inkscape.ps1`** - PowerShell script for Inkscape users
- **`CONVERT_ICONS.md`** - Multiple conversion methods explained

### Submission Guide
- **`BRANDS_SUBMISSION.md`** - 📘 Complete step-by-step guide to submit to home-assistant/brands

---

## 🚀 Quick Start (3 Steps)

### Step 1: Convert SVG to PNG (Choose ONE method)

#### Method A: Browser Converter (Easiest) ⭐
1. **Open**: `convert_in_browser.html` in your web browser
2. **Drag and drop**: `icon_simple.svg` onto the page
3. **Download**: Both `icon.png` and `icon@2x.png`
4. **Done!** ✅

#### Method B: Online Tool
1. Go to https://cloudconvert.com/svg-to-png
2. Upload `icon_simple.svg`
3. Convert to 256x256 → download as `icon.png`
4. Convert to 512x512 → download as `icon@2x.png`

#### Method C: Use Inkscape (if installed)
1. Double-click `convert_with_inkscape.ps1`
2. Wait for conversion
3. Get `icon.png` and `icon@2x.png`

### Step 2: Verify Icon Files
Check that you have:
- ✅ `icon.png` - exactly 256 × 256 pixels
- ✅ `icon@2x.png` - exactly 512 × 512 pixels
- ✅ Both are PNG format

### Step 3: Submit to Brands
Follow the detailed guide in **`BRANDS_SUBMISSION.md`**

---

## 🎨 About the Icon Design

The PriceAnalyzer icon represents:
- **Chart bars** (green/yellow/red) - Price levels and analysis
- **Lightning bolt** (gold) - Electricity and energy
- **Blue background** - Technology and reliability
- **Trend line** - Price tracking over time

The simplified version (`icon_simple.svg`) is optimized for small sizes and quick recognition.

---

## 📋 Next Steps After Icon Creation

1. ✅ Convert SVG to PNG (this folder)
2. ⏳ Submit to home-assistant/brands (use `BRANDS_SUBMISSION.md`)
3. ⏳ Wait for PR merge (1-7 days)
4. ⏳ Create GitHub release for your integration
5. ⏳ Submit to HACS default store

See `../HACS_SUBMISSION_CHECKLIST.md` for the complete roadmap.

---

## 💡 Customizing the Icon

Want to modify the design?

1. **Edit the SVG** in any vector editor:
   - Inkscape (free)
   - Adobe Illustrator
   - Figma
   - VS Code with SVG extension

2. **Keep these requirements**:
   - Square aspect ratio (1:1)
   - Simple design (recognizable at small sizes)
   - 2-3 colors maximum
   - Transparent background preferred
   - Represents electricity/pricing

3. **Re-convert** to PNG using any method above

---

## ❓ Need Help?

- **Conversion issues?** → Check `CONVERT_ICONS.md` for alternative methods
- **Submission questions?** → See `BRANDS_SUBMISSION.md`
- **Icon design feedback?** → Ask in Home Assistant community forums
- **Technical errors?** → Open an issue on your GitHub repo

---

## 🎯 Goal

Get PriceAnalyzer into the default HACS store! This is the first step. 🚀
