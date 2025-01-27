# Blackjack AI  

## Introduction  
Blackjack AI is a Python implementation of the classic Blackjack game, enhanced with AI recommendations. The AI provides strategic advice based on probabilities and expected values, helping players make smarter decisions during gameplay.

---

## How to Play  
1. **Objective**:  
   - Get a hand value as close to **21** as possible without exceeding it.
   - Beat the dealer by having a higher total or by the dealer busting.

2. **Gameplay**:  
   - Each player starts with two cards.  
   - Cards 2-10 are worth their face value.  
   - **J, Q, K** are worth **10 points**, and **Aces** can be worth **1 or 11** depending on the hand.  
   - Players can choose to:  
     - **Hit**: Take another card to try to improve their total.  
     - **Stay**: Keep their current hand total.  
   - The dealer must draw until their total is at least 17.

3. **Winning Conditions**:  
   - **Blackjack**: A total of 21 on your initial hand automatically wins unless the dealer also has 21 (tie).  
   - **Bust**: If your hand exceeds 21, you lose automatically.  

---

## Features  
- **AI Recommendations**:  
  - Provides advice on whether to "hit" or "stay" based on probabilities and expected values.  
  - Displays your chance of busting or achieving a Blackjack for strategic decision-making.

- **Dealer Logic**:  
  - The dealer automatically follows game rules, drawing cards until their hand value is at least 17.  

- **Utility Calculations**:  
  - Calculates probabilities dynamically based on the current hand.

