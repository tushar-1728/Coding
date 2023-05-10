int main() {
    int t, n;
    scanf("%d", &t);
    for (int i = 0; i < t; i++)
    {
        scanf("%d", &n);
        if (n == 0) {
            printf("%d\n", 1);
        }
        else {
            printf("%d\n", 3 * n);
        }
    }
    
}