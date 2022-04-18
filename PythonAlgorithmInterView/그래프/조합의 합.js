/**
 * @param {number[]} candidates
 * @param {number} target
 * @return {number[][]}
 * 문제 39번
 */
 var combinationSum = function(candidates, target) {
    
    let result = [];

    function dfs(csum, index, path){

        if( csum < 0 ){
            return;
        }
        if ( csum == 0 ){
            result.push(path)
        }

        for( let i = index; i < candidates.length; i++){
            dfs( csum - candidates[i], i, path.concat(candidates[i]));
        }
    }

    dfs(target, 0, [])

    return result;
};

let candidates = [2,3,6,7], target = 7;

console.log(combinationSum(candidates, target))
