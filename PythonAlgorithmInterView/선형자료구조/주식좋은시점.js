/**
 * @param {number[]} prices
 * @return {number}
 * 121번 문제.
 */
 var maxProfit = function(prices) {
    let minValue = 10001;
    let maxValue = 0;

    prices.forEach(price=>{
        minValue = Math.min(minValue, price)
        maxValue = Math.max(maxValue, price - minValue)
    })
    return(maxValue)
};


let prices = [7,1,5,3,6,4];
console.log(maxProfit(prices))