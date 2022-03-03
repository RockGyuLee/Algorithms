/**
 * @param {string} paragraph
 * @param {string[]} banned
 * @return {string}
 */
 var mostCommonWord = function(paragraph, banned) {
    let params = paragraph.toLocaleLowerCase().replace(/[^a-z]/g,' ').split(' ');

    let mostWord = '';
    let mostWordNum = 0;
    let paramDatasset = {}

    let bann = new Set(banned)

    let filterParams = params.filter( param => {

        if( banned.length == 0) return param
        if (param == '') return false

        return !bann.has(param)
    })


    filterParams.forEach( param => {
        paramDatasset[param] =  0
    })

    filterParams.forEach( param => {
        paramDatasset[param] += paramDatasset[param] += 1
        if( mostWordNum < paramDatasset[param] ){
            mostWordNum = paramDatasset[param]
            mostWord = param
        }
    })

    console.log(paramDatasset)

    return mostWord

};

let paragraph = "Bob hit a ball, the hit BALL flew far after it was hit.";
let banned = ["hit"];

// let paragraph = "a.";
// let banned =  [];

// let paragraph = "Bob. hIt, baLl";
// let banned = ["bob", "hit"];

console.log(mostCommonWord(paragraph, banned))