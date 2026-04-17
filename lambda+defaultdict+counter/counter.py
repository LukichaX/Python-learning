from collections import Counter

trades = ["NQ", "ES", "NQ", "RTY", "ES", "NQ", "YM", "NQ", "ES", "GC"]

trade_count = Counter(trades)

print(trade_count.most_common(2))