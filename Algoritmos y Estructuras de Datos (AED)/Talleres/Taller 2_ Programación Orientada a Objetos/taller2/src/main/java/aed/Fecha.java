package aed;

public class Fecha {

    private int d;
    private int m;

    public Fecha(int dia, int mes) {
        d = dia;
        m = mes;        
    }

    public Fecha(Fecha fecha) {
        d = fecha.d;
        m = fecha.m;
    }

    public Integer dia() {
        return d;
    }

    public Integer mes() {
        return m;
    }

    public String toString() {
        return d + "/" + m;
    }

    @Override
    public boolean equals(Object otra) {
        // Algunos chequeos burocraticos...
        boolean otraEsNull = (otra == null);
        boolean claseDistinta = otra.getClass() != this.getClass();
        if (otraEsNull || claseDistinta) {
            return false;
        }
        // casting -> cambiar el tipo
        Fecha otraFecha = (Fecha) otra;
        return d == otraFecha.d && m == otraFecha.m;
    }

    public void incrementarDia() {
        if (d == diasEnMes(m)) {
            d = 1;
            if (m == 12) {
                m = 1;
            } else {
                m = m + 1;
            }
        } else {
            d = d + 1;
        }
    }

    private int diasEnMes(int mes) {
        int dias[] = {
                // ene, feb, mar, abr, may, jun
                31, 28, 31, 30, 31, 30,
                // jul, ago, sep, oct, nov, dic
                31, 31, 30, 31, 30, 31
        };
        return dias[mes - 1];
    }

}
