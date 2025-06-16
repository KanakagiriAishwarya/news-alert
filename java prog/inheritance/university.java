package inheritance;
import 

public class university{
    public void placements(){
        System.out.println("Reva university placemts");

    }
    
}
class SVB extends university{
    public void CSE(){
        System.out.println("conducting placements for CSE");
    }
}
class universityMain{
    public static void main(String[] args){
        SVB s=new SVB();
        s.placements();
        s.CSE();

    }
}

