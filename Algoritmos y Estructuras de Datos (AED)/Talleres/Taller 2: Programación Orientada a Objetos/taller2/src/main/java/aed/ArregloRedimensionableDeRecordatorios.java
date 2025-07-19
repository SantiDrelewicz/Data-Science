package aed;

class ArregloRedimensionableDeRecordatorios {

    private Recordatorio[] recordatorios;

    public ArregloRedimensionableDeRecordatorios() {
        recordatorios = new Recordatorio[0];
    }

    public int longitud() {
        return recordatorios.length;
    }

    public void agregarAtras(Recordatorio i) {
        Recordatorio[] recordatorios_nuevo = new Recordatorio[recordatorios.length + 1];
        for(int j = 0; j < recordatorios.length; j++) {
            recordatorios_nuevo[j] = recordatorios[j];
        }
        recordatorios_nuevo[recordatorios_nuevo.length - 1] = i;
        recordatorios = recordatorios_nuevo;
    }


    public Recordatorio obtener(int i) {
        return recordatorios[i];
    }

    public void quitarAtras() {
        if (recordatorios.length > 0)  {
            Recordatorio[] recordatorios_viejo = new Recordatorio[recordatorios.length - 1];
            for (int i = 0; i < recordatorios.length - 1; i++) {
                recordatorios_viejo[i] = recordatorios[i];
            }
            recordatorios = recordatorios_viejo;
        }
    }

    public void modificarPosicion(int indice, Recordatorio valor) {
        Recordatorio[] recordatorios_modificado = new Recordatorio[recordatorios.length];
        for (int i = 0; i < recordatorios.length; i++) {
            if (i != indice) {
                recordatorios_modificado[i] = recordatorios[i];
            } else {
                recordatorios_modificado[i] = valor;
            }
        }
        recordatorios = recordatorios_modificado; 
    }

    public ArregloRedimensionableDeRecordatorios(ArregloRedimensionableDeRecordatorios vector) {
        recordatorios = vector.recordatorios.clone();
    }

    public ArregloRedimensionableDeRecordatorios copiar() {
        ArregloRedimensionableDeRecordatorios copia = new ArregloRedimensionableDeRecordatorios();
        copia.recordatorios = recordatorios;
        return copia;
    }
}
