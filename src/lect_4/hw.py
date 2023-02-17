# # class LeaderBoard:
# #     """Fixed length sequence of high scores in descending order"""
# #
# #     def __init__(self, capacity):
# #         """Initialize leader board with given maximum capacity
# #         All entries are initially None
# #         Capacity must be a positive integer"""
# #         self.capacity = capacity
# #         self.scores = [None] * capacity
# #
# #     def __len__(self):
# #         """Return the number of non None elements in the board"""
# #         return sum(score is not None for score in self.scores)
# #
# #     def get_player(self, player):
# #         """Find a player in leader board using his name
# #         Print not found if that player isn't in the board"""
# #         for i, score in enumerate(self.scores):
# #             if score is not None and score[0] == player:
# #                 print(f"{player} found at rank {i + 1}")
# #                 return
# #         print(f"{player} not found in the leader board")
# #
# #     def __str__(self):
# #         """Return string representation of the LeaderBoard"""
# #         score_strings = []
# #         for i, score in enumerate(self.scores):
# #             if score is not None:
# #                 score_strings.append(f"{i + 1}. {score[0]}: {score[1]}")
# #         return "\n".join(score_strings)
# #
# #     def __delitem__(self, k):
# #         """Delete score of rank k
# #         k must be a positive integer and smaller than LEN of current
# #         leader board"""
# #         if k < 1 or k > len(self):
# #             raise IndexError("Index out of range")
# #         if self.scores[k - 1] is None:
# #             raise IndexError("Index out of range")
# #         for i in range(k - 1, self.capacity - 1):
# #             self.scores[i] = self.scores[i + 1]
# #         self.scores[-1] = None
# #
# #     def add(self, new_entry):
# #         """Consider adding new entry to high scores
# #         new_entry: a tuple including score and player information"""
# #         player,score = new_entry
# #         if len(self) == 0:
# #             self.scores[0] = new_entry
# #         elif len(self) < self.capacity or score > self.scores[-1][1]:
# #             i = len(self) - 1
# #             while i >= 0 and (self.scores[i] is None or score > self.scores[i][1]):
# #                 i -= 1
# #             i += 1
# #             for j in range(min(len(self) - 1, self.capacity - 2), i - 1, -1):
# #                 self.scores[j + 1] = self.scores[j]
# #             self.scores[i] = (player, score)
# #             if len(self) > self.capacity:
# #                 del self[self.capacity]
# #
# #
# # scores = [('Catto', 25), ('Doggo', 28), ('Bunny', 19), ('Panda', 20), ('Snaky', 30), ('Racoon', 23), ('Larma', 21)]
# # leader_board = LeaderBoard(7)
# # for score in scores:
# #     leader_board.add(score)
# # print(leader_board)
# # # Adding Owl with score 26 to the leader board.
# # print("------------------------------")
# # leader_board.add(('Owl',26))
# # print(leader_board)
# # print("------------------------------")
# # # Adding Piggy with score 20 to the leader board.
# # leader_board.add(('Piggy',20))
# # print(leader_board)
# # print("------------------------------")
# # # Racoon was found cheated. Find and remove him from the leader board. Then Piggy is given the slot.
# # del leader_board[6]
# # leader_board.add(('Piggy',20))
# # # # Print out the leader board using the implemented string representation method
# # # print(leader_board)
# # # leader_board.get_player("Piggy")
# #
# # class Leaderboard:
# #     def __init__(self, capacity: int):
# #         self._capacity = capacity
# #         self._scores = [None]*capacity
# #     def __len__(self):
# #         return sum( score is not None for score in self._scores )
# #     def get_player(self, player):
# #         for i, score in enumerate(self._scores):
# #             if score is not None and score[0] == player:
# #                 print(f"player {player} is at rank {i}")
# #     def add(self, new_entry):
# #
# #
# #
# # scores = [('Catto', 25), ('Doggo', 28), ('Bunny', 19), ('Panda', 20), ('Snaky', 30), ('Racoon', 23), ('Larma', 21)]
# # leader_board = Leaderboard(7)
# # for score in scores:
# #     leader_board.add(score)
# # print(leader_board)
# # # Adding Owl with score 26 to the leader board.
# # print("------------------------------")
# # leader_board.add(('Owl',26))
# # print(leader_board)
# # print("------------------------------")
# # # Adding Piggy with score 20 to the leader board.
# # leader_board.add(('Piggy',20))
# # print(leader_board)
# # print("------------------------------")
# # # Racoon was found cheated. Find and remove him from the leader board. Then Piggy is given the slot.
# # del leader_board[6]
# # leader_board.add(('Piggy',20))
# # # Print out the leader board using the implemented string representation method
# # print(leader_board)
# # leader_board.get_player("Piggy")
#
# def best_profit(prices):
#     if not prices:
#         return 0
#
#     min_price = float('inf')
#     max_profit = 0
#
#     for price in prices:
#         if price < min_price:
#             min_price = price
#         else:
#             max_profit = max(max_profit, price - min_price)
#
#     return max_profit
# price = [7, 1, 5, 3, 6, 4]
# print(best_profit(price))
# price = [7, 6, 4, 3, 1]
# print(best_profit(price))
#
# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j >= 0 and key < arr[j]:
#             arr[j+1] = arr[j]
#             j -= 1
#         arr[j+1] = key
#     return arr
#
# arr1 = [6, 9, 10, 2, 0, -1, 4, 5, 8]
# sorted_arr1 = insertion_sort(arr1)
# print(sorted_arr1)

def best_profit(prices):
    i = 0
    n = len(prices)
    valley = prices[0]
    peak = prices[0]
    max_profit = 0
    while i < n - 1:
        while i < n - 1 and prices[i] >= prices[i + 1]:
            i += 1
        valley = prices[i]
        while i < n - 1 and prices[i] <= prices[i + 1]:
            i += 1
        peak = prices[i]
        max_profit += peak - valley
    return max_profit

price = [7, 1, 5, 3, 6, 4]
print(best_profit(price))
price = [7, 6, 4, 3, 1]
print(best_profit(price))