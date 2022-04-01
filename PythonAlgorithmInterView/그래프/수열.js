/**
 * @param {number[]} nums
 * @return {number[][]}
 * 46번 문제.
 */
 var permute = function(nums = []) {

    let result = []
    let prev_ele = [];

    let dfs = (elements) => {

        if(elements.length == 0){
            result.push(prev_ele.slice());
            return
        }


        for( let i =0; i < elements.length; i++){
            let next_ele = elements.slice();
            next_ele.splice(i,1);
            
            prev_ele.push(elements[i]);
            dfs(next_ele);
            prev_ele.pop()
        }
    }

    dfs(nums)

    return result
};


let nums = [1,2,3];

console.log(permute(nums))