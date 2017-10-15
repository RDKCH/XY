from __future__ import division

open = 100
high = 120
low = 85
close = 110

volume = 1500
volume_average = 1000

best_bid = 98
best_ask = 105

highest_bid_quantity = 700
highest_ask_quantity = 200

ask_slippage = 0.0

ask_slippage_1 = 0.1 * close * (best_ask/best_bid-1)

ask_slippage_2 = 0.1 * close * (highest_ask_quantity / (highest_ask_quantity + highest_bid_quantity))

ask_slippage_3 = - 0.1 * close * ((high/close)-1)

ask_slippage_4 = - 0.1 * close * ((volume/volume_average)-1)

 
print("Slippage:")
print(ask_slippage_1 + ask_slippage_2 + ask_slippage_3 + ask_slippage_4)