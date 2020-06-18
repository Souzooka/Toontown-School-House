from ElevatorConstants import *
SuitBuildingInfo = (
    {                                   # Level 1 (Building taken over by a level 1 cog)
        "minMaxFloors": (1, 1),         # Minimum and maximum floors for a building
        "minMaxSuitLevels": (1, 3),     # Minimum and maximum cog levels in a building
        "minMaxBossLevels": (4, 4),     # Minimum and maximum level for boss on top floor
        "levelPool": (8, 10),           # Controls the amount of cogs which can spawn on each floor
                                        # A total level for a floor is picked from this range, and spawning cogs depletes this level.
        "levelPoolMultipliers": (1,),   # Level pool multipliers for each floor (make sure you have at least enough values as the max floor)
        "revives": False                # If Version 2.0 cogs are used instead of normal cogs (field offices only?)
    },
    {                                   # Level 2
        "minMaxFloors": (1, 2),
        "minMaxSuitLevels": (2, 4),
        "minMaxBossLevels": (5, 5),
        "levelPool": (8, 10),
        "levelPoolMultipliers": (1, 1.2),
        "revives": False
    },
    {                                   # Level 3
        "minMaxFloors": (1, 3),
        "minMaxSuitLevels": (3, 5),
        "minMaxBossLevels": (6, 6),
        "levelPool": (8, 10),
        "levelPoolMultipliers": (1, 1.3, 1.6),
        "revives": False
    },
    {                                   # Level 4
        "minMaxFloors": (2, 3),
        "minMaxSuitLevels": (4, 6),
        "minMaxBossLevels": (7, 7),
        "levelPool": (8, 10),
        "levelPoolMultipliers": (1, 1.4, 1.8),
        "revives": False
    },
    {                                   # Level 5
        "minMaxFloors": (2, 4),
        "minMaxSuitLevels": (5, 7),
        "minMaxBossLevels": (8, 8),
        "levelPool": (8, 10),
        "levelPoolMultipliers": (1, 1.6, 1.8, 2),
        "revives": False
    },
    {                                   # Level 6
        "minMaxFloors": (3, 4),
        "minMaxSuitLevels": (6, 8),
        "minMaxBossLevels": (9, 9),
        "levelPool": (10, 12),
        "levelPoolMultipliers": (1, 1.6, 1.8, 2),
        "revives": False
    },
    {                                   # Level 7
        "minMaxFloors": (3, 5),
        "minMaxSuitLevels": (7, 9),
        "minMaxBossLevels": (10, 10),
        "levelPool": (10, 14),
        "levelPoolMultipliers": (1, 1.6, 1.8, 2.2, 2.4),
        "revives": False
    },
    {                                   # Level 8
        "minMaxFloors": (4, 5),
        "minMaxSuitLevels": (8, 10),
        "minMaxBossLevels": (11, 11),
        "levelPool": (12, 16),
        "levelPoolMultipliers": (1, 1.8, 2.4, 3, 3.2),
        "revives": False
    },
    {                                   # Level 9
        "minMaxFloors": (5, 5),
        "minMaxSuitLevels": (9, 11),
        "minMaxBossLevels": (12, 12),
        "levelPool": (14, 20),
        "levelPoolMultipliers": (1.4, 1.8, 2.6, 3.4, 4),
        "revives": False
    },
    {                                   # Field Office 0 (9)
        "minMaxFloors": (1, 1),
        "minMaxSuitLevels": (1, 12),
        "minMaxBossLevels": (12, 12),
        "levelPool": (67, 67),
        "levelPoolMultipliers": (1, 1, 1, 1, 1),
        "revives": False
    },
    {                                   # Field Office 1 (10)
        "minMaxFloors": (1, 1),
        "minMaxSuitLevels": (8, 12),
        "minMaxBossLevels": (12, 12),
        "levelPool": (100, 100),
        "levelPoolMultipliers": (1, 1, 1, 1, 1),
        "revives": False
    },
    {                                   # Field Office 2 (11)
        "minMaxFloors": (1, 1),
        "minMaxSuitLevels": (1, 12),
        "minMaxBossLevels": (12, 12),
        "levelPool": (100, 100),
        "levelPoolMultipliers": (1, 1, 1, 1, 1),
        "revives": False
    },
    {                                   # Field Office 3 (12)
        "minMaxFloors": (1, 1),
        "minMaxSuitLevels": (8, 12),
        "minMaxBossLevels": (12, 12),
        "levelPool": (150, 150),
        "levelPoolMultipliers": (1, 1, 1, 1, 1),
        "revives": False
    },
    {                                   # Field Office 4 (13)
        "minMaxFloors": (1, 1),
        "minMaxSuitLevels": (8, 12),
        "minMaxBossLevels": (12, 12),
        "levelPool": (275, 275),
        "levelPoolMultipliers": (1, 1, 1, 1, 1),
        "revives": False
    },
    {                                   # Field Office 5 (14)
        "minMaxFloors": (1, 1),
        "minMaxSuitLevels": (9, 12),
        "minMaxBossLevels": (12, 12),
        "levelPool": (206, 206),
        "levelPoolMultipliers": (1, 1, 1, 1, 1),
        "revives": True
    },
    {                                   # Field Office 6 (15)
        "minMaxFloors": (1, 1),
        "minMaxSuitLevels": (1, 5),
        "minMaxBossLevels": (5, 5),
        "levelPool": (33, 33),
        "levelPoolMultipliers": (1, 1, 1, 1, 1),
        "revives": True
    },
    {                                   # Field Office 7 (16)
        "minMaxFloors": (1, 1),
        "minMaxSuitLevels": (4, 5),
        "minMaxBossLevels": (5, 5),
        "levelPool": (50, 50),
        "levelPoolMultipliers": (1, 1, 1, 1, 1),
        "revives": True
    },
)
VICTORY_RUN_TIME = ElevatorData[ELEVATOR_NORMAL]['openTime'] + TOON_VICTORY_EXIT_TIME
TO_TOON_BLDG_TIME = 8
VICTORY_SEQUENCE_TIME = VICTORY_RUN_TIME + TO_TOON_BLDG_TIME
CLEAR_OUT_TOON_BLDG_TIME = 4
TO_SUIT_BLDG_TIME = 8
