import java.util.*;
import java.io.*;
public class Special {

static Map<Integer, Boolean> memo = new Hashtable<Integer, Boolean>();

static Boolean isUnique(int[] arr){
	Boolean result = true;
	for(int i=0;i<arr.length;i++){
		if(memo.get(arr[i])==true){
			result = False;
			break
		}
		else{
			memo.put(arr[i]) = true;			
		}				
	}
	return result;		
}
	
public static void main (String[] args) {
	
	int[] val = [
		
		
}
}

