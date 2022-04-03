/*
Question: 
Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:
Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]


*/

var spiralOrder = function (matrix) {
    const res = []

    let row = 0;
    let maxRow = matrix.length - 1;
    let col = 0
    let maxCol = matrix[0].length - 1;
    // direction is a variable that will keep track of the direction we are moving in the matrix
    let d = 0; // 0 = right, 1 = down, 2 = left, 3 = up

    while (row <= maxRow && col <= maxCol) {
        if (d === 0) {
            for (let i = col; i <= maxCol; i++) {
                res.push(matrix[row][i])
            }
            row++
        }


        if (d === 1) {
            for (let i = row; i <= maxRow; i++) {
                res.push(matrix[i][maxCol])
            }
            maxCol--;
        }

        if (d === 2) {
            for (let i = maxCol; i >= col; i--) {
                res.push(matrix[maxRow][i])
            }
            maxRow--
        }

        if (d === 3) {
            for (let i = maxRow; i >= row; i--) {
                res.push(matrix[i][col])
            }
            col++
        }


        d = (d + 1) % 4;


    }

    return res;

    F

};


console.log(spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]));