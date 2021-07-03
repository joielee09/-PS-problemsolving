#include <stdio.h>
#include <iostream>
using namespace std;

int main(void){
  FILE *fp1;
  fp1 = fopen("input.txt", "r");

  long long n1 = 0;
  fscanf(fp1, "%d", &n1);
  cout << n1;
}