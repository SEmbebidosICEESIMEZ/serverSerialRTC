import pygame
import time

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Loading Screen")

# Load a font
font = pygame.font.SysFont('Arial', 30)

# Define the narrative dialogues
narrative_dialogues = [
    "Welcome to the Labyrinth of Whispers.",
    "You will face many challenges ahead.",
    "Trust your instincts and stay alert.",
    "The whispers will guide you, but beware of the shadows."
]

def loading_screen():
    for dialogue in narrative_dialogues:
        # Fill the screen with a color or background image
        screen.fill((0, 0, 0))  # Black background
        
        # Render the dialogue text
        text_surface = font.render(dialogue, True, (255, 255, 255))  # White text
        text_rect = text_surface.get_rect(center=(400, 300))  # Center the text
        screen.blit(text_surface, text_rect)
        
        # Update the display
        pygame.display.flip()
        
        # Wait for a short duration
        time.sleep(2)  # Adjust the duration as needed

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    loading_screen()  # Call the loading screen function

# Quit Pygame
pygame.quit()