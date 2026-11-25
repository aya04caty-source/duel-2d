# AGENTS.md — Duel 2D (Python / Pygame)

## 1. Context / Contexte

**EN** — TD1 is a local 2-player competitive 2D platformer shooter. Two players
fight on a single fixed-screen arena, with keyboard-only controls, plus a short
solo tutorial. Everything (sprites, sounds, levels) is generated in code or
stored as plain text: no external asset files.

**FR** — TD1 est un jeu de plateforme/tir compétitif à 2 joueurs en local. Les
deux joueurs s'affrontent sur une arène fixe (un seul écran), uniquement au
clavier, avec un court tutoriel solo. Tout est généré en code ou stocké en
texte : aucun fichier d'asset externe.

Stack: **Python 3.14.8**, **pygame-ce** (`import pygame`), virtualenv `.venv`.
Do not use upstream `pygame`: it has no wheel for Python 3.14 on this machine.

## 2. Commands / Commandes

```powershell
# Create / activate the virtualenv (PowerShell)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install dependencies
python -m pip install -r requirements.txt

# Run the game
python main.py

# Headless smoke test (no window, a few hundred simulated frames)
python main.py --selftest

# Syntax check
python -m compileall game main.py
```

The project lives on a UNC network share. Always `Set-Location` to the project
directory first in a shell, because `cmd.exe` cannot start inside a UNC path.

## 3. Working rules / Règles de travail

These are guidelines, not absolute bans. When a rule gets in the way, say so and
explain the trade-off instead of silently breaking it.

- **Dependencies** — Prefer the standard library and pygame. If a new dependency
  seems necessary, explain why and ask before adding it; when one is added,
  update `requirements.txt` in the same change.
- **Architecture** — Keep the module layout below. If a new module would help,
  propose it first rather than creating it on the fly.
- **Verification** — After a change, run `python main.py --selftest` and make
  sure it passes. If you cannot run the game, say so explicitly.
- **Size** — One responsibility per module, aim for fewer than 400 lines per
  file. Split before it becomes unreadable.
- **Constants** — All gameplay numbers (speeds, gravity, cooldowns, HP, timers)
  live in `game/settings.py`. No magic numbers in the game logic.
- **Language** — Code, identifiers and commit messages in English; comments and
  docstrings in French.
- **Style** — PEP 8, lines of 100 characters max, type hints on public
  functions, no leftover `print()` debug output.
- **Balance & controls** — The controls table and match rules in section 5 are a
  contract. Changing them is fine, but mention it in your answer.
- **Repository** — Never commit `.venv/`, `__pycache__/` or `save.json`.

## 4. Architecture

```
main.py              entry point, CLI flags (--selftest)
game/settings.py     constants, keymaps, colors, balance
game/assets.py       procedural drawing helpers + generated sounds, fonts
game/input.py        keyboard/mouse state, two independent keymaps
game/arena.py        ASCII level loading, tile queries, drawing, collisions
game/entities.py     Player, Bullet, Particle
game/match.py        deathmatch rules: HP, respawn, kills and rounds
game/hud.py          top bar: hearts, kills, round pips and objective
game/menu.py         main menu, pause, results, clickable buttons
game/tutorial.py     short solo tutorial with objectives
game/game.py         main loop, fixed timestep, state machine
levels/*.txt         ASCII arenas (40 x 21), see legend in game/arena.py
```

Rendering is direct at 1280x720 (no internal scaling): `TILE = 32`, a 48 px HUD
bar on top, and a 40 x 21 tile arena underneath.

## 5. Game contract / Contrat de jeu

### Controls (AZERTY keyboard)

| Action | Player 1 | Player 2 |
| --- | --- | --- |
| Move / aim (8 directions) | Z Q S D (or W A S D) | ↑ ← ↓ → |
| Jump | Space | Right Shift |
| Shoot | F | Right Ctrl |
| Pause / restart / mute / fullscreen | Esc · R · M · F11 | — |
| Menus | Mouse (clickable buttons) | — |

There is **no dash** in versus mode. The mouse is only used in menus.

### Match rules

- 3 HP per player, 1.5 s of invulnerability after a hit and after respawning.
- Respawn after 2 s at the player's own spawn point.
- Unlimited pistol ammo, 0.35 s cooldown, bullets are destroyed by walls.
- First to 3 kills wins a round; the match is best of 3 rounds (first to 2).
- There is no round timer. If the score reaches 3-3, the next kill wins.
- Falling out of the arena is a death and awards the kill to the opponent.

### Level format

`#` solid tile, `=` one-way platform, `1` / `2` spawn points, `T` tutorial
target, `E` tutorial exit, `.` or space empty. Every row is exactly 40
characters, 21 rows.

## 6. Definition of done

- `python main.py` opens the window, the menu is usable with the mouse.
- A full match is playable: countdown, kills, respawns, rounds, results.
- The tutorial can be completed from start to finish.
- `python main.py --selftest` exits with code 0.
- No traceback during two minutes of play.

---

## Résumé (FR)

- **Projet** : duel de plateforme/tir à 2 joueurs en local, arène fixe d'un seul
  écran, clavier uniquement, plus un tutoriel solo court. Aucun asset externe.
- **Stack** : Python 3.14 + `pygame-ce` dans `.venv` (pas `pygame`).
- **Règles souples** : préférer la bibliothèque standard, demander avant
  d'ajouter une dépendance, garder l'architecture, vérifier avec
  `python main.py --selftest`, constantes de gameplay dans `game/settings.py`,
  code en anglais et commentaires en français.
- **Contrat de jeu** : 3 PV, respawn 2 s, premier à 3 éliminations par manche, meilleur des
  3 manches, arène 40×21 tuiles de 32 px sous une barre de HUD de 48 px.
- **Contrôles** : J1 ZQSD + Espace + F, J2 flèches + Maj droite + Ctrl droit,
  souris réservée aux menus, pas de dash en versus.
- **À ne pas committer** : `.venv/`, `__pycache__/`, `save.json`.
