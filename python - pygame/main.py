import pygame
import random
import sys

pygame.init()

width, height = 800, 599
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Throne of IMRAT")

Colour1 = (255, 255, 255)
Colour2 = (0, 0, 0)
Colour3 = (255, 0, 0)
Colour4 = (0, 255, 0)
Colour5 = (0, 0, 255)                                                                       
Colour6 = (255, 255, 0)

bg_image1 = pygame.image.load("background_image1.jpg")
bg_image1 = pygame.transform.scale(bg_image1, (width, height))

bg_image2 = pygame.image.load("background_image2.jpg")
bg_image2 = pygame.transform.scale(bg_image2, (width, height))


pygame.mixer.music.load("background_music.mp3")
pygame.mixer.music.play(-1)

font = pygame.font.Font(None, 36)

houses = {
    1: {"name": "Targaryen", "loyalty": 40, "gold": 80, "army": 300},
    2: {"name": "Stark", "loyalty": 70, "gold": 50, "army": 200},
    3: {"name": "Lannister", "loyalty": 30, "gold": 200, "army": 150},
}

win_conditions = {
    "Targaryen": {"army": 500, "loyalty": 60},
    "Stark": {"loyalty": 80, "army": 200},
    "Lannister": {"gold": 300, "loyalty": 50},
}

def draw_text(text, x, y, color=Colour1):
    label = font.render(text, True, color)
    screen.blit(label, (x, y))

def show_temporary_message(text, duration=999):
    overlay = screen.copy()
    draw_text(text, 200, 500, Colour6)
    pygame.display.flip()
    pygame.time.set_timer(pygame.USEREVENT, duration)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.USEREVENT:
                pygame.time.set_timer(pygame.USEREVENT, 0)
                screen.blit(overlay, (0, 0))
                pygame.display.flip()
                return
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

def welcome_screen():
    screen.blit(bg_image1, (0, 0))
    draw_text("Welcome to Throne of Choices!", 250, 50, Colour1)
    draw_text("Press Enter to Continue", 300, 500, Colour1)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key in [pygame.K_RETURN, pygame.K_KP_ENTER]:
                return

def choose_house():
    screen.blit(bg_image2, (0, 0))
    draw_text("Choose Your House:", 300, 50, Colour1)
    draw_text("1. Targaryen", 300, 150, Colour3)
    draw_text("2. Stark", 300, 250, Colour4)
    draw_text("3. Lannister", 300, 350, Colour5)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_KP1, pygame.K_KP2, pygame.K_KP3]:
                    return int(event.unicode)
                else:
                    show_temporary_message("Wrong key pressed! Please try again.", 1500)

def risky_decision():
    events = [
        ("gain_gold", random.randint(10, 50)),
        ("lose_gold", random.randint(10, 50)),
        ("increase_loyalty", random.randint(5, 20)),
        ("decrease_loyalty", random.randint(5, 20)),
        ("improve_army", random.randint(10, 30)),
        ("weaken_army", random.randint(10, 30)),
    ]
    return random.choice(events)

def play_game(selected_house):
    house = houses[selected_house]
    name = house["name"]
    resources = house.copy()

    for turn in range(1, 6):
        screen.blit(bg_image2, (0, 0))
        draw_text(f"Turn {turn}/5 - {name}", 300, 50, Colour1)
        draw_text(f"Loyalty: {resources['loyalty']}", 50, 100, Colour1)
        draw_text(f"Gold: {resources['gold']}", 50, 150, Colour1)
        draw_text(f"Army: {resources['army']}", 50, 200, Colour1)
        draw_text("Choose an action:", 300, 250, Colour1)
        draw_text("1. Recruit Soldiers", 300, 300, Colour1)
        draw_text("2. Bribe Allies", 300, 350, Colour1)
        draw_text("3. Fortify Defenses", 300, 400, Colour1)
        draw_text("4. Risky Decision", 300, 450, Colour1)
        pygame.display.flip()

        action = None
        while action is None:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key in [pygame.K_1, pygame.K_2, pygame.K_3, pygame.K_4, pygame.K_KP1, pygame.K_KP2, pygame.K_KP3, pygame.K_KP4]:
                        action = int(event.unicode)
                    else:
                        show_temporary_message("Wrong key pressed! Please try again.", 1500)

        animate_turn(resources, action)

        if action == 1 and resources['gold'] >= 20:
            resources['gold'] -= 20
            resources['army'] += 50
        elif action == 2 and resources['gold'] >= 15:
            resources['gold'] -= 15
            resources['loyalty'] += 10
        elif action == 3 and resources['gold'] >= 10:
            resources['gold'] -= 10
            resources['army'] += 20
        elif action == 4:
            event, value = risky_decision()
            if event == "gain_gold":
                resources['gold'] += value
            elif event == "lose_gold":
                resources['gold'] -= value
            elif event == "increase_loyalty":
                resources['loyalty'] += value
            elif event == "decrease_loyalty":
                resources['loyalty'] -= value
            elif event == "improve_army":
                resources['army'] += value
            elif event == "weaken_army":
                resources['army'] -= value

        pygame.time.delay(200)

    check_victory(name, resources)

def animate_turn(resources, action):
    for _ in range(3):
        screen.fill(Colour2)
        draw_text(f"Action {action} in progress...", 300, 300, Colour6)
        pygame.display.flip()
        pygame.time.delay(100)

def check_victory(name, resources):
    screen.blit(bg_image2, (0, 0))
    goal = win_conditions[name]
    if all(resources[key] >= goal[key] for key in goal):
        draw_text(f"Victory! {name} achieved their goals!", 200, 300, Colour4)
    else:
        draw_text(f"Defeat! {name} failed to meet their goals!", 200, 300, Colour3)
    pygame.display.flip()
    pygame.time.delay(3000)
    restart_or_quit()

def restart_or_quit():
    screen.blit(bg_image2, (0, 0))
    draw_text("Game Over. What would you like to do?", 200, 250, Colour1)
    draw_text("1. Restart", 300, 350, Colour4)
    draw_text("2. Quit", 300, 400, Colour3)
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key in [pygame.K_1, pygame.K_KP1]:
                    main()
                elif event.key in [pygame.K_2, pygame.K_KP2]:
                    pygame.quit()
                    sys.exit()

def main():
    welcome_screen()
    selected_house = choose_house()
    play_game(selected_house)

main()
