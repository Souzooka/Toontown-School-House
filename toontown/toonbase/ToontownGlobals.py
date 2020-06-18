import TTLocalizer
from otp.otpbase.OTPGlobals import *
from direct.showbase.PythonUtil import Enum, invertDict
from panda3d.core import BitMask32, Vec4
from toontown.utility.Object import Object
import collections
MapHotkeyOn = 'alt'
MapHotkeyOff = 'alt-up'
MapHotkey = 'alt'
AccountDatabaseChannelId = 4008
ToonDatabaseChannelId = 4021
DoodleDatabaseChannelId = 4023
DefaultDatabaseChannelId = AccountDatabaseChannelId
DatabaseIdFromClassName = {'Account': AccountDatabaseChannelId}
CogHQCameraFov = 60.0
BossBattleCameraFov = 72.0
MakeAToonCameraFov = 52.0
CeilingBitmask = BitMask32(256)
FloorEventBitmask = BitMask32(16)
PieBitmask = BitMask32(256)
PetBitmask = BitMask32(8)
CatchGameBitmask = BitMask32(16)
CashbotBossObjectBitmask = BitMask32(16)
FurnitureSideBitmask = BitMask32(32)
FurnitureTopBitmask = BitMask32(64)
FurnitureDragBitmask = BitMask32(128)
PetLookatPetBitmask = BitMask32(256)
PetLookatNonPetBitmask = BitMask32(512)
BanquetTableBitmask = BitMask32(1024)
FullPies = 65535
CogHQCameraFar = 900.0
CogHQCameraNear = 1.0
CashbotHQCameraFar = 2000.0
CashbotHQCameraNear = 1.0
LawbotHQCameraFar = 3000.0
LawbotHQCameraNear = 1.0
BossbotHQCameraFar = 3000.0
BossbotHQCameraNear = 1.0
SpeedwayCameraFar = 8000.0
SpeedwayCameraNear = 1.0
MaxMailboxContents = 30
MaxHouseItems = 45
MaxAccessories = 50
ExtraDeletedItems = 5
DeletedItemLifetime = 7 * 24 * 60
CatalogNumWeeksPerSeries = 13
CatalogNumWeeks = 78
PetFloorCollPriority = 5
PetPanelProximityPriority = 6
P_NoTrunk = -28
P_AlreadyOwnBiggerCloset = -27
P_ItemAlreadyRented = -26
P_OnAwardOrderListFull = -25
P_AwardMailboxFull = -24
P_ItemInPetTricks = -23
P_ItemInMyPhrases = -22
P_ItemOnAwardOrder = -21
P_ItemInAwardMailbox = -20
P_ItemAlreadyWorn = -19
P_ItemInCloset = -18
P_ItemOnGiftOrder = -17
P_ItemOnOrder = -16
P_ItemInMailbox = -15
P_PartyNotFound = 14
P_WillNotFit = -13
P_NotAGift = -12
P_OnOrderListFull = -11
P_MailboxFull = -10
P_NoPurchaseMethod = -9
P_ReachedPurchaseLimit = -8
P_NoRoomForItem = -7
P_NotShopping = -6
P_NotAtMailbox = -5
P_NotInCatalog = -4
P_NotEnoughMoney = -3
P_InvalidIndex = -2
P_UserCancelled = -1
P_ItemAvailable = 1
P_ItemOnOrder = 2
P_ItemUnneeded = 3
GIFT_user = 0
GIFT_admin = 1
GIFT_RAT = 2
GIFT_mobile = 3
GIFT_cogs = 4
GIFT_partyrefund = 5
FM_InvalidItem = -7
FM_NondeletableItem = -6
FM_InvalidIndex = -5
FM_NotOwner = -4
FM_NotDirector = -3
FM_RoomFull = -2
FM_HouseFull = -1
FM_MovedItem = 1
FM_SwappedItem = 2
FM_DeletedItem = 3
FM_RecoveredItem = 4
SPDonaldsBoat = 3
SPMinniesPiano = 4
CEVirtual = 14
MaxHpLimit = 137
MaxCarryLimit = 80
MaxQuestCarryLimit = 4
MaxCogSuitLevel = 50 - 1
CogSuitHPLevels = (15 - 1, 20 - 1, 30 - 1, 40 - 1, 50 - 1)
setInterfaceFont(TTLocalizer.InterfaceFont)
setSignFont(TTLocalizer.SignFont)
from toontown.toontowngui import TTDialog
setDialogClasses(TTDialog.TTDialog, TTDialog.TTGlobalDialog)
ToonFont = None
BuildingNametagFont = None
MinnieFont = None
SuitFont = None

def getToonFont():
    global ToonFont
    if ToonFont == None:
        ToonFont = loader.loadFont(TTLocalizer.ToonFont, lineHeight=1.0)
    return ToonFont


def getBuildingNametagFont():
    global BuildingNametagFont
    if BuildingNametagFont == None:
        BuildingNametagFont = loader.loadFont(TTLocalizer.BuildingNametagFont)
    return BuildingNametagFont


def getMinnieFont():
    global MinnieFont
    if MinnieFont == None:
        MinnieFont = loader.loadFont(TTLocalizer.MinnieFont)
    return MinnieFont


def getSuitFont():
    global SuitFont
    if SuitFont == None:
        SuitFont = loader.loadFont(TTLocalizer.SuitFont, pixelsPerUnit=40, spaceAdvance=0.25, lineHeight=1.0)
    return SuitFont

