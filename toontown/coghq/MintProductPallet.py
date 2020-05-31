from toontown.toonbase.ToontownGlobals import *
from toontown.coghq import MintProduct

class MintProductPallet(MintProduct.MintProduct):
    Models = {Zones.CashbotMintIntA: 'phase_10/models/cashbotHQ/DoubleCoinStack.bam',
     Zones.CashbotMintIntB: 'phase_10/models/cogHQ/DoubleMoneyStack.bam',
     Zones.CashbotMintIntC: 'phase_10/models/cashbotHQ/DoubleGoldStack.bam'}
    Scales = {Zones.CashbotMintIntA: 1.0,
     Zones.CashbotMintIntB: 1.0,
     Zones.CashbotMintIntC: 1.0}
