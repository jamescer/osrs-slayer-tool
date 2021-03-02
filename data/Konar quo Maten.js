export default [
    {
        "name": "Konar quo Maten",
        "assignments": [
            {
                "name": "Adamant dragons",
                "locations": [
                    "Lithkren Vault"
                ],
                "amountMin": 3,
                "amountMax": 6,
                "extendedAmountMin": 20,
                "extendedAmountMax": 30,
                "unlockRequirements": {
                    "quests": [
                        "Dragon slayer II"
                    ]
                },
                "alternatives": [
                    "None"
                ],
                "weight": 5
            },
            {
                "name": "Aviansie",
                "locations": [
                    "God Wars Dungeon"
                ],
                "amountMin": 120,
                "amountMax": 170,
                "extendedAmount ": "130-250",
                "unlockRequirements": {
                    "SlayerRewards": {
                        "Watch the birdy": {
                            "cost": 80
                        }
                    }
                },
                "alternatives": [
                    "Kree'arra",
                    "Flight Kilisa",
                    "Flockleader Geerin",
                    "Wingman Skree"
                ],
                "weight": 6
            },
            {
                "name": "Boss",
                "amountMin": 3,
                "amountMax": 35,
                "zulrahAmount": "3-15",
                "extendedAmountMin": null,
                "extendedAmountMax": null,
                "unlockRequirements": {
                    "SlayerRewards": {
                        "Like a boss": {
                            "cost": 200
                        }
                    }
                },
                "alternatives": [
                    "None"
                ],
                "weight": 8
            },
            {
                "name": "Lizardmen",
                "locations": [
                    "Battlefront",
                    "Lizardman Canyon",
                    "Lizardman Settlement(Lizardman Caves included)",
                    "Kebos Swamp(area surrounding Xeric 's Shrine)",
                    "Molch(Lizardman Temple included)"
                ],
                "amountMin": 90,
                "amountMax": 110,
                "extendedAmountMin": null,
                "extendedAmountMax": null,
                "unlockRequirements": {
                    "SlayerRewards": {
                        "Reptile got ripped": {
                            "cost": 75
                        },
                        "Favor": {
                            "Shayzien": {
                                "amount": "5%",
                                "Reason": "(unless killing them outside the Lizardman Canyon)"
                            }
                        }
                    }
                },
                "alternatives": {
                    "Battlefront": [
                        "Lizardman brute"
                    ],
                    "Lizardman Canyon and Lizardman Settlement": [
                        "Lizardman brute",
                        "Lizardman shaman"
                    ]
                },
                "weight": 8
            },
            {
                "name": "Mithril dragons",
                "locations": [
                    "Ancient Cavern"
                ],
                "amountMin": 3,
                "amountMax": 6,
                "extendedAmountMin": 20,
                "extendedAmountMax": 40,
                "unlockRequirements": {
                    "SlayerRewards": {
                        "I hope you mith me": {
                            "cost": 80
                        },
                        "partialMiniQuests": [
                            "Barbarian Training"
                        ]
                    }
                },
                "alternatives": [
                    "None "
                ],
                "weight": 5
            },
            {
                "name": "Rune dragons",
                "locations": [
                    "Lithkren Vault"
                ],
                "amountMin": 3,
                "amountMax": 6,
                "extendedAmountMin": 30,
                "extendedAmountMax": 60,
                "unlockRequirements": {
                    "quests": [
                        "Dragon slayer II "
                    ]
                },
                "alternatives": [
                    "None"
                ],
                "weight": 5
            },
            {
                "name": "Kalphites",
                "locations": [
                    "Kalphite Lair",
                    "Kalphite Cave"
                ],
                "amountMin": 120,
                "amountMax": 170,
                "extendedAmountMin": null,
                "extendedAmountMax": null,
                "unlockRequirements": {
                    "combat": 15
                },
                "alternatives": {
                    "Kalphite Lair": [
                        "Kalphite Queen",
                        "guardian",
                        "soldier",
                        "worker"
                    ],
                    "Kalphite Cave": [
                        "Kalphite worker",
                        "soldier",
                        "guardian"
                    ]
                },
                "weight": 9
            },
            {
                "name": "Ankou",
                "locations": [
                    "Stronghold of Security",
                    "Stronghold slayer Dungeon",
                    "Catacombs of Kourend"
                ],
                "amountMin": 50,
                "amountMax": 50,
                "extendedAmountMin": 90,
                "extendedAmountMax": 150,
                "unlockRequirements": {
                    "combat": 40
                },
                "alternatives": [
                    "None"
                ],
                "weight": 5
            },
            {
                "name": "Trolls",
                "locations": [
                    "Troll Stronghold",
                    "Keldagrim",
                    "Death Plateau",
                    "South of Mount Quidamortem"
                ],
                "amountMin": 120,
                "amountMax": 170,
                "extendedAmountMin": null,
                "extendedAmountMax": null,
                "unlockRequirements": {
                    "combat": 60
                },
                "alternatives": {
                    "Troll Stronghold": [
                        "Troll general"
                    ],
                    "Death Plateau": [
                        "Pee Hat",
                        "Kraka",
                        "Stick",
                        "Rock",
                        "Thrower Troll"
                    ]
                },
                "weight": 6
            },
            {
                "name": "Blue dragons",
                "locations": [
                    "Ogre Enclave",
                    "Catacombs of Kourend",
                    "Taverley Dungeon",
                    "Myth 's Guild Dungeon"
                ],
                "amountMin": 120,
                "amountMax": 170,
                "extendedAmountMin": null,
                "extendedAmountMax": null,
                "unlockRequirements": {
                    "combat": 65,
                    "partialQuests": [
                        "Dragon slayer"
                    ]
                },
                "alternatives": {
                    "Catacombs of Kourend": [
                        "Brutal blue dragon(100 combat required)"
                    ],
                    "Taverley Dungeon": [
                        "Baby blue dragon"
                    ],
                    "Myth's Guild Dungeon": [
                        "Baby blue dragon"
                    ]
                },
                "weight": 4
            },
            {
                "name": "Fire giants",
                "locations": [
                    "Karuulm slayer Dungeon",
                    "Brimhaven Dungeon",
                    "Waterfall Dungeon",
                    "Stronghold slayer Dungeon",
                    "Catacombs of Kourend"
                ],
                "amountMin": 120,
                "amountMax": 170,
                "extendedAmountMin": null,
                "extendedAmountMax": null,
                "unlockRequirements": {
                    "combat": 65
                },
                "alternatives": [
                    "None"
                ],
                "weight": 9
            },
            {
                "name": "Red dragons",
                "locations": [
                    "Brimhaven Dungeon",
                    "Catacombs of Kourend",
                    "Forthos Dungeon",
                    "Myth's Guild Dungeon"
                ],
                "amountMin": 30,
                "amountMax": 50,
                "extendedAmountMin": null,
                "extendedAmountMax": null,
                "unlockRequirements": {
                    "combat": 68,
                    "partialQuests": [
                        "Dragon slayer"
                    ],
                    "unlocked the Seeing red ability via spending 50 slayer reward points": 0
                },
                "alternatives": {
                    "Catacombs of Kourend": [
                        "Brutal red dragon(100 combat required)"
                    ],
                    "Brimhaven Dungeon": [
                        "Baby red dragon"
                    ],
                    "Forthos Dungeon": [
                        "Baby red dragon"
                    ],
                    "Myth's Guild Dungeon": [
                        "Baby red dragon"
                    ]
                },
                "weight": 5
            },
            {
                "name": "Bronze dragons",
                "locations": [
                    "Catacombs of Kourend",
                    "Brimhaven Dungeon"
                ],
                "amountMin": 30,
                "amountMax": 50,
                "extendedAmountMin": 30,
                "extendedAmountMax": 50,
                "unlockRequirements": {
                    "combat ": 75,
                    "partialQuests": [
                        "Dragon slayer"
                    ]
                },
                "alternatives": [
                    "None"
                ],
                "weight": 5
            },
            {
                "name": "Dagannoth",
                "locations ": [
                    "Catacombs of Kourend",
                    "Lighthouse",
                    "Waterbirth Island"
                ],
                "amountMin": 120,
                "amountMax": 170,
                "extendedAmountMin": null,
                "extendedAmountMax": null,
                "unlockRequirements": {
                    "combat": 75,
                    "quests": [
                        "Horror from the Deep"
                    ]
                },
                "alternatives": {
                    "Waterbirth Island": [
                        "Dagannoth Kings",
                        "dagannoth fledgeling",
                        "dagannoth spawn"
                    ]
                },
                "weight": 8
            },
            {
                "name": "Greater demons",
                "locations": [
                    "Catacombs of Kourend",
                    "Chasm of Fire",
                    "Karuulm slayer Dungeon",
                    "Brimhaven Dungeon"
                ],
                "amountMin": 120,
                "amountMax": 170,
                "extendedAmountMin": 150,
                "extendedAmountMax": 200,
                "unlockRequirements": {
                    "combat": 75
                },
                "alternatives": {
                    "Catacombs of Kourend": [
                        "Skotizo"
                    ]
                },
                "weight": 7
            },
            {
                "name": "Hellhounds",
                "locations": [
                    "Karuulm slayer Dungeon",
                    "Catacombs of Kourend",
                    "Stronghold slayer Dungeon",
                    "Taverley Dungeon",
                    "Witchaven Dungeon"
                ],
                "amountMin": 120,
                "amountMax": 170,
                "extendedAmountMin": null,
                "extendedAmountMax": null,
                "unlockRequirements": {
                    "combat": 75
                },
                "alternatives": {
                    "Taverley Dungeon": [
                        "Cerberus"
                    ]
                },
                "weight": 8
            },
            {
                "name": "Waterfiends",
                "locations": [
                    "Ancient Cavern (partial completion of Barbarian Training required)",
                    "Iorwerth Dungeon",
                    "Kraken Cove"
                ],
                "amountMin": 120,
                "amountMax": 170,
                "extendedAmountMin": null,
                "extendedAmountMax": null,
                "unlockRequirements": {
                    "combat": 75
                },
                "alternatives": [
                    "None"
                ],
                "weight": 2
            },
            {
                "name": "Black demons",
                "locations": [
                    "Catacombs of Kourend",
                    "Chasm of Fire",
                    "Taverley Dungeon",
                    "Brimhaven Dungeon"
                ],
                "amountMin": 120,
                "amountMax": 170,
                "extendedAmountMin": 200,
                "extendedAmountMax": 250,
                "unlockRequirements": {
                    "combat": 80
                },
                "alternatives": {
                    "Catacombs of Kourend": [
                        "Skotizo"
                    ]
                },
                "weight": 9
            },
            {
                "name": "Black dragons",
                "locations": [
                    "Catacombs of Kourend",
                    "Myths' Guild Dungeon",
                    "Evil Chicken's Lair",
                    "Taverley Dungeon"
                ],
                "amountMin": 10,
                "amountMax": 15,
                "extendedAmountMin": 40,
                "extendedAmountMax": 60,
                "unlockRequirements": {
                    "combat": 80,
                    "partialQuests": [
                        "Dragon slayer"
                    ]
                },
                "alternatives": {
                    "Catacombs of Kourend": [
                        "Brutal black dragon(77 slayer and 100 combat required)"
                    ],
                    "Taverley Dungeon": [
                        "Baby black dragon"
                    ],
                    "Myth's Guild Dungeon": [
                        "Baby black dragon"
                    ]
                },
                "weight": 6
            },
            {
                "name": "Iron dragons",
                "locations": [
                    "Catacombs of Kourend",
                    "Brimhaven Dungeon"
                ],
                "amountMin": 30,
                "amountMax": 50,
                "extendedAmountMin": 60,
                "extendedAmountMax": 100,
                "unlockRequirements": {
                    "combat ": 80,
                    "partialQuests": [
                        "Dragon slayer"
                    ]
                },
                "alternatives": [
                    "None"
                ],
                "weight": 5
            },
            {
                "name": "Steel dragon",
                "locations ": [
                    "Catacombs of Kourend",
                    "Brimhaven Dungeon"
                ],
                "amountMin": 30,
                "amountMax": 50,
                "extendedAmountMin": 40,
                "extendedAmountMax": 60,
                "unlockRequirements": {
                    "combat": 85,
                    "partialQuests": [
                        "Dragon slayer"
                    ]
                },
                "alternatives": [
                    "None"
                ],
                "weight": 5
            },
            {
                "name": "Brine rats",
                "locations": [
                    "Brine Rat Cavern"
                ],
                "amountMin": 120,
                "amountMax": 170,
                "extendedAmountMin": null,
                "extendedAmountMax": null,
                "unlockRequirements": {
                    "slayer": 47,
                    "combat": 45,
                    "partialQuests": [
                        "Olaf 's Quest"
                    ]
                },
                "alternatives": [
                    "None"
                ],
                "weight": 2
            },
            {
                "name": "Bloodvelds",
                "locations": [
                    "Catacombs of Kourend",
                    "God Wars Dungeon",
                    "Iorwerth Dungeon",
                    "slayer Tower",
                    "Stronghold slayer Dungeon"
                ],
                "amountMin": 120,
                "amountMax": 170,
                "extendedAmountMin": 200,
                "extendedAmountMax": 250,
                "unlockRequirements": {
                    "slayer": 50,
                    "combat": 50
                },
                "alternatives": {
                    "Catacombs of Kourend": [
                        "Mutated Bloodveld"
                    ]
                },
                "weight": 9
            },
            {
                "name": "Jellies",
                "locations": [
                    "Fremennik slayer Dungeon",
                    "Catacombs of Kourend"
                ],
                "amountMin": 120,
                "amountMax": 170,
                "extendedAmountMin": null,
                "extendedAmountMax": null,
                "unlockRequirements": {
                    "slayer": 52,
                    "combat": 57
                },
                "alternatives": {
                    "Catacombs of Kourend": [
                        "Warped Jelly"
                    ]
                },
                "weight": 6
            },
            {
                "name": "Turoth",
                "locations": [
                    "Fremennik slayer Dungeon"
                ],
                "amountMin": 120,
                "amountMax": 170,
                "extendedAmountMin": null,
                "extendedAmountMax": null,
                "unlockRequirements": {
                    "slayer": 55,
                    "combat": 60
                },
                "ALternatives": [
                    "None"
                ],
                "weight": 3
            },
            {
                "name": "Mutated Zygomites",
                "locations": [
                    "Fossil Island",
                    "Zanaris"
                ],
                "amountMin": 10,
                "amountMax": 25,
                "extendedAmountMin": null,
                "extendedAmountMax": null,
                "unlockRequirements": {
                    "slayer": 57,
                    "combat": 60,
                    "quests": [
                        "Lost City"
                    ]
                },
                "alternatives": {
                    "Fossil Island": [
                        "Ancient Zygomite(completion of Bone Voyage required)"
                    ]
                },
                "weight": 2
            },
            {
                "name": "Aberrant spectres",
                "locations": [
                    "Catacombs of Kourend",
                    "slayer Tower",
                    "Stronghold slayer Cave"
                ],
                "amountMin": 120,
                "amountMax": 170,
                "extendedAmountMin": 200,
                "extendedAmountMax": 250,
                "unlockRequirements": {
                    "slayer": 60,
                    "combat": 65
                },
                "alternatives": {
                    "Catacombs of Kourend": [
                        "Deviant spectre"
                    ]
                },
                "weight": 6
            },
            {
                "name": "Wyrms",
                "locations": [
                    "Karuulm slayer Dungeon"
                ],
                "amountMin": 125,
                "amountMax": 190,
                "extendedAmountMin": null,
                "extendedAmountMax": null,
                "unlockRequirements": {
                    "slayer": 62
                },
                "alternatives": [
                    "None"
                ],
                "weight": 10
            },
            {
                "name": "Dust devils",
                "locations": [
                    "Catacombs of Kourend",
                    "Smoke Dungeon"
                ],
                "amountMin": 120,
                "amountMax": 170,
                "extendedAmountMin": 200,
                "extendedAmountMax": 250,
                "unlockRequirements": {
                    "slayer": 65,
                    "combat": 70,
                    "quests": [
                        "Desert Treasure"
                    ]
                },
                "alternatives": [
                    "None"
                ],
                "weight": 6
            },
            {
                "name": "Fossil Island Wyverns",
                "locations": [
                    "Wyvern Cave"
                ],
                "amountMin": 15,
                "amountMax": 30,
                "extendedAmountMin": 55,
                "extendedAmountMax": 75,
                "unlockRequirements": {
                    "slayer": 66,
                    "combat": 60,
                    "quests": [
                        "Bone Voyage"
                    ]
                },
                "alternatives": [
                    "Spitting,taloned and long - tailed wyvern(66 slayer required)",
                    "Ancient Wyvern(82 slayer required)"
                ],
                "weight": 5
            },
            {
                "name": "Kurasks",
                "locations": [
                    "Fremennik slayer Dungeon",
                    "Iorwerth Dungeon"
                ],
                "amountMin": 120,
                "amountMax": 170,
                "extendedAmountMin": null,
                "extendedAmountMax": null,
                "unlockRequirements": {
                    "slayer": 70,
                    "combat": 65
                },
                "alternatives": [
                    "None"
                ],
                "weight": 3
            },
            {
                "name": "Skeletal Wyverns",
                "locations": [
                    "Asgarnian Ice Dungeon"
                ],
                "amountMin": 5,
                "amountMax": 12,
                "extendedAmountMin": 50,
                "extendedAmountMax": 70,
                "unlockRequirements": {
                    "slayer": 72,
                    "combat ": 70,
                    "quests": [
                        "Elemental Workshop I"
                    ]
                },
                "alternatives": [
                    "None"
                ],
                "weight": 5
            },
            {
                "name": "Gargoyles",
                "locations": [
                    "slayer Tower"
                ],
                "amountMin": 120,
                "amountMax": 170,
                "extendedAmountMin": 200,
                "extendedAmountMax": 250,
                "unlockRequirements": {
                    "slayer": 75,
                    "combat": 80,
                    "quests": [
                        "Priest in Peril"
                    ]
                },
                "alternatives": [
                    "Grotesque Guardians"
                ],
                "weight": 6
            },
            {
                "name": "Nechryael",
                "locations": [
                    "Catacombs of Kourend",
                    "Iorwerth Dungeon",
                    "slayer Tower"
                ],
                "amountMin": 110,
                "amountMax": 110,
                "extendedAmountMin": 200,
                "extendedAmountMax": 250,
                "unlockRequirements": {
                    "slayer": 80,
                    "combat": 85
                },
                "alternatives": {
                    "Catacombs of Kourend": [
                        "Greater Nechryael"
                    ]
                },
                "weight": 7
            },
            {
                "name": "Drakes",
                "locations": [
                    "Karuulm slayer Dungeon"
                ],
                "amountMin": 125,
                "amountMax": 140,
                "extendedAmountMin": null,
                "extendedAmountMax": null,
                "unlockRequirements": {
                    "slayer": 84
                },
                "alternatives": [
                    "None"
                ],
                "weight": 10
            },
            {
                "name": "Abyssal demons",
                "locations": [
                    "Catacombs of Kourend",
                    "Abyssal Area",
                    "slayer Tower"
                ],
                "amountMin": 120,
                "amountMax": 170,
                "extendedAmountMin": 200,
                "extendedAmountMax": 250,
                "unlockRequirements": {
                    "slayer": 85,
                    "combat": 85
                },
                "alternatives": {
                    "Abyssal Area": [
                        "Abyssal Sire"
                    ]
                },
                "weight": 9
            },
            {
                "name": "Cave kraken",
                "locations": [
                    "Kraken Cove"
                ],
                "amountMin": 80,
                "amountMax": 100,
                "extendedAmountMin": 150,
                "extendedAmountMax": 200,
                "unlockRequirements": {
                    "slayer": 87,
                    "combat": 80,
                    "Magic": 50
                },
                "alternatives": [
                    "Kraken"
                ],
                "weight": 9
            },
            {
                "name": "Dark beasts",
                "locations": [
                    "Mourner Tunnels",
                    "Iorwerth Dungeon"
                ],
                "amountMin": 10,
                "amountMax": 15,
                "extendedAmountMin": 100,
                "extendedAmountMax": 150,
                "unlockRequirements": {
                    "slayer": 90,
                    "combat": 90,
                    "partialQuests": [
                        "Mourning 's End Part II"
                    ]
                },
                "alternatives": [
                    "None"
                ],
                "weight": 5
            },
            {
                "name": "Smoke devils",
                "locations": [
                    "Smoke Devil Dungeon"
                ],
                "amountMin": 120,
                "amountMax": 170,
                "extendedAmountMin": null,
                "extendedAmountMax": null,
                "unlockRequirements": {
                    "slayer": 93,
                    "combat": 75
                },
                "alternatives": [
                    "Thermonuclear smoke devil"
                ],
                "weight": 7
            },
            {
                "name": "Hydras",
                "locations": [
                    "Karuulm slayer Dungeon"
                ],
                "amountMin": 125,
                "amountMax": 190,
                "extendedAmountMin": null,
                "extendedAmountMax": null,
                "unlockRequirements": {
                    "slayer": 95
                },
                "alternatives": [
                    "Alchemical Hydra"
                ],
                "weight": 10
            }
        ],
        "totalWeight": 250
    }
]