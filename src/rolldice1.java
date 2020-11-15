public class rolldice1public class RollDice {

    private int distance(int pip1, int pip2){

        if(pip1 == pip2) return 0;
        if(pip1 + pip2 == 7 ){
            return 2;
        }
        return  1;
    }

    private int minMoves(int[] moves){
        int minMoves = Integer.MAX_VALUE;
        int currentMoves = 0;
        int i = 1;

        while(i < 7){
            for(int move : moves) {
                currentMoves += distance(move, i);
            }
            minMoves =  Math.min(minMoves, currentMoves);
            currentMoves = 0;
            i++;
        }

        return minMoves;
    }

    public static void main(String[] args) {
        System.out.println(new RollDice().minMoves(new int[]{1,2,3}));
        System.out.println(new RollDice().minMoves(new int[]{1,1,6}));
        System.out.println(new RollDice().minMoves(new int[]{1,6,2,3}));

    }

}