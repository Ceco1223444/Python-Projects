class Enemy:
    # Class-level list that stores all active enemy instances
    enemies = []
    def __init__(self, hitpoints, damage):
        self.hitpoints = hitpoints
        self.damage = damage
        # Register this enemy in the shared enemy list
        Enemy.enemies.append(self)
    def __repr__(self):
        return f"Enemy(hitpoints = {self.hitpoints}, damage = {self.damage})"
    def take_hit(self, injury):
        # Reduce hitpoints based on the incoming damage
        self.hitpoints -= injury
        # Remove the enemy from the list if its hitpoints drop to zero or below
        if self.hitpoints <= 0:
            Enemy.enemies.remove(self)
        return None
    def shoot(self, player):
        # Damage the player and return whether the player has died
        return player.take_hit(self.damage)
class Player:
    def __init__(self, hitpoints, damage, n=False):
        self.hitpoints = hitpoints
        self.damage = damage
        self.n = n  # Optional mode flag that affects shooting behavior
    def __repr__(self):
        return f"Player(hitpoints = {self.hitpoints}, damage = {self.damage})"
    def take_hit(self, injury):
        # Reduce the player’s hitpoints
        self.hitpoints -= injury
        # Return True only if the player has been defeated
        return self.hitpoints <= 0
    def shoot_5_times(self):
        # The player fires up to five shots in a single turn
        for _ in range(5):
            # Stop early if there are no enemies left
            if not Enemy.enemies:
                break
            # Select the first enemy in the list
            enemy = Enemy.enemies[0]
            if self.n is True:
                # Special mode: double the player’s damage before shooting
                self.damage *= 2
                enemy.take_hit(self.damage)
            else:
                # Standard attack
                enemy.take_hit(self.damage)
        # Return True if all enemies have been eliminated
        return len(Enemy.enemies) == 0
def duel(player):
    # Main loop for the fight sequence
    while True:
        # Player attacks first
        all_dead = player.shoot_5_times()
        if all_dead:
            print("The player won!")
            return
        # Remaining enemies take their turns attacking the player
        for enemy in list(Enemy.enemies):
            player_dead = enemy.shoot(player)
            if player_dead:
                print("The enemies won!")
                return
if __name__ == "__main__":
    player = Player(50, 15)
    # Create several enemies for the duel
    Enemy(20, 10)
    Enemy(30, 5)
    Enemy(25, 8)
    # Run the duel simulation
    duel(player)
    # Display the final state of the player and any surviving enemies
    print(player)
    print(Enemy.enemies)
