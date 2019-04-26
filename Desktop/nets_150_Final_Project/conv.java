import java.io.*;
import java.util.*;


class conv{

public static void main(String args[]) throws FileNotFoundException, IOException {
double[][] arr = new double[50692][151];
int c=0;

try (BufferedReader br = new BufferedReader(new FileReader("jesterfinal151cols.csv"))) {
    String line;
    while ((line = br.readLine()) != null) {
        String[] values = line.split(",");
        for(int x = 0; x < values.length; x++) {
            arr[c][x] = Double.parseDouble(values[x]);
        }
        c++;
    }
}
//System.out.println(records);
System.out.println(arr[50687][149]);
}
}