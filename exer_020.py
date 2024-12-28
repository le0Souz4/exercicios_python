"""
Faça um programa que abra e reproduza o áudio de um
arquivo MP3
"""

import pygame

# Inicializa o mixer do Pygame
pygame.mixer.init()

# Carrega a música
pygame.mixer.music.load('golfinho_symphony.mp3')

# Reproduz a música
pygame.mixer.music.play()

# Mantém o programa rodando enquanto a música toca
input("Pressione Enter para sair enquanto a música toca...")



