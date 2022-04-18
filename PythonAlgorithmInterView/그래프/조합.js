/**
 * @param {number} n
 * @param {number} k
 * @return {number[][]}
 * 문제 77번
 */
 var combine = function(n, k) {
    
    let result = [];

    function dfs(elements, start, k){
        if(k == 0){
            result.push(elements.slice());
            return;
        }

        for(let i = start; i < n+1; i++){
            elements.push(i);
            dfs(elements, i+1, k-1);
            elements.pop();
        }
    }

    dfs([], 1, k);

    return result
};


let n = 4, k = 2;
console.log( combine(n,k))