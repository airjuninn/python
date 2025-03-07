import pygame   
import random

# Inicializa o Pygame
pygame.init()

# Configurações da tela
largura_tela = 600
altura_tela = 400
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Pac-Man Simples")

# Cores
preto = (0, 0, 0)
amarelo = (255, 255, 0)
branco = (255, 255, 255)

# Configurações do Pac-Man
pacman_pos = [100, 100]
pacman_tamanho = 20.0
pacman_velocidade = 5

# Pontos
pontos = []
for _ in range(10):
    x = random.randint(0, largura_tela - pacman_tamanho)
    y = random.randint(0, altura_tela - pacman_tamanho)
    pontos.append([x, y])

# Função para desenhar o Pac-Man
def desenhar_pacman(pos):
    pygame.draw.circle(tela, amarelo, pos, pacman_tamanho // 2)

# Função para desenhar os pontos
def desenhar_pontos(pontos):
    for ponto in pontos:
        pygame.draw.circle(tela, branco, ponto, 5)

# Loop principal do jogo
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Movimentação do Pac-Man
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        pacman_pos[0] -= pacman_velocidade
    if teclas[pygame.K_RIGHT]:
        pacman_pos[0] += pacman_velocidade
    if teclas[pygame.K_UP]:
        pacman_pos[1] -= pacman_velocidade
    if teclas[pygame.K_DOWN]:
        pacman_pos[1] += pacman_velocidade
    if teclas[pygame.K_r]:
        for _ in range(10):
            x = random.randint(0, largura_tela - pacman_tamanho)
            y = random.randint(0, altura_tela - pacman_tamanho)
        pontos.append([x, y])
        def desenhar_pontos(pontos):
            for ponto in pontos:
                pygame.draw.circle(tela, branco, ponto, 5)

    # Limitar movimento dentro da tela
    pacman_pos[0] = max(pacman_tamanho // 2, min(largura_tela - pacman_tamanho // 2, pacman_pos[0]))
    pacman_pos[1] = max(pacman_tamanho // 2, min(altura_tela - pacman_tamanho // 2, pacman_pos[1]))

    # Verificar colisão com os pontos
    for ponto in pontos[:]:
        if (pacman_pos[0] - ponto[0]) ** 2 + (pacman_pos[1] - ponto[1]) ** 2 < (pacman_tamanho // 2) ** 2:
            pontos.remove(ponto)
        if (pacman_pos[0] - ponto[0]) ** 2 + (pacman_pos[1] - ponto[1]) ** 2 < (pacman_tamanho // 2) ** 2:
            pacman_tamanho += 1

    # Atualiza a tela
    tela.fill(preto)
    desenhar_pacman(pacman_pos)
    desenhar_pontos(pontos)
    pygame.display.flip()




    # Controla a taxa de quadros
    pygame.time.Clock().tick(120)

    

pygame.quit()