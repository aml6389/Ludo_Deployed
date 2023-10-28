try:
    import aio.gthread as threading
except:
    ...

import asyncio
import pygame
import random
import warnings

warnings.filterwarnings("ignore", category=DeprecationWarning)

pygame.init()
# import module

running = True
screen = pygame.display.set_mode((550, 550))

# Controlling Class for the game
# [r,y,b]
class Ludo_Game():
    def __init__(self, pieces):
        # create title and icon
        pygame.display.set_caption("Ludo_Icons/Ludo Game")
        self.icon = pygame.image.load("Ludo_Icons/project.png")
        pygame.display.set_icon(self.icon)
        # create a background board
        self.floor = pygame.image.load("Ludo_Icons/ludo_board.gif")

        self.turn = "Yellow Turn"
        self.font = pygame.font.Font("freesansbold.ttf", 24)
        self.over_font = pygame.font.Font("freesansbold.ttf", 64)
        self.blastimg  = pygame.image.load("Ludo_Icons/flame.png")
        self.last_turn = " "
        self.piece_list = pieces
        self.turn_text = "Yellow Turn"

    def update(self):
        screen.blit(self.floor, (0, 0))
        t_text = self.font.render(self.turn_text, True, (255, 255, 255))
        screen.blit(t_text, (40, 15))

