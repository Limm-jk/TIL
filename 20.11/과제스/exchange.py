# N원을 줬더니 받을 돈으로 get을 책정해주더라 
# 그럼 그간의 bill의 1000당 환률은 뭐냐
# bill/1000 * 정답 = get
def exchangeRate(bill:int, get:float) -> float:
    return get * 1000 / bill

