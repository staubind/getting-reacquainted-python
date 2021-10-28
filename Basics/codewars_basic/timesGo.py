def how_many_times(annual_price, individual_price):
    # code here
    return annual_price // individual_price if annual_price % individual_price == 0 else annual_price // individual_price + 1