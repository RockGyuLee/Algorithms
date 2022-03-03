/**
 * @param {string[]} strs
 * @return {string[][]}
 * 45번 문제.
 */
 var groupAnagrams = function(strs) {
    let argument = {}

    strs.forEach( str => {
        argument[str.split('').sort().toString()] = []
    })

    strs.forEach( str => {
        argument[str.split('').sort().toString()] = argument[str.split('').sort().toString()].concat(str).sort();
    })

    return Object.values(argument)
};

strs = ["eat","tea","tan","ate","nat","bat"]


console.log(groupAnagrams(strs))