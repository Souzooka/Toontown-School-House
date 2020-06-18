from panda3d.core import *
from panda3d.toontown import *
import random
import string
from direct.directnotify import DirectNotifyGlobal
from toontown.hood import ZoneUtil
from toontown.toonbase import ToontownGlobals
from toontown.toonbase import ToontownBattleGlobals
from toontown.hood import HoodUtil
from toontown.building import SuitBuildingGlobals

class SuitPlannerBase:
    notify = DirectNotifyGlobal.directNotify.newCategory('SuitPlannerBase')

    # This information is shown when the map is opened,
    # and is the same as the data in DistributedSuitPlannerAI
    # Probably better to get this info from the server
    # than to duplicate it
    SuitFrequencies = (
        {
            "zone": ToontownGlobals.Zones.SillyStreet,
            "tracks": (25, 25, 25, 25)
        },
        {
            "zone": ToontownGlobals.Zones.LoopyLane,
            "tracks": (10, 70, 10, 10)
        },
        {
            "zone": ToontownGlobals.Zones.PunchlinePlace,
            "tracks": (10, 10, 40, 40)
        },
        {
            "zone": ToontownGlobals.Zones.BarnacleBoulevard,
            "tracks": (90, 10, 0, 0)
        },
        {
            "zone": ToontownGlobals.Zones.SeaweedStreet,
            "tracks": (0, 0, 90, 10)
        },
        {
            "zone": ToontownGlobals.Zones.LighthouseLane,
            "tracks": (40, 40, 10, 10)
        },
        {
            "zone": ToontownGlobals.Zones.WalrusWay,
            "tracks": (90, 10, 0, 0)
        },
        {
            "zone": ToontownGlobals.Zones.SleetStreet,
            "tracks": (10, 20, 30, 40)
        },
        {
            "zone": ToontownGlobals.Zones.PolarPlace,
            "tracks": (5, 85, 5, 5)
        },
        {
            "zone": ToontownGlobals.Zones.AltoAvenue,
            "tracks": (0, 0, 50, 50)
        },
        {
            "zone": ToontownGlobals.Zones.BaritoneBoulevard,
            "tracks": (0, 0, 90, 10)
        },
        {
            "zone": ToontownGlobals.Zones.TenorTerrace,
            "tracks": (50, 50, 0, 0)
        },
        {
            "zone": ToontownGlobals.Zones.ElmStreet,
            "tracks": (0, 20, 10, 70)
        },
        {
            "zone": ToontownGlobals.Zones.MapleStreet,
            "tracks": (10, 70, 0, 20)
        },
        {
            "zone": ToontownGlobals.Zones.OakStreet,
            "tracks": (5, 5, 5, 85)
        },
        {
            "zone": ToontownGlobals.Zones.LullabyLane,
            "tracks": (25, 25, 25, 25)
        },
        {
            "zone": ToontownGlobals.Zones.PajamaPlace,
            "tracks": (5, 5, 85, 5)
        },
    )
    
    def __init__(self):
        self.suitWalkSpeed = ToontownGlobals.NPCSpeed["suit"]
        self.dnaStore = None
        self.pointIndexes = {}
        return

    def setupDNA(self):
        if self.dnaStore:
            return None
        self.dnaStore = DNAStorage()
        dnaFileName = self.genDNAFileName()
        try:
            simbase.air.loadDNAFileAI(self.dnaStore, dnaFileName)
        except:
            loader.loadDNAFileAI(self.dnaStore, dnaFileName)

        self.initDNAInfo()
        return None

    def genDNAFileName(self):
        try:
            return simbase.air.genDNAFileName(self.getZoneId())
        except:
            zoneId = ZoneUtil.getCanonicalZoneId(self.getZoneId())
            hoodId = ZoneUtil.getCanonicalHoodId(zoneId)
            hood = ToontownGlobals.dnaMap[hoodId]
            phase = ToontownGlobals.streetPhaseMap[hoodId]
            if hoodId == zoneId:
                zoneId = 'sz'
            return 'phase_%s/dna/%s_%s.dna' % (phase, hood, zoneId)

    def getZoneId(self):
        return self.zoneId

    def setZoneId(self, zoneId):
        self.notify.debug('setting zone id for suit planner')
        self.zoneId = zoneId
        self.setupDNA()

    def extractGroupName(self, groupFullName):
        return str(groupFullName).split(':', 1)[0]

    def initDNAInfo(self):
        numGraphs = self.dnaStore.discoverContinuity()
        if numGraphs != 1:
            self.notify.info('zone %s has %s disconnected suit paths.' % (self.zoneId, numGraphs))
        self.battlePosDict = {}
        self.cellToGagBonusDict = {}
        for i in xrange(self.dnaStore.getNumDNAVisGroupsAI()):
            vg = self.dnaStore.getDNAVisGroupAI(i)
            zoneId = int(self.extractGroupName(vg.getName()))
            if vg.getNumBattleCells() == 1:
                battleCell = vg.getBattleCell(0)
                self.battlePosDict[zoneId] = vg.getBattleCell(0).getPos()
            elif vg.getNumBattleCells() > 1:
                self.notify.warning('multiple battle cells for zone: %d' % zoneId)
                self.battlePosDict[zoneId] = vg.getBattleCell(0).getPos()
            if True:
                for i in xrange(vg.getNumChildren()):
                    childDnaGroup = vg.at(i)
                    if isinstance(childDnaGroup, DNAInteractiveProp):
                        self.notify.debug('got interactive prop %s' % childDnaGroup)
                        battleCellId = childDnaGroup.getCellId()
                        if battleCellId == -1:
                            self.notify.warning('interactive prop %s  at %s not associated with a a battle' % (childDnaGroup, zoneId))
                        elif battleCellId == 0:
                            if zoneId in self.cellToGagBonusDict:
                                self.notify.error('FIXME battle cell at zone %s has two props %s %s linked to it' % (zoneId, self.cellToGagBonusDict[zoneId], childDnaGroup))
                            else:
                                name = childDnaGroup.getName()
                                propType = HoodUtil.calcPropType(name)
                                if propType in ToontownBattleGlobals.PropTypeToTrackBonus:
                                    trackBonus = ToontownBattleGlobals.PropTypeToTrackBonus[propType]
                                    self.cellToGagBonusDict[zoneId] = trackBonus

        self.dnaStore.resetDNAGroups()
        self.dnaStore.resetDNAVisGroups()
        self.dnaStore.resetDNAVisGroupsAI()
        self.streetPointList = []
        self.frontdoorPointList = []
        self.sidedoorPointList = []
        self.cogHQDoorPointList = []
        numPoints = self.dnaStore.getNumSuitPoints()
        for i in xrange(numPoints):
            point = self.dnaStore.getSuitPointAtIndex(i)
            if point.getPointType() == DNASuitPoint.FRONTDOORPOINT:
                self.frontdoorPointList.append(point)
            elif point.getPointType() == DNASuitPoint.SIDEDOORPOINT:
                self.sidedoorPointList.append(point)
            elif point.getPointType() == DNASuitPoint.COGHQINPOINT or point.getPointType() == DNASuitPoint.COGHQOUTPOINT:
                self.cogHQDoorPointList.append(point)
            else:
                self.streetPointList.append(point)
            self.pointIndexes[point.getIndex()] = point

        return None

    def performPathTest(self):
        if not self.notify.getDebug():
            return None
        startAndEnd = self.pickPath()
        if not startAndEnd:
            return None
        startPoint = startAndEnd[0]
        endPoint = startAndEnd[1]
        path = self.dnaStore.getSuitPath(startPoint, endPoint)
        numPathPoints = path.getNumPoints()
        for i in xrange(numPathPoints - 1):
            zone = self.dnaStore.getSuitEdgeZone(path.getPointIndex(i), path.getPointIndex(i + 1))
            travelTime = self.dnaStore.getSuitEdgeTravelTime(path.getPointIndex(i), path.getPointIndex(i + 1), self.suitWalkSpeed)
            self.notify.debug('edge from point ' + `i` + ' to point ' + `(i + 1)` + ' is in zone: ' + `zone` + ' and will take ' + `travelTime` + ' seconds to walk.')

        return None

    def genPath(self, startPoint, endPoint, minPathLen, maxPathLen):
        return self.dnaStore.getSuitPath(startPoint, endPoint, minPathLen, maxPathLen)

    def getDnaStore(self):
        return self.dnaStore
