# Throne of Choices

*Throne of Choices* is a Python-based strategic game built with Pygame. Lead one of the three houses—Targaryen, Stark, or Lannister—by managing resources and making crucial decisions across five turns. Strategize effectively to achieve victory and fulfill your chosen house's objectives.

---

## Features

### Gameplay
- *House Selection*: Choose between Targaryen, Stark, and Lannister, each with unique starting resources and traits.
- *Strategic Decisions*: Manage resources like loyalty, gold, and army strength through well-timed actions.
- *Random Events*: Encounter positive or negative random events to keep gameplay unpredictable.

### Visuals and Audio
- Immersive graphics with themed backgrounds for different phases of the game.
- Continuous background music to enhance gameplay experience.

### Replayability
- Multiple strategies and distinct goals for each house provide high replay value.

---

## Gameplay Overview

### 1. Team Selection
Choose your house by pressing the corresponding number:
- *1*: Targaryen  
  *Goal*: Reclaim the Iron Throne  
  *Traits*: Strong army but limited gold  
  *Starting Resources*:
  - Loyalty: 40
  - Gold: 80
  - Army: 300

- *2*: Stark  
  *Goal*: Defend the North  
  *Traits*: High loyalty but weak finances  
  *Starting Resources*:
  - Loyalty: 70
  - Gold: 50
  - Army: 200

- *3*: Lannister  
  *Goal*: Maintain control through wealth  
  *Traits*: Wealthy but low loyalty  
  *Starting Resources*:
  - Loyalty: 30
  - Gold: 200
  - Army: 150

### 2. Turn-Based Actions
The game is played over *5 turns*, with one action allowed per turn:
1. *Recruit Soldiers*: Use gold to increase your army.
2. *Bribe Allies*: Spend gold to increase loyalty.
3. *Fortify Defenses*: Spend small amounts of gold to slightly improve army strength.
4. *Risky Decision*: Trigger random events that might either benefit or harm your resources.

### 3. Random Events
Choosing "Risky Decision" can result in:
- *Gaining or Losing Gold*: Financial boons or losses.
- *Increasing or Decreasing Loyalty*: Affects your house's support.
- *Army Strength Adjustments*: Your army can grow stronger or weaker.

---

## Winning Conditions
Victory depends on fulfilling your house's unique conditions by the end of the fifth turn:

| House         | Goal                                         | Conditions                             |
|---------------|---------------------------------------------|----------------------------------------|
| *Targaryen* | Reclaim the Iron Throne                     | Army strength ≥ 500, Loyalty ≥ 60     |
| *Stark*     | Defend the North                            | Loyalty ≥ 80, Army strength ≥ 200     |
| *Lannister* | Maintain control through wealth and loyalty | Gold ≥ 300, Loyalty ≥ 50              |

Failing to meet these conditions results in defeat.

---
