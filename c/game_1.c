#include <SDL2/SDL.h>

int main() {
    // Inicializa a SDL
    SDL_Init(SDL_INIT_VIDEO);

    // Cria uma janela
    SDL_Window* window = SDL_CreateWindow("Simple Game", SDL_WINDOWPOS_UNDEFINED, SDL_WINDOWPOS_UNDEFINED, 640, 480, 0);

    // Cria um renderer
    SDL_Renderer* renderer = SDL_CreateRenderer(window, -1, SDL_RENDERER_ACCELERATED);

    // Posição inicial do quadrado
    int x = 100;
    int y = 100;

    // Loop principal do jogo
    int quit = 0;
    SDL_Event event;
    while (!quit) {
        // Lida com eventos
        while (SDL_PollEvent(&event) != 0) {
            if (event.type == SDL_QUIT) {
                quit = 1;
            }
            else if (event.type == SDL_KEYDOWN) {
                switch (event.key.keysym.sym) {
                    case SDLK_UP:
                        y -= 10;
                        break;
                    case SDLK_DOWN:
                        y += 10;
                        break;
                    case SDLK_LEFT:
                        x -= 10;
                        break;
                    case SDLK_RIGHT:
                        x += 10;
                        break;
                }
            }
        }

        // Limpa a tela
        SDL_RenderClear(renderer);

        // Desenha o quadrado
        SDL_Rect rect = {x, y, 20, 20};
        SDL_SetRenderDrawColor(renderer, 255, 0, 0, 255);
        SDL_RenderFillRect(renderer, &rect);

        // Atualiza a tela
        SDL_RenderPresent(renderer);

        // Espera um curto período de tempo (ajuste conforme necessário)
        SDL_Delay(16); // Aproximadamente 60 FPS
    }

    // Libera recursos
    SDL_DestroyRenderer(renderer);
    SDL_DestroyWindow(window);
    SDL_Quit();

    return 0;
}