Zones = Object(
    MockupFactoryId = 0,
    WelcomeValleyToken = 0,
    DonaldsDock = 1000,
    ToontownCentral = 2000,
    TheBrrrgh = 3000,
    MinniesMelodyland = 4000,
    DaisyGardens = 5000,
    OutdoorZone = 6000,
    FunnyFarm = 7000,
    GoofySpeedway = 8000,
    DonaldsDreamland = 9000,
    BarnacleBoulevard = 1100,
    SeaweedStreet = 1200,
    LighthouseLane = 1300,
    SillyStreet = 2100,
    LoopyLane = 2200,
    PunchlinePlace = 2300,
    WalrusWay = 3100,
    SleetStreet = 3200,
    PolarPlace = 3300,
    AltoAvenue = 4100,
    BaritoneBoulevard = 4200,
    TenorTerrace = 4300,
    ElmStreet = 5100,
    MapleStreet = 5200,
    OakStreet = 5300,
    LullabyLane = 9100,
    PajamaPlace = 9200,
    ToonHall = 2513,
    BossbotHQ = 10000,
    BossbotLobby = 10100,
    BossbotCountryClubIntA = 10500,
    BossbotCountryClubIntB = 10600,
    BossbotCountryClubIntC = 10700,
    BossbotHQEnd = 11000,
    SellbotHQ = 11000,
    SellbotLobby = 11100,
    SellbotFactoryExt = 11200,
    SellbotFactoryInt = 11500,
    SellbotHQEnd = 12000,
    CashbotHQ = 12000,
    CashbotLobby = 12100,
    CashbotMintIntA = 12500,
    CashbotMintIntB = 12600,
    CashbotMintIntC = 12700,
    CashbotHQEnd = 13000,
    LawbotHQ = 13000,
    LawbotLobby = 13100,
    LawbotOfficeExt = 13200,
    LawbotOfficeInt = 13300,
    LawbotStageIntA = 13300,
    LawbotStageIntB = 13400,
    LawbotStageIntC = 13500,
    LawbotStageIntD = 13600,
    LawbotHQEnd = 14000,
    Tutorial = 15000,
    MyEstate = 16000,
    GolfZone = 17000,
    PartyHood = 18000,
    HoodsAlwaysVisited = [17000, 18000],
    WelcomeValleyBegin = 22000,
    WelcomeValleyEnd = 61000,
    DynamicZonesBegin = 61000,
    DynamicZonesEnd = 1 << 20
)
HoodHierarchy = {
    Zones.ToontownCentral: (
        Zones.SillyStreet, 
        Zones.LoopyLane, 
        Zones.PunchlinePlace
    ),
    Zones.DonaldsDock: (
        Zones.BarnacleBoulevard, 
        Zones.SeaweedStreet, 
        Zones.LighthouseLane
    ),
    Zones.TheBrrrgh: (
        Zones.WalrusWay, 
        Zones.SleetStreet, 
        Zones.PolarPlace
    ),
    Zones.MinniesMelodyland: (
        Zones.AltoAvenue, 
        Zones.BaritoneBoulevard, 
        Zones.TenorTerrace
    ),
    Zones.DaisyGardens: (
        Zones.ElmStreet, 
        Zones.MapleStreet, 
        Zones.OakStreet
    ),
    Zones.DonaldsDreamland: (
        Zones.LullabyLane, 
        Zones.PajamaPlace
    ),
    Zones.GoofySpeedway: ()
}
cogDept2index = {'c': 0,
 'l': 1,
 'm': 2,
 's': 3}
cogIndex2dept = invertDict(cogDept2index)
HQToSafezone = {
    Zones.SellbotHQ: Zones.DaisyGardens,
    Zones.CashbotHQ: Zones.DonaldsDreamland,
    Zones.LawbotHQ: Zones.TheBrrrgh,
    Zones.BossbotHQ: Zones.DonaldsDock}
CogDeptNames = [TTLocalizer.Bossbot,
 TTLocalizer.Lawbot,
 TTLocalizer.Cashbot,
 TTLocalizer.Sellbot]

def cogHQZoneId2deptIndex(zone):
    if zone >= Zones.BossbotHQ and zone < Zones.BossbotHQEnd:
        return 0
    elif zone >= Zones.LawbotHQ and zone < Zones.LawbotHQEnd:
        return 1
    elif zone >= Zones.CashbotHQ and zone < Zones.CashbotHQEnd:
        return 2
    elif zone >= Zones.SellbotHQ and zone < Zones.SellbotHQEnd:
        return 3
    
    raise StandardError("zone %s is not part of a cog HQ", zone)


def cogHQZoneId2dept(zone):
    return cogIndex2dept[cogHQZoneId2deptIndex(zone)]


def dept2cogHQ(dept):
    dept2hq = {'c': Zones.BossbotHQ,
     'l': Zones.LawbotHQ,
     'm': Zones.CashbotHQ,
     's': Zones.SellbotHQ}
    return dept2hq[dept]

# CBHQ config
CashbotMintCogLevel = 10
CashbotMintSkelecogLevel = 11
CashbotMintBossLevel = 12
MintNumFloors = {
    Zones.CashbotMintIntA: 20,
    Zones.CashbotMintIntB: 20,
    Zones.CashbotMintIntC: 20
}
MintNumBattles = {
    Zones.CashbotMintIntA: 4,
    Zones.CashbotMintIntB: 6,
    Zones.CashbotMintIntC: 8
}
MintCogBuckRewards = {
    Zones.CashbotMintIntA: 8,
    Zones.CashbotMintIntB: 14,
    Zones.CashbotMintIntC: 20
}
MintNumRooms = {
    Zones.CashbotMintIntA: 2 * (6,) + 5 * (7,) + 5 * (8,) + 5 * (9,) + 3 * (10,),
    Zones.CashbotMintIntB: 3 * (8,) + 6 * (9,) + 6 * (10,) + 5 * (11,),
    Zones.CashbotMintIntC: 4 * (10,) + 10 * (11,) + 6 * (12,)
}

# BBHQ config
BossbotCountryClubCogLevel = 11
BossbotCountryClubSkelecogLevel = 12
BossbotCountryClubBossLevel = 12
CountryClubNumRooms = {
    Zones.BossbotCountryClubIntA: (4,),
    Zones.BossbotCountryClubIntB: 3 * (8,) + 6 * (9,) + 6 * (10,) + 5 * (11,),
    Zones.BossbotCountryClubIntC: 4 * (10,) + 10 * (11,) + 6 * (12,)
}
CountryClubNumBattles = {
    Zones.BossbotCountryClubIntA: 3,
    Zones.BossbotCountryClubIntB: 2,
    Zones.BossbotCountryClubIntC: 3
}
CountryClubCogBuckRewards = {
    Zones.BossbotCountryClubIntA: 8,
    Zones.BossbotCountryClubIntB: 14,
    Zones.BossbotCountryClubIntC: 20
}

# LBHQ config
LawbotStageCogLevel = 10
LawbotStageSkelecogLevel = 11
LawbotStageBossLevel = 12
StageNumBattles = {
    Zones.LawbotStageIntA: 0,
    Zones.LawbotStageIntB: 0,
    Zones.LawbotStageIntC: 0,
    Zones.LawbotStageIntD: 0
}
StageNoticeRewards = {
    Zones.LawbotStageIntA: 75,
    Zones.LawbotStageIntB: 150,
    Zones.LawbotStageIntC: 225,
    Zones.LawbotStageIntD: 300
}
StageNumRooms = {
    Zones.LawbotStageIntA: 2 * (6,) + 5 * (7,) + 5 * (8,) + 5 * (9,) + 3 * (10,),
    Zones.LawbotStageIntB: 3 * (8,) + 6 * (9,) + 6 * (10,) + 5 * (11,),
    Zones.LawbotStageIntC: 4 * (10,) + 10 * (11,) + 6 * (12,),
    Zones.LawbotStageIntD: 4 * (10,) + 10 * (11,) + 6 * (12,)
}


