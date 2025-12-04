# Home Assistant Brands Preparation Guide

## Required Images for PriceAnalyzer

To get into the default HACS store, you must add your integration to the [home-assistant/brands](https://github.com/home-assistant/brands) repository.

### Image Requirements

You need to create **icon** and **logo** images in PNG format:

#### Icon Images (Required)
- **Aspect ratio**: 1:1 (square)
- **Sizes needed**:
  - `icon.png` - 256x256 pixels
  - `icon@2x.png` - 512x512 pixels (hDPI version)
- **Design**: Should be a simple, recognizable symbol representing PriceAnalyzer

#### Logo Images (Optional but Recommended)
- **Aspect ratio**: Landscape preferred, but should respect your brand
- **Sizes needed**:
  - `logo.png` - Shortest side: 128-256 pixels
  - `logo@2x.png` - Shortest side: 256-512 pixels (hDPI version)
- **Design**: Can include text "PriceAnalyzer" with icon

### General Requirements for All Images
- ✅ PNG format
- ✅ Properly compressed and optimized (lossless preferred)
- ✅ Interlaced/progressive preferred
- ✅ Transparency preferred
- ✅ Optimized for white background
- ✅ Trimmed with minimum empty space
- ❌ Cannot use Home Assistant branded images

### Design Suggestions for PriceAnalyzer

Consider these design concepts:
1. **Price tag icon** with a chart/graph element
2. **Lightning bolt** combined with a currency symbol (representing energy pricing)
3. **Graph/chart bars** in a circular or square frame
4. **Thermometer with price tag** (representing temperature control)
5. **Coins/money** with energy symbols

The icon should be:
- Simple and recognizable at small sizes
- Use 2-3 colors maximum
- Related to electricity pricing/energy optimization

### Tools to Create Images

- **Design tools**:
  - [Canva](https://www.canva.com/) - Easy online design tool
  - [Figma](https://www.figma.com/) - Professional design tool
  - [GIMP](https://www.gimp.org/) - Free image editor
  - [Inkscape](https://inkscape.org/) - Free vector graphics editor

- **Image optimization**:
  - [TinyPNG](https://tinypng.com/) - PNG compression
  - [RedKetchup Image Resizer](https://redketchup.io/image-resizer) - Resize to exact dimensions
  - [Squoosh](https://squoosh.app/) - Image optimization

- **Icon resources** (for inspiration):
  - [Font Awesome](https://fontawesome.com/icons)
  - [Material Design Icons](https://materialdesignicons.com/)
  - [Heroicons](https://heroicons.com/)

## File Structure to Create

Once you have the images, you'll need to submit them to home-assistant/brands in this structure:

```
custom_integrations/
  priceanalyzer/
    icon.png          # 256x256
    icon@2x.png       # 512x512
    logo.png          # 128-256px shortest side (optional)
    logo@2x.png       # 256-512px shortest side (optional)
```

## Next Steps

1. **Create the images** following the specifications above
2. **Save them locally** in a temporary folder
3. **Fork the [home-assistant/brands](https://github.com/home-assistant/brands) repository**
4. **Create the folder structure**:
   - Navigate to `custom_integrations/`
   - Create new folder `priceanalyzer/`
   - Upload your images
5. **Submit a Pull Request** with your images

## Example PR Description

When submitting to home-assistant/brands, use this PR description:

```
## Description
Add brand images for PriceAnalyzer custom integration

## Integration Details
- **Domain**: priceanalyzer
- **Repository**: https://github.com/erlendsellie/priceanalyzer
- **Description**: Smart energy management for Home Assistant based on Nordpool electricity prices

## Checklist
- [x] Images are PNG format
- [x] Icon is 256x256 and 512x512
- [x] Logo is within size requirements (if included)
- [x] Images are optimized and compressed
- [x] Images have transparency
- [x] Images are trimmed with minimal whitespace
- [x] No Home Assistant branding used
```

## Important Notes

- The domain name in the brands repository (`priceanalyzer`) must **exactly match** the domain in your `manifest.json`
- Once your PR to brands is merged, you can proceed with submitting to hacs/default
- The HACS validation workflow will fail until your images are in the brands repository
