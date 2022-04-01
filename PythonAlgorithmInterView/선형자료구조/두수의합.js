/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
 var twoSum = function(nums, target) {
    
    for(let i = 0; i < nums.length; i++){
        for(let j = i+1; j < nums.length; j++){
            if(nums[i] + nums[j] == target){
                return [i, j]
            }
        }
    }
};

// 자바스크립트 경우 이렇게 푸는게 더 느리게 된다. 왜냐하면 slice, findIndex가 n시간만큼 걸리기 때문이다.
var twoSum2 = function(nums, target) {
    
    for(let i = 0; i < nums.length; i++){
        
        let ele = target - nums[i];

        let findIndex = nums.slice(i+1).findIndex((num)=> num == ele );

        console.log(
            nums.slice(i+1), findIndex
        )

        if( findIndex >= 0 ){
            return [i, findIndex + ( i + 1)]
        }
    }
};

// 객체에 값을 할당하여 시간복잡도를 줄일 수 있다. 
var twoSum3 = function(nums, target) {
    
    let nums_map = {}

    nums.forEach(( num, index )=> nums_map[num] = index)

    for(let i = 0; i < nums.length; i++){
        console.log(nums.indexOf(target - nums[i]))
        if( nums.indexOf(target - nums[i]) >= 0  && i != nums_map[target - nums[i]] ){
            return [ i, nums_map[target - nums[i]]]
        }
    }
};

// 객체에 값을 할당하여 시간복잡도를 줄일 수 있다. 자바스크립트같은 경우 n번 만큼 걸리는 시간을 줄이는게 제일 좋다.
var twoSum4 = function(nums, target) {
    
    let nums_map = {}

    for( let i = 0; i < nums.length; i++){
        // console.log(nums_map, target - nums[i])
        if( nums_map[target - nums[i]] >= 0){
            return [nums_map[target - nums[i]], i]
        }
        nums_map[nums[i]] = i
    }
    
};
let nums = [2,7,11,15];
let target = 9
console.log(twoSum4(nums, target))