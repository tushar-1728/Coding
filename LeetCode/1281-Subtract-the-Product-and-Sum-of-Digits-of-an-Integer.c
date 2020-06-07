

int subtractProductAndSum(int n){
	int sum = 0;
	int mul = 1;
	int temp;
	while(n){
		temp = n%10;
		sum += temp;
		mul *= temp;
		n /= 10;
	}
	return mul-sum;
}