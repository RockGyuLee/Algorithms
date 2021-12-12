function solution(dartResult) {

    let str = ''
    let arr = [];
    let ret = 0;

    for( let i = 0; i < dartResult.length; i++){
        if( dartResult[i] == 'S'){
            arr.push( Math.pow(Number.parseInt(str), 1))
            str = ''
        }else if(dartResult[i] == 'D'){
            arr.push( Math.pow(Number.parseInt(str), 2))
            str = ''
        } else if(dartResult[i] == 'T'){
            arr.push( Math.pow(Number.parseInt(str), 3))
            str = ''

        } else if( dartResult[i] == '#'){
            arr[arr.length -1] = arr[arr.length -1] * -1
        } else if( dartResult[i] == '*'){
            let len = arr.length;
            arr[ len - 1 ] = arr[ len - 1 ] * 2;
            if(len - 2 < 0 ) continue
            arr[ len - 2 ] = arr[ len - 2 ] * 2;
        } else {
            str += dartResult[i]
        }
    }

    arr.forEach( i => ret += i)

    return ret;
}

solution("1D#2S*3S")
solution("1T2D3D#")
solution("1D2S3T*")