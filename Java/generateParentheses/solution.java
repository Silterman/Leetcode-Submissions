package Java.generateParentheses;

import java.util.ArrayList;
import java.util.List;

public class solution {
    public List<String> generateParenthesis(int n) {
        List<String>parentheses = new ArrayList<>();
        parentheses.add("(");

        while (true) {
            List<String> temporaryParentheses = new ArrayList<>();
            for (String i: parentheses) {
                if ((countOccurrence(i, '(') > countOccurrence(i, ')')) && (countOccurrence(i, '(') < n)) {
                    temporaryParentheses.add(i+'('); temporaryParentheses.add(i+')');
                } else if (countOccurrence(i, '(') == n) {
                    temporaryParentheses.add(i+')');
                } else {
                    temporaryParentheses.add(i+'(');
                }
            }

            if (temporaryParentheses.size() == parentheses.size()) {
                List<String> output = new ArrayList<>();
                for (String i: temporaryParentheses) {
                    output.add(i+')');
                }
                return output;
            }
            parentheses = temporaryParentheses;
        } 
    }

    // returns number of occurrences of a certain character in a string
    public int countOccurrence(String word, char letter){
        int occurrence = 0;

        for (int i = 0; i < word.length(); i++){
            if (word.charAt(i) == letter) {
                occurrence++;
            }
        }

        return occurrence;
    }

    public static void main(String[] args) {
        //generate solution class to make methods callable
        solution obj = new solution();

        List<String> output = obj.generateParenthesis(3);
        System.out.println(output);
    }
}