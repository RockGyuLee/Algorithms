/**
 * @param {string[]} logs
 * @return {string[]}
 */
 var reorderLogFiles = function(logs) {
    let letters = [];
    let digits = [];

    logs.forEach((log)=>{
        if( isNaN(log.split(' ')[1]) ){
            letters.push(log)
        }
        else {
            digits.push(log)
        }
    })

    letters.sort((a, b)=> {

        let a_list = a.split(' ')
        let b_list = b.split(' ')

        console.log(a_list.slice(1).toString().localeCompare(b_list.slice(1).toString()));

        if( a_list.slice(1).toString().localeCompare(b_list.slice(1).toString()) < 0){
            return -1
        }
        else if(a_list.slice(1).toString().localeCompare(b_list.slice(1).toString()) > 0){
            return 1
        } else {
            let value = 0;
            value = a_list[0].localeCompare(b_list[0]) < 0 ? -1 : 1
            return value
        }
    })

    return letters.concat(digits)


};

// logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"];
// logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
logs = ["j mo", "5 m w", "g 07", "o 2 0", "t q h"]

console.log(reorderLogFiles(logs));

/**
 * ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
 */