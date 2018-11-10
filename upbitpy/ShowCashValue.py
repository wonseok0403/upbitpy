#-*- coding: euc-kr -*-

from upbitpy import Upbitpy
from time import sleep
GlobalList = []

f = open("./list.txt", 'r')
lines = f.readlines()
for line in lines :
	GlobalList.append(line.strip())

upbit = Upbitpy()
KRWList = []
BTCList = []
sleep(0.05)
print('no')


def BUYKRW(TargetToBuy, price) :
	myBudget = int(float(upbit.get_accounts()[0]['balance']) * 0.5) 
	print(myBudget)
	volume = round(float(myBudget / price), 8)
	sample=upbit.get_chance(TargetToBuy[0])
	limitLow = sample['market']['bid']['min_total']
	print("매수 신청, 개수 : ", volume, "가격 : ",int(price), "총 가격 : ", volume*price)
	result = upbit.order(TargetToBuy[0], 'bid', volume, int(price))#float(price)
	
	uuid = result['uuid']
	
	volume = 0
	while( True ) :
		try:
			sleep(2)
			orderResult = upbit.get_order(uuid)
			if( orderResult['state'] == 'done' ):
				print('매수 완료')
				trades_count = orderResult['trades_count']
				volume = orderResult['executed_volume']
				price = orderResult['price']
				break
			else :
				print('매수 확인 중')
		except :
			print('예외발생')
	
	SELLBTC(TargetToBuy, volume. price)
	#SELLBTC(TargetToBuy, volume. price)


def SELLBTC(TargetToBuy, volume, price) :
	# BitCoin sell
	which = TargetToBuy.split('-')[1]
	print("매수 신청, 개수 : ", volume, "가격 : ",int(price), "총 가격 : ", volume*price)
	result = upbit.order('BTC-'+which, 'ask', volume, int(price))
	uuid = result['uuid']

	volume = 0
	while( True ):
		try:
			sleep(2)
			print('매수 확인 중..')
			KRWTicker = upbit.get_ticker(KRWList)
			BTCTicker = upbit.get_ticker(BTCList)
			KRWtoBTC = upbit.get_ticker(['KRW-BTC'])
			KRW = KRWTicker[0]['trade_price'];
			BTC = BTCTicker[0]['trade_price'] * KRWtoBTC[0]['trade_price'];
			if( (BTC-KRW) < KRW*0.01 ) :
				upbit.cancel_order(uuid)

			if( orderResult['state'] == 'done'):
				print('매수 확인 완료')
				volume = orderResult['executed_volume']
				price = orderResult['trades']['price']
				break
		except :
			print('예외발생')

	# Bitcoin to KRW
	print("매도 신청, 개수 : ", volume, "가격 : ",int(price), "총 가격 : ", volume*price)
	result = upbit.order('KRW-BTC', 'ask', volume, int(price) )
	uuid = result['uuid']
	while( True ):
		try:
			sleep(2) 
			print('매도 확인 중...')
			orderResult = upbit.get_order(uuid)
			if( orderResult['state'] == 'done') :
				print('매도 확인 완료!')
				break
		except :
			print('예외발생')


while True:
	print('no')
	try:
		sleep(0.05)
		for component in GlobalList :
			KRWList.append(component)
			BTCList.append(component.replace('KRW','BTC'))
		
			KRWTicker = upbit.get_ticker(KRWList)
			BTCTicker = upbit.get_ticker(BTCList)
			KRWtoBTC = upbit.get_ticker(['KRW-BTC'])
			KRW = KRWTicker[0]['trade_price'];
			BTC = BTCTicker[0]['trade_price'] * KRWtoBTC[0]['trade_price'];
			if( (BTC-KRW) > KRW*0.01 ) :
				BUYKRW([component], KRW)
				#while( ORDER ) :
				#	sleep(0.05)
				#	SELLKRW()
				print( upbit.get_chance(KRWList[0]) )
				print( component, KRWTicker[0]['trade_price'], BTCTicker[0]['trade_price'] * KRWtoBTC[0]['trade_price'])
				
				KRWList.pop()
				BTCList.pop()
				continue
		KRWList.pop()
		BTCList.pop()
	except  :
			print('예외발생')
