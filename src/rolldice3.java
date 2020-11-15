public class rolldice3public int solution(int[] dices) {
    int res = dices.length * 2;
    int[] count = new int[6];
    for(int dice: dices) {
        count[dice- 1]++;
    }
    for(int i = 0; i < 6; i++) {
        res = Math.min(res, count[5 - i] + dices.length - count[i]);
    }
    return res;
}