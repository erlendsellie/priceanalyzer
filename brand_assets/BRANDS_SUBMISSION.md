# Submit PriceAnalyzer to Home Assistant Brands

## Step-by-Step Guide

### Prerequisites
- [x] You have `icon.png` (256x256) and `icon@2x.png` (512x512) ready
- [ ] You have a GitHub account
- [ ] You are logged into GitHub

---

## Step 1: Fork the Brands Repository

1. **Go to**: https://github.com/home-assistant/brands
2. **Click**: "Fork" button in the top-right corner
3. **Wait**: For GitHub to create your fork (takes a few seconds)
4. **Result**: You now have `https://github.com/YOUR_USERNAME/brands`

---

## Step 2: Create the Integration Folder

### Option A: Using GitHub Web Interface (Easiest)

1. **Navigate to your fork**: `https://github.com/YOUR_USERNAME/brands`

2. **Navigate to**: `custom_integrations` folder (click on it)

3. **Click**: "Add file" → "Create new file"

4. **In the filename box, type**: `priceanalyzer/README.md`
   - This will create the `priceanalyzer` folder automatically

5. **In the file content, type**:
   ```
   PriceAnalyzer brand assets
   ```

6. **Scroll down** and click "Commit new file" (keep default branch)

---

## Step 3: Upload Icon Files

1. **Navigate to**: `custom_integrations/priceanalyzer` folder in your fork

2. **Click**: "Add file" → "Upload files"

3. **Drag and drop** or select:
   - `icon.png` (from your local machine)
   - `icon@2x.png` (from your local machine)

4. **Commit changes**:
   - Commit message: "Add PriceAnalyzer icons"
   - Click "Commit changes"

5. **Verify**: You should now see:
   ```
   custom_integrations/priceanalyzer/
     ├── icon.png
     ├── icon@2x.png
     └── README.md
   ```

---

## Step 4: Delete README.md (Optional Cleanup)

The README.md was just temporary to create the folder:

1. **Click on** `README.md` in your fork
2. **Click** trash icon (🗑️) to delete it
3. **Commit** the deletion

Your final structure should be:
```
custom_integrations/priceanalyzer/
  ├── icon.png
  └── icon@2x.png
```

---

## Step 5: Create Pull Request

1. **Go to**: https://github.com/home-assistant/brands

2. **You should see** a yellow banner saying "YOUR_USERNAME:main had recent pushes"
   - Click **"Compare & pull request"**
   
   **OR** manually:
   - Click "Pull requests" tab
   - Click "New pull request"
   - Click "compare across forks"
   - Set: `base repository: home-assistant/brands` ← `head repository: YOUR_USERNAME/brands`

3. **Fill out the PR template**:

---

### PR Title
```
Add priceanalyzer custom integration
```

### PR Description Template

Copy and paste this:

```markdown
## Description
Add brand images for PriceAnalyzer custom integration

## Integration Details
- **Domain**: priceanalyzer
- **Type**: Custom Integration
- **Repository**: https://github.com/erlendsellie/priceanalyzer
- **Description**: Smart energy management for Home Assistant based on Nordpool electricity prices

## What's Included
- Icon 256x256 (icon.png)
- Icon 512x512 (icon@2x.png)

## Design Rationale
The icon represents:
- **Chart bars**: Price analysis and comparison
- **Lightning bolt**: Electricity/energy
- **Color scheme**: Blue (technology), Green/Yellow/Red (price levels)

## Checklist
- [x] Images are PNG format
- [x] Icon is 256x256 pixels
- [x] Icon@2x is 512x512 pixels
- [x] Images are optimized and compressed
- [x] Images have appropriate transparency
- [x] Images are trimmed with minimal whitespace
- [x] No Home Assistant branding used
- [x] Domain name matches manifest.json domain
- [x] I am the owner/maintainer of the integration

## Additional Information
This integration is available as a custom repository in HACS and will be submitted to the default HACS store after this PR is merged.
```

---

4. **Click**: "Create pull request"

---

## Step 6: Wait for Review

### What Happens Next

1. **Automated checks run**:
   - Validates PNG format
   - Checks image dimensions
   - Verifies file structure
   - These should all pass ✅

2. **Community review**:
   - Maintainers review your submission
   - Usually takes 1-7 days
   - They may request changes or approve immediately

3. **If changes requested**:
   - Make updates in your fork
   - Changes automatically appear in the PR

4. **When merged**:
   - Your icons are now in the brands repository! 🎉
   - Wait ~1 hour for CDN cache to update
   - You can now proceed with HACS submission

---

## Troubleshooting

### PR Check Failed: "Image dimensions incorrect"
- Verify icon.png is exactly 256x256
- Verify icon@2x.png is exactly 512x512
- Use an image viewer or `file properties` to check

### PR Check Failed: "Not PNG format"
- Make sure files have `.png` extension
- Re-export from your SVG using PNG format

### Can't See Upload Button
- Make sure you're in YOUR fork, not the original repository
- URL should be `github.com/YOUR_USERNAME/brands`

### Changes Not Showing in PR
- Make sure you committed the changes in your fork
- Refresh the PR page
- May take a few seconds to update

---

## After PR is Merged

Once your PR to brands is merged:

1. ✅ **Wait 1 hour** for CDN cache
2. ✅ **Create GitHub release** for your integration (v2.4.6)
3. ✅ **Verify repository settings** (description, topics, issues enabled)
4. ✅ **Submit to HACS** default store

See `HACS_SUBMISSION_CHECKLIST.md` for the next steps!

---

## Need Help?

- **Brands Issues**: https://github.com/home-assistant/brands/issues
- **General Questions**: https://community.home-assistant.io/
- **This looks wrong?**: Double-check against https://github.com/home-assistant/brands/blob/master/README.md
