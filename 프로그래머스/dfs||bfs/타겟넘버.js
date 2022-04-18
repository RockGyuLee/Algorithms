function solution(numbers, target) {
    var answer = 0;

    //양수 or 음수
    let positive_numbeer_type = [ true, false]

    let dfs = (elements, addNum)=> {
        if(elements.length == 0){
            if(addNum == target){
                answer += 1;
            }
            return;
        }

        for(let index=0; index < positive_numbeer_type.length; index++){
            let isType = positive_numbeer_type[index];
            let copy_ele = elements.slice()
            let value = copy_ele.shift() 

            if(isType){
                addNum += value
                dfs(copy_ele, addNum)
                addNum -= value
            }else {
                addNum -= value
                dfs(copy_ele, addNum)
                addNum += value
            }
        }
    }

    dfs(numbers, 0, target)
    return answer;
}


// let nums = [1, 1, 1, 1, 1];
let nums = [1, 1, 1, 1, 1];
let target = 3;


console.log("solution",solution(nums, target))