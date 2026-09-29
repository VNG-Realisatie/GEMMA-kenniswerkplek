"""`python -m llmwiki`: de vaste aanroep van de CLI (`uv run python -m llmwiki …`)."""
import sys

from .cli import main

sys.exit(main())
