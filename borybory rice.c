#include <stdio.h>
#include <stdio.h>
#include <stdlib.h> //srand, rand를 사용하기 위한 헤더파일
#include <time.h> // time을 사용하기 위한 헤더파일
#include <unistd.h>
int num=0, speak,a=0,choice;
double duration;
void attack(){
	while (1){
		scanf("%d", &speak);
		if(speak==1)
			num--;
		else if(speak==2){
			if(num==0){
				printf("승리\n");
				break;
			}
			else{
				printf("패배\n");
				break;
			}
		}
		else if((speak==3)&&(a==0)){
			if(num<4)
				printf("3번이하 남음");
			else
				printf("4번이상 남음");
			a++;
		}
		else if((speak==3)&&(a!=0))
			printf("이미 힌트 씀");
	}
}
void defense(){
	int a, ch;
	while(num>=0){
		printf("보리\n");
		num--;
		scanf("%d", &ch);
		if(ch!=1){
			printf("틀렸습니다\n");
			break;
		}
		sleep(1);
	}
	printf("쌀\n");
	time_t start, end;
	time(&start);
	scanf("%d", &a);
	time(&end);
	printf("time = %f\n", (float)(end - start)); // 출력
	if((float)(end - start) == 0.000000)
		printf("승리");
	else
		printf("패배");
}
int main()
{
	printf("공 수 정해주세요 1:공격, 2: 수비");
	scanf("%d", &choice);
	printf("보리 : 1, 쌀 : 2, 힌트(1번) : 3\n");
	if(choice==1){
		srand(time(NULL)); // 난수 초기화
		num = rand() % 8; // 0 ~ 7 사이의 숫자를 뽑아서 random 변수에 저장
		int result = num;
		attack();
		printf("정답은 보리%d번이였습니다", result);
	}
	else if(choice==2){
		srand(time(NULL)); // 난수 초기화
		num = rand() % 8; // 0 ~ 7 사이의 숫자를 뽑아서 random 변수에 저장
		defense();
	}
}