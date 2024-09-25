class Solution{

	public int[] dailyTemperatures(int[] temperatures){
	// [1,2,4,1,2,4,3]
	// asnwer 
	Stack<Pair<Integer, Integer>> st = new Stack<>();
	int[] answer = new int[temperatures.length];
	
	for(int i = temperatures.length - 1; i >=0; --i){
		
		while(!st.isEmpty() && temperatures[i] >= st.peek().getKey()){
			
			st.pop();
}

answer[i] = st.isEmpty() == true ? 0: st.peek().getValue() - i;
st.push(new Pair<Integer, Integer>(temperatures[i], i));
}

return answer;
}}
