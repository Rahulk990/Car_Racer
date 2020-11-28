import pygame
import random as rn

HEIGHT = 680
WIDTH = 1280

PAUSE = False
WINDOW = 0
CLOCK = 0
IMAGES = 0

COLORS = {
    'Black': (0, 0, 0),
    'Grey': (192, 192, 192),
    'Green': (0, 200, 0),
    'Red': (200, 0, 0),
    'Bright_Green': (0, 255, 0),
    'Yellow': (200, 200, 0),
    'Bright_Red': (255, 0, 0),
    'White': (255, 255, 255)
}


def load_window():
    # To write the Global Variable
    global WINDOW
    global CLOCK

    # Initialize the Pygame
    pygame.init()

    # Set the Screen Dimensions
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))

    # Set the Screen Title
    pygame.display.set_caption('The Car Racer')

    # Set the Game Clock
    CLOCK = pygame.time.Clock()


def destroy_window():
    # Destroys the Pygame Window
    pygame.quit()
    quit()


def load_images():
    # To write the Global Variable
    global IMAGES

    # Load Road Image
    road = pygame.image.load('Data/road.jpg').convert_alpha()

    # Load Player Car Image
    player = pygame.image.load('Data/player.png').convert_alpha()

    # Load Other Car Images
    up = [pygame.image.load('Data/u' + str(x) + '.png').convert_alpha()
          for x in range(1, 5)]
    down = [pygame.image.load('Data/d' + str(x) + '.png').convert_alpha()
            for x in range(1, 5)]

    IMAGES = {
        'Road': road,
        'Player': player,
        'Up_Car': up,
        'Down_Car': down
    }


def display_road(road_img, y1, y2):
    # Moving and Drawing the Road on Window
    y1 += 8

    # Removing Redundant Road
    if y1 > HEIGHT:
        y1 = 0
        y2 = -680

    if y1 > 0:
        WINDOW.blit(road_img, (0, y1))
        y2 += 8
        WINDOW.blit(road_img, (0, y2))

    return (y1, y2)


def display_car(car_img, x, y):
    # Drawing the cars on window
    WINDOW.blit(car_img, (x, y))


def display_text(text, x_coor, y_coor, text_size, text_font="comicsansms"):
    # Set the Text Font and Text Size
    font = pygame.font.SysFont(text_font, text_size)

    # Render the Text on Screen
    TextSurf = font.render(text, True, COLORS['Black'])
    TextRect = TextSurf.get_rect()
    TextRect.center = (x_coor, y_coor)
    WINDOW.blit(TextSurf, TextRect)


def display_button(text, x_coor, y_coor, width, height, fill_color, active_color, action=None):
    # Get Current Mouse Position
    mouse = pygame.mouse.get_pos()

    # Check if Mouse Button is Pressed
    click = pygame.mouse.get_pressed()

    # Check if Mouse is within the Button or not
    if x_coor + width > mouse[0] > x_coor and y_coor + height > mouse[1] > y_coor:
        pygame.draw.rect(WINDOW, active_color,
                         (x_coor, y_coor, width, height))

        # Perform Action if the Mouse Button is Pressed
        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(WINDOW, fill_color, (x_coor, y_coor, width, height))

    # Display Text within the Button
    display_text(text, (x_coor + width / 2),
                 (y_coor + height / 2), 20)


def game_intro():
    # Freeze the Screen until some action is taken
    while True:
        # Handle Events happened in Last Clock
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                destroy_window()

        # Display Text on Window
        WINDOW.fill(COLORS['Yellow'])
        display_text('Start Game!', (WIDTH / 2), (HEIGHT / 2), 75)

        # Display Buttons on Window
        display_button("GO!", 350, 450, 100, 50,
                       COLORS['Green'], COLORS['Bright_Green'], gameloop)
        display_button("Quit", 900, 450, 100, 50,
                       COLORS['Red'], COLORS['Bright_Red'], destroy_window)

        # Update the Window
        pygame.display.update()
        CLOCK.tick(60)


