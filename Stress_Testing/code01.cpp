#include<iostream>
#include<stdio.h>

using namespace std;

int row[11], column[11], ara[11][11];

int main(void)

{
    int i, j, a;
    char ch;
    for(i = 0; i < 9; i++){
        for(j = 0; j < 9;){
            scanf("%c", &ch);
            if(ch != '\n'){
                ara[i][j] = ch-'0';
                j++;
            }
        }
    }
    int flag = 0;
    if(flag == 0){
    for(i = 0; i < 9; i++){
        if(flag == 0){
        for(j = 0; j < 9; j++){
            a = ara[i][j];
            row[a]++;
            }
        }
            for(int k = 1; k < 10; k++){
                if(row[k] != 1){
                    flag = 1;
                    break;
                }
                else
                    row[k] = 0;
            }
    }
    }
    if(flag == 0){
    for(i = 0; i < 9; i++){
        if(flag == 0){
        for(j = 0; j < 9; j++){
            a = ara[j][i];
            row[a]++;
            }
        }
            for(int k = 1; k < 10; k++){
                if(row[k] != 1){
                    flag = 1;
                    break;
                }
                else
                    row[k] = 0;
            }
    }
    }
    if(flag == 0)
        printf("Congratulations!\n");
    else
        printf("Oh No!\n");
    return 0;
}