FT_FullSuit = 'fullSuit'
FT_Leg = 'leg'
FT_Arm = 'arm'
FT_Torso = 'torso'
factoryId2factoryType = {
    Zones.MockupFactoryId: FT_FullSuit,
    Zones.SellbotFactoryInt: FT_FullSuit,
    Zones.LawbotOfficeInt: FT_FullSuit}
StreetNames = TTLocalizer.GlobalStreetNames
StreetBranchZones = StreetNames.keys()
Hoods = (
    Zones.DonaldsDock,
    Zones.ToontownCentral,
    Zones.TheBrrrgh,
    Zones.MinniesMelodyland,
    Zones.DaisyGardens,
    Zones.OutdoorZone,
    Zones.FunnyFarm,
    Zones.GoofySpeedway,
    Zones.DonaldsDreamland,
    Zones.BossbotHQ,
    Zones.SellbotHQ,
    Zones.CashbotHQ,
    Zones.LawbotHQ,
    Zones.GolfZone
)
HoodsForTeleportAll = (
    Zones.DonaldsDock,
    Zones.ToontownCentral,
    Zones.TheBrrrgh,
    Zones.MinniesMelodyland,
    Zones.DaisyGardens,
    Zones.OutdoorZone,
    Zones.GoofySpeedway,
    Zones.DonaldsDreamland,
    Zones.BossbotHQ,
    Zones.SellbotHQ,
    Zones.CashbotHQ,
    Zones.LawbotHQ,
    Zones.GolfZone
)
NoPreviousGameId = 0
RaceGameId = 1
CannonGameId = 2
TagGameId = 3
PatternGameId = 4
RingGameId = 5
MazeGameId = 6
TugOfWarGameId = 7
CatchGameId = 8
DivingGameId = 9
TargetGameId = 10
PairingGameId = 11
VineGameId = 12
IceGameId = 13
CogThiefGameId = 14
TwoDGameId = 15
PhotoGameId = 16
TravelGameId = 100
MinigameNames = {
    'race': RaceGameId,
    'cannon': CannonGameId,
    'tag': TagGameId,
    'pattern': PatternGameId,
    'minnie': PatternGameId,
    'match': PatternGameId,
    'matching': PatternGameId,
    'ring': RingGameId,
    'maze': MazeGameId,
    'tug': TugOfWarGameId,
    'catch': CatchGameId,
    'diving': DivingGameId,
    'target': TargetGameId,
    'pairing': PairingGameId,
    'vine': VineGameId,
    'ice': IceGameId,
    'thief': CogThiefGameId,
    '2d': TwoDGameId,
    'photo': PhotoGameId,
    'travel': TravelGameId
}
MinigameTemplateId = -1
MinigameIDs = (
    RaceGameId,
    CannonGameId,
    TagGameId,
    PatternGameId,
    RingGameId,
    MazeGameId,
    TugOfWarGameId,
    CatchGameId,
    DivingGameId,
    TargetGameId,
    PairingGameId,
    VineGameId,
    IceGameId,
    CogThiefGameId,
    TwoDGameId,
    PhotoGameId,
    TravelGameId
)
MinigamePlayerMatrix = {1: (CannonGameId,
     RingGameId,
     MazeGameId,
     TugOfWarGameId,
     CatchGameId,
     DivingGameId,
     TargetGameId,
     PairingGameId,
     VineGameId,
     CogThiefGameId,
     TwoDGameId),
 2: (CannonGameId,
     PatternGameId,
     RingGameId,
     TagGameId,
     MazeGameId,
     TugOfWarGameId,
     CatchGameId,
     DivingGameId,
     TargetGameId,
     PairingGameId,
     VineGameId,
     IceGameId,
     CogThiefGameId,
     TwoDGameId),
 3: (CannonGameId,
     PatternGameId,
     RingGameId,
     TagGameId,
     RaceGameId,
     MazeGameId,
     TugOfWarGameId,
     CatchGameId,
     DivingGameId,
     TargetGameId,
     PairingGameId,
     VineGameId,
     IceGameId,
     CogThiefGameId,
     TwoDGameId),
 4: (CannonGameId,
     PatternGameId,
     RingGameId,
     TagGameId,
     RaceGameId,
     MazeGameId,
     TugOfWarGameId,
     CatchGameId,
     DivingGameId,
     TargetGameId,
     PairingGameId,
     VineGameId,
     IceGameId,
     CogThiefGameId,
     TwoDGameId)}
MinigameReleaseDates = {
    IceGameId: (2008, 8, 5),
    PhotoGameId: (2008, 8, 13),
    TwoDGameId: (2008, 8, 20),
    CogThiefGameId: (2008, 8, 27)
}
KeyboardTimeout = 300

