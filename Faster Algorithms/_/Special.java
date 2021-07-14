import java.util.*;
import java.io.*;
public class Special {



static Boolean isUnique(int[] arr){
	Map<Integer, Boolean> memo = new Hashtable<Integer, Boolean>();
	Boolean result = true;	
	
	
	for(int i=0;i<arr.length;i++){		
		if(memo.getOrDefault(arr[i],false)){
			result = false;
			break;
		}
		else{
			memo.put(arr[i],true);			
		}				
	}
	
	
	System.out.println(memo);
	return result;		
}
	
public static void main (String[] args) {
	
	int[] val = new int[]{1,2,4,5};
	int[] val2 = new int[]{1,2,2,5};
	
	System.out.println(isUnique(val));		 	
	System.out.println(isUnique(val2));
	System.out.println(isUnique(val));		
}
}

