#include <SDL2/SDL.h>

int main() {
    // Inicializar a SDL
    if (SDL_Init(SDL_INIT_VIDEO) < 0) {
        printf("Erro ao inicializar a SDL: %s\n", SDL_GetError());
        return 1;
    }

    // Criar uma janela
    SDL_Window* janela = SDL_CreateWindow("Quadrado Colorido", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, 800, 600, SDL_WINDOW_SHOWN);
    if (janela == NULL) {
        printf("Erro ao criar a janela: %s\n", SDL_GetError());
        return 1;
    }

    // Criar um renderer
    SDL_Renderer* renderer = SDL_CreateRenderer(janela, -1, SDL_RENDERER_ACCELERATED | SDL_RENDERER_PRESENTVSYNC);
    if (renderer == NULL) {
        printf("Erro ao criar o renderer: %s\n", SDL_GetError());
        return 1;
    }

    // Definir a cor do quadrado (vermelho no exemplo)
    SDL_SetRenderDrawColor(renderer, 255, 0, 0, 255);

    // Limpar a tela
    SDL_RenderClear(renderer);

    // Definir as coordenadas e dimensões do quadrado
    SDL_Rect quadrado;
    quadrado.x = 100;
    quadrado.y = 100;
    quadrado.w = 200;
    quadrado.h = 200;

    // Desenhar o quadrado na tela
    SDL_RenderFillRect(renderer, &quadrado);

    // Atualizar a tela
    SDL_RenderPresent(renderer);

    // Aguardar um evento de fechamento
    SDL_Event evento;
    int rodando = 1;
    while (rodando) {
        while (SDL_PollEvent(&evento) != 0) {
            if (evento.type == SDL_QUIT) {
                rodando = 0;
            }
        }
    }

    // Liberar recursos
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(janela);
    SDL_Quit();

    return 0;
}