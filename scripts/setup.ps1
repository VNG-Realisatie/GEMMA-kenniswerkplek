# Richt de werkplek in op Windows: installeert 'uv' indien nodig, installeert de
# Python-omgeving en controleert het resultaat. Voor niet-technische redacteuren:
# open PowerShell in deze map en typ: .\scripts\setup.ps1
$ErrorActionPreference = "Stop"
Set-Location (Join-Path $PSScriptRoot "..")

Write-Host "== Werkplek inrichten voor second-brain =="
Write-Host ""

if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
    Write-Host "'uv' (de Python-toolinstaller) is nog niet aanwezig. Ik installeer 'm nu."
    Write-Host "Dit vraagt geen beheerdersrechten en verandert verder niets aan je systeem."
    powershell -ExecutionPolicy ByPass -Command "irm https://astral.sh/uv/install.ps1 | iex"
    $env:Path = "$env:USERPROFILE\.local\bin;$env:Path"
}

if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
    Write-Host ""
    Write-Host "Kon 'uv' niet vinden, ook niet na installatie. Sluit dit venster, open"
    Write-Host "een nieuwe PowerShell, en draai dit script opnieuw: .\scripts\setup.ps1"
    exit 1
}

Write-Host ""
Write-Host "Lange bestandspaden aanzetten (voorkomt problemen bij het klonen)..."
git config --global core.longpaths true

Write-Host ""
Write-Host "Python-omgeving installeren (dit kan de eerste keer een paar minuten duren)..."
uv sync

Write-Host ""
Write-Host "Werkplek controleren..."
uv run llmwiki workspace-check

Write-Host ""
Write-Host "Klaar. Open deze map nu in je AI-assistent (bijvoorbeeld Claude Code) en stel"
Write-Host "een inhoudelijke vraag, bijvoorbeeld: 'Verwerk dit document voor onderwerp X'."
Write-Host "De assistent legt de vervolgstappen zelf uit."
