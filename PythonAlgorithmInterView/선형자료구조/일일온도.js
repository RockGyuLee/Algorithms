/**
 * @param {number[]} temperatures
 * @return {number[]}
 * 739문제.
 */
 var dailyTemperatures = function(temperatures) {
    let stack = [];
    let answer = new Array(temperatures.length).fill(0);

    temperatures.forEach( (temp, index)=> {

        while( stack.length > 0 && temp > temperatures[stack[stack.length-1]]){
            last = stack.pop();
            answer[last] = index - last
        }
        stack.push(index)
    })

    return answer
};

let temperatures = [73,74,75,71,69,72,76,73];
console.log(dailyTemperatures(temperatures))