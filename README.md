# bow-or-axe
Simple game-like application based on classes. Demonstrates working with inheritance and classes.

Both `Bow` and `Axe` classes are derived from the `Weapon` class. They're using the `super` method to override the `__init__` from the base class.
`Character` class has simple methods like
- `attack` where we deal damage to another instance (another `Character`), 
- `take_damage` which calculates the character's hp after the hit and updates if the `Character` is alive,
- `is_alive` which only returns if the `Character` is alive.
