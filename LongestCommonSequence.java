
public class LongestCommonSequence{
    public static void main(String[] args) {
        String [] s1 = {"A","B","C","D"};
        String [] s2 = {"A","X","B","X","C","X","D"};

        int result = lcs(s1, s2, s1.length-1, s2.length-1);
        System.out.println("The result is: "+ result);
        
    }

    private static int lcs(String[] s1, String[] s2, int p1, int p2){
        if(p1 == 0 || p2 == 0) return 0;

        else if(s1[p1] == s2[p2]){
            return lcs(s1, s2, p1-1, p2-1) + 1;
        }else{
            return Math.max(lcs(s1, s2, p1-1, p2), lcs(s1, s2, p1, p2-1));
        }
        
    }
}