## June 28th, 2025

* Built one parent class and two child classes.
* Added unique methods to each child class.
* Practiced method overriding.
* Got different class instances to interact. First step toward more complex behavior.

---

## June 29th, 2025

* Worked on basic loops with `try-except` blocks. Learned that using `continue` inside an exception handler can reset the loop properly.
* Practiced calling class methods and attributes from outside the class:

  * Use the object’s name instead of `self` (e.g., `fighter.fight()` instead of `self.fight()`).
  * Same applies to attributes (`fighter.hp`, `fighter.name`).
* Learned how to use `python3 -m` to run a module that’s not in the current directory.
* Gained a surface-level understanding of the role of `__init__.py` for treating folders as packages.
* As a bonus, experimented with creating a simple plugin for Neovim.

---

## June 30th, 2025

* Created an enemy class for my player to fight.
* Practiced controlling game logic with `if` statements: if an enemy’s HP drops to 0, it can’t be attacked again and shows a death message instead.
* Added basic checks to prevent dead enemies from calling any methods — fragile but working for now.
* Simulated turn-based combat inside a `while` loop.
* Simplified and modularized methods: one method can now call another cleanly.
* Practiced clean logic flow for combat turns and HP updates.

---

## Current Goals

* Add a save/load feature to store the player’s state and attributes, including an inventory system to track loot.
* Make the death check logic more robust and less error-prone.
* Expand the parent class so instances can deactivate themselves and stay inactive until reactivated. 

---