############# CHECK THIS FUNCTION :
    def move_piece(self, piece_num, final_pos, a_pos, b_pos, turn):
        if self.piece_list[piece_num].state == "in":
            screen.blit(self.piece_list[piece_num].img, (self.piece_list[piece_num].x, self.piece_list[piece_num].y))
        else:
            global init_pos
            screen.blit(self.piece_list[piece_num].img, self.piece_list[piece_num].p_list[final_pos])
            init_pos = final_pos
        if self.last_turn == self.piece_list[piece_num].turn and self.turn == self.piece_list[piece_num].turn:
            self.iscollision(final_pos, a_pos, b_pos)
        if self.turn == self.piece_list[a_pos].turn and self.last_turn != self.piece_list[a_pos].turn:
            self.iscollision(final_pos, a_pos, b_pos)
        self.game_over(final_pos, a_pos, b_pos)


    def iscollision(self, first_pos, op1_pos, op2_pos):
        # global initial_position, final_position, init_pos, fin_pos, yellow_state, blue_state, init_position, fin_position, red_state, turn
        if self.turn == "Yellow Turn":
            # distance = math.sqrt(math.pow(enemyx - bulletx, 2) + math.pow(enemyy - bullety, 2))
            if self.piece_list[1].p_list[first_pos][0] == self.piece_list[0].p_list[op1_pos][0] and self.piece_list[1].p_list[first_pos][1] == self.piece_list[0].p_list[first_pos][
                1]:
                print("collision R to Y")
                print(self.piece_list[1].p_list[first_pos][0], self.piece_list[0].p_list[op1_pos][0], ":", self.piece_list[1].p_list[first_pos][1],
                      self.piece_list[0].p_list[op1_pos][1])
                self.piece_list[0].initial_position = 0
                self.piece_list[0].final_position = 0
                self.piece_list[0].state = "in"
                self.turn = "Red Turn"
            if self.piece_list[1].p_list[first_pos][0] == self.piece_list[2].p_list[op2_pos][0] and self.piece_list[1].p_list[first_pos][1] == self.piece_list[2].p_list[op2_pos][1]:
                print("collision R to B")
                print(self.piece_list[1].p_list[first_pos][0], self.piece_list[2].p_list[op2_pos][0], ":", self.piece_list[1].p_list[first_pos][1],
                      self.piece_list[2].p_list[op2_pos][1])
                self.piece_list[2].initial_position = 0
                self.piece_list[2].final_position = 0
                self.piece_list[2].state = "in"
                self.turn = "Red Turn"
        elif self.turn == "Blue Turn":
            if self.piece_list[0].p_list[first_pos][0] == self.piece_list[2].p_list[op1_pos][0] and self.piece_list[0].p_list[first_pos][1] == self.piece_list[2].p_list[op1_pos][1]:
                print("collision Y to B")
                print(self.piece_list[0].p_list[first_pos][0], self.piece_list[2].p_list[op1_pos][0], ":", self.piece_list[0].p_list[first_pos][1],
                      self.piece_list[2].p_list[op1_pos][1])
                self.piece_list[2].initial_position = 0
                self.piece_list[2].final_position = 0
                self.piece_list[2].state = "in"
                self.turn = "Yellow Turn"
            if self.piece_list[0].p_list[first_pos][0] == self.piece_list[1].p_list[op2_pos][0] and self.piece_list[0].p_list[first_pos][1] == self.piece_list[1].p_list[op2_pos][1]:
                print("collision Y to R")
                print(self.piece_list[0].p_list[first_pos][0], self.piece_list[1].p_list[op2_pos][0], ":", self.piece_list[0].p_list[first_pos][1],
                      self.piece_list[1].p_list[op2_pos][1])
                self.piece_list[1].initial_position = 0
                self.piece_list[1].final_position = 0
                self.piece_list[1].state = "in"
                self.turn = "Yellow Turn"
        elif self.turn == "Red Turn":
            if (self.piece_list[2].p_list[first_pos][0] == self.piece_list[1].p_list[op2_pos][0] and self.piece_list[2].p_list[first_pos][1] == self.piece_list[1].p_list[op2_pos][
                1]):
                print("collision B to R")
                print(self.piece_list[2].p_list[first_pos][0], self.piece_list[1].p_list[op2_pos][0], ":", self.piece_list[2].p_list[first_pos][1],
                      self.piece_list[1].p_list[op2_pos][1])
                self.piece_list[1].initial_position = 0
                self.piece_list[1].final_position = 0
                self.piece_list[1].state = "in"
                self.turn = "Blue Turn"
            if (self.piece_list[2].p_list[first_pos][0] == self.piece_list[0].p_list[op1_pos][0] and self.piece_list[2].p_list[first_pos][1] == self.piece_list[0].p_list[op1_pos][
                1]):
                print("collision B to Y")
                print(self.piece_list[2].p_list[first_pos][0], self.piece_list[0].p_list[op1_pos][0], ":", self.piece_list[2].p_list[first_pos][1],
                      self.piece_list[0].p_list[op1_pos][1])
                self.piece_list[0].initial_position = 0
                self.piece_list[0].final_position = 0
                self.piece_list[0].state = "in"
                self.turn = "Blue Turn"

    def game_over(self, blue_pos, yellow_pos, red_pos):
        # global turn
        if (self.piece_list[2].p_list[blue_pos][0], self.piece_list[2].p_list[blue_pos][1]) == (227, 260) or (
                self.piece_list[0].p_list[yellow_pos][0], self.piece_list[0].p_list[yellow_pos][1]) == (262, 295) or (
                self.piece_list[1].p_list[red_pos][0], self.piece_list[1].p_list[red_pos][1]) == (262, 225):
            game_over_text = over_font.render("GAME OVER", True, (255, 0, 0))
            screen.blit(game_over_text, (80, 250))
            self.turn = "No Turn"


# Piece class to be instantiated for each piece in play
class Pieces(pygame.sprite.Sprite):
    def __init__(self, img_file, pos, curr, pos_list, a_turn):
        self.img = pygame.image.load(img_file)
        self.x = pos[0]
        self.y = pos[1]
        self.initial_position = 0
        self.final_position = 0
        self.state = curr
        self.p_list = pos_list
        self.turn = a_turn

    def update(self, x, y):
        screen.blit(self.img, (x, y))
        self.x = x 
        self.y = y 

