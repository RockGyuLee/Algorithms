var letterCombinations = function(digits) {
    let  result = []
    const dic = {
        "2" : "abc",
        "3" : "def",
        "4" : "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
        "0": "+",
    }

    if( digits == ""){
        return [];
    }

    const dfs = (index, path) => {

        if(path.length == digits.length){
            result.push(path);
            return
        }

        for( let i = index; i < digits.length; i++){
            let d = dic[digits[i]];
            for(let j= 0; j < d.length; j++){
                dfs(i+1, path+d[j])
            }
        }
    }

    dfs(0, "")

    return result
};


let digits="23"

console.log(letterCombinations(digits))