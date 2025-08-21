package aed;

public class Recordatorio {

    private String msj;
    private Fecha f;
    private Horario h;

    public Recordatorio(String mensaje, Fecha fecha, Horario horario) {
        msj = mensaje;
        f = new Fecha(fecha);
        h = horario;
    }

    public Horario horario() {
        return h;
    }

    public Fecha fecha() {
        return new Fecha(f);
    }

    public String mensaje() {
        return msj;
    }

    @Override
    public String toString() {
        return msj + " @ " + f.toString() + " " + h.toString() ;
    }

    @Override
    public boolean equals(Object otro) {
        // Algunos chequeos burocraticos...
        boolean otroEsNull = (otro == null);
        boolean claseDistinta = otro.getClass() != this.getClass();
        if (otroEsNull || claseDistinta) {
        return false;
        }
        // casting -> cambiar el tipo
        Recordatorio otroRecordatorio = (Recordatorio) otro;
        return msj == otroRecordatorio.msj && 
               f.equals(otroRecordatorio.f) && 
               h.equals(otroRecordatorio.h);
    }
}


