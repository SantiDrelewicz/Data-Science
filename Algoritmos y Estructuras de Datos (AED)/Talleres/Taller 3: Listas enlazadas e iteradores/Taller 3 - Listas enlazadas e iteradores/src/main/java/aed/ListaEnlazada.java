package aed;

import java.util.*;

public class ListaEnlazada<T> implements Secuencia<T> {

    private Nodo primero;
    private Nodo ultimo;
    private int largo;

    private class Nodo {
        T valor;
        Nodo sig;
        Nodo ant;
        Nodo(T v) { valor = v; }
    }

    public ListaEnlazada() {
        primero = null;
        ultimo = null;
        largo = 0;

    }

    public int longitud() {
        return largo;
    }

    public void agregarAdelante(T elem) {
        Nodo nuevo = new Nodo(elem);
        nuevo.ant = null;
        if (largo == 0) {
            nuevo.sig = null;
            ultimo = nuevo;
        } else {
            nuevo.sig = primero;
            primero.ant = nuevo;
        }
        primero = nuevo;
        largo += 1;
    }

    public void agregarAtras(T elem) {
        Nodo nuevo = new Nodo(elem);
        nuevo.sig = null;
        if (largo == 0) {
            nuevo.ant = null;
            primero = nuevo;
        } else {
            nuevo.ant = ultimo;
            ultimo.sig = nuevo;
        }
        ultimo = nuevo;
        largo += 1;
        
    }

    public T obtener(int i) {
        Nodo actual = primero;
        for (int j = 0; j < i; j++) {
            actual = actual.sig;
        }
        return actual.valor;
    }

    public void eliminar(int i) {
        Nodo actual = primero;
        Nodo prev = primero;
        for (int j = 0; j < i; j++) {
            prev = actual;
            actual = actual.sig;
        }
        if (i == 0) {
            primero = actual.sig;
        } else {
            prev.sig = actual.sig;
        }
        largo -= 1;
    }

    public void modificarPosicion(int indice, T elem) {
        Nodo actual = primero;
        for (int j = 0; j < indice; j++) {
            actual = actual.sig;
        } 
        actual.valor = elem;
    }

    public ListaEnlazada(ListaEnlazada<T> lista) {
        Nodo actual = lista.primero;
        while (actual != null) {
            agregarAtras(actual.valor);
            actual = actual.sig;
        }
    }
    
    @Override
    public String toString() {
        String res = "[";
        Nodo actual = primero;
        while (actual != null) {
            if (actual.sig != null) {
                res += actual.valor + ", ";
            } else {
                res += actual.valor + "]";
            }
            actual = actual.sig;
        }
        return res;
    }

    private class ListaIterador implements Iterador<T> {
        private Nodo next = primero;
        private Nodo prev = null;

        public boolean haySiguiente() {
            return next != null;
        }
        
        public boolean hayAnterior() {
	        return prev != null;
        }

        public T siguiente() {
            T res = next.valor;
            prev = next;
            next = next.sig;
            return res;
        }
        

        public T anterior() {
            T res = prev.valor;
            next = prev;
            prev = prev.ant;
            return res;
        }
    }

    public Iterador<T> iterador(){
	    return new ListaIterador();
    }

}
