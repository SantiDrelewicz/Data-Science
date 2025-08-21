package aed;

import java.util.*;

// Todos los tipos de datos "Comparables" tienen el método compareTo()
// elem1.compareTo(elem2) devuelve un entero. Si es mayor a 0, entonces elem1 > elem2
public class ABB<T extends Comparable<T>> implements Conjunto<T> {
    
    private Nodo raiz;
    private int cardinal;

    private class Nodo {
        
        T valor;
        Nodo izq;
        Nodo der;
        Nodo padre;
        Nodo(T v) {
                    valor = v;
                    izq = null;
                    der = null;
                    padre = null;
        }
    }

    public ABB() {
        raiz = null;
        cardinal = 0;
    }

    public int cardinal() {
        return cardinal;
    }

    public T minimo(){
        Nodo actual = this.raiz;
        while (actual.izq != null) {
            actual = actual.izq;
        }
        return actual.valor;
    }

    public T maximo(){
        Nodo actual = this.raiz;
        while (actual.der != null) {
            actual = actual.der;
        }
        return actual.valor;
    }

    public void insertar(T elem){
        if (!this.pertenece(elem)) {
            Nodo nuevo = new Nodo(elem);
            Nodo actual = this.raiz;
            if (actual == null) this.raiz = nuevo;
            else this.insertarIterativo(actual, nuevo);
            this.cardinal ++;
        }
    }

    private void insertarIterativo(Nodo raiz, Nodo nuevo) {
        Nodo padre_actual = this.raiz.padre;
        Nodo actual = this.raiz;
        while (actual != null) {
            padre_actual = actual;
            if (nuevo.valor.compareTo(actual.valor) < 0) actual = actual.izq;
            else actual = actual.der;
        }
        nuevo.padre = padre_actual;
        if (nuevo.valor.compareTo(padre_actual.valor) < 0) padre_actual.izq = nuevo;
        else padre_actual.der = nuevo;
    }

    public boolean pertenece(T elem){
        return busquedaRecursiva(elem, this.raiz);
    }

    private boolean busquedaRecursiva(T elem, Nodo arbol) {
        if (arbol == null) return false;
        else if (elem.compareTo(arbol.valor) == 0) return true;
        else if (elem.compareTo(arbol.valor) < 0) return busquedaRecursiva(elem, arbol.izq);
        else return busquedaRecursiva(elem, arbol.der);
    }

    public void eliminar(T elem){
        Nodo nodo = this.raiz;
        Nodo nodo_padre = null;
        //Si el elemento a eliminar es la raiz y no tiene hijos. 
        if (elem.compareTo(nodo.valor) == 0 && nodo.izq == null && nodo.der == null) {
            this.raiz = null;
            this.cardinal -= 1;
        } else eliminarRecursivo(elem, nodo_padre, nodo);
    }

    public void eliminarRecursivo(T elem, Nodo arbol_padre, Nodo arbol) {
        if (arbol == null) return; 
        else if (elem.compareTo(arbol.valor) > 0) eliminarRecursivo(elem, arbol, arbol.der);
        else if (elem.compareTo(arbol.valor) < 0) eliminarRecursivo(elem, arbol, arbol.izq);
        else {
            if (arbol.izq == null || arbol.der == null) { // Si tiene 0 o 1 hijos

                Nodo hijo = null;
                if (arbol.izq != null && arbol.der == null) hijo = arbol.izq;
                if (arbol.izq == null && arbol.der != null) hijo = arbol.der; 

                if (arbol_padre == null) { // Si el elemento a eliminar es la raiz (y tiene hijos)
                    this.raiz = hijo; // El hijo pasa a ser la raiz
                } else if (arbol_padre.izq == arbol) { // Si no es la raiz y es el hijo izquierdo del padre
                    arbol_padre.izq = hijo;
                } else { // SI es el hijo derecho del padre
                    arbol_padre.der = hijo;
                }
                this.cardinal--;
            } else { // Si tiene dos hijos busco el sucesor 
                Nodo actual = arbol; 
                Nodo sucesor = actual.der; // me muevo al arbol derecho
                while (sucesor.izq != null) { // busco el minimo de ese arbol
                    actual = sucesor; 
                    sucesor = sucesor.izq;
                }
                arbol.valor = sucesor.valor; // reemplazo el valor del sucesor en el nodo a eliminar              
                if (actual == arbol) { // Si el sucesor es el hijo derecho
                    actual.der = sucesor.der; 
                } else { // Si el sucesor esta mas abajo
                    actual.izq = sucesor.der; 
                }
                this.cardinal--;
            }
        }
        return; 
    }

    public String toString(){
        ABB_Iterador iter = new ABB_Iterador();
        if (cardinal == 0) return "{}";
        else if (cardinal == 1) return "{" + iter.siguiente() + "}";
        else {
            int i = 0;
            String res = "{";
            while (i < cardinal - 1) {
                res += iter.siguiente() + ",";
                i ++;
            }
            return res += iter.siguiente() + "}"; 
        }
    }


    private class ABB_Iterador implements Iterador<T> {
        private Nodo iter;

        public ABB_Iterador() {
            if (raiz != null) {
                iter = raiz;
                while (iter.izq != null){
                    iter = iter.izq;
                }
            } else {
                iter = null;
            }

        }

        public boolean haySiguiente() {            
            return iter != null;
        }

        public T siguiente() {
            T res = iter.valor;
            if (iter.der != null){
                iter = iter.der;
                while (iter.izq != null){
                    iter = iter.izq;
                }
            } else {
            // caso contrario: no tiene subarbol derecho
            // el siguiente es el primer padre de un subarbol izquierdo
                iter = iter.padre;
                while (iter != null && iter.der != null && iter.der.valor.equals(res)) {
                    iter = iter.padre;
                }
            }
            return res;
        }

        
    }
    public Iterador<T> iterador() {
        return new ABB_Iterador();
    }
}
