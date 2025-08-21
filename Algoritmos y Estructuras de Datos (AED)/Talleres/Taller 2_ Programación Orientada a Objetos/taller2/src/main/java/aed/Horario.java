package aed;

public class Horario {

    private int hr;
    private int mins;

    public Horario(int hora, int minutos) {
        hr = hora;
        mins = minutos;
    }

    public int hora() {
        return hr;
    }

    public int minutos() {
        return mins;
    }

    @Override
    public String toString() {
        return hr + ":" + mins;
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
        Horario otroHorario = (Horario) otro;
        return hr == otroHorario.hr && mins == otroHorario.mins;
    }

}
