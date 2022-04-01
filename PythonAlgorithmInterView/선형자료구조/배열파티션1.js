/**
 * @param {number[]} nums
 * @return {number}
 * 561번 문제.
 */
 var arrayPairSum = function(nums) {

    let minArr = []
    let sum = 0;

    nums.sort((a, b)=> a-b)

    nums.forEach((num)=> {
        minArr.push(num)

        if(minArr.length == 2){
            sum += Math.min(minArr[0], minArr[1]);
            minArr = []
        }
    })
    return sum
};

let nums = [1,4,3,2];
console.log(arrayPairSum(nums))