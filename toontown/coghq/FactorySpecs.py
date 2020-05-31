from toontown.toonbase import ToontownGlobals
import SellbotLegFactorySpec
import SellbotLegFactoryCogs
import LawbotLegFactorySpec
import LawbotLegFactoryCogs

def getFactorySpecModule(factoryId):
    return FactorySpecModules[factoryId]


def getCogSpecModule(factoryId):
    return CogSpecModules[factoryId]


FactorySpecModules = {ToontownGlobals.Zones.SellbotFactoryInt: SellbotLegFactorySpec,
 ToontownGlobals.Zones.LawbotOfficeInt: LawbotLegFactorySpec}
CogSpecModules = {ToontownGlobals.Zones.SellbotFactoryInt: SellbotLegFactoryCogs,
 ToontownGlobals.Zones.LawbotOfficeInt: LawbotLegFactoryCogs}
if __dev__:
    import FactoryMockupSpec
    FactorySpecModules[ToontownGlobals.Zones.MockupFactoryId] = FactoryMockupSpec
    import FactoryMockupCogs
    CogSpecModules[ToontownGlobals.Zones.MockupFactoryId] = FactoryMockupCogs