def display_score(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("SCORE: " + str(count), True, COLORS['Black'])
    WINDOW.blit(text, (0, 0))


def display_obstacles(obstacles):
    for obstacle in obstacles:
        display_car(obstacle[2], obstacle[0], obstacle[1])


def move_obstacles(obstacles, speed):
    # Apply Changes to Y_Coordinate
    for obstacle in obstacles:
        obstacle[1] += (rn.choice([0.8, 0.85, 0.9])) * speed

    return obstacles


def check_obstacles(obstacles, obs_height, type):
    total_increment = 0

    # Check for Collision with the Lower Boundary
    for obstacle in obstacles:

        # Removing Object and Initializing New Object if Boundary Hit
        if obstacle[1] > HEIGHT:

            # Setting new Y_Coordinate
            obstacle[1] = -obs_height

            # Setting new X_Coordinate
            if type == 'Down':
                obstacle[0] = rn.randrange(0.55 * WIDTH, 0.95 * WIDTH)
            elif type == 'Up':
                obstacle[0] = rn.randrange(0.05 * WIDTH, 0.45 * WIDTH)

            # Setting new Image
            if type == 'Down':
                obstacle[2] = rn.choice(IMAGES['Down_Car'])
            elif type == 'Up':
                obstacle[2] = rn.choice(IMAGES['Up_Car'])

            # Incrementing Score
            if type == 'Down':
                total_increment += 20
            elif type == 'Up':
                total_increment += 10

    return (total_increment, obstacles)


def crashed(score):
    # Freeze the Screen until some action is taken
    while True:
        # Handle Events happened in Last Clock
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                destroy_window()

        # Display Text on Window
            WINDOW.fill(COLORS['Yellow'])
            display_text('You Crashed!',
                         (WIDTH / 2), (HEIGHT / 2) -25, 50)
            display_text('Score: ' + str(score),
                         (WIDTH / 2), (HEIGHT / 2) + 25, 50)             

        # Display Buttons on Window
        display_button("Play Again!", 350, 450, 100, 50,
                       COLORS['Green'], COLORS['Bright_Green'], gameloop)
        display_button("Quit", 900, 450, 100, 50,
                       COLORS['Red'], COLORS['Bright_Red'], destroy_window)

        # Update the Window
        pygame.display.update()
        CLOCK.tick(60)


def check_crash(px, py, pw, up_obs, down_obs, obs_width, obs_height):
    # Checking Collision with Boundaries
    if px + pw > WIDTH or px < 0 or py < 0 or py > HEIGHT:
        return True

    # Checking Collision with Obstacles
    for obs in up_obs:
        if py < obs[1] + obs_height and py + 155 > obs[1]:
            if px >= obs[0] and px <= obs[0] + obs_width or px + pw >= obs[0] and px + pw <= obs[0] + obs_width:
                return True

    for obs in down_obs:
        if py < obs[1] + obs_height and py + 155 > obs[1]:
            if px >= obs[0] and px <= obs[0] + obs_width or px + pw >= obs[0] and px + pw <= obs[0] + obs_width:
                return True

    return False


def gameloop():
    # To write the Global Variable
    global PAUSE

    # Initialize the Player Coordinates
    x = (WIDTH * 0.45)
    y = (HEIGHT * 0.7)
    player_width = 75

    # Initialize Obstacles
    up_obs = [
        [rn.randrange(0.05 * WIDTH, 0.45 * WIDTH), -
         100, rn.choice(IMAGES['Up_Car'])],
        [rn.randrange(0.05 * WIDTH, 0.45 * WIDTH), -
         200, rn.choice(IMAGES['Up_Car'])],
        [rn.randrange(0.05 * WIDTH, 0.45 * WIDTH), -
         300, rn.choice(IMAGES['Up_Car'])]
    ]
    down_obs = [
        [rn.randrange(0.55 * WIDTH, 0.95 * WIDTH), -400,
         rn.choice(IMAGES['Down_Car'])],
        [rn.randrange(0.55 * WIDTH, 0.95 * WIDTH), -500,
         rn.choice(IMAGES['Down_Car'])],
        [rn.randrange(0.55 * WIDTH, 0.95 * WIDTH), -
         600, rn.choice(IMAGES['Down_Car'])]
    ]
    obs_width = 65
    obs_height = 130

    # Speed Variables
    x_speed = 0
    y_speed = 0
    obs_speed = 8

    # Initialize Road Images
    road1_y = 0
    road2_y = -680

    # Initialize Score
    score = 0

    # Keep on running the Game Loop, until Quit
    while True:

        # Handle Events happened in Last Clock
        for event in pygame.event.get():

            # Quit Command
            if event.type == pygame.QUIT:
                destroy_window()

            # Some key is Pressed
            if event.type == pygame.KEYDOWN:

                # Set the Player's Speed accordingly
                if event.key == pygame.K_LEFT:
                    x_speed = -5
                elif event.key == pygame.K_RIGHT:
                    x_speed = 5
                elif event.key == pygame.K_UP:
                    y_speed = -5
                elif event.key == pygame.K_DOWN:
                    y_speed = 5
                else:
                    paused()

            # Some Key is Released
            if event.type == pygame.KEYUP:

                # Reset the Player's Speed
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    x_speed = 0
                    y_speed = 0

        # Apply the Changes to Player's Position
        x += x_speed
        y += y_speed

        # Apply Changes to Road
        road1_y, road2_y = display_road(IMAGES['Road'], road1_y, road2_y)

        # Display Obstacles
        display_obstacles(up_obs)
        display_obstacles(down_obs)

        # Apply the Changes to Obstacles' Positions
        down_obs = move_obstacles(down_obs, obs_speed - y_speed)
        up_obs = move_obstacles(up_obs, 2 - y_speed)

        # Remove Redundant Obstacles and Increment Score
        up_inc, up_obs = check_obstacles(up_obs, obs_height, 'Up')
        down_inc, down_obs = check_obstacles(down_obs, obs_height, 'Down')
        score += up_inc + down_inc

        # Render Player and Score
        display_car(IMAGES['Player'], x, y)
        display_score(score)

        # Check for Crash
        if check_crash(x, y, player_width, up_obs, down_obs, obs_width, obs_height):
            crashed(score)

        # Update the Window
        pygame.display.update()
        CLOCK.tick(60)


def paused():
    # To write the Global Variable
    global PAUSE

    # Pause the Game
    PAUSE = True

    # Freeze the Screen until some action is taken
    while PAUSE:
        # Handle Events happened in Last Clock
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                destroy_window()

        # Display Text on Window
        WINDOW.fill(COLORS['Yellow'])
        display_text('Paused!', (WIDTH / 2), (HEIGHT / 2), 75)

        # Display Buttons on Window
        display_button("Continue!", 350, 450, 100, 50,
                       COLORS['Green'], COLORS['Bright_Green'], unpause)
        display_button("Quit", 900, 450, 100, 50,
                       COLORS['Red'], COLORS['Bright_Red'], destroy_window)

        # Update the Window
        pygame.display.update()
        CLOCK.tick(60)


def unpause():
    # To write the Global Variable
    global PAUSE

    # Unpause the Game
    PAUSE = False


if __name__ == '__main__':

    # Load the Window
    load_window()

    # Load the Images
    load_images()

    # Start the Game
    game_intro()
