package com.company;

import java.util.Arrays;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
	// write your code here

        Scanner sc = new Scanner(System.in);

        int personNumber = sc.nextInt();

        Integer[] arr = new Integer[personNumber];

        for(int i = 0; i < personNumber; i++){
            arr[i] = sc.nextInt();
        }

        System.out.println(get2sendTime(personNumber,arr));

    }

    private static int get2sendTime(int p ,Integer[] arr){

        int time = 0, result = 0;

        Arrays.sort(arr);

        for (int i = 0; i < arr.length; i++){
            time = time + arr[i];
            result += time;
        }

        return result;
    }
}
