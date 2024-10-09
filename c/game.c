#include <ncurses.h>

int main() {
    // Inicializa a biblioteca ncurses
    initscr();
    // Habilita a captura das teclas de função (F1, F2, etc.)
    keypad(stdscr, TRUE);
    // Não exibe as teclas pressionadas na tela
    noecho();
    // Não espera pela tecla Enter após a entrada
    nodelay(stdscr, TRUE);

    // Posição inicial do quadrado
    int x = 10;
    int y = 10;

    // Loop principal do jogo
    while (1) {
        // Limpa a tela
        clear();

        // Imprime o quadrado na tela
        mvprintw(y, x,   "  O");
        mvprintw(y+1, x, " 0oa");
        mvprintw(y+2, x, "aa as");
        mvprintw(y+3, x, "aa aa");
        // Atualiza a tela
        refresh();

        // Captura a tecla pressionada
        int key = getch();

        // Verifica a tecla pressionada
        switch (key) {
            case KEY_UP:
                y--;
                break;
            case KEY_DOWN:
                y++;
                break;
            case KEY_LEFT:
                x--;
                break;
            case KEY_RIGHT:
                x++;
                break;
        }

        // Espera um curto período de tempo (ajuste conforme necessário)
        napms(100);
    }

    // Finaliza a biblioteca ncurses
    endwin();

    return 0;
}