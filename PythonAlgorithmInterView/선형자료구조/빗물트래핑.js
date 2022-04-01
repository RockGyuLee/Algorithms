/**
 * @param {number[]} height
 * @return {number}
 * 42번 문제.
 */

// 투 포인터를 이용하여 배열중 가장 큰 값을 확인 후 좌측 포인터와 우측 포인터의 최대 값을 비교하면서 옆으로 전진한다.
 var trap = function(height) {

    let volume = 0;

    let left = 0, right = height.length - 1;

    let left_max = height[left], right_max = height[right];

    // 배열 index left가 right를 넘으면 loop를 빠져나온다.
    while(left < right){

        left_max = Math.max(left_max, height[left]);
        right_max = Math.max(right_max, height[right]);

        if( left_max <= right_max){
            volume += left_max - height[left];
            left += 1;
        } else{
            volume += right_max - height[right];
            right -= 1;
        }
    }
    return volume;
};
let height = [0,1,0,2,1,0,1,3,2,1,2,1];
console.log(trap(height))