# Dice class to handle the Dice functions
class Dice(pygame.sprite.Sprite):
    def __init__(self):
        # load dice image
        self.state_1 = pygame.image.load("Ludo_Icons/Dice_1.jpg")
        self.state_2 = pygame.image.load("Ludo_Icons/Dice_2.jpg")
        self.state_3 = pygame.image.load("Ludo_Icons/Dice_3.jpg")
        self.state_4 = pygame.image.load("Ludo_Icons/Dice_4.jpg")
        self.state_5 = pygame.image.load("Ludo_Icons/Dice_5.jpg")
        self.state_6 = pygame.image.load("Ludo_Icons/Dice_6.jpg")
        self.dice_list = [self.state_1, self.state_2, self.state_3, self.state_4, self.state_5, self.state_6]

    def update(self, a):
        screen.blit(self.dice_list[a-1], (245, 245))


## Old Code ##

from threading import Thread

## End Old Code ##

async def main():
    a = 0
    d = 0
    running = True

    # x & y coordination of moves
    piece_listy = [(135, 450), (227, 470), (227, 435), (227, 400), (227, 365), (227, 330), (192, 295), (157, 295),
                   (122, 295),
                   (87, 295), (52, 295), (17, 295), (17, 260), (17, 225), (52, 225), (87, 225), (122, 225), (157, 225),
                   (192, 225), (227, 190), (227, 155), (227, 120), (227, 85), (227, 50), (227, 15), (262, 15), (297, 15),
                   (297, 50), (297, 85), (297, 120), (297, 155), (297, 190), (332, 225), (367, 225), (402, 225), (437, 225),
                   (472, 225), (507, 225), (507, 260), (507, 295), (472, 295), (437, 295), (402, 295), (367, 295),
                   (332, 295), (297, 330), (297, 365), (297, 400), (297, 435), (297, 470), (297, 505), (262, 505),
                   (262, 470), (262, 435), (262, 400), (262, 365), (262, 330), (262, 295)]
    piece_listb = [(75, 130), (52, 225), (87, 225), (122, 225), (157, 225), (192, 225), (227, 190), (227, 155), (227, 120),
                   (227, 85),
                   (227, 50), (227, 15), (262, 15), (297, 15), (297, 50), (297, 85), (297, 120), (297, 155), (297, 190),
                   (332, 225), (367, 225), (402, 225), (437, 225), (472, 225), (507, 225), (507, 260), (507, 295),
                   (472, 295), (437, 295), (402, 295), (367, 295), (332, 295), (297, 330), (297, 365), (297, 400),
                   (297, 435), (297, 470), (297, 505), (262, 505), (227, 505), (227, 470), (227, 435), (227, 400),
                   (227, 365), (227, 330), (192, 295), (157, 295), (122, 295), (87, 295), (52, 295), (17, 295), (17, 260),
                   (52, 260), (87, 260), (122, 260), (157, 260), (192, 260), (227, 260)]
    piece_listr = [(392, 70), (297, 50), (297, 85), (297, 120), (297, 155), (297, 190), (332, 225), (367, 225), (402, 225),
                   (437, 225), (472, 225), (507, 225), (507, 260), (507, 295), (472, 295), (437, 295), (402, 295),
                   (367, 295), (332, 295), (297, 330), (297, 365), (297, 400), (297, 435), (297, 470), (297, 505),
                   (262, 505), (227, 505), (227, 470), (227, 435), (227, 400), (227, 365), (227, 330), (192, 295),
                   (157, 295), (122, 295), (87, 295), (52, 295), (17, 295), (17, 260), (17, 225), (52, 225), (87, 225),
                   (122, 225), (157, 225), (192, 225), (227, 190), (227, 155), (227, 120), (227, 85), (227, 50), (227, 15),
                   (262, 15), (262, 50), (262, 85), (262, 120), (262, 155), (262, 190), (262, 225)]


    # Create needed classes and definitions:
    yellow_piece = Pieces("Ludo_Icons/yellow.png", (135, 450), "in", piece_listy, "Yellow Turn")
    red_piece = Pieces("Ludo_Icons/red.png", (392, 70), "in", piece_listr, "Red Turn")
    blue_piece = Pieces("Ludo_Icons/blue.png", (75, 130), "in", piece_listb, "Blue Turn")
    Piece_List = [yellow_piece, red_piece, blue_piece]
    game = Ludo_Game(Piece_List)
    dice = Dice()

    # game loop
    while running:
    
        # fill the screen with black colour
        screen.fill((0, 0, 0))
        # check for the event happen in pygame
        for event in pygame.event.get():
    
            # check if exit key is pressed
            if event.type == pygame.QUIT:
                running = False
    
            # check if key is pressed
            if event.type == pygame.KEYDOWN:
                # space key to change the dice
                if event.key == pygame.K_SPACE:
                    # pygame.time.wait(800)
                    a = random.randint(1, 6)
                    d = a
                    last_turn = game.turn
                    if game.turn == "Yellow Turn":
                        # Piece will out first only when 6 appears
                        if a == 6 and game.piece_list[0].state == "in":
                            game.piece_list[0].state = "out"
                            final_position = 1
                        # if piece are already out
                        elif game.piece_list[0].state == "out":
                            last_posy = game.piece_list[0].final_position
                            game.piece_list[0].final_position = game.piece_list[0].initial_position + a
                            if game.piece_list[0].final_position > 57:
                                game.piece_list[0].final_position = last_posy
                        # if initially 6 is not appears then make a=0
                        else:
                            a = 0
                        game.turn = "Blue Turn"
                        if a == 6:
                            game.turn = "Yellow Turn"

                    elif game.turn == "Blue Turn":
                        # Piece will out first only when 6 appers
                        if a == 6 and game.piece_list[2].state == "in":
                            game.piece_list[2].state = "out"
                            game.piece_list[2].final_position = 1
                        # if piece are already out
                        elif game.piece_list[2].state == "out":
                            last_posb = game.piece_list[2].final_position
                            game.piece_list[2].final_position = game.piece_list[2].initial_position + a
                            if game.piece_list[2].final_position > 57:
                                game.piece_list[2].final_position = last_posb
                        # if initially 6 is not appears then make a=0
                        else:
                            a = 0
                        game.turn = "Red Turn"
                        if a == 6:
                            game.turn = "Blue Turn"
                    elif game.turn == "Red Turn":
                        # Piece will out first only when 6 appears
                        if a == 6 and game.piece_list[1].state == "in":
                            game.piece_list[1].state = "out"
                            game.piece_list[1].final_position = 1
                        # if piece are already out
                        elif game.piece_list[1].state == "out":
                            last_posr = game.piece_list[1].final_position
                            game.piece_list[1].final_position = game.piece_list[1].initial_position + a
                            if game.piece_list[1].final_position > 57:
                                game.piece_list[1].final_position = last_posr
                        # if initially 6 is not appears then make a=0
                        else:
                            a = 0
                        game.turn = "Yellow Turn"
                        if a == 6:
                            game.turn = "Red Turn"
    
        game.update()
        screen.blit(game.blastimg, (84, 295))
        screen.blit(game.blastimg, (294, 435))
        screen.blit(game.blastimg, (224, 82))
        screen.blit(game.blastimg, (437, 225))
    
        # to show dice
        if d != 0:
            dice.update(d)
        # to show piece
        if a == 0:
            if game.piece_list[0].state == "in":
                game.piece_list[0].update(game.piece_list[0].x, game.piece_list[0].y)
            if game.piece_list[2].state == "in":
                game.piece_list[2].update(game.piece_list[2].x, game.piece_list[2].y)
            if game.piece_list[1].state == "in":
                game.piece_list[1].update(game.piece_list[1].x, game.piece_list[1].y)
    
        # to move piece
        game.move_piece(2, game.piece_list[2].final_position, game.piece_list[0].final_position, game.piece_list[1].final_position, game.turn)
        game.move_piece(0, game.piece_list[0].final_position, game.piece_list[2].final_position, game.piece_list[1].final_position, game.turn)
        game.move_piece(1, game.piece_list[1].final_position, game.piece_list[0].final_position, game.piece_list[2].final_position, game.turn)
    
        # update the display
        pygame.display.update()
        await asyncio.sleep(0)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    asyncio.run(main())