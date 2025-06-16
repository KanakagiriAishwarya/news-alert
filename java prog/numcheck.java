import java.util.Scanner;
public class numcheck
{
	public static void main(String[] args) {
	    Scanner sc=new Scanner(System.in);
		System.out.println("enter number");
		int num=sc.nextInt();
		if(num>0){
		    System.out.println("number is positive");
		}
		else if(num<0){
		    System.out.println("number is negative");
		}
		else{
		    System.out.println("number is zero");
		}
		sc.close();
	}
}
// import java.util.Scanner;
// public class Main
// {
// 	public static void main(String[] args) {
	    
// 	}
// 	    Scanner sc=new Scanner(System.in);
//         System.out.println("enter name");
//         String name=sc.next();
//         System.out.println("enter rollno");
//         int rollno=sc.nextInt();
//         System.out.println("enter sub1");
//         int sub1=sc.nextInt();
//         System.out.println("enter sub2");
//         int sub2=sc.nextInt();
//         System.out.println("enter sub3");
//         int sub3=sc.nextInt();
//          int average = grade(sub1, sub2, sub3);  
//         System.out.println("Average Marks: " + average);

//         sc.close();
//         //System.out.println("Grade"+grade(sub1,sub2,sub3));
        
//     }
//     public static int grade(int sub1,int sub2,int sub3){
//         int total=sub1+sub2+sub3;
//         int average=total/3;
//         if(total>=90&&total<=100){
//             System.out.println("Grade:A");
//         }
//         else if(total>=75&&total<=89){
//             System.out.println("Grade:B");
//         }
//         else if(total>=60&&total<=74){
//             System.out.println("Grade:c");
//         }
//         else if(total>=40&&total<=59){
//             System.out.println("Grade:D");
//         }
//         else{
//             System.out.println("Grade:E");
//         }
//         return average;
//     }
// }   
    
//     public static int sumdigit(int num){
//         if(num==0){
//             return 0;
//         }else{
//         return(num%10)+sumdigit(num/10);
//         }
//     }
   
// }

// 		boolean isprime=false;
// 		if(num<=1){
// 		    isprime=false;
// 		}
// 		else{
// 		for(int i=2;i<num;i++){
// 		    if(num%2==0){
// 		        isprime=false;
// 		        break;
// 		    }
// 		}
// 	}
// 	if(isprime){
// 	    System.out.println("prime");
// 	}
// 	else{
// 	    System.out.println("not");
// 	}
// 	sc.close();