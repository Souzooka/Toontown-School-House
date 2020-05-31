import math
from panda3d.core import Point3
from toontown.toonbase import ToontownGlobals
InputTimeout = 15
TireMovieTimeout = 120
MinWall = (-20.0, -15.0)
MaxWall = (20.0, 15.0)
TireRadius = 1.5
WallMargin = 1 + TireRadius
StartingPositions = (Point3(MinWall[0] + WallMargin, MinWall[1] + WallMargin, TireRadius),
 Point3(MaxWall[0] - WallMargin, MaxWall[1] - WallMargin, TireRadius),
 Point3(MinWall[0] + WallMargin, MaxWall[1] - WallMargin, TireRadius),
 Point3(MaxWall[0] - WallMargin, MinWall[1] + WallMargin, TireRadius))
NumMatches = 3
NumRounds = 2
PointsDeadCenter = {0: 5,
 1: 5,
 2: 5,
 3: 4,
 4: 3}
PointsInCorner = 1
FarthestLength = math.sqrt((MaxWall[0] - TireRadius) * (MaxWall[0] - TireRadius) + (MaxWall[1] - TireRadius) * (MaxWall[1] - TireRadius))
BonusPointsForPlace = (3,
 2,
 1,
 0)
ExpandFeetPerSec = 5
ScoreCountUpRate = 0.15
ShowScoresDuration = 4.0
NumTreasures = {ToontownGlobals.Zones.ToontownCentral: 2,
 ToontownGlobals.Zones.DonaldsDock: 2,
 ToontownGlobals.Zones.DaisyGardens: 2,
 ToontownGlobals.Zones.MinniesMelodyland: 2,
 ToontownGlobals.Zones.TheBrrrgh: 1,
 ToontownGlobals.Zones.DonaldsDreamland: 1}
NumPenalties = {ToontownGlobals.Zones.ToontownCentral: 0,
 ToontownGlobals.Zones.DonaldsDock: 1,
 ToontownGlobals.Zones.DaisyGardens: 1,
 ToontownGlobals.Zones.MinniesMelodyland: 1,
 ToontownGlobals.Zones.TheBrrrgh: 2,
 ToontownGlobals.Zones.DonaldsDreamland: 2}
Obstacles = {ToontownGlobals.Zones.ToontownCentral: (),
 ToontownGlobals.Zones.DonaldsDock: ((0, 0),),
 ToontownGlobals.Zones.DaisyGardens: ((MinWall[0] / 2, 0), (MaxWall[0] / 2, 0)),
 ToontownGlobals.Zones.MinniesMelodyland: ((0, MinWall[1] / 2), (0, MaxWall[1] / 2)),
 ToontownGlobals.Zones.TheBrrrgh: ((MinWall[0] / 2, 0),
                             (MaxWall[0] / 2, 0),
                             (0, MinWall[1] / 2),
                             (0, MaxWall[1] / 2)),
 ToontownGlobals.Zones.DonaldsDreamland: ((MinWall[0] / 2, MinWall[1] / 2),
                                    (MinWall[0] / 2, MaxWall[1] / 2),
                                    (MaxWall[0] / 2, MinWall[1] / 2),
                                    (MaxWall[0] / 2, MaxWall[1] / 2))}
ObstacleShapes = {ToontownGlobals.Zones.ToontownCentral: True,
 ToontownGlobals.Zones.DonaldsDock: True,
 ToontownGlobals.Zones.DaisyGardens: True,
 ToontownGlobals.Zones.MinniesMelodyland: True,
 ToontownGlobals.Zones.TheBrrrgh: False,
 ToontownGlobals.Zones.DonaldsDreamland: False}
