#include "sudoku.h"


void print_board(u_int8_t*** board, u_int8_t size) {
    u_int8_t n = size * size;
    for (u_int8_t i = 0; i < n; ++i) {
        for (u_int8_t j = 0; j < n; ++j) {
            printf(" %d |", (*board)[i][j]);
        }
        printf("\n");
    }
}


int main(int argc, char** argv) {
    u_int8_t size = 3;
    u_int8_t** board;
    generate_board(&board, size);
    print_board(&board, size);
    return 0;
}
