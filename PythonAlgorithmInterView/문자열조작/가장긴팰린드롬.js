/**
 * @param {string} s
 * @return {string}
 * 5번 문제
 */
 var longestPalindrome = function(s) {

    const lenPalindrome = (left, right) => {

        while(left >= 0 && right <= s.length && s[left] == s[right]){
            left -= 1;
            right += 1;
        }

        return s.slice(left+1, right)

    }


    if( s.length < 2 || s ==  s.split('').reverse().join('')){
        return s;
    }

    result = ''

    for(let i = 0; i < s.length; i++){
        let arr = [result, lenPalindrome(i, i+1), lenPalindrome(i, i+2)]
        arr.sort((a,b) => b.length - a.length);
        result = arr[0]
    }

    return result

};

let s = 
'babad'

console.log(longestPalindrome(s))