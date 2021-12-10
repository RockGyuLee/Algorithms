function solution(name) {
    var answer = 0;
    let nameList = name.split('');
    let alpabetList = [
        'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z',
    ]
    console.log(nameList);

    nameList.map( (item, idx) => {
        alpabetList.find( (iitem, iidex) => {
            if(iitem == item) return true
        })
    })
    return answer;
}

console.log(solution("JEROEN"))