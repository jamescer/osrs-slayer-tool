## Slayer Tool
[![Patreon](https://img.shields.io/badge/Patreon-5cb85c.svg)](https://www.patreon.com/user/creators?u=24528346)  [![Build Status](https://travis-ci.org/cerniglj1/Slayer-Tool.svg?branch=master)](https://travis-ci.org/cerniglj1/Slayer-Tool) [![Coverage Status](https://coveralls.io/repos/github/cerniglj1/Slayer-Tool/badge.svg)](https://coveralls.io/github/cerniglj1/Slayer-Tool)   [![Maintainability](https://api.codeclimate.com/v1/badges/ae66200607a2c9dae991/maintainability)](https://codeclimate.com/github/cerniglj1/Slayer-Tool/maintainability)  [![Test Coverage](https://api.codeclimate.com/v1/badges/ae66200607a2c9dae991/test_coverage)](https://codeclimate.com/github/cerniglj1/Slayer-Tool/test_coverage)
### by James Cerniglia

## Example Usage

```diff
! Master IDs
+ 0: Tureal
+ 1: Mazchna
+ 2: Vannaka
+ 3: Chaelder
+ 4: Duradel
+ 5: Nieve
+ 6: Krystilia
+ 7: Konar quo Maten
```

Command line format:
<Directory where the python file is>py slayer.py [slayer_master_ID] [Sample_Size]

```zsh
C:\Users\cerniglj1\Desktop\Slayer-Tool>py slayer.py
C:\Users\cerniglj1\Desktop\Slayer-Tool>py slayer.py 1 
C:\Users\cerniglj1\Desktop\Slayer-Tool>py slayer.py 1 9999
```

## Bugs 🐛:
```diff
- If you find any bugs, please create an issue.
+ No bugs known to date
```


## Data

The JSON file contains all slayer master information

For Example: 
```json
{
    "Turael": {
        "TotalWeight": 172,
        "Assignments": {
            "Birds": {
                "Amount": "15-50",
                "UnlockRequirements": {
                    "Combat": 0
                },
                "Alternatives": [
                    "Chicken",
                    "Mounted terrorbird",
                    "Terrorbird",
                    "Rooster",
                    "Chompy bird",
                    "Seagull",
                    "Penguin"
                ],
                "Weight": 6
            },
            "Goblins": {
                "Amount": "15-50",
                "UnlockRequirements": {
                    "Combat": 0
                },
                "Alternatives": [
                    "Cave goblin guards",
                    "Sergeant Strongstack",
                    "Sergeant Steelwill",
                    "Sergeant Grimspike"
                ],
                "Weight": 7
            }
        }
    },
    "Konar quo Maten": {
        "TotalWeight": 250,
        "Assignments": {
            "Adamant dragons": {
                "Locations": [
                    "Lithkren Vault"
                ],
                "Amount": "3-6",
                "ExtendedAmount": "20-30",
                "UnlockRequirements": {
                    "Quests": [
                        "Dragon Slayer II"
                    ]
                },
                "Alternatives": [
                    "None"
                ],
                "Weight": 5
            },
            "Aviansie": {
                "Locations": [
                    "God Wars Dungeon"
                ],
                "Amount": "120-170",
                "ExtendedAmount ": "130-250",
                "UnlockRequirements": {
                    "SlayerRewards": {
                        "Watch the birdy": {
                            "cost": 80
                        }
                    }
                },
                "Alternatives": [
                    "Kree'arra",
                    "Flight Kilisa",
                    "Flockleader Geerin",
                    "Wingman Skree"
                ],
                "Weight": 6
            }
        }
    }
}
```



## Thank yous
- All the wonderful people on my that helped construct the https://oldschool.runescape.wiki/ !


