/**
 * @param {number[]} nums
 * @return {number[][]}
 * 15번 문제.
 */
 var threeSum = function(nums) {

    let result = [];

    let sortedNums = nums.sort((a,b)=> {
        return a - b
    });

    for( let i = 0; i < sortedNums.length - 2; i++){

        if( i > 0 && sortedNums[i] == sortedNums[i - 1 ]){
            continue
        }

        let left = i+1, right = sortedNums.length -1;

        while( left < right ){
            let sum = nums[i] + nums[left] + nums[right];

            if(sum < 0){
                left += 1
            } else if( sum > 0){
                right -= 1
            } else {
                result.push([nums[i], nums[left], nums[right]]);

                while(left < right && nums[left] == nums[left+1]){
                    left += 1
                }
                while(left < right && nums[right] == nums[right-1]){
                    right -= 1
                }

                left += 1;
                right -= 1;
            }
        }
    }

    return result
};

let nums = [-1,0,1,2,-1,-4];

console.log(threeSum(nums))