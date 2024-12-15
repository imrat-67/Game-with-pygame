# Throne of Choices

*Throne of Choices* is a strategic resource management game built with Python and Pygame. Lead your chosen house (Targaryen, Stark, or Lannister) to victory by managing resources and making critical decisions across five turns. Each house has unique traits, strengths, and victory conditions, challenging you to devise the perfect strategy.

---

## Features

### *1. Immersive Gameplay*
- *Team Selection: Choose your house—Targaryen, **Stark, or **Lannister*—each with unique strengths and objectives.  
- *Decision-Making*: Perform actions each turn to manage resources like loyalty, gold, and army strength.  
- *Strategic Thinking*: Plan moves based on house traits and adapt to challenges brought by resource constraints and random events.

### *2. Random Events*
Taking a "Risky Decision" triggers random events that can either:
- Reward you with increased resources, or  
- Penalize you with reduced loyalty, gold, or army strength.  

### *3. Unique Goals for Each House*
Your selected house determines your starting resources and endgame conditions:
- *House Targaryen*: Build the strongest army and reclaim the Iron Throne.  
- *House Stark*: Uphold honor and defend the North through loyalty and defense.  
- *House Lannister*: Use wealth and alliances to secure the kingdom.

---

## Gameplay Mechanics

### *1. Game Launch*
- The welcome screen displays a themed message with background music and imagery.  

### *2. Team Selection*
Choose your house by selecting:
- *1*: Targaryen  
- *2*: Stark  
- *3*: Lannister  

### *3. Resource Management*
Each house starts with predefined resources:
| House          | Loyalty | Gold | Army Strength |  
|----------------|---------|------|---------------|  
| Targaryen      | 40      | 80   | 300           |  
| Stark          | 70      | 50   | 200           |  
| Lannister      | 30      | 200  | 150           |  

### *4. Turn-Based Decisions*
Over five turns, choose one of four actions per turn:
1. *Recruit Soldiers*: Increase your army at the cost of gold.  
2. *Bribe Allies*: Increase loyalty by spending gold.  
3. *Fortify Defenses*: Slightly increase your army at a small gold cost.  
4. *Risky Decision*: Random events with potentially high risks and rewards.

Each decision directly impacts your resources. Insufficient gold can prevent you from executing certain actions.

### *5. Winning Conditions*
To win, you must meet your house's unique objectives:
- *Targaryen*:  
  - Army strength ≥ 500  
  - Loyalty ≥ 60  

- *Stark*:  
  - Loyalty ≥ 80  
  - Army strength ≥ 200  

- *Lannister*:  
  - Gold ≥ 300  
  - Loyalty ≥ 50  

At the end of five turns, your progress is evaluated to determine victory or defeat.

---

## How to Play

### *Setup*
1. Clone this repository:
   ```bash
   git clone <repository_url>
