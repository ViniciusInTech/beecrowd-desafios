import java.io.IOException;

/ **
*IMPORTANT:
*O
nome
da
classe
deve
ser
"Main"
para
que
a
sua
solução
execute
*Class
name
must
be
"Main"
for your solution to execute
*El
nombre
de
la
clase
debe
ser
"Main"
para
que
su
solución
ejecutar
* /

import java.io.IOException;
import java.util.Scanner;

public


class Main {

public static void main(String[] args) throws IOException {
Scanner leitor = new Scanner(System.in );
double soma = 0;
char O = leitor.next().toUpperCase().charAt(0);
double[][] M = new double[12][12];
for (int i = 0; i < M.length; i++) {
for (int j = 0; j < M[i].length; j++) {
M[i][j] = leitor.nextDouble();
}
}

for (int i = 0; i < M.length; i++) {
for (int j = 0; j < M[i].length; j++) {
if (j < i & & j > M.length-i-1) soma += M[i][j];
}
}

if (O == 'M') soma /= 30;
System.out.println(String.format("%.1f", soma));
}

}