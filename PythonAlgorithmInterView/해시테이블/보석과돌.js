
/**
 * @param {string} jewels
 * @param {string} stones
 * @return {number}
 * 771번문제
 */
 var numJewelsInStones = function(jewels, stones) {
    
    let freqs = new Map();
    let count = 0;


    for( let i = 0 ; i < stones.length; i++){
        let char = stones[i];

        if( freqs.get(char) === undefined ){
            freqs.set(char, 1)
        } else {
            freqs.set(char, freqs.get(char)+1)
        }
    }

    for( let i = 0; i < jewels.length; i++){
        let char = jewels[i];
        let c= freqs.get(char)
        if( c !== undefined){
            count += c
        }

    }

    return count

};


let jewels = "aA", stones = "aAAbbbb";

console.log(numJewelsInStones(jewels, stones))