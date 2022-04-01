/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {boolean}
 * 234번 문제.
 */
 var isPalindrome = function(head) {
    q = [];

    if( head.length === 0) return true;

    for (let index = 0; index < head.length; index++) {
        q.push(head[index].val)
    }


    while(q.length > 1){
        if(q.shift() != q.pop()){
            return false;
        }
    }

    return true;
};

let head =[
    {
        val : 1,
        next : 'next'
    },
    {
        val : 2,
        next : 'next'
    }
]

console.log(isPalindrome(head))