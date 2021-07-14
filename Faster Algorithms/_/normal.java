import java.util.*;
import java.text.DecimalFormat;

public class normal {


static Boolean isUnique(int[] arr){
	Boolean result = true;
	int length = arr.length;
	
	// 1,2,4,5
	for(int i=0;i<length;i++){  n = 4 n^(innver loop count)
		
		1
		2
		4
		5
		
		for(int j=0;j<length;j++){		
			
			2,4,5
			1,4,5
			1,2,5
			1,2,4
			
				
			if ((arr[i]==arr[j])&&(i!=j)){
			result = false;
			break;			
		}		
	}
	
	
}

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

