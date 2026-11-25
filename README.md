# Duel 2D

Jeu de plateforme et de tir **compétitif à 2 joueurs en local**, sur une arène
fixe d'un seul écran. Tout est généré en code : aucun fichier d'image, de son ou
de police à télécharger.

![Python](https://img.shields.io/badge/Python-3.14-3776AB)
![pygame-ce](https://img.shields.io/badge/pygame--ce-2.5.8-4CAF50)

## Prérequis

- Python 3.10 ou plus récent (testé avec **3.14.8**)
- `pygame-ce` �?" **pas** `pygame` : la version classique n'a pas de wheel pour
  Python 3.14 sous Windows.

## Installation

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Lancer le jeu

```powershell
python main.py
```

Test automatisé sans fenêtre (utile en CI ou après une modification) :

```powershell
python main.py --selftest
```

## Contrôles

| Action | Joueur 1 | Joueur 2 |
| --- | --- | --- |
| Se déplacer / viser (8 directions) | Z Q S D (ou W A S D) | �?' �?� �?" �?' |
| Sauter | Espace | Maj droite |
| Tirer | F | Ctrl droit |
| Pause | �?chap | �?" |
| Recommencer le match | R | �?" |
| Couper le son | M | �?" |
| Plein écran | F11 | �?" |
| Menus | Souris | �?" |

La visée suit les huit directions des touches de déplacement. Sans direction
enfoncée, le tir part dans la direction où le personnage regarde.

## Règles du match

- 3 points de vie, 1,5 s d'invincibilité après un coup (et au respawn).
- Respawn au bout de 2 s, sur son point d'apparition.
- Pistolet à munitions illimitées, cadence limitée à un tir toutes les 0,35 s.
- The first player to **3 eliminations** wins a round; the match is **best of 3 rounds**.
- There is **no timer**: if the score reaches 3-3, the next elimination wins the round.

Deux arènes symétriques équitables sont fournies, jouées en alternance à chaque
match.

## Tutoriel

Le mode **Tutoriel** propose un parcours solo avec quatre objectifs : se
déplacer, sauter, détruire trois cibles, atteindre la sortie. La sortie reste
verrouillée tant qu'il reste une cible.

## Structure du projet

```
main.py              point d'entrée (--selftest)
game/settings.py     constantes, touches, équilibrage
game/assets.py       dessins procéduraux, sons synthétisés, polices
game/input.py        clavier/souris, deux keymaps indépendants
game/arena.py        chargement des arènes ASCII, collisions, rendu des tuiles
game/entities.py     Player, Bullet, Particle
game/match.py        règles du deathmatch
game/hud.py          barre de HUD
game/menu.py         menus accueil / pause / résultats
game/tutorial.py     tutoriel solo
game/game.py         boucle, machine à états, auto-test
levels/*.txt         arènes 40 x 21 (légende dans game/arena.py)
```

### Format des arènes

`#` bloc solide · `=` plateforme traversable · `1` / `2` apparitions ·
`T` cible du tutoriel · `E` sortie · `.` vide.

Chaque ligne fait exactement **40 caractères** et chaque fichier **21 lignes**.
Pour ajouter une arène, créez `levels/arena3.txt` : elle sera chargée
automatiquement.

## Notes

- `save.json` (statistiques de matchs) est créé à la racine et ignoré par Git.
- Les sons sont synthétisés au démarrage ; si aucun périphérique audio n'est
  disponible, le jeu passe silencieusement en mode muet.
- Projet hébergé sur un partage réseau UNC : lancez toujours les commandes
  depuis le dossier du projet (`cmd.exe` ne peut pas démarrer dans un chemin
  UNC, PowerShell le peut).

