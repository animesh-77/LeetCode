class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:

        import bisect

        optimal_item = {}
        available_prices = []

        for (price, beauty) in items:

            if price not in optimal_item:
                bisect.insort(available_prices, price)
            optimal_item[price] = max(optimal_item.get(price, 0), beauty)

        for pos, available_price in enumerate(available_prices[1::], 1):
            optimal_item[available_price] = max(optimal_item[available_price], optimal_item[available_prices[pos - 1]])

        print(available_prices)
        print(optimal_item)

        ret = []

        for query in queries:
            optimal_pos = bisect.bisect_right(available_prices, query)
            if optimal_pos > 0:
                if optimal_pos < len(available_prices) and query == optimal_item[available_prices[optimal_pos]]:
                    ret.append(optimal_item[available_prices[optimal_pos]])
                    # print(query, optimal_item[available_prices[optimal_pos]])
                else:
                    ret.append(optimal_item[available_prices[optimal_pos - 1]])
                    # print(query, optimal_item[available_prices[optimal_pos-1]])
            else:
                ret.append(0)
                # print(query, 0)
        return ret