# Phase files in which assets for particular hoods can be found
phaseMap = {
    Zones.Tutorial: 4,
    Zones.ToontownCentral: 4,
    Zones.MyEstate: 5.5,
    Zones.DonaldsDock: 6,
    Zones.MinniesMelodyland: 6,
    Zones.GoofySpeedway: 6,
    Zones.TheBrrrgh: 8,
    Zones.DaisyGardens: 8,
    Zones.FunnyFarm: 8,
    Zones.DonaldsDreamland: 8,
    Zones.OutdoorZone: 8,
    Zones.BossbotHQ: 12,
    Zones.SellbotHQ: 9,
    Zones.CashbotHQ: 10,
    Zones.LawbotHQ: 11,
    Zones.GolfZone: 8,
    Zones.PartyHood: 13
}
# Phase files in which assets for particular streets can be found
streetPhaseMap = {
    Zones.ToontownCentral: 5,
    Zones.DonaldsDock: 6,
    Zones.MinniesMelodyland: 6,
    Zones.GoofySpeedway: 6,
    Zones.TheBrrrgh: 8,
    Zones.DaisyGardens: 8,
    Zones.FunnyFarm: 8,
    Zones.DonaldsDreamland: 8,
    Zones.OutdoorZone: 8,
    Zones.BossbotHQ: 12,
    Zones.SellbotHQ: 9,
    Zones.CashbotHQ: 10,
    Zones.LawbotHQ: 11,
    Zones.PartyHood: 13
}
dnaMap = {
    Zones.Tutorial: 'toontown_central',
    Zones.ToontownCentral: 'toontown_central',
    Zones.DonaldsDock: 'donalds_dock',
    Zones.MinniesMelodyland: 'minnies_melody_land',
    Zones.GoofySpeedway: 'goofy_speedway',
    Zones.TheBrrrgh: 'the_burrrgh',
    Zones.DaisyGardens: 'daisys_garden',
    Zones.FunnyFarm: 'not done yet',
    Zones.DonaldsDreamland: 'donalds_dreamland',
    Zones.OutdoorZone: 'outdoor_zone',
    Zones.BossbotHQ: 'cog_hq_bossbot',
    Zones.SellbotHQ: 'cog_hq_sellbot',
    Zones.CashbotHQ: 'cog_hq_cashbot',
    Zones.LawbotHQ: 'cog_hq_lawbot',
    Zones.GolfZone: 'golf_zone'
}
hoodNameMap = {
    Zones.DonaldsDock: TTLocalizer.DonaldsDock,
    Zones.ToontownCentral: TTLocalizer.ToontownCentral,
    Zones.TheBrrrgh: TTLocalizer.TheBrrrgh,
    Zones.MinniesMelodyland: TTLocalizer.MinniesMelodyland,
    Zones.DaisyGardens: TTLocalizer.DaisyGardens,
    Zones.OutdoorZone: TTLocalizer.OutdoorZone,
    Zones.FunnyFarm: TTLocalizer.FunnyFarm,
    Zones.GoofySpeedway: TTLocalizer.GoofySpeedway,
    Zones.DonaldsDreamland: TTLocalizer.DonaldsDreamland,
    Zones.BossbotHQ: TTLocalizer.BossbotHQ,
    Zones.SellbotHQ: TTLocalizer.SellbotHQ,
    Zones.CashbotHQ: TTLocalizer.CashbotHQ,
    Zones.LawbotHQ: TTLocalizer.LawbotHQ,
    Zones.Tutorial: TTLocalizer.Tutorial,
    Zones.MyEstate: TTLocalizer.MyEstate,
    Zones.GolfZone: TTLocalizer.GolfZone,
    Zones.PartyHood: TTLocalizer.PartyHood
}
safeZoneCountMap = {
    Zones.MyEstate: 8,
    Zones.Tutorial: 6,
    Zones.ToontownCentral: 6,
    Zones.DonaldsDock: 10,
    Zones.MinniesMelodyland: 5,
    Zones.GoofySpeedway: 500,
    Zones.TheBrrrgh: 8,
    Zones.DaisyGardens: 9,
    Zones.FunnyFarm: 500,
    Zones.DonaldsDreamland: 5,
    Zones.OutdoorZone: 500,
    Zones.GolfZone: 500,
    Zones.PartyHood: 500
}
townCountMap = {
    Zones.MyEstate: 8,
    Zones.Tutorial: 40,
    Zones.ToontownCentral: 37,
    Zones.DonaldsDock: 40,
    Zones.MinniesMelodyland: 40,
    Zones.GoofySpeedway: 40,
    Zones.TheBrrrgh: 40,
    Zones.DaisyGardens: 40,
    Zones.FunnyFarm: 40,
    Zones.DonaldsDreamland: 40,
    Zones.OutdoorZone: 40,
    Zones.PartyHood: 20
}
hoodCountMap = {
    Zones.MyEstate: 2,
    Zones.Tutorial: 2,
    Zones.ToontownCentral: 2,
    Zones.DonaldsDock: 2,
    Zones.MinniesMelodyland: 2,
    Zones.GoofySpeedway: 2,
    Zones.TheBrrrgh: 2,
    Zones.DaisyGardens: 2,
    Zones.FunnyFarm: 2,
    Zones.DonaldsDreamland: 2,
    Zones.OutdoorZone: 2,
    Zones.BossbotHQ: 2,
    Zones.SellbotHQ: 43,
    Zones.CashbotHQ: 2,
    Zones.LawbotHQ: 2,
    Zones.GolfZone: 2,
    Zones.PartyHood: 2
}
# Amount of building floors required to achieve a particular star above a toon's head
TrophyStarLevels = (10, 20, 30, 50, 75, 100)

# Colors of building stars
TrophyStarColors = (
    Vec4(0.9, 0.6, 0.2, 1), # Bronze Static
    Vec4(0.9, 0.6, 0.2, 1), # Bronze Spinning
    Vec4(0.8, 0.8, 0.8, 1), # Silver Static
    Vec4(0.8, 0.8, 0.8, 1), # Silver Spinning
    Vec4(1, 1, 0, 1),       # Gold Static
    Vec4(1, 1, 0, 1)        # Gold Spinning
)

# Speeds of various characters
NPCSpeed = {
    "mickey": 5.0,
    "vampireMickey": 1.15,
    "minnie": 3.2,
    "witchMinnie": 1.8,
    "donald": 3.68,
    "frankenDonald": 0.9,
    "daisy": 2.3,
    "goofy": 5.2,
    "superGoofy": 1.6,
    "pluto": 5.5,
    "westernPluto": 3.2,
    "chip": 3,
    "dale": 3.5,
    "suit": 4.8
}
DaleOrbitDistance = 3 # Distance at which Dale orbits Chip
PieCodeBossCog = 1
PieCodeNotBossCog = 2
PieCodeToon = 3
PieCodeBossInsides = 4
PieCodeDefensePan = 5
PieCodeProsecutionPan = 6
PieCodeLawyer = 7
PieCodeColors = {
    PieCodeBossCog: None,
    PieCodeNotBossCog: (0.8, 0.8, 0.8, 1),
    PieCodeToon: None
}
BossCogRollSpeed = 7.5
BossCogTurnSpeed = 20
BossCogTreadSpeed = 3.5
BossCogDizzy = 0
BossCogElectricFence = 1
BossCogSwatLeft = 2
BossCogSwatRight = 3
BossCogAreaAttack = 4
BossCogFrontAttack = 5
BossCogRecoverDizzyAttack = 6
BossCogDirectedAttack = 7
BossCogStrafeAttack = 8
BossCogNoAttack = 9
BossCogGoonZap = 10
BossCogSlowDirectedAttack = 11
BossCogDizzyNow = 12
BossCogGavelStomp = 13
BossCogGavelHandle = 14
BossCogLawyerAttack = 15
BossCogMoveAttack = 16
BossCogGolfAttack = 17
BossCogGolfAreaAttack = 18
BossCogGearDirectedAttack = 19
BossCogOvertimeAttack = 20
BossCogAttackTimes = {BossCogElectricFence: 0,
 BossCogSwatLeft: 5.5,
 BossCogSwatRight: 5.5,
 BossCogAreaAttack: 4.21,
 BossCogFrontAttack: 2.65,
 BossCogRecoverDizzyAttack: 5.1,
 BossCogDirectedAttack: 4.84,
 BossCogNoAttack: 6,
 BossCogSlowDirectedAttack: 7.84,
 BossCogMoveAttack: 3,
 BossCogGolfAttack: 6,
 BossCogGolfAreaAttack: 7,
 BossCogGearDirectedAttack: 4.84,
 BossCogOvertimeAttack: 5}
