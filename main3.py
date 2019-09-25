#Copy the contents from http://arcade.academy/examples/move_keyboard.html#move-keyboard and see if you can figure out what is going on. Add comments to any uncommented lines
"""
Move with a Sprite Animation

Simple program to show basic sprite usage.

Artwork from http://kenney.nl

If Python and Arcade are installed, this example can be run from the command line with:
python -m arcade.examples.sprite_move_animation
"""
import arcade
import random
import os

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Move with a Sprite Animation Example"

COIN_SCALE = 0.5
COIN_COUNT = 50

MOVEMENT_SPEED = 5
# what is os and why random for import?

class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self, width, height, title):
        """
        Initializer
        """
        super().__init__(width, height, title)

        # Set the working directory (where we expect to find files) to the same
        # directory this .py file is in. You can leave this out of your own
        # code, but it is needed to easily run the examples using "python -m"
        # as mentioned at the top of this program.
        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.player_list = None
        self.coin_list = None

        # Set up the player
        self.score = 0
        self.player = None
        #setting up the starting line of the game

    def setup(self):
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        # Set up the player
        self.score = 0
        self.player = arcade.AnimatedWalkingSprite()

        character_scale = 0.75
        self.player.stand_right_textures = []
        self.player.stand_right_textures.append(arcade.load_texture("images/character_sprites/spellun-sprite.png",
                                                                    scale=1.5))
        self.player.stand_left_textures = []
        self.player.stand_left_textures.append(arcade.load_texture("images/character_sprites/spellun-sprite.png",
                                                                   scale=1.5, mirrored=True))
        #why is player standing right or left?  What is thet mean?
        self.player.walk_right_textures = []

        self.player.walk_right_textures.append(arcade.load_texture("images/character_sprites/spellun-sprite.png",
                                                                   scale=1.5))
        self.player.walk_right_textures.append(arcade.load_texture("images/character_sprites/spellun-sprite.png",
                                                                   scale=1.5))
        self.player.walk_right_textures.append(arcade.load_texture("images/character_sprites/spellun-sprite.png",
                                                                   scale=1.5))
        self.player.walk_right_textures.append(arcade.load_texture("images/character_sprites/sprellun-sprite.png",
                                                                   scale=1.5))

        self.player.walk_left_textures = []

        self.player.walk_left_textures.append(arcade.load_texture("images/character_sprites/spellun-sprite.png",
                                                                  scale=1.5, mirrored=True))
        self.player.walk_left_textures.append(arcade.load_texture("images/character_sprites/spellun-sprite.png",
                                                                  scale=1.5, mirrored=True))
        self.player.walk_left_textures.append(arcade.load_texture("images/character_sprites/spellun-sprite.png",
                                                                  scale=1.5, mirrored=True))
        self.player.walk_left_textures.append(arcade.load_texture("images/character_sprites/spellun-sprite.png",
                                                                  scale=1.5, mirrored=True))
        #I thought walk will be in update
        self.player.texture_change_distance = 20

        self.player.center_x = SCREEN_WIDTH // 2
        self.player.center_y = SCREEN_HEIGHT // 2
        self.player.scale = 0.8

        self.player_list.append(self.player)

        for i in range(COIN_COUNT):
            coin = arcade.AnimatedTimeSprite(scale=0.5)
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)
            #setting up the location of the coin randomly?
            coin.textures = []
            coin.textures.append(arcade.load_texture("images/character_sprites/RedDragon.png", scale=0.5))
            coin.textures.append(arcade.load_texture("images/character_sprites/RedDragon.png", scale=0.5))
            coin.textures.append(arcade.load_texture("images/character_sprites/RedDragon.png", scale=0.5))
            coin.textures.append(arcade.load_texture("images/character_sprites/RedDragon.png", scale=0.5))
            coin.textures.append(arcade.load_texture("images/character_sprites/RedDragon.png", scale=0.5))
            coin.textures.append(arcade.load_texture("images/character_sprites/RedDragon.png", scale=0.5))
            coin.cur_texture_index = random.randrange(len(coin.textures))

            self.coin_list.append(coin)

        # Set the background color
        arcade.set_background_color(arcade.color.AMAZON)

    def on_draw(self):
        """
        Render the screen.
        """

        # This command has to happen before we start drawing
        arcade.start_render()

        # Draw all the sprites.
        self.coin_list.draw()
        self.player_list.draw()

        # Put the text on the screen.
        output = f"Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)
        #gives the score

    def on_key_press(self, key, modifiers):
        """
        Called whenever a key is pressed.
        """
        if key == arcade.key.UP:
            self.player.change_y = MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.player.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.player.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player.change_x = MOVEMENT_SPEED
            #move the character based on the player's input based on the ,ove,emt speed

    def on_key_release(self, key, modifiers):
        """
        Called when the user releases a key.
        """
        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.change_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0

    def update(self, delta_time):
        """ Movement and game logic """

        self.coin_list.update()
        self.coin_list.update_animation()
        self.player_list.update()
        self.player_list.update_animation()

        # Generate a list of all sprites that collided with the player.
        hit_list = arcade.check_for_collision_with_list(self.player, self.coin_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1
            #add to the score with each coin the the character picked


def main():
    """ Main method """
    window = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()