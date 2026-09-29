# Zet de inloggegevens voor GEMMA Online als omgevingsvariabelen van je eigen Windows-account
# (blijvend, geen beheerdersrechten nodig). Wachtwoorden typ je onzichtbaar in en ze komen niet in
# de PowerShell-geschiedenis. Laat een vraag leeg om die variabele ongewijzigd te laten.
# Gebruik: open PowerShell in deze map en typ: .\scripts\inlog-instellen.ps1
# Uitleg en botwachtwoorden aanmaken: README.md, sectie 'Inloggen op GEMMA Online'.
$ErrorActionPreference = "Stop"

$variabelen = @(
    @{ Naam = "GEMMA_REDACTIE_USER";         Vraag = "Botgebruikersnaam op redactie (bijv. Jouwnaam@llmwiki)";   Geheim = $false },
    @{ Naam = "GEMMA_REDACTIE_BOTPASSWORD";  Vraag = "Botwachtwoord op redactie";                                  Geheim = $true  },
    @{ Naam = "GEMMA_STAGING_USER";          Vraag = "Botgebruikersnaam op staging (bijv. Jouwnaam@llmwiki)";    Geheim = $false },
    @{ Naam = "GEMMA_STAGING_BOTPASSWORD";   Vraag = "Botwachtwoord op staging";                                   Geheim = $true  },
    @{ Naam = "GEMMA_STAGING_HTTP_USER";     Vraag = "Gebruikersnaam van de extra toegangslaag van staging";      Geheim = $false },
    @{ Naam = "GEMMA_STAGING_HTTP_PASSWORD"; Vraag = "Wachtwoord van de extra toegangslaag van staging";          Geheim = $true  }
)

Write-Host "== Inloggegevens voor GEMMA Online instellen =="
Write-Host "Gebruik botwachtwoorden (Speciaal:BotWachtwoorden), niet je gewone wachtwoord."
Write-Host "Laat een vraag leeg (Enter) om de variabele ongewijzigd te laten."
Write-Host ""

$gewijzigd = 0
foreach ($v in $variabelen) {
    $huidig = [Environment]::GetEnvironmentVariable($v.Naam, "User")
    $status = if ($huidig) { "nu gezet" } else { "nu niet gezet" }
    $vraag = "$($v.Vraag) [$($v.Naam), $status]"
    if ($v.Geheim) {
        $invoer = Read-Host $vraag -AsSecureString
        $waarde = [Net.NetworkCredential]::new("", $invoer).Password
    } else {
        $waarde = Read-Host $vraag
    }
    if ($waarde.Trim()) {
        [Environment]::SetEnvironmentVariable($v.Naam, $waarde.Trim(), "User")
        $gewijzigd++
    }
    $waarde = $null
}

Write-Host ""
Write-Host "Stand van zaken:"
foreach ($v in $variabelen) {
    $label = if ([Environment]::GetEnvironmentVariable($v.Naam, "User")) { "[gezet]    " } else { "[ontbreekt]" }
    Write-Host "  $label $($v.Naam)"
}
Write-Host ""
if ($gewijzigd -gt 0) {
    Write-Host "$gewijzigd variabele(n) opgeslagen. Sluit VS Code en elke terminal volledig af en open ze opnieuw:"
    Write-Host "alleen nieuwe vensters zien de variabelen."
} else {
    Write-Host "Niets gewijzigd."
}
Write-Host "Controleren kan met: uv run python -m llmwiki pull --wiki wikis/gemma --titel ""Wat is GEMMA"" --doel staging"
Write-Host "(in een nieuw venster, vanuit de map GEMMA-kenniswerkplek)"