BossCogDamageLevels = {BossCogElectricFence: 1,
 BossCogSwatLeft: 5,
 BossCogSwatRight: 5,
 BossCogAreaAttack: 10,
 BossCogFrontAttack: 3,
 BossCogRecoverDizzyAttack: 3,
 BossCogDirectedAttack: 3,
 BossCogStrafeAttack: 2,
 BossCogGoonZap: 5,
 BossCogSlowDirectedAttack: 10,
 BossCogGavelStomp: 20,
 BossCogGavelHandle: 2,
 BossCogLawyerAttack: 5,
 BossCogMoveAttack: 20,
 BossCogGolfAttack: 15,
 BossCogGolfAreaAttack: 15,
 BossCogGearDirectedAttack: 15,
 BossCogOvertimeAttack: 10}
BossCogBattleAPosHpr = (0, -25, 0, 0, 0, 0)
BossCogBattleBPosHpr = (0, 25, 0, 180, 0, 0)
SellbotBossMaxDamage = 100
SellbotBossMaxDamageNerfed = 100
SellbotBossBattleOnePosHpr = (0, -35, 0, -90, 0, 0)
SellbotBossBattleTwoPosHpr = (0, 60, 18, -90, 0, 0)
SellbotBossBattleThreeHpr = (180, 0, 0)
SellbotBossBottomPos = (0, -110, -6.5)
SellbotBossDeathPos = (0, -175, -6.5)
SellbotBossDooberTurnPosA = (-20, -50, 0)
SellbotBossDooberTurnPosB = (20, -50, 0)
SellbotBossDooberTurnPosDown = (0, -50, 0)
SellbotBossDooberFlyPos = (0, -135, -6.5)
SellbotBossTopRampPosA = (-80, -35, 18)
SellbotBossTopRampTurnPosA = (-80, 10, 18)
SellbotBossP3PosA = (-50, 40, 18)
SellbotBossTopRampPosB = (80, -35, 18)
SellbotBossTopRampTurnPosB = (80, 10, 18)
SellbotBossP3PosB = (50, 60, 18)
CashbotBossMaxDamage = 500
CashbotBossOffstagePosHpr = (120, -195, 0, 0, 0, 0)
CashbotBossBattleOnePosHpr = (120, -230, 0, 90, 0, 0)
CashbotRTBattleOneStartPosHpr = (94, -220, 0, 110, 0, 0)
CashbotBossBattleThreePosHpr = (120, -315, 0, 180, 0, 0)
CashbotToonsBattleThreeStartPosHpr = [
    (105, -285, 0, 208, 0, 0),
    (136, -342, 0, 398, 0, 0),
    (105, -342, 0, 333, 0, 0),
    (135, -292, 0, 146, 0, 0),
    (93, -303, 0, 242, 0, 0),
    (144, -327, 0, 64, 0, 0),
    (145, -302, 0, 117, 0, 0),
    (93, -327, 0, -65, 0, 0)
]
CashbotBossSafePosHprs = [
    (120, -315, 30, 0, 0, 0),
    (77.2, -329.3, 0, -90, 0, 0),
    (77.1, -302.7, 0, -90, 0, 0),
    (165.7, -326.4, 0, 90, 0, 0),
    (165.5, -302.4, 0, 90, 0, 0),
    (107.8, -359.1, 0, 0, 0, 0),
    (133.9, -359.1, 0, 0, 0, 0),
    (107.0, -274.7, 0, 180, 0, 0),
    (134.2, -274.7, 0, 180, 0, 0)
]
CashbotBossCranePosHprs = [
    (97.4, -337.6, 0, -45, 0, 0),
    (97.4, -292.4, 0, -135, 0, 0),
    (142.6, -292.4, 0, 135, 0, 0),
    (142.6, -337.6, 0, 45, 0, 0)
]
CashbotBossToMagnetTime = 0.2
CashbotBossFromMagnetTime = 1
CashbotBossSafeKnockImpact = 0.5
CashbotBossSafeNewImpact = 0.0
CashbotBossGoonImpact = 0.1
CashbotBossKnockoutDamage = 15
TTWakeWaterHeight = -4.79
DDWakeWaterHeight = 1.669
EstateWakeWaterHeight = -.3
OZWakeWaterHeight = -0.5
WakeRunDelta = 0.1
WakeWalkDelta = 0.2
NoItems = 0
NewItems = 1
OldItems = 2
SuitInvasionState = Enum(["Begin", "Update", "End", "Bulletin"])
Holidays = Enum(
    [
        "NoHoliday",
        "February14Fireworks",
        "June22Fireworks",
        "July4Fireworks",
        "July14Fireworks",
        "October31Fireworks",
        "November19Fireworks",
        "NewYearsFireworks",
        "ComboFireworks",
        "ValentinesDay",
        "IdesOfMarch",
        "AprilFoolsCostumes",
        "TaxDayInvasion",
        "PreJuly4BigWigInvasion",
        "PreJuly4DownsizerInvasion",
        "BlackCatDay",
        "Halloween",
        "HalloweenCostumes",
        "HalloweenProps",
        "SpookyBlackCat",
        "SpookyCostumes",
        "SpookyProps",
        "TrickOrTreat",
        "WackyWinterCaroling",
        "WackyWinterDecorations",
        "WinterCaroling",
        "WinterDecorations",
        "BankUpgradeHoliday",
        "CircuitRacing",
        "CircuitRacingEvent",
        "CrashedLeaderboard",
        "ElectionPromotion",
        "ExpandedClosets",
        "FishBingoNight",
        "JellybeanDay",
        "JellyBeanFishingHoliday",
        "JellyBeanFishingHolidayMonth",
        "JellyBeanPartiesHoliday",
        "JellyBeanPartiesHolidayMonth",
        "JellyBeanTrolleyHoliday",
        "JellyBeanTrolleyHolidayMonth",
        "KartingTicketsHoliday",
        "KartRecordDailyReset",
        "KartRecordWeeklyReset",
        "MoreXPHoliday",
        "PolarPlaceEvent",
        "ResistanceEvent",
        "RoamingTrialerWeekend",
        "SillySaturdayBingo",
        "SillySaturdayCircuit",
        "SillySaturdayTrolley",
        "SellbotFieldOffice",
        "SellbotNerfHoliday",
        "TopToonsMarathon",
        "TrolleyHoliday",
        "TrolleyWeekend",
        "VictoryPartyHoliday",
        "SellbotSurprise1",
        "SellbotSurprise2",
        "SellbotSurprise3",
        "SellbotSurprise4",
        "CashbotConundrum1",
        "CashbotConundrum2",
        "CashbotConundrum3",
        "CashbotConundrum4",
        "LawbotGambit1",
        "LawbotGambit2",
        "LawbotGambit3",
        "LawbotGambit4",
        "TroubleBossbots1",
        "TroubleBossbots2",
        "TroubleBossbots3",
        "TroubleBossbots4",
        "SillyChatter1",
        "SillyChatter2",
        "SillyChatter3",
        "SillyChatter4",
        "SillyChatter5",
        "SillyTest",
        "SillyMeterHoliday",
        "SillyMeterExtHoliday",
        "SillySurgeHoliday",
        "HydrantZeroHoliday",
        "MailboxZeroHoliday",
        "TrashcanZeroHoliday",
        "HydrantsBuffBattles",
        "MailboxesBuffBattles",
        "TrashcansBuffBattles",
        "ColdCallerInvasion",
        "TelemarketerInvasion",
        "NameDropperInvasion",
        "GladHanderInvasion",
        "MoverAndShakerInvasion",
        "TwoFaceInvasion",
        "TheMinglerInvasion",
        "MrHollywoodInvasion",
        "ShortChangeInvasion",
        "PennyPincherInvasion",
        "TightwadInvasion",
        "BeanCounterInvasion",
        "NumberCruncherInvasion",
        "MoneyBagsInvasion",
        "LoanSharkInvasion",
        "RobberBaronInvasion",
        "BottomFeederInvasion",
        "BloodsuckerInvasion",
        "DoubleTalkerInvasion",
        "AmbulanceChaserInvasion",
        "BackStabberInvasion",
        "SpinDoctorInvasion",
        "LegalEagleInvasion",
        "BigWigInvasion",
        "FlunkyInvasion",
        "PencilPusherInvasion",
        "YesManInvasion",
        "MicromanagerInvasion",
        "DownsizerInvasion",
        "HeadHunterInvasion",
        "CorporateRaiderInvasion",
        "TheBigCheeseInvasion",
        "SellbotInvasion",
        "BossCogInvasion",
        "SkelecogInvasion",
        "MarchInvasion",
        "DecemberInvasion",
    ]
)
TOT_REWARD_JELLYBEAN_AMOUNT = 100
TOT_REWARD_END_OFFSET_AMOUNT = 0
LawbotBossMaxDamage = 2700
LawbotBossWinningTilt = 40
LawbotBossInitialDamage = 1350
LawbotBossBattleOnePosHpr = (-2.798, -60, 0, 0, 0, 0)
LawbotBossBattleTwoPosHpr = (-2.798, 89, 19.145, 0, 0, 0)
LawbotBossBattleThreePosHpr = LawbotBossBattleTwoPosHpr
LawbotBossTopRampPosA = (-80, -35, 18)
LawbotBossTopRampTurnPosA = (-80, 10, 18)
LawbotBossTopRampPosB = (80, -35, 18)
LawbotBossTopRampTurnPosB = (80, 10, 18)
LawbotBossP3PosA = (55, -9, 0)
LawbotBossP3PosB = (55, -9, 0)
LawbotBossBottomPos = (50, 39, 0)
LawbotBossDeathPos = (50, 40, 0)
LawbotBossGavelPosHprs = [
    (35, 78.328, 0, -135, 0, 0),
    (68.5, 78.328, 0, 135, 0, 0),
    (47, -33, 0, 45, 0, 0),
    (-50, -39, 0, -45, 0, 0),
    (-9, -37, 0, 0, 0, 0),
    (-9, 49, 0, -180, 0, 0),
    (32, 0, 0, 45, 0, 0),
    (33, 56, 0, 135, 0, 0)
]
LawbotBossGavelTimes = [
    (0.2, 0.9, 0.6),
    (0.25, 1, 0.5),
    (1.0, 6, 0.5),
    (0.3, 3, 1),
    (0.26, 0.9, 0.45),
    (0.24, 1.1, 0.65),
    (0.27, 1.2, 0.45),
    (0.25, 0.95, 0.5)
 ]
