import pygame
import sys
import os
import traceback

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        base_path = sys._MEIPASS
    else:
        base_path = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(base_path, relative_path)

try:
    pygame.init()
    pygame.mixer.init()  # explicit mixer init

    SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
    FPS = 30
    audio_enabled = True

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Bongocat App")

    clock = pygame.time.Clock()

    cat_idle_img = pygame.image.load(resource_path("assets/cat_idle.png")).convert_alpha()
    cat_tap1 = pygame.image.load(resource_path("assets/cat_tap1.gif")).convert_alpha()
    cat_tap2 = pygame.image.load(resource_path("assets/cat_tap2.gif")).convert_alpha()
    bongo_sound = pygame.mixer.Sound(resource_path("assets/bongo.wav"))

    idle = True
    tap_frames = [cat_tap1, cat_tap2]
    tap_index = 0
    tap_timer = 0
    tap_delay = 200  # ms

    def draw():
        screen.fill((255, 255, 255))
        if idle:
            img = cat_idle_img
        else:
            img = tap_frames[tap_index]

        screen.blit(img, (SCREEN_WIDTH//2 - img.get_width()//2, SCREEN_HEIGHT//2 - img.get_height()//2))

        font = pygame.font.SysFont(None, 30)
        text = font.render(f"Audio: {'ON' if audio_enabled else 'OFF'} (Press A to toggle)", True, (0,0,0))
        screen.blit(text, (10, 10))

        pygame.display.flip()

    running = True

    while running:
        dt = clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                elif event.key == pygame.K_a:
                    audio_enabled = not audio_enabled

            elif event.type == pygame.MOUSEBUTTONDOWN:
                idle = False
                tap_index = 0
                tap_timer = 0
                if audio_enabled:
                    bongo_sound.play()

        if not idle:
            tap_timer += dt
            if tap_timer > tap_delay:
                tap_timer = 0
                tap_index += 1
                if tap_index >= len(tap_frames):
                    idle = True

        draw()

    pygame.quit()
    sys.exit()

except Exception:
    print("An error occurred:")
    traceback.print_exc()
    input("Press Enter to exit...")
