'''
DEFINICJA:
    Graf skierowany/(nieskierowany) to ...

Nowe Pojecia:
    - las
    - cykl
    - spojnosc
    - (a)cyklicznosc
FAKT:
    Jesli G=(V,E) jest drzewem, to |E|=|V|-1

GRAFY LOSOWE:
    ##Pierwszy model
    G(n, m) = kolekcja wsz grafow o n wierzcholkach i m kraw.
    g ∈ G(n, m), wtedy Pr(g)= 1/( (n 2)/m ) - p-nstwo dyskretne
    
    ##Drugi model
    G(m, p) - p∈(0, 1) 
    Pr( {1, 2, ..., n}, E ) = p^(|E|) * (1-p)^( (n 2) - E )
    G(m, p) = { ( {1, 2, ..., n}, E ): E⊆[{1, 2, ..., n}]^2 }
    
    ##Trzeci model - podejscie nieskonczone (zbior Cantora)
    Pr( { E∈{0,1}^(N*N) : E({a,b})=1 } ) = p
    
Przeszukiwanie wszerz (BFS - Breadth-first search):
    BFS(G, s):
        ## G - graf jako listy sasiedstwa
        ## s∈G.V
        ## Bedziemy dekorowac wierz. v∈G.V
        ## v.pi - kto jest ojcem
        ## v.d - jak daleko od praojca
        ## v.color 
        
        for every v∈G.V\{s} :
            v.pi = NIL
            v.d = +inf
            v.color = 'bialy'
        s.pi = NIL
        s.d = 0
        s.color = 'szary'
    
    ENQUEUE( Q, s ):
        while Q:
            u = DEQUEUE(Q)
            for every v∈G.Adj[u]:
                if v.color = 'bialy':
                    v.pi = uu
                    v.d = u.d+1
                    v.color = 'szary'
                    ENQUEUE( Q, v )
            u.color = 'czarny'
    
    
'''













