import pygame
pygame.init()

screen = pygame.display.set_mode((450, 600))
timer_font = pygame.font.SysFont("Calibri", 38)

start_time = pygame.time.get_ticks()
time_hms = 0, 0
timer_surf = timer_font.render(f'{time_hms[0]:02d}:{time_hms[1]:02d}', True, (255, 255, 255))

running = True
while running:
    print(".")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    time_ms = pygame.time.get_ticks() - start_time
    new_hms = (time_ms//(1000*60)), (time_ms//1000)%60
    if new_hms != time_hms:
        time_hms = new_hms
        timer_surf = timer_font.render(f'{time_hms[0]:02d}:{time_hms[1]:02d}', True, (255, 255, 255))

    screen.fill(0)
    screen.blit(timer_surf, (300, 20))
    pygame.display.update()

pygame.quit()