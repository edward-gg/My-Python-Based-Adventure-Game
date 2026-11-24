class Game:
    def __init__(self):
        print("\n🏠 Jungle Temple Adventure")
        print("---------------------------------")
        print("You wake up inside a forgotten ancient temple.")
        print("The stone doors behind you have collapsed...")
        print("There is no way back.")
        print("Strange echoes move through the halls.")
        print("You must explore, find items, and escape alive.")
        print("---------------------------------")
        
        self.name = input("Enter your name: ")
        
        # Game State
        self.location = "Entrance Chamber"
        self.inventory = []
        self.game_over = False
        self.saved_explorer = False

        # MAP
        self.map = {
            "Entrance Chamber": {"east": "Main Hall"},
            "Main Hall": {"west": "Entrance Chamber", "east": "Armory Ruins", "south": "Library"},
            "Armory Ruins": {"west": "Main Hall", "east": "Storage Room"},
            "Storage Room": {"west": "Armory Ruins"},
            "Library": {"north": "Main Hall", "south": "Sacred Shrine"},
            "Sacred Shrine": {"north": "Library", "east": "Healing Room", "south": "Puzzle Chamber"},
            "Healing Room": {"west": "Sacred Shrine"},
            "Puzzle Chamber": {"north": "Sacred Shrine", "south": "Trap Corridor"},
            "Trap Corridor": {"north": "Puzzle Chamber", "south": "Underground River"},
            "Underground River": {"north": "Trap Corridor", "east": "Hidden Tomb"},
            "Hidden Tomb": {"west": "Underground River", "east": "Exit Gate"},
            "Exit Gate": {"west": "Hidden Tomb"}
        }

        # ITEMS
        self.items = {
            "Armory Ruins": "ancient key",
            "Storage Room": "torch",
            "Puzzle Chamber": "rope",
            "Healing Room": "bandages",
            "Library": "stone tablet"
        }

        # ROOM TEXT
        self.text = {
            "Entrance Chamber": "A broken doorway blocks your escape.",
            "Main Hall": "Tall pillars surround you.",
            "Armory Ruins": "Broken weapons lie everywhere.",
            "Storage Room": "Old dusty boxes fill the room.",
            "Library": "Ancient books are scattered around.",
            "Sacred Shrine": "A glowing altar shines brightly.",
            "Healing Room": "Healing herbs are stored here.",
            "Puzzle Chamber": "Strange symbols glow on walls.",
            "Trap Corridor": "You hear moving stones nearby.",
            "Underground River": "Dark water flows silently.",
            "Hidden Tomb": "A silent ancient tomb.",
            "Exit Gate": "A huge locked exit door."
        }

    # SHOW AVAILABLE MOVES
    def show_available_locations(self):
        print("\nAvailable locations:")
        for direction in self.map[self.location]:
            print(f"  {direction} → {self.map[self.location][direction]}")

    # SHOW STATUS
    def show(self):
        print("\n-------------------")
        print(f"Location: {self.location}")
        print(f"Inventory: {self.inventory}")
        print(f" {self.text[self.location]}")
        self.show_available_locations()

    # MOVE PLAYER
    def move(self):
        direction = input("\nMove (north/south/east/west): ").strip().lower()
        
        if direction not in self.map[self.location]:
            print("✗ You can't go that way!")
            return
            
        new_location = self.map[self.location][direction]

        # LOCKS (Puzzles)
        if new_location == "Sacred Shrine" and "ancient key" not in self.inventory:
            print("📖 You need an ancient key to unlock this.")
            return
        if new_location == "Trap Corridor" and "rope" not in self.inventory:
            print("➡️ You need a rope to cross the broken path.")
            return
        if new_location == "Underground River" and "torch" not in self.inventory:
            print("🔥 You need a torch to see in the dark.")
            return
            
        self.location = new_location
        print(f"➡️ You moved to {self.location}")

    # PICK ITEM
    def pick(self):
        if self.location in self.items:
            item = self.items[self.location]
            
            # Check inventory limit
            if len(self.inventory) >= 4:
                print("🎒 Your bag is full! (Max 4 items)")
                choice = input("Do you want to drop an item? (yes/no): ").strip().lower()
                
                if choice != "yes":
                    print("You leave the item.")
                    return
                
                print(f"Your items: {self.inventory}")
                drop_item = input("Which item do you want to drop? ").strip().lower()
                
                if drop_item in self.inventory:
                    self.inventory.remove(drop_item)
                    self.items[self.location] = drop_item
                    print(f" Dropped: {drop_item}")
                else:
                    print("✗ Invalid item. You can't drop something you don't have.")
                    return
            
            # Pick up the item
            self.inventory.append(item)
            del self.items[self.location]
            print(f"✅ You picked up: {item}")
        else:
            print("✗ No item here.")

    # DROP ITEM
    def drop(self):
        print(f"🎒 Inventory: {self.inventory}")
        item = input("Drop item: ").strip().lower()
        
        if item in self.inventory:
            self.inventory.remove(item)
            self.items[self.location] = item
            print(f" Dropped: {item}")
        else:
            print("✗ Item not in bag.")

    # USE ITEM
    def use(self):
        item = input("Use item: ").strip().lower()
        
        if item not in self.inventory:
            print("✗ You don't have that item!")
            return
            
        if item == "bandages" and self.location == "Hidden Tomb":
            self.saved_explorer = True
            print("💡 You saved the injured explorer!")
            
        elif item == "stone tablet" and self.location == "Exit Gate":
            if self.saved_explorer:
                print("🏆 You used the stone tablet to unlock the gate.")
                print("🎉 YOU ESCAPED THE TEMPLE! YOU WIN! 🎉")
                self.game_over = True
            else:
                print("⚠️ The tablet has no power. You must save the explorer first.")
                
        else:
            print("✗ You cannot use that here.")

    # MAIN LOOP
    def run(self):
        while not self.game_over:
            self.show()
            print("\nActions: move, pick, drop, use, inventory")
            action = input("Choose action: ").strip().lower()
            
            if action == "move":
                self.move()
            elif action == "pick":
                self.pick()
            elif action == "drop":
                self.drop()
            elif action == "use":
                self.use()
            elif action == "inventory":
                print(f"🎒 Current Inventory: {self.inventory}")
            else:
                print("✗ Invalid action. Please type move, pick, drop, use, or inventory.")

# START GAME
if __name__ == "__main__":
    game = Game()
    game.run()
