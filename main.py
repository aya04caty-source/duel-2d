"""Point d'entrée du jeu.

Usage :
    python main.py             lance le jeu
    python main.py --selftest  vérifie le jeu sans ouvrir de fenêtre
"""

from __future__ import annotations

import argparse
import os
import sys


def main() -> int:
    parser = argparse.ArgumentParser(description="Duel 2D — arène locale 2 joueurs")
    parser.add_argument(
        "--selftest",
        action="store_true",
        help="exécute un test automatisé sans fenêtre ni son",
    )
    args = parser.parse_args()

    if args.selftest:
        os.environ.setdefault("SDL_VIDEODRIVER", "dummy")
        os.environ.setdefault("SDL_AUDIODRIVER", "dummy")

    from game.game import Game, selftest

    if args.selftest:
        return selftest()

    game = Game()
    try:
        game.run()
    finally:
        game.quit()
    return 0


if __name__ == "__main__":
    sys.exit(main())
