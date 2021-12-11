function solution(n, arr1, arr2) {
    let ret = []

    /*
        1. arr1과 arr2의 각 element들의 비트 연산자 or를 사용하여 해당하는 숫자를 알아낸다.
        2. Number 객체의 method toString(param : 몇진수)를 사용하여 해당 숫자를 2진수로 변경한다.
        3. String method padStart를 사용하여 n번째자리를 0으로 채워줌으로 써 2진수 데이터를 n번째에 맞게 가공한다.
    */
    for(let i = 0; i < n; i++){
       ret.push( Number(arr1[i] | arr2[i]).toString(2).padStart(n, '0') )
    }

    /*
        1. 1은 특수문자 #으로 대체 해야한다.
        2. 0은 특수문자 white space로 대체 해야한다.
        3. String method replace를 사용하여 각 요소드을 변환한다.
    */
    let reg1 = /1/ig;
    let reg0 = /0/ig;
    let answer = ret.map(item => {
        return item.replace(reg1,'#').replace(reg0,' ');
    })

    return answer;
}

// solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28])
// solution(6 ,[46, 33, 33 ,22, 31, 50] , [27 ,56, 19, 14, 14, 10])

/**
    n	        5
    arr1	    [9, 20, 28, 18, 11]
    arr2	    [30, 1, 21, 17, 28]
    출력	    ["#####","# # #", "### #", "# ##", "#####"]
 */