LawbotBossGavelHeadings = [
    (0, -15, 4, -70 - 45, 5, 45),
    (0, -45, -4, -35, -45, -16, 32),
    (0, -8, 19, -7, 5, 23),
    (0, -4, 8, -16, 32, -45, 7, 7, -30, 19, -13, 25),
    (0, -45, -90, 45, 90),
    (0, -45, -90, 45, 90),
    (0, -45, 45),
    (0, -45, 45)
]
LawbotBossCogRelBattleAPosHpr = (-25, -10, 0, 0, 0, 0)
LawbotBossCogRelBattleBPosHpr = (-25, 10, 0, 0, 0, 0)
LawbotBossCogAbsBattleAPosHpr = (-5, -2, 0, 0, 0, 0)
LawbotBossCogAbsBattleBPosHpr = (-5, 0, 0, 0, 0, 0)
LawbotBossWitnessStandPosHpr = (54, 100, 0, -90, 0, 0)
LawbotBossInjusticePosHpr = (-3, 12, 0, 90, 0, 0)
LawbotBossInjusticeScale = (1.75, 1.75, 1.5)
LawbotBossDefensePanDamage = 1
LawbotBossLawyerPosHprs = [
    (-57, -24, 0, -90, 0, 0),
    (-57, -12, 0, -90, 0, 0),
    (-57, 0, 0, -90, 0, 0),
    (-57, 12, 0, -90, 0, 0),
    (-57, 24, 0, -90, 0, 0),
    (-57, 36, 0, -90, 0, 0),
    (-57, 48, 0, -90, 0, 0),
    (-57, 60, 0, -90, 0, 0),
    (-3, -37.3, 0, 0, 0, 0),
    (-3, 53, 0, -180, 0, 0)
]
LawbotBossLawyerCycleTime = 6
LawbotBossLawyerToPanTime = 2.5
LawbotBossLawyerChanceToAttack = 50
LawbotBossLawyerHeal = 2
LawbotBossLawyerStunTime = 5
LawbotBossDifficultySettings = [
    (38, 4, 8, 1, 0, 0),
    (36, 5, 8, 1, 0, 0),
    (34, 5, 8, 1, 0, 0),
    (32, 6, 8, 2, 0, 0),
    (30, 6, 8, 2, 0, 0),
    (28, 7, 8, 3, 0, 0),
    (26, 7, 9, 3, 1, 1),
    (24, 8, 9, 4, 1, 1),
    (22, 8, 10, 4, 1, 0)
]
LawbotBossCannonPosHprs = [
    (-40, -12, 0, -90, 0, 0),
    (-40, 0, 0, -90, 0, 0),
    (-40, 12, 0, -90, 0, 0),
    (-40, 24, 0, -90, 0, 0),
    (-40, 36, 0, -90, 0, 0),
    (-40, 48, 0, -90, 0, 0),
    (-40, 60, 0, -90, 0, 0),
    (-40, 72, 0, -90, 0, 0)]
