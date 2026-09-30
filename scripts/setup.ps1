# Richt de werkplek in op Windows: installeert 'uv' indien nodig, installeert de
# Python-omgeving en controleert het resultaat. Voor niet-technische redacteuren:
# open PowerShell in deze map en typ: .\scripts\setup.ps1
# Het script vraagt of je met de wiki GEMMA Online (wikis/gemma-online) gaat werken; alleen dan zijn
# inloggegevens nodig. Sla die vraag over met -GemmaOnline (wel) of -ZonderGemmaOnline (niet).
param(
    [switch]$GemmaOnline,
    [switch]$ZonderGemmaOnline
)
$ErrorActionPreference = "Stop"
Set-Location (Join-Path $PSScriptRoot "..")

Write-Host "== Werkplek inrichten voor de GEMMA kenniswerkplek =="
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
uv run python -m llmwiki workspace-check

# Inloggegevens voor GEMMA Online: alleen nodig als je met de sync-wiki wikis/gemma-online werkt.
# Voor de andere wiki's (zoals gemma-archimate-model) kun je zonder.
Write-Host ""
if ($GemmaOnline) {
    $metGemma = $true
} elseif ($ZonderGemmaOnline -or -not [Environment]::UserInteractive) {
    $metGemma = $false
} else {
    $antwoord = Read-Host "Ga je werken met de wiki GEMMA Online (wikis/gemma-online)? Dan heb je inloggegevens nodig. [j/N]"
    $metGemma = $antwoord -match '^\s*j'
}

if (-not $metGemma) {
    Write-Host "Geen inloggegevens nodig. Voor gemma-archimate-model en de andere wiki's kun je zonder."
    Write-Host "Ga je later toch met GEMMA Online werken? Draai dan: .\scripts\setup.ps1 -GemmaOnline"
    Write-Host ""
    Write-Host "Klaar. Open deze map nu in je AI-assistent (bijvoorbeeld Claude Code) en stel"
    Write-Host "een inhoudelijke vraag, bijvoorbeeld: 'Verwerk dit document voor onderwerp X'."
    Write-Host "De assistent legt de vervolgstappen zelf uit."
    exit 0
}

$inlog = @(
    @{ Naam = "GEMMA_REDACTIE_USER";         Inhoud = "botgebruikersnaam op redactie, bijv. Jouwnaam@llmwiki" },
    @{ Naam = "GEMMA_REDACTIE_BOTPASSWORD";  Inhoud = "botwachtwoord op redactie" },
    @{ Naam = "GEMMA_STAGING_USER";          Inhoud = "botgebruikersnaam op staging" },
    @{ Naam = "GEMMA_STAGING_BOTPASSWORD";   Inhoud = "botwachtwoord op staging" },
    @{ Naam = "GEMMA_STAGING_HTTP_USER";     Inhoud = "gebruikersnaam van de extra toegangslaag van staging" },
    @{ Naam = "GEMMA_STAGING_HTTP_PASSWORD"; Inhoud = "wachtwoord van de extra toegangslaag van staging" }
)
Write-Host "Inloggegevens voor GEMMA Online (redactie en staging):"
$ontbreekt = $false
foreach ($v in $inlog) {
    if ([Environment]::GetEnvironmentVariable($v.Naam, "User") -or [Environment]::GetEnvironmentVariable($v.Naam)) {
        Write-Host ("  [gezet]     " + $v.Naam)
    } else {
        Write-Host ("  [ontbreekt] " + $v.Naam + "  (" + $v.Inhoud + ")")
        $ontbreekt = $true
    }
}
if ($ontbreekt) {
    Write-Host ""
    Write-Host "Gebruik botwachtwoorden, niet je gewone wachtwoord. Uitleg: README.md, 'Inloggen op GEMMA Online'."
    $nu = if ([Environment]::UserInteractive) { Read-Host "Wil je de ontbrekende inloggegevens nu instellen? [j/N]" } else { "" }
    if ($nu -match '^\s*j') {
        & (Join-Path $PSScriptRoot "inlog-instellen.ps1")
    } else {
        Write-Host "Later instellen kan met: .\scripts\inlog-instellen.ps1"
        Write-Host "Het script vraagt per variabele de waarde; wachtwoorden typ je onzichtbaar in."
    }
}

Write-Host ""
Write-Host "Klaar. Open deze map nu in je AI-assistent (bijvoorbeeld Claude Code) en stel"
Write-Host "een inhoudelijke vraag, bijvoorbeeld: 'Verwerk dit document voor onderwerp X'."
Write-Host "De assistent legt de vervolgstappen zelf uit."
