function solution(brown, yellow) {
    var answer = [];

    let totalSize = brown + yellow;

    let row = 1;
    let column = 1;
    while(row <= column){
        if(totalSize % row == 0){
            column =  totalSize / row;
            row++;
            continue
        }
        row++
    }
    row -= 1;


    let testY = ( row - 2 ) * ( column  - 2);
    let testB = ( row * 2 ) + row * ( column - 2 ) - testY;

    console.log(testY,testB)

    if( yellow == testY && brown == testB){
        return [row,column]
    }
}

// console.log(solution(10,2));
// console.log(solution(8,1));
console.log(solution(5000,2497));