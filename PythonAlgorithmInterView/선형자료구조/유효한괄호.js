/**
 * @param {string} s
 * @return {boolean}
 * 20번 문제.
 */
 var isValid = function(s) {

    let answer = true
    let stack = [];

    let table = {
        ')':'(',
        '}':'{',
        ']':'['
    }

    let charList = s.split('');

    charList.forEach( char => {
        if( !table[char]){
            stack.push(char)
        } else if( table[char] != stack.pop()){
            answer = false
        }
    })

    if(answer && stack.length == 0){
        return true;
    }
    return false
};


let s = "()"
console.log(isValid(s));