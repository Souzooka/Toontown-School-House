from otp.otpbase import OTPGlobals
from otp.ai import BanManagerAI
from toontown.toonbase import ToontownGlobals
from toontown.hood import ZoneUtil

def canWearSuit(avatarId, zoneId):
    canonicalZoneId = ZoneUtil.getCanonicalHoodId(zoneId)
    allowedSuitZones = [ToontownGlobals.Zones.LawbotHQ,
     ToontownGlobals.Zones.CashbotHQ,
     ToontownGlobals.Zones.SellbotHQ,
     ToontownGlobals.Zones.BossbotHQ]
    if canonicalZoneId in allowedSuitZones:
        return True
    elif zoneId >= ToontownGlobals.Zones.DynamicZonesBegin:
        return True
    else:
        return False