LawbotBossCannonPosA = (-80, -51.48, 0)
LawbotBossCannonPosB = (-80, 70.73, 0)
LawbotBossChairPosHprs = [
    (60, 72, 0, -90, 0, 0),
    (60, 62, 0, -90, 0, 0),
    (60, 52, 0, -90, 0, 0),
    (60, 42, 0, -90, 0, 0),
    (60, 32, 0, -90, 0, 0),
    (60, 22, 0, -90, 0, 0),
    (70, 72, 5, -90, 0, 0),
    (70, 62, 5, -90, 0, 0),
    (70, 52, 5, -90, 0, 0),
    (70, 42, 5, -90, 0, 0),
    (70, 32, 5, -90, 0, 0),
    (70, 22, 5, -90, 0, 0)
]
LawbotBossChairRow1PosB = (59.3, 48, 14.05)
LawbotBossChairRow1PosA = (59.3, -18.2, 14.05)
LawbotBossChairRow2PosB = (75.1, 48, 28.2)
LawbotBossChairRow2PosA = (75.1, -18.2, 28.2)
LawbotBossCannonBallMax = 12
LawbotBossJuryBoxStartPos = (94, -8, 5)
LawbotBossJuryBoxRelativeEndPos = (30, 0, 12.645)
LawbotBossJuryBoxMoveTime = 70
LawbotBossJurorsForBalancedScale = 8
LawbotBossDamagePerJuror = 68
LawbotBossCogJurorFlightTime = 10
LawbotBossCogJurorDistance = 75
LawbotBossBaseJurorNpcId = 2001
LawbotBossWitnessEpiloguePosHpr = (-3, 0, 0, 180, 0, 0)
LawbotBossChanceForTaunt = 25
LawbotBossBonusWaitTime = 60
LawbotBossBonusDuration = 20
LawbotBossBonusToonup = 10
LawbotBossBonusWeightMultiplier = 2
LawbotBossChanceToDoAreaAttack = 11
LOW_POP_JP = 0
MID_POP_JP = 100
HIGH_POP_JP = 200
LOW_POP_INTL = 399
MID_POP_INTL = 499
HIGH_POP_INTL = -1
LOW_POP = 399
MID_POP = 599
HIGH_POP = -1
PinballCannonBumper = 0
PinballCloudBumperLow = 1
PinballCloudBumperMed = 2
PinballCloudBumperHigh = 3
PinballTarget = 4
PinballRoof = 5
PinballHouse = 6
PinballFence = 7
PinballBridge = 8
PinballStatuary = 9
PinballScoring = [(100, 1),
 (150, 1),
 (200, 1),
 (250, 1),
 (350, 1),
 (100, 1),
 (50, 1),
 (25, 1),
 (100, 1),
 (10, 1)]
PinballCannonBumperInitialPos = (0, -20, 40)
RentalCop = 0
RentalCannon = 1
RentalGameTable = 2
GlitchKillerZones = [13300, 13400, 13500, 13600]
ColorPlayer = (0.3, 0.7, 0.3, 1)
ColorAvatar = (0.3, 0.3, 0.7, 1)
ColorPet = (0.6, 0.4, 0.2, 1)
ColorFreeChat = (0.3, 0.3, 0.8, 1)
ColorSpeedChat = (0.2, 0.6, 0.4, 1)
ColorNoChat = (0.8, 0.5, 0.1, 1)
FactoryLaffMinimums = [(0, 31),
 (0, 66, 71),
 (0, 81, 86, 96),
 (0, 101, 106)]
PICNIC_COUNTDOWN_TIME = 60
BossbotRTIntroStartPosHpr = (0, -64, 0, 180, 0, 0)
BossbotRTPreTwoPosHpr = (0, -20, 0, 180, 0, 0)
BossbotRTEpiloguePosHpr = (0, 90, 0, 180, 0, 0)
BossbotBossBattleOnePosHpr = (0, 355, 0, 0, 0, 0)
BossbotBossPreTwoPosHpr = (0, 20, 0, 0, 0, 0)
BossbotElevCamPosHpr = (0, -100.544, 7.18258, 0, 0, 0)
BossbotFoodModelScale = 0.75
BossbotNumFoodToExplode = 3
BossbotBossServingDuration = 300
BossbotPrepareBattleThreeDuration = 20
WaiterBattleAPosHpr = (20, -400, 0, 0, 0, 0)
WaiterBattleBPosHpr = (-20, -400, 0, 0, 0, 0)
BossbotBossBattleThreePosHpr = (0, 355, 0, 0, 0, 0)
DinerBattleAPosHpr = (20, -240, 0, 0, 0, 0)
DinerBattleBPosHpr = (-20, -240, 0, 0, 0, 0)
BossbotBossMaxDamage = 500
BossbotMaxSpeedDamage = 90
BossbotSpeedRecoverRate = 20
BossbotBossDifficultySettings = [
    (8, 4, 11, 3, 30, 25),
    (9, 5, 12, 6, 28, 26),
    (10, 6, 11, 7, 26, 27),
    (8, 8, 12, 8, 24, 28),
    (13, 5, 12, 9, 22, 29)]
