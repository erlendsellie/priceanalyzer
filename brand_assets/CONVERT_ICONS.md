# Icon Conversion Instructions

I've created two SVG icon designs for PriceAnalyzer:
- `icon_design.svg` - More detailed version
- `icon_simple.svg` - Simplified version (recommended for better visibility at small sizes)

## Option 1: Online Conversion (Easiest)

### Use CloudConvert (Recommended)
1. Go to https://cloudconvert.com/svg-to-png
2. Upload `icon_simple.svg`
3. Click "⚙️" (settings icon) and set:
   - **Width**: 256 pixels
   - **Height**: 256 pixels
   - Keep aspect ratio: Yes
4. Click "Convert"
5. Download and rename to `icon.png`
6. Repeat steps 2-5 but use **512x512** pixels and rename to `icon@2x.png`

### Alternative: RedKetchup
1. Go to https://redketchup.io/image-resizer
2. Upload the SVG file
3. Set dimensions to 256x256
4. Download as PNG
5. Repeat for 512x512

## Option 2: Using Inkscape (Free Desktop Tool)

### Install Inkscape
- Download from: https://inkscape.org/release/

### Convert to PNG
1. Open `icon_simple.svg` in Inkscape
2. Go to **File** → **Export PNG Image**
3. Set **Export area**: Page
4. Set **Image size**: Width = 256, Height = 256
5. Set **Filename**: icon.png
6. Click **Export**
7. Repeat with Width/Height = 512 for icon@2x.png

## Option 3: Using Command Line (ImageMagick)

If you have ImageMagick installed:

```bash
# Install ImageMagick (Windows with Chocolatey)
choco install imagemagick

# Convert to required sizes
magick icon_simple.svg -resize 256x256 icon.png
magick icon_simple.svg -resize 512x512 icon@2x.png
```

## Option 4: Using Node.js (sharp)

If you have Node.js installed:

```bash
npm install sharp
```

Then create and run `convert_icons.js`:

```javascript
const sharp = require('sharp');
const fs = require('fs');

const svgBuffer = fs.readFileSync('icon_simple.svg');

// Convert to 256x256
sharp(svgBuffer)
  .resize(256, 256)
  .png()
  .toFile('icon.png')
  .then(() => console.log('icon.png created'));

// Convert to 512x512
sharp(svgBuffer)
  .resize(512, 512)
  .png()
  .toFile('icon@2x.png')
  .then(() => console.log('icon@2x.png created'));
```

## Verify Your Icons

After conversion, check:
- ✅ icon.png is exactly 256x256 pixels
- ✅ icon@2x.png is exactly 512x512 pixels
- ✅ Both are PNG format
- ✅ Both have transparency (if possible)
- ✅ File sizes are reasonable (under 50KB each)

## Next Steps

Once you have the PNG files:
1. Place them in a temporary folder
2. Follow the brands submission instructions in `BRANDS_SUBMISSION.md`
