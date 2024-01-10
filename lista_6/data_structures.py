'''
Pewne Struktury Dannych:
    
    Stos S (Stack) - FILO:
        ## metody stosu
        STACK_EMPTY(S) - czy S jest Pusty
        POP(S) - oddaje+usuwa górny (-1) element ze stosu
        PUSH(S, x) - dodaje x na góre (-1) stosu S
    
    Kolejka Q (Queue) - FIFO:
        ## metody kolejki
        QUEUE_EMPTY(S) - czy Q jest Pusty
        ENQUEUE(Q, x) - dokladamy x do Q
        DEQUQU(Q) - zabranie pierwszego elementu z Q
    
    Lista L (List) :
        lista sklada sie z obiektow x:
            x.prev - wskazuje na poprzedni obiekt
            x.next - wskazuje na nastepny obiekt
            x.key - klusz
        Jesli (x.prev|x.next) = NIL (Not In List), 
        to (poprzedniego|nastepnego) nie ma
        
        ## atrybuty L
        L.head - pierwszy (0) element, 'glowa' listy
        ## metody L
        LIST_SEARCH(L, key) - szuka objektu o kluczu 'key' 
            (NIL otherwise)
        LIST_INSERT(L, x, y) - dodaje 'y' po 'x'
        LIST_DELETE(L, x) - usuwa 'x' z 'L' 
            (z przepisaniem odpowiednich .prev, .next)
            
'''

