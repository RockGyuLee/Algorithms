package com.company;

import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
	// write your code here
        Scanner sc = new Scanner(System.in);

        int weight = sc.nextInt();

        System.out.println(sum(weight));

    }

    public static int sum(int weight){

        int w = weight;
        int count = 0;

       while(true){
           if( w % 5 == 0){
               count += w / 5;
               return count;
           } else {
               w -= 3;
               count++;
           }

           if( w < 0 ) {
               return -1;
           }
       }
    }
}
