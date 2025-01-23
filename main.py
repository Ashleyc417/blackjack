# 1. **Initial Deal (Player)**
#    - Deal the player two cards.
#    - Display both cards (e.g., "Queen" and "5") and show their total (e.g., 15).
#
# 2. **Player Turn**
#    - Prompt the player to **Hit** (take another card) or **Stand** (stop taking cards).
#    - If the player **Hits**:
#      - Deal one additional card and update the total.
#      - If the total is **exactly 21**, stop immediately (player has Blackjack).
#      - If the total **exceeds 21**, stop immediately (player is Bust).
#    - Continue prompting the player to **Hit** or **Stand** until they bust or choose to stand.
#
# 3. **Dealer Turn**
#    - Once the player stands (and hasn’t busted), deal the dealer two cards.
#    - The dealer’s turn follows the **same flow** as the player’s:
#      - Prompt to Hit or Stand.
#      - If dealer hits 21, stop (Blackjack).
#      - If dealer exceeds 21, stop (Bust).
#
# 4. **Outcome (If Both Survive)**
#    - If both player and dealer finish without busting:
#      - Compare totals to determine the winner (closest to 21 without going over).
#      - Declare a tie (push) if totals are the same.