BossbotRollSpeedMax = 22
BossbotRollSpeedMin = 7.5
BossbotTurnSpeedMax = 60
BossbotTurnSpeedMin = 20
BossbotTreadSpeedMax = 10.5
BossbotTreadSpeedMin = 3.5
CalendarFilterShowAll = 0
CalendarFilterShowOnlyHolidays = 1
CalendarFilterShowOnlyParties = 2
TTC = 1
DD = 2
MM = 3
GS = 4
DG = 5
BR = 6
OZ = 7
DL = 8
DefaultWantNewsPageSetting = 1
gmMagicWordList = [
    'restock',
    'restockUber',
    'autoRestock',
    'resistanceRestock',
    'restockSummons',
    'uberDrop',
    'rich',
    'maxBankMoney',
    'toonUp',
    'rod',
    'cogPageFull',
    'pinkSlips',
    'Tickets',
    'newSummons',
    'who',
    'who all'
]
NewsPageScaleAdjust = 0.85
AnimPropTypes = Enum(('Unknown', 'Hydrant', 'Mailbox', 'Trashcan'), start=-1)
EmblemTypes = Enum(('Silver', 'Gold'))
NumEmblemTypes = 2
DefaultMaxBankMoney = 12000
DefaultBankItemId = 1350
ToonAnimStates = set(['off',
    'neutral',
    'victory',
    'Happy',
    'Sad',
    'Catching',
    'CatchEating',
    'Sleep',
    'walk',
    'jumpSquat',
    'jump',
    'jumpAirborne',
    'jumpLand',
    'run',
    'swim',
    'swimhold',
    'dive',
    'cringe',
    'OpenBook',
    'ReadBook',
    'CloseBook',
    'TeleportOut',
    'Died',
    'TeleportedOut',
    'TeleportIn',
    'Emote',
    'SitStart',
    'Sit',
    'Push',
    'Squish',
    'FallDown',
    'GolfPuttLoop',
    'GolfRotateLeft',
    'GolfRotateRight',
    'GolfPuttSwing',
    'GolfGoodPutt',
    'GolfBadPutt',
    'Flattened',
    'CogThiefRunning',
    'ScientistJealous',
    'ScientistEmcee',
    'ScientistWork',
    'ScientistLessWork',
    'ScientistPlay'
 ])
AV_FLAG_REASON_TOUCH = 1
AV_FLAG_HISTORY_LEN = 500
AV_TOUCH_CHECK_DELAY_AI = 3.0
AV_TOUCH_CHECK_DELAY_CL = 1.0
AV_TOUCH_CHECK_DIST = 2.0
AV_TOUCH_CHECK_DIST_Z = 5.0
AV_TOUCH_CHECK_TIMELIMIT_CL = 0.002
AV_TOUCH_COUNT_LIMIT = 5
AV_TOUCH_COUNT_TIME = 300
SuitLevels = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
GravityValue = 32.174
hood2Id = [
    ('TTC', (Zones.ToontownCentral,)),
    ('DD', (Zones.DonaldsDock,)),
    ('MML', (Zones.MinniesMelodyland,)),
    ('DG', (Zones.DaisyGardens,)),
    ('TB', (Zones.TheBrrrgh,)),
    ('DDL', (Zones.DonaldsDreamland,)),
    ('GZ', (Zones.GolfZone,)),
    ('GSW', (Zones.GoofySpeedway,)),
    ('GS', (Zones.GoofySpeedway,)),
    ('OZ', (Zones.OutdoorZone,)),
    ('CEO', (Zones.BossbotHQ,)),
    ('CJ', (Zones.LawbotHQ,)),
    ('CFO', (Zones.CashbotHQ,)),
    ('VP', (Zones.SellbotHQ,)),
    ('BBHQ', (Zones.BossbotHQ,)),
    ('LBHQ', (Zones.LawbotHQ,)),
    ('CBHQ', (Zones.CashbotHQ,)),
    ('SBHQ', (Zones.SellbotHQ,)),
    ('FACTORY', (Zones.SellbotHQ, Zones.SellbotFactoryExt)),
    ('FRONTENTRY', (Zones.SellbotHQ, Zones.SellbotFactoryExt)),
    ('SIDEENTRY', (Zones.SellbotHQ, Zones.SellbotFactoryExt)),
    ('BULLION', (Zones.CashbotHQ,)),
    ('DOLLAR', (Zones.CashbotHQ,)),
    ('COIN', (Zones.CashbotHQ,)),
    ('OFFICEA', (Zones.LawbotHQ, Zones.LawbotOfficeExt)),
    ('OFFICEB', (Zones.LawbotHQ, Zones.LawbotOfficeExt)),
    ('OFFICEC', (Zones.LawbotHQ, Zones.LawbotOfficeExt)),
    ('OFFICED', (Zones.LawbotHQ, Zones.LawbotOfficeExt)),
    ('BACK', (Zones.BossbotHQ,)),
    ('MIDDLE', (Zones.BossbotHQ,)),
    ('FRONT', (Zones.BossbotHQ,))]
hood2Id = collections.OrderedDict(hood2Id)
hood2Coords = {
    'CEO': [(61.044, 119.014, 0.025, -4.680, 0, 0)],
    'CJ': [(333.700, -179.869, -42.932, -807.174, 0, 0)],
    'CFO': [(125.155, 546.084, 32.246, 360.056, 0, 0)],
    'VP': [(25.512, -51.193, 10.095, 40.868, 0, 0)],
    'FACTORY': [(62.204, -89.739, 0.025, -7.144, 0, 0)],
    'FRONTENTRY': [(62.204, -89.739, 0.025, -7.144, 0, 0)],
    'SIDEENTRY': [(-165.940, 26.804, 0.025, -97.144, 0, 0)],
    'BULLION': [(-118.641, 64.131, -23.434, 449.182, 0, 0)],
    'DOLLAR': [(178.612, -175.786, -63.244, 274.225, 0, 0)],
    'COIN': [(-122.43, -428.856, -23.439, 450.141, 0, 0)],
    'OFFICE': [(-170.371, -191.902, -16.280, -633.031, 0, 0)],
    'OFFICEA': [(47.594, 78.874, 51.692, -35, 0, 0)],
    'OFFICEB': [(94.816, 78.874, 51.692, -15, 0, 0)],
    'OFFICEC': [(137.586, 78.874, 51.692, 15, 0, 0)],
    'OFFICED': [(178.331, 78.874, 51.692, 35, 0, 0)],
    'BACK': [(-73.911, 87.426, 11.803, 10.170, 0, 0)],
    'MIDDLE': [(-98.805, 39.180, 11.364, -253.350, 0, 0)],
    'FRONT': [(-105.626, -33.441, 9.777, -211.885, 0, 0)]
}
