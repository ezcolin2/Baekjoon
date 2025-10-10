class Solution {
    public String solution(String newId) {
        newId = newId.toLowerCase()
            .replaceAll("[^a-z0-9-_.]", "")
            .replaceAll("\\.{2,}", "\\.")
            .replaceAll("^\\.", "")
            .replaceAll("\\.$", "");
        
        if (newId.length() == 0){
            newId = "a";
        }
        
        if (newId.length() >= 16){
            newId = newId.substring(0, 15);
        }
        
        newId = newId.replaceAll("\\.$", "");
        
        while (newId.length() <= 2){
            newId = newId + newId.charAt(newId.length()-1);
        }
        return newId;
    }
}