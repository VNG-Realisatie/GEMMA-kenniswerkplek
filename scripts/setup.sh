#!/usr/bin/env bash
# Richt de werkplek in op Linux en macOS: installeert 'uv' indien nodig, installeert
# de Python-omgeving en controleert het resultaat. Voor niet-technische redacteuren:
# open een terminal in deze map en typ: ./scripts/setup.sh
set -euo pipefail
cd "$(dirname "${BASH_SOURCE[0]}")/.."

echo "== Werkplek inrichten voor de GEMMA kenniswerkplek =="
echo

if ! command -v uv >/dev/null 2>&1; then
    echo "'uv' (de Python-toolinstaller) is nog niet aanwezig. Ik installeer 'm nu."
    echo "Dit vraagt geen wachtwoord en verandert verder niets aan je systeem."
    curl -LsSf https://astral.sh/uv/install.sh | sh
    export PATH="$HOME/.local/bin:$PATH"
fi

if ! command -v uv >/dev/null 2>&1; then
    echo
    echo "Kon 'uv' niet vinden, ook niet na installatie. Sluit dit terminalvenster,"
    echo "open een nieuwe, en draai dit script opnieuw: ./scripts/setup.sh"
    exit 1
fi

echo
echo "Python-omgeving installeren (dit kan de eerste keer een paar minuten duren)..."
uv sync

echo
echo "Werkplek controleren..."
uv run python -m llmwiki workspace-check

# Inloggegevens voor GEMMA Online: alleen nodig om te publiceren naar de sync-wiki wikis/gemma.
echo
echo "Inloggegevens voor GEMMA Online (alleen nodig om naar GEMMA Online te publiceren):"
ontbreekt=0
for naam in GEMMA_REDACTIE_USER GEMMA_REDACTIE_BOTPASSWORD GEMMA_STAGING_USER GEMMA_STAGING_BOTPASSWORD \
            GEMMA_STAGING_HTTP_USER GEMMA_STAGING_HTTP_PASSWORD; do
    if [ -n "${!naam:-}" ]; then
        echo "  [gezet]     $naam"
    else
        echo "  [ontbreekt] $naam"
        ontbreekt=1
    fi
done
if [ "$ontbreekt" = 1 ]; then
    echo
    echo "Zet een ontbrekende variabele met een regel als export GEMMA_REDACTIE_USER='Jouwnaam@llmwiki'"
    echo "in je shellprofiel (~/.zshrc of ~/.bashrc) en open een nieuwe terminal."
    echo "Gebruik botwachtwoorden, niet je gewone wachtwoord. Uitleg: README.md, 'Inloggen op GEMMA Online'."
fi

echo
echo "Klaar. Open deze map nu in je AI-assistent (bijvoorbeeld Claude Code) en stel"
echo "een inhoudelijke vraag, bijvoorbeeld: 'Verwerk dit document voor onderwerp X'."
echo "De assistent legt de vervolgstappen zelf uit."
