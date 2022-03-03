/**
 * @param {string} s
 * @return {boolean}
 * 125번 문제.
 */
 var isPalindrome = function(s) {
    let replace_str_list = s.toLowerCase().replace(/[^a-z0-9]/g,'').split('');
    
    while(replace_str_list.length > 1){
        if(replace_str_list.pop() != replace_str_list.shift()){
            return false;
        }
    }

    return true;
    
};

console.log(isPalindrome("A man, a plan, a canal: Panama"));
console.log(isPalindrome("race a car"));
console.log(isPalindrome("0P"));
