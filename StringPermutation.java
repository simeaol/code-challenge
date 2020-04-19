public class StringPermutation {

    public static void main(String[] args) {
        String str = "ABC";
        permutation(str, 0, str.length()-1);
    }

    private static void permutation(String str, int left, int rigth){
        if(left == rigth) {
            System.out.println("right == left: "+str);
        }else{
            for(int i=left; i<= rigth; i++){
                System.out.println("str before permutation: "+str+ " for left="+left+" right="+rigth+" and i="+i);
                String swapped = swap(str, left, i);
                System.out.println("str swapped="+swapped);
                permutation(swapped, left+1, rigth);
            }
        }
    }

    private static String swap(String str, int p1, int p2){
        char[] array = str.toCharArray();
        char v1 = array[p1];
        char v2 = array[p2];
        array[p1] = v2;
        array[p2] = v1;


        return String.valueOf(array);
    }
}