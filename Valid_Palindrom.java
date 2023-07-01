class Solution {
    public boolean isPalindrome(String s) {
        String fixed="";
        for (char c:s.toCharArray()){
            if(Character.isDigit(c)||Character.isLetter(c)){
                fixed+=c;
            }
        }
        fixed=fixed.toLowerCase();
        int a_pointer=0;
        int b_pointer=fixed.length()-1;
        while(a_pointer<=b_pointer){
            if(fixed.charAt(a_pointer)!=fixed.charAt(b_pointer)){
                return false;
            }
            a_pointer+=1;
            b_pointer-=1;
        }
        return true;
        }
    }
