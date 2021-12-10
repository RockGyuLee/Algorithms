/*
1단계 new_id의 모든 대문자를 대응되는 소문자로 치환합니다.
2단계 new_id에서 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
3단계 new_id에서 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
4단계 new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
5단계 new_id가 빈 문자열이라면, new_id에 "a"를 대입합니다.
6단계 new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
     만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
7단계 new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙입니다.
*/

'use strict';
function solution(new_id) {
    let id = secondAndThreeCase(firestCase(new_id));
    let answer = sevenCase(sixCase(fiveCase(fourthCase(id))));

    return answer;
}

// 모든 대문자를 대응되는 소문자로 치환합니다.
function firestCase( pId ){
    return pId.toLowerCase();
}
// 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자를 제거합니다.
// 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환합니다.
function secondAndThreeCase( pId ){
    const secondReg = /[^a-z|\d|\-_.]/g;
    const threeReg = /[.]{2,}/g;

    let sePId = pId.replace(secondReg,"");
    let threeId = sePId.replace(threeReg,".")

    return threeId
}

// new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거합니다.
function fourthCase(pId){
    const words = pId.split('');

    if(words[0] == '.') words.shift();
    else if(words[words.length - 1 ] == '.') words.pop();

    let strWords = convertArray2String(words);
    return strWords;
}

// 빈 문자열이라면, new_id에 "a"를 대입합니다.
function fiveCase(pId){
    if(pId == '') return 'a';
    
    return pId;
}

// new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거합니다.
// 만약 제거 후 마침표(.)가 new_id의 끝에 위치한다면 끝에 위치한 마침표(.) 문자를 제거합니다.
function sixCase(pId){
    const words = pId.split('');
    
    if(words.length >= 16) {
        words.splice(15);
    }
    if(words[words.length - 1] == '.') words.pop();

    let strWords = convertArray2String(words);
    return strWords;
}

function sevenCase(pId){
    const words = pId.split('');

    let str = words[words.length -1]
    while( words.length <= 2){
        words.push(str)
    }

    let strWords = convertArray2String(words);
    return strWords;
}

function convertArray2String(array){
    let str = array.toString();
    const reg = /[,]/g;
    return str.replace(reg,'');
}



console.log(solution('...!@BaT#*..y.abcdefghijklm'));
console.log(solution("z-+.^."));
solution("=.=");


"bat.y.abcdefghi"