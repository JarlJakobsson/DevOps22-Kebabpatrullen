# Dungeon Run

Dungeon Run is a single-player text-based adventure game. It is played by making selections from menus containing various options. You choose the type of hero you want to play, and then explore a map with random content in search of treasure. But watch out for monsters! It's all about collecting as much treasure as possible and finding your way out alive.

---

## Requirements & Delivery

- The game shall meet the features set out in this design document
- The game must be able to run on Windows
- The game must be delivered compiled (as an exe file)
- The game must be delivered with a document describing the code architecture at a high level
- If the game contains graphical elements, this is a bonus

---

## A game round

1. On the home screen, the player can choose to create a new character or load an existing one:

   - The player chooses a type of hero
   - The player may enter a name for his/her character (the name may not already be saved)
   - Each character created should be automatically saved for reloading

2. The next step is to start an adventure. The player chooses the size of the adventure:

   - Small
   - Medium
   - Large

3. A map with random content is created in the chosen size and the player gets to choose in which corner of the map he wants to start:

   - Top left
   - Top right
   - Bottom left
   - Bottom right

4. The player chooses which way to go to reach a new room

5. When the player enters a new room (not already visited room):

   - Fight with monsters (if there are any in the room)
   - Collecting treasures (if any, and if the player is still alive)
   - Choosing which way the player should continue walking
   - If the room contains an exit, neither a. nor b. occurs. Instead, the player gets a option to leave the map, or to stay.

6. If the player enters a room already visited, he can only choose to continue

7. The adventure ends when the player leaves the map or is defeated

8. When an adventure ends, the collected treasures are added to the saved player character.

You can therefore play several adventures with the same saved character to collect treasures.

---

## Main features

### Maps

The maps are constructed as matrices with coordinates, much like a chessboard. In programming, this is called "multi-dimensional arrays"

[X] [X] [X] [X]

[X] [X] [X] [X]

[X] [X] [X] [X]

[X] [X] [X] [X]

[X] = ea room on the map.

The player should be able to choose the size of the map for each new adventure as follows:

- Small = 4x4 rooms
- Medium = 5x5 rooms
- Large = 8x8 rooms

---

### Game characters

The player must be able to choose from three different characters:

- Knight
- Wizard
- Thief

Each with different attribute values and special abilities. How these values affect combat is explained under Combat. All special abilities are passive and do not need to be activated by the player.

---

### The Knight

| Attribute  | Value |
| ---------- | ----- |
| Initiative | 5     |
| Strength   | 9     |
| Attack     | 6     |
| Agility    | 4     |

Special ability: **Shield Block**.

The knight always blocks the first attack per battle with his shield, and therefore does not need to dodge or take any damage.

---

### The Wizard

| Attribute  | Value |
| ---------- | ----- |
| Initiative | 6     |
| Strength   | 4     |
| Attack     | 9     |
| Agility    | 5     |

Special ability: **Bright Light**.

The wizard can blind monsters and therefore always has an 80% chance of escaping from battles.

---

### The Thief

| Attribute  | Value |
| ---------- | ----- |
| Initiative | 7     |
| Strength   | 5     |
| Attack     | 5     |
| Agility    | 7     |

Special ability: **Critical Hit**.

The thief has a 25% chance to do double damage each time attacking.

---

### Monster

A room can contain one, several or no monsters. It is randomly selected in each room based on the familiarity of the monster. The following monster types are found in Dungeon Run.

### Giant Spider

| Attribute              | Value |
| ---------------------- | ----- |
| Initiative             | 7     |
| Strength               | 1     |
| Attack                 | 2     |
| Agility                | 3     |
| Possibility to show up | 20%   |

### Skeleton

| Attribute              | Value |
| ---------------------- | ----- |
| Initiative             | 4     |
| Strength               | 2     |
| Attack                 | 3     |
| Agility                | 3     |
| Possibility to show up | 15%   |

### Orc

| Attribute              | Value |
| ---------------------- | ----- |
| Initiative             | 6     |
| Strength               | 3     |
| Attack                 | 4     |
| Agility                | 4     |
| Possibility to show up | 10%   |

### Troll

| Attribute              | Value |
| ---------------------- | ----- |
| Initiative             | 2     |
| Strength               | 4     |
| Attack                 | 7     |
| Agility                | 2     |
| Possibility to show up | 5%    |

---

## Combat

Battles occur when the player enters a room containing one or more monsters. They are settled by rolling six-sided dice. For example, if a monster has an Attack value of 2, then 2 six-sided dice should be rolled and totaled. The battles take place in turn and not in real time.

A battle follows this process:

1. The turn order is determined by all combatants rolling the same number of dice as their Initiative. The highest starts and the rest are ordered in descending order. This turn order is valid until the end of the battle.

2. We assume the player starts, who then gets the options Attack and Try to escape
   1. **Attack**: rolls the same number of dice as his Attack value. The opponent rolls
      equal to his Agility value. - If the Attack result is greater than the Dexterity result, the monster gets 1 in
      damage, which is deducted from Toughness. If Toughness reaches zero, the monster is defeated. - If the Agility result is greater than the Attack result, the attack misses.
   2. **Attempt to escape**: Agility \* 10 = X% chance to escape.
      - If the player succeeds, he is moved back to the previous room and
        the battle is cancelled. No treasure can be picked up because the monsters were not defeated. The game should remember which monsters are still in the room, however, Toughness should be reset on monsters when a room is left.
      - If the player fails to escape, they remain in the room and it is the monster's turn to attack.
3. When it's a monster's turn, it always attacks. The same calculation as above is performed (see 2.a.), except that the monster's Attack result is compared to the player's Agility result.
4. The battle continues until the player is defeated, has escaped or all monsters have been defeated.
   - If the player is defeated, the adventure is over.
   - If all monsters are defeated, the player picks up any treasure and and then chooses which way he wants to go.

---

## Treasure

Each room may contain one, several or no taxes. These are automatically picked up when the player enters a room, unless there are monsters. They are then picked up after the battle, unless the player has escaped or been defeated. Treasures are randomly picked up in each room based on their frequency as shown in the table below.

| Treasure             | Points | Frequency |
| -------------------- | ------ | --------- |
| Coins                | 2      | 40%       |
| Coin bag             | 6      | 30%       |
| Gold jewelry         | 10     | 15%       |
| Gemstones            | 14     | 10%       |
| Small treasure chest | 20     | 5%        |

---
