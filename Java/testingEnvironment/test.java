package Java.testingEnvironment;

public class test {
    public static int testConditionalReturn(int n) {
        return (n%2==0)? n*2 : 0;
    }

    public static void main(String[] args) {
        int output = testConditionalReturn(3);
        System.out.println(output);
    }
}
