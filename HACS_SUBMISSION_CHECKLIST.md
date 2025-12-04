# HACS Default Store Submission Checklist

## Current Status: Almost Ready! 🎉

Your repository is well-prepared. Here's what remains to be done:

---

## ✅ Already Complete

- [x] Repository structure is correct
- [x] `manifest.json` has all required fields (domain, name, version, documentation, issue_tracker, codeowners)
- [x] GitHub Actions workflows set up (HACS Action + Hassfest)
- [x] `hacs.json` exists with required name field
- [x] Workflows updated to remove `ignore: brands`

---

## 🔲 To-Do Items

### 1. GitHub Repository Settings

Verify these settings on GitHub (https://github.com/erlendsellie/priceanalyzer/settings):

#### Repository Description ✅ (verify)
- Go to your repository main page
- Click the ⚙️ (gear icon) next to "About"
- Ensure there's a short, descriptive description like:
  > "Smart energy management for Home Assistant based on Nordpool electricity prices"

#### Topics/Tags ✅ (verify)
- In the same "About" section, add topics such as:
  - `home-assistant`
  - `hacs`
  - `nordpool`
  - `electricity-prices`
  - `energy-management`
  - `custom-component`
  - `home-automation`

#### Issues Enabled ✅ (verify)
- Go to Settings → General → Features
- Ensure "Issues" checkbox is **checked**
- Your repository already has an issue tracker URL in manifest.json, so this should be enabled

---

### 2. Create Brand Images for Home Assistant Brands

**Status**: See `BRANDS_PREPARATION.md` for detailed instructions

**Required files** (to create):
- `icon.png` (256x256)
- `icon@2x.png` (512x512)
- Optional: `logo.png` and `logo@2x.png`

**Action Steps**:
1. Create the icon images following the specifications in BRANDS_PREPARATION.md
2. Fork https://github.com/home-assistant/brands
3. Create folder: `custom_integrations/priceanalyzer/`
4. Upload your icon images
5. Submit Pull Request

**Important**: Wait for this PR to be **merged** before proceeding to HACS submission!

---

### 3. Create a GitHub Release

**Why**: HACS requires at least one release to be published

**Steps**:
1. Go to https://github.com/erlendsellie/priceanalyzer/releases
2. Click "Create a new release"
3. Fill in the details:
   - **Tag**: Use semantic versioning matching your manifest.json version (e.g., `v2.4.6`)
   - **Release title**: `v2.4.6` or `Version 2.4.6`
   - **Description**: Add release notes describing features and changes

**Example Release Notes**:
```markdown
## PriceAnalyzer v2.4.6

### Features
- Smart energy management based on Nordpool electricity prices
- Climate control sensor with temperature correction recommendations
- Hot water heater sensor with price-based temperature optimization
- Price sensor with configurable additional costs
- Support for hourly and 15-minute (quarterly) price intervals
- Multiple sensor setups per region support

### Configuration
- UI-based configuration flow
- Customizable hot water temperatures for different price scenarios
- Jinja2 template support for additional costs
- Region support: NO1-NO5, SE1-SE4, DK1-DK2, FI, EE, LT, LV, etc.

### Installation
- Compatible with Home Assistant via HACS
- Supports multiple instances per region

For documentation and usage examples, see the [README](https://github.com/erlendsellie/priceanalyzer/blob/master/README.md)
```

4. Click "Publish release"

---

### 4. Submit to HACS Default Repository

**When**: Only after brands PR is merged and you have a GitHub release

**Steps**:

1. **Fork the repository**:
   - Go to https://github.com/hacs/default
   - Click "Fork"

2. **Create a new branch** (not from master):
   ```bash
   git checkout -b add-priceanalyzer
   ```

3. **Edit the integration file**:
   - Open `/integration` file in your fork
   - Add your repository in **alphabetical order**:
   ```
   erlendsellie/priceanalyzer
   ```
   - The list should be sorted alphabetically

4. **Commit your change**:
   ```bash
   git add integration
   git commit -m "Add erlendsellie/priceanalyzer"
   git push origin add-priceanalyzer
   ```

5. **Create Pull Request**:
   - Go to https://github.com/hacs/default/pulls
   - Click "New pull request"
   - Select your fork and branch
   - Fill out the PR template completely

**Example PR Template Response**:

```markdown
## Repository owner
- [x] I'm the owner of this repository

## Repository
https://github.com/erlendsellie/priceanalyzer

## Category
integration

## Description
PriceAnalyzer is a smart energy management integration for Home Assistant that optimizes energy consumption based on Nordpool electricity prices. It provides intelligent sensors for climate control, hot water heating, and price monitoring with customizable additional costs.

## Documentation
https://github.com/erlendsellie/priceanalyzer

## Visibility
This integration is useful for anyone in Nordpool regions (Norway, Sweden, Denmark, Finland, Baltics) who wants to optimize their energy consumption and reduce electricity costs through automated climate and hot water heater control.

## homeassistant/brands
- [x] I have added my integration to home-assistant/brands (PR merged)

## Checklist
- [x] The PR is made from a new branch from master and not from my master branch
- [x] I'm the owner or major contributor of the repository
- [x] The repository is public and on GitHub
- [x] I have added my integration to home-assistant/brands
- [x] I have added my repository in alphabetical order
- [x] I have verified HACS Action passes
- [x] I have verified Hassfest passes
- [x] I have at least one release published
- [x] The repository has a description
- [x] The repository has topics
- [x] The repository has issues enabled
```

---

## Automated Checks That Will Run

When you submit your PR to hacs/default, these automated checks will run:

1. **Check brands** - Verifies your integration is in home-assistant/brands ✅
2. **Check manifest** - Validates manifest.json ✅
3. **Check hacs-validation** - Runs HACS validation ✅
4. **Check HACS manifest** - Validates hacs.json ✅
5. **Check archived** - Ensures repo is not archived ✅
6. **Check releases** - Verifies at least one release exists
7. **Check owner** - Confirms submitter is owner/contributor ✅
8. **Check repository** - Checks description, topics, issues ✅
9. **lint jq** - Validates JSON ✅
10. **lint sorted** - Ensures alphabetical order ✅

---

## Timeline Estimate

1. **Create brand images**: 1-2 hours (design + optimization)
2. **Submit to brands**: Immediate (PR submission)
3. **Brands PR review**: 1-7 days (community review)
4. **Create GitHub release**: 5 minutes
5. **Submit to HACS**: Immediate (after brands merge)
6. **HACS PR review**: 1-3 days (automated checks + review)

**Total**: Approximately 1-2 weeks from start to being in default HACS store

---

## Support and Resources

- **HACS Documentation**: https://hacs.xyz/docs/publish/
- **Brands Repository**: https://github.com/home-assistant/brands
- **HACS Default Repo**: https://github.com/hacs/default
- **HACS Discord**: https://discord.gg/apgchf8

---

## Quick Command Reference

```bash
# Check your current version
cat custom_components/priceanalyzer/manifest.json | grep version

# Create and push a tag for release
git tag v2.4.6
git push origin v2.4.6

# Fork and clone hacs/default
git clone https://github.com/YOUR_USERNAME/default.git
cd default
git checkout -b add-priceanalyzer

# Edit integration file (add erlendsellie/priceanalyzer in alphabetical order)
# Then commit and push
git add integration
git commit -m "Add erlendsellie/priceanalyzer"
git push origin add-priceanalyzer
```

---

## Notes

- Your `manifest.json` already has version `2.4.6` - use this for your first release
- The integration domain `priceanalyzer` must match exactly in brands and manifest
- Do NOT submit to hacs/default until brands PR is merged
- Be patient - review processes can take a few days
- HACS maintainers are volunteers, be respectful and follow guidelines carefully
