#include<stdio.h>
main()
{
printf("Pick a food item:\n1. Pizza \n2. Pasta \n3. French fries \n4. Burger \n5. Sandwich");
int choice=0;
scanf("%d",&choice);
switch(choice)
{ 
case 1:
printf ("Food item-Pizza \nPrice-Rs 239");
break;  
case 2:
	printf("food item-Pasta \nPrice-Rs 179");
	break;
case 3:
	printf("Food item-French fries \nPrice-Rs 99");
	break;
case 4:
	printf("Food item-Burger \nPrice-Rs 129");
	break;
case 5:
	printf("Food item-Sandwich \nPrice-Rs 149");
	break;
default:
	printf("invalid choice");
return 0;

}

}
