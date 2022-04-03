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

function spiralOrder(matrix) {
    //The array to store the result
    let result = [];
    //if the matrix is empty, return the result as it is
    if (matrix.length === 0) return result;

    //The four directions in the matrix
    // we need 4 pointers to keep track of the current position in the matrix

    let rowStart = 0; // keeps track of the row start index
    let rowEnd = matrix.length - 1; // keeps track of the row end index
    let colStart = 0; // keeps track of the col start index
    let colEnd = matrix[0].length - 1; // keeps track of the col end index

    //The while loop will run until the rowStart is less than the rowEnd and the colStart is less than the colEnd
    //this is because as wee move the pointers, we need to make sure we are not out of bounds
    // in the end of the loop the rowStart will be equal to the rowEnd and the colStart will be equal to the colEnd
    // at this pint we know that we have traversed the entire matrix
    // this is because all the pointers will point to the same index

    while (rowStart <= rowEnd && colStart <= colEnd) {
        //we need to print the elements in the top row from left to right 
        for (let i = colStart; i <= colEnd; i++) {
            result.push(matrix[rowStart][i]);
        }
        //we now need to move the rowStart pointer to the next row so that we do not print that row again
        rowStart++;



        //we need to print the elements in the right column from top to bottom
        for (let i = rowStart; i <= rowEnd; i++) {
            result.push(matrix[i][colEnd]);
        }
        //we now need to move the colEnd pointer to the next column so that we do not print that column again
        colEnd--;


        //we need to print the elements in the bottom row from right to left
        if (rowStart <= rowEnd) {
            for (let i = colEnd; i >= colStart; i--) {
                result.push(matrix[rowEnd][i]);
            }
        }
        //we now need to move the rowEnd pointer to the next row so that we do not print that row again
        rowEnd--;

        //we need to print the elements in the left column from bottom to top
        if (colStart <= colEnd) {
            for (let i = rowEnd; i >= rowStart; i--) {
                result.push(matrix[i][colStart]);
            }
        }
        //we now need to move the colStart pointer to the next column so that we do not print that column again
        colStart++;
    }
    return result;
}

console.log(spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]]));