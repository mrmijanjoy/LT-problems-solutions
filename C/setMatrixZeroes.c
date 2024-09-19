#include <stdbool.h>

void setZeroes(int** matrix, int matrixSize, int* matrixColSize) {
    int m = matrixSize;
    int n = *matrixColSize;
    
    bool firstRowZero = false, firstColZero = false;
    
    // Check if the first row should be set to zero
    for (int j = 0; j < n; j++) {
        if (matrix[0][j] == 0) {
            firstRowZero = true;
            break;
        }
    }
    
    // Check if the first column should be set to zero
    for (int i = 0; i < m; i++) {
        if (matrix[i][0] == 0) {
            firstColZero = true;
            break;
        }
    }
    
    // Use the first row and column to mark zeros
    for (int i = 1; i < m; i++) {
        for (int j = 1; j < n; j++) {
            if (matrix[i][j] == 0) {
                matrix[i][0] = 0;  // Mark row
                matrix[0][j] = 0;  // Mark column
            }
        }
    }
    
    // Set rows and columns based on the marks
    for (int i = 1; i < m; i++) {
        if (matrix[i][0] == 0) {
            for (int j = 1; j < n; j++) {
                matrix[i][j] = 0;
            }
        }
    }
    
    for (int j = 1; j < n; j++) {
        if (matrix[0][j] == 0) {
            for (int i = 1; i < m; i++) {
                matrix[i][j] = 0;
            }
        }
    }
    
    // Handle the first row
    if (firstRowZero) {
        for (int j = 0; j < n; j++) {
            matrix[0][j] = 0;
        }
    }
    
    // Handle the first column
    if (firstColZero) {
        for (int i = 0; i < m; i++) {
            matrix[i][0] = 0;
        }
    }
}
