def day_to_tuple(x): # 날짜 문자열을 튜플로 바꿔서 반환
    year, month, day = map(int, x.split('.'))
    return (year, month, day)
def is_expired(x_tuple, today_tuple): # 만료 일자가 x일 때 만료 여부
    expired_year, expired_month, expired_day = x_tuple
    today_year, today_month, today_day = today_tuple
    expired=False
    
    if today_year>expired_year:
        expired=True
    elif today_year==expired_year and today_month>expired_month:
        expired=True
    elif today_year==expired_year and today_month==expired_month and today_day>=expired_day:
        expired=True
    return expired
def solution(today, terms, privacies):
    # terms 전처리
    terms_dict={} # 약관을 사용하기 좋게 dictionary로 변경
    for i in terms:
        term_type, period = i.split()
        terms_dict[term_type] = int(period)    
    answer = []
    # privacies 유효 여부 판단
    for idx, i in enumerate(privacies):
        due, term_type = i.split() # 유효 기간과 종류
        year, month, day = day_to_tuple(due)
        
        #해당 정책의 만료 일자 구하기
        month+=terms_dict[term_type]
        year+=(month-1)//12
        month=month%12
        month=12 if month==0 else month
        
        if is_expired((year, month, day), day_to_tuple(today)):
            answer.append(idx+1)
        
    return answer