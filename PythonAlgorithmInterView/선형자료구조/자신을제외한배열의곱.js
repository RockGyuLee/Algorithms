/**
 * @param {number[]} nums
 * @return {number[]}
 * 238번 문제.
 */
 var productExceptSelf = function(nums) {
    
    let result = [];
    let numsSize = nums.length;

    let pointer = 1;

    for(let i = 0; i< numsSize; i++){
        result.push(pointer)
        pointer *= nums[i]
    }

    pointer = 1;

    for(let i = numsSize-1; i >= 0; i--){
        result[i] *= pointer
        pointer *= nums[i]
    }

    return result

};

let nums = [1,2,3,4];
console.log(productExceptSelf(nums))