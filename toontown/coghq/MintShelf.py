from toontown.toonbase.ToontownGlobals import *
from toontown.coghq import MintProduct

class MintShelf(MintProduct.MintProduct):
    Models = {Zones.CashbotMintIntA: 'phase_10/models/cashbotHQ/shelf_A1MoneyBags',
     Zones.CashbotMintIntB: 'phase_10/models/cashbotHQ/shelf_A1Money',
     Zones.CashbotMintIntC: 'phase_10/models/cashbotHQ/shelf_A1Gold'}
    Scales = {Zones.CashbotMintIntA: 1.0,
     Zones.CashbotMintIntB: 1.0,
     Zones.CashbotMintIntC: 1.0}
