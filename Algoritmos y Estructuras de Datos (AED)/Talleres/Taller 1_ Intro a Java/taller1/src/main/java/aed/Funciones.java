package aed;

class Funciones {
    int cuadrado(int x) {
        return x*x;
    }
    
    double distancia(double x, double y) {
        return Math.sqrt(x*x+y*y);
    }

    boolean divideA(int d, int n) {
        return n % d == 0;
    }
    
    boolean esPar(int n) {
        return divideA(2,n);
    }

    boolean esBisiesto(int n) {
        return (divideA(4, n) && !divideA(100, n)) || divideA(400, n);
    }

    int factorialIterativo(int n) {
        int res = 1;
        if (n != 0) {
            for (int i = 1; i <= n; i++) {
                res *= i;
            }
        }
        return res;
    }

    int factorialRecursivo(int n) {
        int res;
        if (n == 0) {
            res = 1; 
        } else {
            res = n*factorialIterativo(n-1);
        }
        return res;
    }

    boolean esPrimo(int n) {
        return primo(n);
    }

    boolean primo(int n) {
        int suma_1_si_divide = 0;
        for (int i = 1; i <= n; i++) {
            if (divideA(i,n)) {
                suma_1_si_divide ++;
            }
        }
        return suma_1_si_divide == 2;
    }
    
    int sumatoria(int[] numeros) {
        int res = 0;
        for (int n : numeros) {
            res += n;
        }
        return res;
    }
    
    int busqueda(int[] numeros, int buscado) {
        int res = 0;
        for (int i = 0; i < numeros.length; i++) {
            if (numeros[i] == buscado) {
                res = i;
            }
        }
        return res;
    }

    boolean tienePrimo(int[] numeros) {
        for (int n : numeros) {
            if (primo(n)) {
                return true;
            }
        }
        return false;
    }

    boolean todosPares(int[] numeros) {
        for (int n : numeros) {
            if (!divideA(2,n)) {
                return false;
            }
        }
        return true;
    }

    boolean esPrefijo(String s1, String s2) {
        if (s1.length() > s2.length()) {
            return false;
        } else {
            for (int i = 0; i < s1.length(); i++) {
                if (s1.charAt(i) != s2.charAt(i)) {
                    return false;
                }
            }
        }
        return true;
    }
   
    boolean esSufijo(String s1, String s2) {
        return esPrefijo(darVueltaString(s1), darVueltaString(s2));
    }

    String darVueltaString(String s) {
        String reverso = "";
        for (int i = s.length(); i > 0; i--) {
            reverso += s.charAt(i-1);
        }
        return reverso;
    }

}
