
import pygame
import random
import sys

pygame.init()

# Configurações da tela
LARGURA = 800
ALTURA = 600
TELA = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Rato em Busca do Queijo")

# Cores
BRANCO = (255, 255, 255)
CINZA = (150, 150, 150)
ROSA = (255, 150, 180)
AMARELO = (255, 210, 0)
LARANJA = (220, 150, 0)
PRETO = (0, 0, 0)
VERDE = (100, 200, 100)

# Relógio e pontuação
relogio = pygame.time.Clock()
pontos = 0
fonte = pygame.font.SysFont(None, 36)

# Rato
rato = pygame.Rect(100, 100, 40, 40)
velocidade = 5

# Queijo
queijo = pygame.Rect(
    random.randint(0, LARGURA - 30),
    random.randint(50, ALTURA - 30),
    30, 30
)


def desenhar_rato():
    # Corpo
    pygame.draw.ellipse(TELA, CINZA, rato)

    # Orelhas
    pygame.draw.circle(TELA, CINZA, (rato.x + 8, rato.y + 5), 10)
    pygame.draw.circle(TELA, ROSA, (rato.x + 8, rato.y + 5), 5)
    pygame.draw.circle(TELA, CINZA, (rato.x + 30, rato.y + 5), 10)
    pygame.draw.circle(TELA, ROSA, (rato.x + 30, rato.y + 5), 5)

    # Olho e nariz
    pygame.draw.circle(TELA, PRETO, (rato.x + 28, rato.y + 17), 3)
    pygame.draw.circle(TELA, ROSA, (rato.x + 38, rato.y + 23), 4)


def desenhar_queijo():
    # Queijo triangular
    pontos_queijo = [
        (queijo.x, queijo.y),
        (queijo.x + 30, queijo.y + 10),
        (queijo.x + 5, queijo.y + 30)
    ]
    pygame.draw.polygon(TELA, AMARELO, pontos_queijo)

    # Furinhos do queijo
    pygame.draw.circle(TELA, LARANJA, (queijo.x + 10, queijo.y + 10), 3)
    pygame.draw.circle(TELA, LARANJA, (queijo.x + 20, queijo.y + 16), 3)


# Loop principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimentação pelas setas
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT]:
        rato.x -= velocidade
    if teclas[pygame.K_RIGHT]:
        rato.x += velocidade
    if teclas[pygame.K_UP]:
        rato.y -= velocidade
    if teclas[pygame.K_DOWN]:
        rato.y += velocidade

    # Impede o rato de sair da tela
    rato.clamp_ip(TELA.get_rect())

    # Detecta colisão com o queijo
    if rato.colliderect(queijo):
        pontos += 1

        # Reposiciona o queijo aleatoriamente
        queijo.x = random.randint(0, LARGURA - queijo.width)
        queijo.y = random.randint(50, ALTURA - queijo.height)

    # Desenha o cenário
    TELA.fill(VERDE)

    desenhar_rato()
    desenhar_queijo()

    # Mostra a pontuação
    texto = fonte.render(f"Pontos: {pontos}", True, PRETO)
    TELA.blit(texto, (10, 10))

    pygame.display.update()
    relogio.tick(60)
