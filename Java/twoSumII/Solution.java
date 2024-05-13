package Java.twoSumII;

class Solution {
    public int[] twoSum(int[] numbers, int target) {
        int beginPointer = 0;
        int endPointer = numbers.length-1;

        int sum = 0;

        while (true) {
            sum = numbers[beginPointer]+numbers[endPointer];
            
            if (sum == target) {
                int[] output = {beginPointer+1, endPointer+1};
                return output;
            }

            if (sum < target) {
                beginPointer++;
            } else {
                endPointer--;
            }
        }
    }

    public static void main(String[] args) {
        Solution obj = new Solution();

        int[] listOfInputs = {2, 7, 11, 15};
        int[] output = obj.twoSum(listOfInputs, 9);
        System.out.println(output);
    }
}