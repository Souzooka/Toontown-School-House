from otp.otpbase import OTPGlobals
from otp.ai import BanManagerAI
from toontown.toonbase import ToontownGlobals
from toontown.hood import ZoneUtil

def canAccess(avatarId, zoneId, function = ''):
    avatar = simbase.air.doId2do.get(avatarId)
    if avatar and avatar.getGameAccess() != OTPGlobals.AccessFull and not openToAll(zoneId, avatar):
        if cmp(function, 'DistributedBoardingPartyAI.checkBoard') == 0:
            return False
        simbase.air.writeServerEvent('suspicious', avatarId, 'User with rights: %s requesting enter for paid access content without proper rights in zone %s from %s' % (avatar.getGameAccess(), zoneId, function))
        if simbase.config.GetBool('want-ban-ispaid', True):
            commentStr = 'User with rights: %s tried to gain access zone %s from function %s, an area they were not allowed to using TTInjector Hack' % (avatar.getGameAccess(), zoneId, function)
            dislId = avatar.DISLid
            simbase.air.banManager.ban(avatarId, dislId, commentStr)
        return False
    else:
        return True


def openToAll(zoneId, avatar):
    allowed = False
    canonicalZoneId = ZoneUtil.getCanonicalHoodId(zoneId)
    allowedZones = [ToontownGlobals.Zones.ToontownCentral,
     ToontownGlobals.Zones.MyEstate,
     ToontownGlobals.Zones.GoofySpeedway,
     ToontownGlobals.Zones.Tutorial]
    specialZones = [ToontownGlobals.Zones.SellbotLobby]
    if ToontownGlobals.Holidays.SellbotNerfHoliday in simbase.air.holidayManager.currentHolidays:
        specialZones.append(ToontownGlobals.Zones.SellbotHQ)
    ownerId = simbase.air.estateMgr.getOwnerFromZone(zoneId)
    if ownerId:
        for zone in simbase.air.estateMgr.getEstateZones(ownerId):
            specialZones.append(zone)

    if canonicalZoneId in allowedZones or avatar.isInEstate():
        allowed = True
    elif zoneId in specialZones:
        allowed = True
    elif canonicalZoneId >= ToontownGlobals.Zones.DynamicZonesBegin and not avatar.getTutorialAck():
        zoneDict = simbase.air.tutorialManager.playerDict.get(avatar.doId)
        if zoneDict:
            allowed = True
    return allowed


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
