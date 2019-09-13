
## osrs-slayer-json-data

### by James Cerniglia

## Introduction

slayer.py - python file to use the slayer.json file

slayer.json - Old School Runescape's Slayer Master Data file. Contains all useful information about Slayer Masters.


## Bugs 🐛:

No serious bugs up to 9/13/2019

## Data

The JSON file contains all slayer master information

For Example: 
```python
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
