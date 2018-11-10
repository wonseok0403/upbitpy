from upbitpy import Upbitpy

upbitpy = Upbitpy()
allMarket = upbitpy.get_market_all()
KRWList = []
BTCList = []

def GetBTCList(MarketList):
	List = []
	for i in MarketList :
		if( i['market'][0:3] == 'BTC' ) :
			List.append(i['market'])

	global BTCList
	BTCList = List


def GetKRWList(MarketList):
	List = []
	for i in MarketList :
		if( i['market'][0:3] == 'KRW' ) :
			List.append(i['market'])

	global KRWList
	KRWList = List


def CanTradeKRWByBTC(KRWList, BTCList) :
	List = []
	for i in KRWList :
		for j in BTCList :
			if( i.split('-')[1] == j.split('-')[1] ) :
				print(i)


GetKRWList(allMarket)
GetBTCList(allMarket)
print(BTCList)
CanTradeKRWByBTC(KRWList, BTCList)