package com.company;

import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.Scanner;

public class Main {

    public static void main(String[] args) {
	// write your code here

        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int K = sc.nextInt();

        Integer[] coin = new Integer[N];

        for(int i = 0; i < N; i++) {
            coin[i] = sc.nextInt();
        }

        System.out.println(getMinMoney(K, coin));

    }

    public static int getMinMoney(int money, Integer[] coinArr){

        int m = money;
        int result = 0;

        List<Integer> list = Arrays.asList(coinArr);

        Collections.reverse(list);

        for (Integer item : list){
            if(m == 0) break;

            result += Integer.valueOf( m / item );
            m = m % item;
        }

        return result;
    }
}
