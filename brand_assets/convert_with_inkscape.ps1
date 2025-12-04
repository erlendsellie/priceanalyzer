# PowerShell script to convert SVG to PNG using Inkscape
# Run this if you have Inkscape installed

$inkscapePath = "C:\Program Files\Inkscape\bin\inkscape.exe"
$svgFile = "icon_simple.svg"

# Check if Inkscape is installed
if (-not (Test-Path $inkscapePath)) {
    Write-Host "Inkscape not found at $inkscapePath" -ForegroundColor Red
    Write-Host "Please install Inkscape from https://inkscape.org/ or use online conversion" -ForegroundColor Yellow
    Write-Host "Press any key to exit..."
    $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
    exit
}

Write-Host "Converting SVG to PNG icons..." -ForegroundColor Green

# Convert to 256x256
Write-Host "Creating icon.png (256x256)..."
& $inkscapePath --export-type=png --export-filename="icon.png" --export-width=256 --export-height=256 $svgFile

# Convert to 512x512
Write-Host "Creating icon@2x.png (512x512)..."
& $inkscapePath --export-type=png --export-filename="icon@2x.png" --export-width=512 --export-height=512 $svgFile

Write-Host "`nDone! Created:" -ForegroundColor Green
Write-Host "  - icon.png (256x256)"
Write-Host "  - icon@2x.png (512x512)"
Write-Host "`nNext steps:" -ForegroundColor Cyan
Write-Host "  1. Review the generated PNG files"
Write-Host "  2. Follow BRANDS_SUBMISSION.md to submit to home-assistant/brands"
Write-Host "`nPress any key to exit..."
$null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
