from toontown.toonbase import TTLocalizer
from toontown.toonbase import ToontownGlobals
GREETING = 0
COMMENT = 1
GOODBYE = 2
DaisyChatter = TTLocalizer.DaisyChatter
MickeyChatter = TTLocalizer.MickeyChatter
VampireMickeyChatter = TTLocalizer.VampireMickeyChatter
MinnieChatter = TTLocalizer.MinnieChatter
GoofyChatter = TTLocalizer.GoofyChatter
GoofySpeedwayChatter = TTLocalizer.GoofySpeedwayChatter
DonaldChatter = TTLocalizer.DonaldChatter
ChipChatter = TTLocalizer.ChipChatter
DaleChatter = TTLocalizer.DaleChatter

def getExtendedChat(chatset, extendedChat):
    newChat = []
    for chatList in chatset:
        newChat.append(list(chatList))

    newChat[1] += extendedChat
    return newChat


def getChatter(charName, chatterType):
    if charName == TTLocalizer.Mickey:
        if chatterType == ToontownGlobals.Holidays.AprilFoolsCostumes:
            return TTLocalizer.AFMickeyChatter
        elif chatterType == ToontownGlobals.Holidays.WinterCaroling:
            return TTLocalizer.WinterMickeyCChatter
        elif chatterType == ToontownGlobals.Holidays.WinterDecorations:
            return TTLocalizer.WinterMickeyDChatter
        elif chatterType == ToontownGlobals.Holidays.WackyWinterCaroling:
            return TTLocalizer.WinterMickeyCChatter
        elif chatterType == ToontownGlobals.Holidays.WackyWinterDecorations:
            return TTLocalizer.WinterMickeyDChatter
        elif chatterType == ToontownGlobals.Holidays.ValentinesDay:
            return TTLocalizer.ValentinesMickeyChatter
        elif chatterType == ToontownGlobals.Holidays.SillyChatter1:
            SillyMickeyChatter = getExtendedChat(MickeyChatter, TTLocalizer.SillyPhase1Chatter)
            return SillyMickeyChatter
        elif chatterType == ToontownGlobals.Holidays.SillyChatter2:
            SillyMickeyChatter = getExtendedChat(MickeyChatter, TTLocalizer.SillyPhase2Chatter)
            return SillyMickeyChatter
        elif chatterType == ToontownGlobals.Holidays.SillyChatter3:
            SillyMickeyChatter = getExtendedChat(MickeyChatter, TTLocalizer.SillyPhase3Chatter)
            return SillyMickeyChatter
        elif chatterType == ToontownGlobals.Holidays.SillyChatter4:
            SillyMickeyChatter = getExtendedChat(MickeyChatter, TTLocalizer.SillyPhase4Chatter)
            return SillyMickeyChatter
        elif chatterType == ToontownGlobals.Holidays.SellbotFieldOffice:
            fieldOfficeMickeyChatter = getExtendedChat(MickeyChatter, TTLocalizer.FieldOfficeMickeyChatter)
            return fieldOfficeMickeyChatter
        else:
            return MickeyChatter
    elif charName == TTLocalizer.VampireMickey:
        return VampireMickeyChatter
    elif charName == TTLocalizer.Minnie:
        if chatterType == ToontownGlobals.Holidays.AprilFoolsCostumes:
            return TTLocalizer.AFMinnieChatter
        elif chatterType == ToontownGlobals.Holidays.WinterCaroling:
            return TTLocalizer.WinterMinnieCChatter
        elif chatterType == ToontownGlobals.Holidays.WinterDecorations:
            return TTLocalizer.WinterMinnieDChatter
        elif chatterType == ToontownGlobals.Holidays.WackyWinterCaroling:
            return TTLocalizer.WinterMinnieCChatter
        elif chatterType == ToontownGlobals.Holidays.WackyWinterDecorations:
            return TTLocalizer.WinterMinnieDChatter
        elif chatterType == ToontownGlobals.Holidays.ValentinesDay:
            return TTLocalizer.ValentinesMinnieChatter
        elif chatterType == ToontownGlobals.Holidays.SillyChatter1:
            SillyMinnieChatter = getExtendedChat(MinnieChatter, TTLocalizer.SillyPhase1Chatter)
            return SillyMinnieChatter
        elif chatterType == ToontownGlobals.Holidays.SillyChatter2:
            SillyMinnieChatter = getExtendedChat(MinnieChatter, TTLocalizer.SillyPhase2Chatter)
            return SillyMinnieChatter
        elif chatterType == ToontownGlobals.Holidays.SillyChatter3:
            SillyMinnieChatter = getExtendedChat(MinnieChatter, TTLocalizer.SillyPhase3Chatter)
            return SillyMinnieChatter
        elif chatterType == ToontownGlobals.Holidays.SillyChatter4:
            SillyMinnieChatter = getExtendedChat(MinnieChatter, TTLocalizer.SillyPhase4Chatter)
            return SillyMinnieChatter
        elif chatterType == ToontownGlobals.Holidays.SellbotFieldOffice:
            fieldOfficeMinnieChatter = getExtendedChat(MinnieChatter, TTLocalizer.FieldOfficeMinnieChatter)
            return fieldOfficeMinnieChatter
        else:
            return MinnieChatter
    elif charName == TTLocalizer.WitchMinnie:
        return TTLocalizer.WitchMinnieChatter
    elif charName == TTLocalizer.Daisy or charName == TTLocalizer.SockHopDaisy:
        if chatterType == ToontownGlobals.Holidays.AprilFoolsCostumes:
            return TTLocalizer.AFDaisyChatter
        elif chatterType == ToontownGlobals.Holidays.HalloweenCostumes:
            return TTLocalizer.HalloweenDaisyChatter
        elif chatterType == ToontownGlobals.Holidays.SpookyCostumes:
            return TTLocalizer.HalloweenDaisyChatter
        elif chatterType == ToontownGlobals.Holidays.WinterCaroling:
            return TTLocalizer.WinterDaisyCChatter
        elif chatterType == ToontownGlobals.Holidays.WinterDecorations:
            return TTLocalizer.WinterDaisyDChatter
        elif chatterType == ToontownGlobals.Holidays.WackyWinterCaroling:
            return TTLocalizer.WinterDaisyCChatter
        elif chatterType == ToontownGlobals.Holidays.WackyWinterDecorations:
            return TTLocalizer.WinterDaisyDChatter
        elif chatterType == ToontownGlobals.Holidays.ValentinesDay:
            return TTLocalizer.ValentinesDaisyChatter
        elif chatterType == ToontownGlobals.Holidays.SillyChatter1:
            SillyDaisyChatter = getExtendedChat(DaisyChatter, TTLocalizer.SillyPhase1Chatter)
            return SillyDaisyChatter
        elif chatterType == ToontownGlobals.Holidays.SillyChatter2:
            SillyDaisyChatter = getExtendedChat(DaisyChatter, TTLocalizer.SillyPhase2Chatter)
            return SillyDaisyChatter
        elif chatterType == ToontownGlobals.Holidays.SillyChatter3:
            SillyDaisyChatter = getExtendedChat(DaisyChatter, TTLocalizer.SillyPhase3Chatter)
            return SillyDaisyChatter
        elif chatterType == ToontownGlobals.Holidays.SillyChatter4:
            SillyDaisyChatter = getExtendedChat(DaisyChatter, TTLocalizer.SillyPhase4Chatter)
            return SillyDaisyChatter
        elif chatterType == ToontownGlobals.Holidays.SellbotFieldOffice:
            fieldOfficeDaisyChatter = getExtendedChat(DaisyChatter, TTLocalizer.FieldOfficeDaisyChatter)
            return fieldOfficeDaisyChatter
        else:
            return DaisyChatter
    elif charName == TTLocalizer.Goofy:
        if chatterType == ToontownGlobals.Holidays.AprilFoolsCostumes:
            return TTLocalizer.AFGoofySpeedwayChatter
        elif chatterType == ToontownGlobals.Holidays.CrashedLeaderboard:
            return TTLocalizer.CLGoofySpeedwayChatter
        elif chatterType == ToontownGlobals.Holidays.CircuitRacingEvent:
            return TTLocalizer.GPGoofySpeedwayChatter
        elif chatterType == ToontownGlobals.Holidays.WinterDecorations or chatterType == ToontownGlobals.Holidays.WinterCaroling or chatterType == ToontownGlobals.Holidays.WackyWinterDecorations or chatterType == ToontownGlobals.Holidays.WackyWinterCaroling:
            return TTLocalizer.WinterGoofyChatter
        elif chatterType == ToontownGlobals.Holidays.ValentinesDay:
            return TTLocalizer.ValentinesGoofyChatter
        elif chatterType == ToontownGlobals.Holidays.SillyChatter1:
            SillyGoofySpeedwayChatter = getExtendedChat(GoofySpeedwayChatter, TTLocalizer.SillyPhase1Chatter)
            return SillyGoofySpeedwayChatter
        elif chatterType == ToontownGlobals.Holidays.SillyChatter2:
            SillyGoofySpeedwayChatter = getExtendedChat(GoofySpeedwayChatter, TTLocalizer.SillyPhase2Chatter)
            return SillyGoofySpeedwayChatter
        elif chatterType == ToontownGlobals.Holidays.SillyChatter3:
            SillyGoofySpeedwayChatter = getExtendedChat(GoofySpeedwayChatter, TTLocalizer.SillyPhase3Chatter)
            return SillyGoofySpeedwayChatter
        elif chatterType == ToontownGlobals.Holidays.SillyChatter4:
            SillyGoofySpeedwayChatter = getExtendedChat(GoofySpeedwayChatter, TTLocalizer.SillyPhase4Chatter)
            return SillyGoofySpeedwayChatter
        else:
            return GoofySpeedwayChatter
    elif charName == TTLocalizer.SuperGoofy:
        return TTLocalizer.SuperGoofyChatter
    elif charName == TTLocalizer.Donald or charName == TTLocalizer.FrankenDonald:
        if chatterType == ToontownGlobals.Holidays.AprilFoolsCostumes:
            return TTLocalizer.AFDonaldChatter
        elif chatterType == ToontownGlobals.Holidays.HalloweenCostumes:
            return TTLocalizer.HalloweenDreamlandChatter
        elif chatterType == ToontownGlobals.Holidays.SpookyCostumes:
            return TTLocalizer.HalloweenDreamlandChatter
        elif chatterType == ToontownGlobals.Holidays.WinterCaroling:
            return TTLocalizer.WinterDreamlandCChatter
        elif chatterType == ToontownGlobals.Holidays.WinterDecorations:
            return TTLocalizer.WinterDreamlandDChatter
        elif chatterType == ToontownGlobals.Holidays.WackyWinterCaroling:
            return TTLocalizer.WinterDreamlandCChatter
        elif chatterType == ToontownGlobals.Holidays.WackyWinterDecorations:
            return TTLocalizer.WinterDreamlandDChatter
        elif chatterType == ToontownGlobals.Holidays.ValentinesDay:
            return TTLocalizer.ValentinesDreamlandChatter
        elif chatterType == ToontownGlobals.Holidays.SellbotFieldOffice:
            fieldOfficeDreamlandChatter = getExtendedChat(DonaldChatter, TTLocalizer.FieldOfficeDreamlandChatter)
            return fieldOfficeDreamlandChatter
        else:
            return DonaldChatter
    elif charName == TTLocalizer.DonaldDock:
        if chatterType == ToontownGlobals.Holidays.AprilFoolsCostumes:
            return TTLocalizer.AFDonaldDockChatter
        elif chatterType == ToontownGlobals.Holidays.HalloweenCostumes:
            return TTLocalizer.HalloweenDonaldChatter
        elif chatterType == ToontownGlobals.Holidays.SpookyCostumes:
            return TTLocalizer.HalloweenDonaldChatter
        elif chatterType == ToontownGlobals.Holidays.WinterCaroling:
            return TTLocalizer.WinterDonaldCChatter
        elif chatterType == ToontownGlobals.Holidays.WinterDecorations:
            return TTLocalizer.WinterDonaldDChatter
        elif chatterType == ToontownGlobals.Holidays.WackyWinterCaroling:
            return TTLocalizer.WinterDonaldCChatter
        elif chatterType == ToontownGlobals.Holidays.WackyWinterDecorations:
            return TTLocalizer.WinterDonaldDChatter
        elif chatterType == ToontownGlobals.Holidays.ValentinesDay:
            return TTLocalizer.ValentinesDonaldChatter
        else:
            return None
    elif charName == TTLocalizer.Pluto:
        if chatterType == ToontownGlobals.Holidays.AprilFoolsCostumes:
            return TTLocalizer.AFPlutoChatter
        elif chatterType == ToontownGlobals.Holidays.HalloweenCostumes:
            return TTLocalizer.WesternPlutoChatter
        elif chatterType == ToontownGlobals.Holidays.SpookyCostumes:
            return TTLocalizer.WesternPlutoChatter
        elif chatterType == ToontownGlobals.Holidays.WinterCaroling:
            return TTLocalizer.WinterPlutoCChatter
        elif chatterType == ToontownGlobals.Holidays.WinterDecorations:
            return TTLocalizer.WinterPlutoDChatter
        elif chatterType == ToontownGlobals.Holidays.WackyWinterCaroling:
            return TTLocalizer.WinterPlutoCChatter
        elif chatterType == ToontownGlobals.Holidays.WackyWinterDecorations:
            return TTLocalizer.WinterPlutoDChatter
        else:
            return None
    elif charName == TTLocalizer.WesternPluto:
        if chatterType == ToontownGlobals.Holidays.HalloweenCostumes:
            return TTLocalizer.WesternPlutoChatter
        elif chatterType == ToontownGlobals.Holidays.SpookyCostumes:
            return TTLocalizer.WesternPlutoChatter
        else:
            return None
    elif charName == TTLocalizer.Chip or charName == TTLocalizer.PoliceChip:
        if chatterType == ToontownGlobals.Holidays.AprilFoolsCostumes:
            return TTLocalizer.AFChipChatter
        elif chatterType == ToontownGlobals.Holidays.HalloweenCostumes:
            return TTLocalizer.HalloweenChipChatter
        elif chatterType == ToontownGlobals.Holidays.SpookyCostumes:
            return TTLocalizer.HalloweenChipChatter
        elif chatterType == ToontownGlobals.Holidays.WinterDecorations or chatterType == ToontownGlobals.Holidays.WinterCaroling or chatterType == ToontownGlobals.Holidays.WackyWinterDecorations or chatterType == ToontownGlobals.Holidays.WackyWinterCaroling:
            return TTLocalizer.WinterChipChatter
        elif chatterType == ToontownGlobals.Holidays.ValentinesDay:
            return TTLocalizer.ValentinesChipChatter
        elif chatterType == ToontownGlobals.Holidays.SillyChatter1:
            SillyChipChatter = getExtendedChat(ChipChatter, TTLocalizer.SillyPhase1Chatter)
            return SillyChipChatter
        elif chatterType == ToontownGlobals.Holidays.SillyChatter2:
            SillyChipChatter = getExtendedChat(ChipChatter, TTLocalizer.SillyPhase2Chatter)
            return SillyChipChatter
        elif chatterType == ToontownGlobals.Holidays.SillyChatter3:
            SillyChipChatter = getExtendedChat(ChipChatter, TTLocalizer.SillyPhase3Chatter)
            return SillyChipChatter
        elif chatterType == ToontownGlobals.Holidays.SillyChatter4:
            SillyChipChatter = getExtendedChat(ChipChatter, TTLocalizer.SillyPhase4Chatter)
            return SillyChipChatter
        else:
            return ChipChatter
    elif charName == TTLocalizer.Dale or TTLocalizer.JailbirdDale:
        if chatterType == ToontownGlobals.Holidays.AprilFoolsCostumes:
            return TTLocalizer.AFDaleChatter
        elif chatterType == ToontownGlobals.Holidays.HalloweenCostumes:
            return TTLocalizer.HalloweenDaleChatter
        elif chatterType == ToontownGlobals.Holidays.SpookyCostumes:
            return TTLocalizer.HalloweenDaleChatter
        elif chatterType == ToontownGlobals.Holidays.WinterDecorations or chatterType == ToontownGlobals.Holidays.WinterCaroling or chatterType == ToontownGlobals.Holidays.WackyWinterDecorations or chatterType == ToontownGlobals.Holidays.WackyWinterCaroling:
            return TTLocalizer.WinterDaleChatter
        elif chatterType == ToontownGlobals.Holidays.ValentinesDay:
            return TTLocalizer.ValentinesDaleChatter
        elif chatterType == ToontownGlobals.Holidays.SillyChatter1:
            SillyDaleChatter = getExtendedChat(DaleChatter, TTLocalizer.SillyPhase1Chatter)
            return SillyDaleChatter
        elif chatterType == ToontownGlobals.Holidays.SillyChatter2:
            SillyDaleChatter = getExtendedChat(DaleChatter, TTLocalizer.SillyPhase2Chatter)
            return SillyDaleChatter
        elif chatterType == ToontownGlobals.Holidays.SillyChatter3:
            SillyDaleChatter = getExtendedChat(DaleChatter, TTLocalizer.SillyPhase3Chatter)
            return SillyDaleChatter
        elif chatterType == ToontownGlobals.Holidays.SillyChatter4:
            SillyDaleChatter = getExtendedChat(DaleChatter, TTLocalizer.SillyPhase4Chatter)
            return SillyDaleChatter
        else:
            return DaleChatter
    return None
